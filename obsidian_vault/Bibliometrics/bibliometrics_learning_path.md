# 文献计量学入门详细路径

## 核心目标
在4周内掌握文献计量学基础技能，为医学AI研究提供趋势分析和选题支持。

---

## 第一周：基础概念与数据收集

### Day 1-2: 理论基础速成

#### 📖 必读材料
1. **入门文章**：直接搜索"文献计量学 入门 综述"
2. **核心概念**：
   - 引文分析 (Citation Analysis)
   - 共被引分析 (Co-citation Analysis)  
   - 关键词共现分析 (Co-word Analysis)
   - 作者合作网络分析
   - h指数、影响因子等指标

#### 🎯 学习任务
- 理解文献计量学的4大核心分析方法
- 掌握常见指标的含义和应用场景
- **时间投入**：每天1小时，共2小时

### Day 3-5: 数据收集技能

#### 🔍 数据源选择
**医学AI文献主要来源**：
1. **PubMed** - 医学文献主库
2. **Web of Science** - 引文数据完整
3. **IEEE Xplore** - 计算机/工程技术
4. **Google Scholar** - 覆盖面广但数据质量参差

#### 📊 数据收集实践
**具体任务**：以"deep learning medical imaging"为主题
1. **PubMed检索**：
   - 检索式：`("deep learning"[MeSH] OR "neural networks"[MeSH]) AND "medical imaging"[MeSH]`
   - 时间范围：2019-2024
   - 导出格式：CSV/RIS

2. **Web of Science检索**：
   - 检索式：`TS=(("deep learning" OR "neural network*") AND "medical imag*")`
   - 数据库：SCI-E, CPCI-S
   - 导出格式：纯文本，包含引文信息

#### 🛠️ 工具准备
- **文献管理**：Zotero或EndNote
- **数据清洗**：Excel + Python pandas
- **时间投入**：每天1.5小时，共4.5小时

---

## 第二周：VOSviewer入门与实践

### Day 6-8: VOSviewer基础操作

#### 📥 软件安装与配置
1. 下载VOSviewer官方版本（免费）
2. 观看官方tutorial（YouTube，约30分钟）
3. 准备测试数据集

#### 🎨 基础分析实践
**任务1：关键词共现网络**
- 导入第一周收集的WoS数据
- 生成关键词共现图谱
- 调整参数：最小出现次数≥5
- 输出高清图片和网络数据

**任务2：作者合作网络**
- 分析核心作者群体
- 识别研究热点机构
- 生成作者合作图谱

**任务3：引文网络分析**
- 构建文献共被引网络
- 识别经典文献和研究脉络
- **时间投入**：每天2小时，共6小时

### Day 9-10: 高级可视化与解读

#### 🎯 进阶技巧
- **聚类算法选择**：了解不同聚类方法的适用场景
- **颜色和布局优化**：制作发表级别的图表
- **网络指标计算**：中心性、密度等网络特征

#### 📊 结果解读
- 学会从图谱中识别：
  - 研究热点和趋势
  - 核心作者和机构
  - 知识结构演变
  - 新兴研究方向

---

## 第三周：CiteSpace进阶分析

### Day 11-13: CiteSpace安装与基础操作

#### 🚀 软件准备
1. 下载CiteSpace最新版
2. 安装Java运行环境
3. 观看陈超美教授的入门视频教程

#### 🔄 时序分析实践
**CiteSpace独特优势**：时间切片分析

**任务1：突发词检测**
- 识别医学AI领域的新兴热点
- 生成时间轴突发词图谱
- 分析热点词汇的生命周期

**任务2：时区视图分析**
- 构建知识演化路径
- 识别里程碑文献
- 追踪技术发展脉络

#### 📈 趋势分析
- **双图叠加分析**：期刊分布模式
- **聚类时间线**：研究主题演变
- **时间投入**：每天2小时，共6小时

### Day 14: 对比分析与工具选择

#### ⚖️ VOSviewer vs CiteSpace
| 特性 | VOSviewer | CiteSpace |
|------|-----------|-----------|
| 易用性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 可视化美观度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 时序分析 | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| 网络分析 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 学习门槛 | 低 | 中等 |

**建议**：VOSviewer用于快速分析和美观展示，CiteSpace用于深度时序研究

---

## 第四周：Python编程增强与综合实践

### Day 15-17: Python文献计量学编程

#### 🐍 Python库生态
**核心库推荐**：
1. **scientometrics** - 专业文献计量学库
2. **pybliometrics** - Scopus API接口
3. **networkx** - 网络分析
4. **plotly** - 交互式可视化
5. **wordcloud** - 词云生成

#### 💻 编程实践项目
**项目**：医学AI发展趋势自动化分析系统

```python
# 示例代码框架
import pandas as pd
import networkx as nx
import plotly.graph_objects as go
from scientometrics import *

# 数据预处理
def clean_bibliometric_data(file_path):
    # 清洗WoS导出数据
    pass

# 网络构建
def build_coword_network(data):
    # 构建关键词共现网络
    pass

# 可视化
def create_interactive_network(G):
    # 创建交互式网络图
    pass
```

**功能目标**：
- 自动化数据收集和清洗
- 批量生成各类分析图表
- 生成HTML交互式报告
- **时间投入**：每天2.5小时，共7.5小时

### Day 18-21: 综合项目实战

#### 🎯 完整案例：《深度学习在医学影像中的十年发展轨迹》

**研究设计**：
1. **数据收集**：2014-2024年相关文献
2. **多维分析**：
   - 发文量趋势分析
   - 关键词演化路径
   - 核心作者网络
   - 期刊分布格局
   - 国际合作模式

**技术路线**：
- VOSviewer：关键词共现和作者合作
- CiteSpace：时序演化和突发检测  
- Python：数据整合和交互可视化
- 绘图技能：制作专业图表和信息图

**预期成果**：
- 5000字分析报告
- 10张高质量图表
- 1个交互式在线展示页面

---

## 文献计量学论文资源库

### 📚 顶级期刊
1. **Scientometrics** - 文献计量学顶级期刊
2. **Journal of Informetrics** - 信息计量学专业期刊  
3. **Research Policy** - 科技政策与评价
4. **Journal of the American Society for Information Science and Technology** - 信息科学

### 🔍 论文搜索策略
**数据库选择**：
- **Web of Science**：WC=Information Science & Library Science
- **Scopus**：SUBJAREA(COMP) AND SUBJAREA(SOCI)
- **PubMed**：仅医学领域的文献计量学研究

**检索词组合**：
```
("bibliometric*" OR "scientometric*" OR "informetric*") 
AND 
("medical imaging" OR "artificial intelligence" OR "deep learning")
```

### 📖 必读经典论文
1. **方法论经典**：
   - "Bibliometric methods in management and organization" (Zupic & Čater, 2015)
   - "Software survey: VOSviewer" (van Eck & Waltman, 2010)

2. **医学AI应用**：
   - "Artificial intelligence in healthcare: A bibliometric analysis" (2020)
   - "Deep learning in medical imaging: A bibliometric analysis" (2021)

### 🌐 开放资源
1. **Dimensions.ai** - 免费的科研数据库
2. **OpenCitations** - 开放引文数据
3. **Microsoft Academic Graph** - 微软学术图谱（已停服，但历史数据可用）
4. **arXiv** - 预印本论文，了解最新趋势

---

## 学习成果检验

### 🎯 第一周检验点
- [ ] 能解释5个核心文献计量学概念
- [ ] 能从PubMed和WoS收集到500+篇相关文献
- [ ] 数据格式转换和基础清洗

### 🎯 第二周检验点  
- [ ] 熟练使用VOSviewer生成3种网络图
- [ ] 能从图谱中识别研究热点和核心作者
- [ ] 输出发表级别的可视化图表

### 🎯 第三周检验点
- [ ] 掌握CiteSpace的时序分析功能
- [ ] 能识别突发词和演化路径
- [ ] 理解两种工具的适用场景差异

### 🎯 第四周检验点
- [ ] 完成Python自动化分析脚本
- [ ] 输出完整的文献计量学研究报告
- [ ] 具备独立开展文献计量学研究的能力

---

## 时间投入与学习节奏

| 周次 | 主要内容 | 每日时间 | 周总时间 |
|------|----------|----------|----------|
| 第1周 | 理论基础+数据收集 | 1-1.5h | 6.5h |
| 第2周 | VOSviewer实践 | 2h | 8h |  
| 第3周 | CiteSpace进阶 | 2h | 8h |
| 第4周 | Python编程+综合项目 | 2.5h | 10h |
| **总计** | - | - | **32.5h** |

**学习建议**：
- 保持每日学习连续性，避免间断
- 多实践少理论，边做边学效率最高
- 每周末总结，巩固所学知识
- 遇到问题及时记录，形成FAQ文档

---

## 与主线任务的整合

### 🔄 与深度学习学习的配合
- **9月**：文献计量学入门（每天1小时）+ ML基础学习（6-8小时）
- **10-11月**：持续关注医学AI文献趋势，为项目选题提供数据支持
- **12月**：使用文献计量学方法验证项目创新性和实用性

### 📊 为科研选题服务
通过文献计量学分析，你将能够：
- 识别医学AI的研究空白和机会
- 了解技术发展的时间节点和路径
- 找到潜在的合作导师和研究团队
- 预判未来3-5年的技术发展方向

这样，文献计量学就不是额外的学习负担，而是为你的深度学习研究提供战略指导的重要工具！