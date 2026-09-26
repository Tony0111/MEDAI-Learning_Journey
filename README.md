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
| 🧪 **模型实验** | MONAI 教程实践：图像分类、图像分割 | `models/` |

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
├── scripts/                       # ① 科研小工具
│   ├── download_datasets.py       # 数据集下载（MedNIST 等）
│   ├── Pubmed.py                  # PubMed 研究热点爬取与可视化
│   ├── Translate_csv.py           # 批量翻译 CSV
│   ├── Reading/
│   │   └── English_research_read.py   # 英文文献阅读助手
│   ├── 医学AI模型测试/             # transformers 文本生成小实验
│   └── …                          # 各主题的分析输出（话题热点报告等）
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
├── models/MONAI/                  # ③ 模型实验
│   ├── DenseNet121/               # MedNIST 六分类（DenseNet121）
│   │   ├── model-traning.py
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
pip install torch monai transformers pandas requests beautifulsoup4 \
            matplotlib seaborn jieba wordcloud PyPDF2
```

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

## 说明

- **数据集 / 权重不进 Git**：`.pth`、`MedNIST/`、`*.tar.gz` 等已在 `.gitignore` 中忽略。
- **模型的 `.pth` 权重**是本机训练产物，重新训练即可得到，不属于源码。
- `scripts/` 中调用外部 API 的脚本（如翻译）需要自行配置密钥，建议使用环境变量。

---

## 相关文档

- [`medai_project_structure.md`](medai_project_structure.md) — 目录结构逐项说明
- [`docs/项目整理方案.md`](docs/项目整理方案.md) — 仓库清理历程与后续计划
