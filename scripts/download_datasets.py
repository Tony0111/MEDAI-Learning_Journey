#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据集下载脚本
================

本仓库不存放任何图像数据集（体积太大，也不适合放进 Git）。
需要用数据时，运行本脚本现下载即可。

目前支持：
  - MedNIST : DenseNet121 二维分类教程用的 6 类医学影像数据集（约 6 万张图，解压后约 250MB）

用法：
    # 默认下载到 <仓库根目录>/data/raw/datasets/
    python scripts/download_datasets.py

    # 只下载 MedNIST
    python scripts/download_datasets.py --dataset mednist

    # 指定数据根目录（会在此目录下生成 MedNIST/）
    python scripts/download_datasets.py --data-dir D:/AI/MONAI/DenseNet121/data

    # 也可以用环境变量
    $env:MONAI_DATA_DIRECTORY = "D:/AI/MONAI/DenseNet121/data"   # PowerShell
    export MONAI_DATA_DIRECTORY=/path/to/data                     # bash
    python scripts/download_datasets.py

下载完成后目录形如：
    <data-dir>/
    ├── MedNIST.tar.gz
    └── MedNIST/
        ├── AbdomenCT/  BreastMRI/  ChestCT/  CXR/  Hand/  HeadCT/
        └── ...
"""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
import tarfile
import urllib.request
from pathlib import Path

# 仓库根目录 = 本文件的上一级
REPO_ROOT = Path(__file__).resolve().parents[1]

# --------------------------------------------------------------------------- #
# 数据集定义
# --------------------------------------------------------------------------- #
DATASETS = {
    "mednist": {
        "url": "https://github.com/Project-MONAI/MONAI-extra-test-data/releases/download/0.8.1/MedNIST.tar.gz",
        "md5": "0bc7306e7427e00ad1c5526a6677552d",
        "archive": "MedNIST.tar.gz",
        "folder": "MedNIST",
        "desc": "MedNIST（6 类医学影像，约 6 万张图，解压后约 250MB）",
    },
}


# --------------------------------------------------------------------------- #
# 工具函数
# --------------------------------------------------------------------------- #
def _log(msg: str) -> None:
    print(f"[download] {msg}", flush=True)


def _md5sum(path: Path, chunk_size: int = 1 << 20) -> str:
    """计算文件 MD5。"""
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


def _download(url: str, dest: Path) -> None:
    """带进度显示地下载文件。"""
    if dest.exists():
        _log(f"压缩包已存在，跳过下载：{dest}")
        return

    dest.parent.mkdir(parents=True, exist_ok=True)
    _log(f"正在下载：{url}")

    tmp = dest.with_suffix(dest.suffix + ".part")
    try:
        with urllib.request.urlopen(url) as resp, tmp.open("wb") as out:
            total = resp.length or 0
            done = 0
            while True:
                chunk = resp.read(1 << 20)
                if not chunk:
                    break
                out.write(chunk)
                done += len(chunk)
                if total:
                    pct = done * 100 / total
                    sys.stdout.write(
                        f"\r[download]   {done / 1e6:7.1f} / {total / 1e6:.1f} MB ({pct:5.1f}%)"
                    )
                else:
                    sys.stdout.write(f"\r[download]   {done / 1e6:7.1f} MB")
                sys.stdout.flush()
        sys.stdout.write("\n")
        tmp.replace(dest)
    finally:
        if tmp.exists():
            tmp.unlink(missing_ok=True)


def _extract(archive: Path, dest_dir: Path) -> None:
    """解压 .tar.gz。"""
    _log(f"正在解压：{archive} -> {dest_dir}")
    dest_dir.mkdir(parents=True, exist_ok=True)
    with tarfile.open(archive, "r:gz") as tar:
        tar.extractall(dest_dir)


# --------------------------------------------------------------------------- #
# 主逻辑
# --------------------------------------------------------------------------- #
def ensure_dataset(key: str, data_root: Path, keep_archive: bool = True) -> Path:
    """确保某个数据集已就绪，返回数据集文件夹路径。"""
    if key not in DATASETS:
        raise KeyError(f"未知数据集：{key}，可选：{list(DATASETS)}")

    info = DATASETS[key]
    target_dir = data_root / info["folder"]

    # 已经解压过就直接复用
    if target_dir.is_dir() and any(target_dir.iterdir()):
        _log(f"数据已存在，跳过：{target_dir}")
        return target_dir

    archive = data_root / info["archive"]
    _download(info["url"], archive)

    # 校验 MD5
    _log("校验文件完整性…")
    actual = _md5sum(archive)
    if info["md5"] and actual != info["md5"]:
        archive.unlink(missing_ok=True)
        raise RuntimeError(
            f"MD5 校验失败！\n  期望: {info['md5']}\n  实际: {actual}\n"
            f"文件可能下载不完整，已删除，请重试。"
        )
    _log("校验通过 ✓")

    _extract(archive, data_root)

    if not keep_archive:
        archive.unlink(missing_ok=True)
        _log(f"已删除压缩包：{archive}")

    return target_dir


def main() -> None:
    parser = argparse.ArgumentParser(
        description="下载本仓库需要的数据集（不随 Git 分发）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--dataset",
        default="mednist",
        choices=list(DATASETS),
        help="要下载的数据集（默认：mednist）",
    )
    parser.add_argument(
        "--data-dir",
        default=None,
        help="数据根目录。默认依次取环境变量 MONAI_DATA_DIRECTORY、"
        "否则为 <仓库>/data/raw/datasets",
    )
    parser.add_argument(
        "--no-keep-archive",
        action="store_true",
        help="解压后删除 .tar.gz 压缩包（默认保留）",
    )
    args = parser.parse_args()

    data_root = Path(
        args.data_dir
        or os.environ.get("MONAI_DATA_DIRECTORY")
        or (REPO_ROOT / "data" / "raw" / "datasets")
    ).expanduser().resolve()

    _log(f"数据集：{DATASETS[args.dataset]['desc']}")
    _log(f"存放目录：{data_root}")

    path = ensure_dataset(args.dataset, data_root, keep_archive=not args.no_keep_archive)
    _log(f"完成 ✓ 数据位于：{path}")


if __name__ == "__main__":
    main()
