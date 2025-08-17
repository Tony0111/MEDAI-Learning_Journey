# 医学AI学习项目文件结构设计

## 项目概览
这是一个医学生的AI学习项目，整合了代码开发、论文研究、日志记录和AI反馈的完整工作流程。

## 推荐的文件结构

```
MEDAI-Learning-Project/
├── README.md                          # 项目总体介绍
├── .gitignore                         # Git忽略文件
├── requirements.txt                   # Python依赖包
├── config/                            # 配置文件
│   ├── ai_config.yaml                # AI模型配置
│   ├── pubmed_config.json            # PubMed爬虫配置
│   └── workflow_settings.json        # 工作流设置
├── scripts/                           # VSCode中的脚本文件
│   ├── __init__.py
│   ├── ai_models/                     # AI模型相关脚本
│   │   ├── __init__.py
│   │   ├── model_training.py          # 模型训练
│   │   ├── model_evaluation.py       # 模型评估
│   │   └── inference.py              # 推理脚本
│   ├── data_processing/               # 数据处理脚本
│   │   ├── __init__.py
│   │   ├── data_loader.py            # 数据加载
│   │   ├── preprocessing.py          # 数据预处理
│   │   └── feature_extraction.py     # 特征提取
│   ├── pubmed_crawler/                # 论文爬虫
│   │   ├── __init__.py
│   │   ├── crawler.py                # 主爬虫脚本
│   │   ├── parser.py                 # 论文解析
│   │   └── utils.py                  # 工具函数
│   └── utils/                         # 通用工具
│       ├── __init__.py
│       ├── file_manager.py           # 文件管理
│       ├── logger.py                 # 日志工具
│       └── ai_interface.py           # AI接口封装
├── obsidian_vault/                    # Obsidian知识库
│   ├── Templates/                     # Obsidian模板
│   │   ├── daily_log_template.md     # 日志模板
│   │   ├── paper_review_template.md  # 论文阅读模板
│   │   └── ai_feedback_template.md   # AI反馈模板
│   ├── Daily_Logs/                    # 日常学习日志
│   │   ├── 2024/
│   │   │   ├── 01-January/
│   │   │   ├── 02-February/
│   │   │   └── ...
│   │   └── README.md                 # 日志说明
│   ├── Paper_Reviews/                 # 论文阅读笔记
│   │   ├── By_Topic/                 # 按主题分类
│   │   │   ├── Medical_Imaging/
│   │   │   ├── NLP_in_Medicine/
│   │   │   ├── Drug_Discovery/
│   │   │   └── ...
│   │   ├── By_Date/                  # 按时间分类
│   │   │   ├── 2024-01/
│   │   │   ├── 2024-02/
│   │   │   └── ...
│   │   └── README.md                 # 阅读说明
│   ├── AI_Feedback/                   # AI反馈记录
│   │   ├── Code_Reviews/             # 代码审查反馈
│   │   ├── Learning_Progress/        # 学习进度反馈
│   │   └── Paper_Analysis/           # 论文分析反馈
│   ├── Knowledge_Base/                # 知识库
│   │   ├── Concepts/                 # 概念整理
│   │   ├── Techniques/               # 技术笔记
│   │   └── Resources/                # 资源汇总
│   └── .obsidian/                    # Obsidian配置（可选是否上传）
├── data/                              # 数据文件夹
│   ├── raw/                          # 原始数据
│   │   ├── papers/                   # 下载的论文PDF
│   │   └── datasets/                 # 数据集
│   ├── processed/                    # 处理后数据
│   └── outputs/                      # 输出结果
├── models/                           # 模型文件
│   ├── trained_models/               # 训练好的模型
│   ├── checkpoints/                  # 模型检查点
│   └── configs/                      # 模型配置
├── notebooks/                        # Jupyter笔记本
│   ├── exploratory/                  # 探索性分析
│   ├── experiments/                  # 实验记录
│   └── tutorials/                    # 学习教程
├── docs/                             # 项目文档
│   ├── workflow_guide.md             # 工作流程指南
│   ├── setup_instructions.md         # 环境设置说明
│   ├── ai_feedback_analysis.md       # AI反馈分析总结
│   └── learning_roadmap.md           # 学习路线图
└── automation/                       # 自动化脚本
    ├── sync_obsidian.py              # 同步Obsidian内容
    ├── generate_reports.py           # 生成学习报告
    └── backup_system.py              # 备份系统
```

## 文件夹详细说明

### 1. 根目录文件
- **README.md**: 项目介绍、使用方法、工作流程说明
- **.gitignore**: 忽略敏感文件、大文件、临时文件
- **requirements.txt**: Python依赖包列表

### 2. scripts/ - VSCode脚本区域
按功能模块化组织，便于代码复用和维护：
- **ai_models/**: 所有AI相关的代码
- **pubmed_crawler/**: 论文爬取专用脚本
- **data_processing/**: 数据处理工具
- **utils/**: 通用工具函数

### 3. obsidian_vault/ - Obsidian知识库
**设计原则**: 按内容类型和时间双重组织
- **Templates/**: 标准化模板，确保记录格式一致
- **Daily_Logs/**: 按年月组织的日常学习记录
- **Paper_Reviews/**: 论文笔记，同时支持主题和时间检索
- **AI_Feedback/**: AI反馈分类存储，便于后续分析
- **Knowledge_Base/**: 知识沉淀区域

### 4. 其他重要文件夹
- **data/**: 三级数据管理（原始→处理→输出）
- **models/**: 模型文件专区
- **notebooks/**: Jupyter实验记录
- **docs/**: 项目文档化
- **automation/**: 工作流自动化脚本

## 工作流程集成建议

### 1. 日常工作流程
```
1. VSCode中开发/实验 → scripts/对应模块
2. 写日志 → obsidian_vault/Daily_Logs/
3. Cherry Studio反馈 → obsidian_vault/AI_Feedback/
4. 论文爬取 → scripts/pubmed_crawler/ → data/raw/papers/
5. 论文阅读笔记 → obsidian_vault/Paper_Reviews/
```

### 2. 文件命名规范
- **日志文件**: `YYYY-MM-DD_daily_log.md`
- **论文笔记**: `YYYY-MM-DD_[论文标题简写].md`
- **AI反馈**: `YYYY-MM-DD_feedback_[类型].md`
- **脚本文件**: 使用小写字母和下划线，如`model_training.py`

### 3. Git管理建议
```bash
# .gitignore 应包含:
*.pdf                    # 避免上传大量论文PDF
data/raw/               # 原始数据不上传
models/trained_models/  # 训练好的模型文件
.obsidian/workspace*    # Obsidian工作区配置
__pycache__/           # Python缓存
*.log                  # 日志文件
config/*_secret*       # 包含API密钥的配置
```

## 推荐的自动化改进

### 1. 自动化脚本建议
创建以下自动化脚本提高效率：

```python
# automation/sync_obsidian.py
# 自动同步Obsidian笔记到对应文件夹
# 自动备份重要笔记

# automation/generate_reports.py  
# 定期生成学习进度报告
# 统计AI反馈趋势

# automation/backup_system.py
# 定期备份重要文件
# 清理临时文件
```

### 2. Cherry Studio集成
考虑创建API脚本直接与Cherry Studio交互：
```python
# scripts/utils/ai_interface.py
# 封装Cherry Studio API调用
# 自动化日志提交和反馈获取
```

## 使用建议

### 1. 初始化项目
1. 按结构创建文件夹
2. 复制Obsidian模板到Templates文件夹
3. 配置.gitignore文件
4. 编写详细的README.md

### 2. 日常维护
- 每周整理一次文件结构
- 定期备份Obsidian vault
- 月度回顾AI反馈，总结学习进展
- 季度重构代码，优化工作流

### 3. 分享建议
- 论文PDF不上传GitHub（版权问题）
- 敏感的API配置使用环境变量
- 提供详细的setup指南
- 考虑制作工作流程图

这个结构既保持了你现有工作流的完整性，又便于他人理解和贡献。随着项目发展，可以根据需要调整文件夹结构。