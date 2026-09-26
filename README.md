# MEDAI Learning Journey

一个医学生的医学 AI 学习项目。把**编程工具**、**学习笔记**、**模型实验**三条线放在同一个仓库里，
记录从零开始学习「AI 在医学中的应用」的过程。

> 起点：2025 年 8 月 ｜ 方向：医学影像、诊断、医学文献与研究方法

---

## 这是什么

这个仓库不是一个大项目，而是**三件并行的事**：

| 主线 | 内容 | 位置 |
|---|---|---|
| 🔧 **科研小工具** | 自己写的脚本：PubMed 热点分析、批量翻译、文献阅读助手 | `scripts/` |
| 📓 **学习笔记** | Obsidian 知识库：模型学习日志、文献精读、医学统计/文献计量 | `obsidian_vault/` |
| 🧪 **模型实验** | 深度学习入门实践（MONAI + PyTorch）：医学影像**六分类**、图像**分割** | `models/` |

**重要原则：数据集和模型权重不放进仓库。** 数据集用脚本按需下载，避免仓库被几个 GB 的图片撑爆。

---

## 目录结构

```
MEDAI-Learning-Project/
│
├── README.md                      # 本文件
├── medai_project_structure.md     # 文件结构详细说明
├── docs/
│   └── 项目整理方案.md             # 仓库清理与重构记录
│
├── scripts/                       # ① 科研小工具（三条独立工具链）
│   ├── README.md                  # 脚本目录详细说明
│   ├── download_datasets.py       # 数据集下载（MedNIST 等）
│   ├── pubmed_hotspot/            # 链1：PubMed 热点分析 + CSV 翻译
│   ├── paper_reading/             # 链2：单篇英文文献精读
│   └── model_playground/          # 链3：API 调用 / BioGPT 小实验
│
├── obsidian_vault/                # ② Obsidian 学习笔记
│   ├── Model_learning/            # MONAI / 环境 / GPU 学习日志
│   ├── Paper_Reviews/             # 文献精读笔记
│   ├── Bibliometrics/             # 文献计量学 + 医学统计学
│   ├── Theoretical_Study/         # 理论笔记（神经网络、梯度下降…）
│   ├── 医学AI学习项目初始化/       # 项目起步时的对话与 AI 反馈
│   ├── Templates/                 # 笔记模板
│   └── copilot-custom-prompts/    # Obsidian Copilot 提示词
│
├── models/MONAI/                  # ③ 模型实验（深度学习）
│   ├── DenseNet121/               # 医学影像六分类（DenseNet121 + MedNIST）
│   │   ├── model-traning.py
│   │   ├── guide.md               # 逐步讲解
│   │   └── data/                  # 数据集下载到这里（不进 Git）
│   └── 2d_segmentation/           # 2D 图像分割（UNet，合成数据）
│
└── data/                          # 数据（大部分被 .gitignore 忽略）
    └── raw/papers/                # 下载的论文 PDF
```

---

## 快速开始

### 环境依赖

```bash
pip install -r requirements.txt
```

> 需精确复现（含 Python 版本与 CUDA 版 PyTorch）见 `requirements.lock.txt`。

### 下载数据集

仓库里**没有**数据集，需要时用脚本现下（自动校验 MD5）：

```bash
# 默认下载到 data/raw/datasets/（已被 .gitignore 忽略）
python scripts/download_datasets.py

# 也可指定目录
python scripts/download_datasets.py --data-dir "D:/AI/MONAI/DenseNet121/data"
```

- **MedNIST**（约 6 万张医学影像，解压后 ~250MB）：DenseNet121 分类教程使用
- 2D 分割教程使用 `create_test_image_2d` **现场生成合成数据**，无需下载

### 跑模型

```bash
# 分类：需要先下载 MedNIST
python models/MONAI/DenseNet121/model-traning.py

# 分割：无需数据，直接跑
python models/MONAI/2d_segmentation/unet_training_array.py
```

> `model-traning.py` 中的数据集路径可通过环境变量 `MONAI_DATA_DIRECTORY` 指定。

---

## 模型实验说明

这部分是跟着 **MONAI 官方入门教程**做的深度学习实践（目的是跑通流程，不是科研项目）。

> 层级关系：人工智能 ⊃ 机器学习 ⊃ **深度学习**。本项目用的是深度学习。

### ① 医学影像六分类 — `models/MONAI/DenseNet121/`

| 项目 | 内容 |
|---|---|
| 数据 | MedNIST，约 6 万张 **64×64 灰度影像** |
| 类别（6 类） | 腹部CT、乳腺MRI、胸部X光、胸部CT、手部X光、头部CT |
| 模型 | DenseNet121（2D 分类网络） |
| 任务 | 输入一张影像，判断它属于 6 类中的哪一类 |
| 产物 | `data/best_metric_model.pth`（按验证集 AUC 保存的最优权重） |

> ⚠️ 这是**影像归类**，**不是**“肺炎 vs 正常”的疾病诊断。
> `guide.md` 里用“判断 X 光片是否肺炎”只是打个比方。

### ② 图像分割 — `models/MONAI/2d_segmentation/`

- **模型**：UNet；**任务**：把图像中的目标区域分割出来
- **数据**：`create_test_image_2d` **现场生成的随机图形**（非真实医学影像），只为跑通流程

### MONAI 是什么

**MONAI**（Medical Open Network for AI）是一个**面向医学影像的第三方开源深度学习库**，
建立在 **PyTorch** 之上，领域属于 **医学影像 + 人工智能**。

它把医学影像特有的麻烦事都封装好了：读取 DICOM/NIfTI、3D 体数据、医学数据增强、
现成网络（UNet、DenseNet、SwinUNETR…）、损失函数与评估指标（Dice、AUC）、滑窗推理等，
覆盖**分割、分类、检测、配准**等任务。

---

## 说明

- **数据集 / 权重不进 Git**：`.pth`、`MedNIST/`、`*.tar.gz` 等已在 `.gitignore` 中忽略。
- **模型的 `.pth` 权重**是本机训练产物，重新训练即可得到，不属于源码。
- `scripts/` 中调用外部 API 的脚本（如翻译）需要自行配置密钥，建议使用环境变量。

---

## 相关文档

- [`medai_project_structure.md`](medai_project_structure.md) — 目录结构逐项说明
- [`docs/项目整理方案.md`](docs/项目整理方案.md) — 仓库清理历程与后续计划
