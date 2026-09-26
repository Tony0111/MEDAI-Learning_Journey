# 项目文件结构说明

> 本文件描述**当前真实的结构**（不再是"理想蓝图"）。
> 最后更新：仓库清理后（移除数据集与 MONAI 源码子模块）。

---

## 一、总体结构

```
MEDAI-Learning-Project/
├── README.md                      # 项目总览
├── medai_project_structure.md     # 本文件
├── .gitignore                     # 忽略数据集、权重、缓存等
│
├── docs/                          # 项目文档
│   └── 项目整理方案.md
│
├── scripts/                       # ① 自写的科研小工具
├── obsidian_vault/                # ② Obsidian 学习笔记
├── models/                        # ③ 模型实验代码
└── data/                          # 数据（多数被 .gitignore 忽略）
```

三条主线：`scripts/`（工具）、`obsidian_vault/`（笔记）、`models/`（模型）。

---

## 二、逐项说明

### `scripts/` —— 科研小工具

按**三条独立工具链**组织，每条链一个文件夹，各自有 `output/`（不进 Git）：

| 目录 | 作用 |
|---|---|
| `download_datasets.py` | 通用：按需下载数据集（MedNIST 等），带 MD5 校验 |
| `pubmed_hotspot/` | 链1：PubMed 热点分析（`Pubmed.py`、`pubmed_test.py`）+ CSV 翻译（`Translate_csv.py`） |
| `paper_reading/` | 链2：单篇英文文献精读（`English_research_read.py`） |
| `model_playground/` | 链3：API 调用测试、BioGPT 小实验 |

> 运行结果输出到各链的 `output/` 目录，已由 `.gitignore` 忽略；详见 `scripts/README.md`。

### `obsidian_vault/` —— 学习笔记

| 目录 | 内容 |
|---|---|
| `Model_learning/` | MONAI 学习日志、conda/GPU 环境笔记 |
| `Paper_Reviews/` | 文献精读笔记（按主题分文件夹） |
| `Bibliometrics/` | 文献计量学（VOSviewer 等）+ 医学统计学基础 |
| `Theoretical_Study/` | 理论笔记（神经网络结构、梯度下降、科研计划） |
| `医学AI学习项目初始化/` | 项目起步阶段的对话记录、AI 反馈、Git 初始化日志 |
| `Templates/` | 笔记模板 |
| `copilot-custom-prompts/` | Obsidian Copilot 自定义提示词 |

> 建议：Obsidian 每次打开都会改写 `.obsidian/workspace.json`，建议将其加入 `.gitignore`。

### `models/` —— 模型实验

| 目录 | 内容 |
|---|---|
| `MONAI/DenseNet121/` | MedNIST 六分类（DenseNet121 教程） |
| `MONAI/2d_segmentation/` | 2D 图像分割（UNet，使用合成数据） |

- 训练得到的 `.pth` 权重保留在本地，**不进入 Git**。
- 数据集通过 `scripts/download_datasets.py` 下载，默认落在 `models/MONAI/DenseNet121/data/`。

### `data/` —— 数据

| 目录 | 内容 | 是否进 Git |
|---|---|---|
| `raw/papers/` | 下载的论文 PDF | ❌（`.gitignore` 忽略 `*.pdf`） |
| `raw/datasets/` | 数据集下载目标目录（脚本自动创建） | ❌ |

---

## 三、命名与约定

- **笔记文件**：`YYYY-MM-DD_[标题]_学习指导.md` / `..._阅读分析_[时间戳].md`
- **脚本文件**：小写字母 + 下划线，如 `download_datasets.py`
- **数据不进 Git**：数据集、权重、PDF、训练输出一律忽略
- **API 密钥**：不写死在代码里，使用环境变量

---

## 四、不进版本控制的内容

以下内容已被 `.gitignore` 忽略，**不要**提交：

```
data/raw/            # 原始数据、论文 PDF
MedNIST/             # 下载的数据集
*.pth                # 模型权重
*.pdf                # 论文
*.log, __pycache__/  # 缓存与日志
```

---

## 五、与旧版文档的区别

旧版本文档描述的是一份**未落地的理想结构**（`scripts/ai_models/`、`notebooks/`、
`config/`、`automation/` 等），与实际仓库不符，且曾误导后续整理。

现版本只描述**真实存在**的内容；空目录（`config/`、`automation/`）已删除，
不再保留"占位但无内容"的文件夹。
