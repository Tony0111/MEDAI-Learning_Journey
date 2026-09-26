# Zotero文献计量学完整指导手册

## 目录
1. [文献收集详细流程](#文献收集详细流程)
2. [数据预处理步骤](#数据预处理步骤)
3. [导出格式配置](#导出格式配置)
4. [VOSviewer数据准备](#vosviewer数据准备)
5. [CiteSpace数据准备](#citespace数据准备)
6. [实际操作示例](#实际操作示例)
7. [常见问题解决](#常见问题解决)
8. [学习资源推荐](#学习资源推荐)

---

## 文献收集详细流程

### 1. 数据库选择策略

#### 核心数据库
- **Web of Science (WoS)**：最权威的引文数据库，适合国际文献分析
- **Scopus**：覆盖面广，更新及时
- **Google Scholar**：覆盖灰色文献，但数据质量参差不齐

#### 学科专业数据库
- **PubMed**：生物医学领域
- **IEEE Xplore**：工程技术领域
- **CNKI**：中文文献主要来源
- **万方数据**：中文文献补充来源

### 2. 检索策略制定

#### 关键词组合原则
```
主题词 + 同义词 + 近义词 + 英文缩写

示例：人工智能领域
("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "neural network")
```

#### 布尔逻辑运算
- **AND**：缩小检索范围
- **OR**：扩大检索范围  
- **NOT**：排除无关文献

#### 检索式示例
```
主题检索：
TS=("artificial intelligence" OR "machine learning") AND TS=("healthcare" OR "medical")

时间限制：
PY=(2019-2024)

文献类型：
DT=(Article OR Review)
```

### 3. Zotero文献导入操作

#### 3.1 浏览器插件导入
1. 安装Zotero Connector浏览器插件
2. 在数据库检索结果页面点击Zotero图标
3. 选择要导入的文献（建议批量选择）
4. 确认导入到指定文件夹

#### 3.2 文件导入方式
1. 从数据库导出RIS/BibTeX格式文件
2. 在Zotero中选择"文件"→"导入"
3. 选择导出的文件进行批量导入

#### 3.3 DOI批量导入
1. 收集文献DOI列表
2. 使用"通过标识符添加"功能
3. 粘贴DOI列表，Zotero自动抓取元数据

### 4. 文献收集质量控制

#### 去重策略
- 使用Zotero内置去重功能："工具"→"重复条目"
- 手工检查相似标题的文献
- 核对DOI、PMID等唯一标识符

#### 质量筛选标准
- 发表年限：通常选择近5-10年
- 期刊影响因子：根据研究需要设定阈值
- 引用次数：筛选高被引文献
- 文献类型：优先选择期刊论文和综述

---

## 数据预处理步骤

### 1. 元数据标准化

#### 1.1 作者姓名标准化
```
问题：同一作者的不同表示方式
- Zhang Wei
- Zhang, W.
- Zhang, Wei
- W. Zhang

解决方案：
1. 在Zotero中统一作者姓名格式
2. 创建作者姓名对照表
3. 使用批量编辑工具统一格式
```

#### 1.2 机构名称标准化
```
常见问题：
- 中国科学院 vs Chinese Academy of Sciences
- 清华大学 vs Tsinghua University
- 缩写不统一：MIT vs Massachusetts Institute of Technology

处理方法：
1. 建立机构名称词典
2. 使用查找替换功能批量修改
3. 手动核查重要机构名称
```

#### 1.3 期刊名称标准化
```
统一原则：
- 使用期刊全名或标准缩写
- 避免同一期刊多种表示方式
- 参考JCR期刊缩写标准

示例：
Nature → Nature
Nat Commun → Nature Communications
```

### 2. 关键词预处理

#### 2.1 关键词提取与清洗
```python
# 关键词预处理示例（概念性）
常见问题：
- 大小写不统一：Machine Learning vs machine learning
- 单复数不统一：algorithm vs algorithms  
- 同义词：AI vs artificial intelligence
- 拼写错误：machien learning

处理步骤：
1. 转换为小写
2. 单复数统一
3. 同义词合并
4. 拼写检查
```

### 3. 数据完整性检查

#### 必需字段检查清单
- [ ] 标题 (Title)
- [ ] 作者 (Authors)
- [ ] 期刊名称 (Journal)
- [ ] 发表年份 (Year)
- [ ] 卷期号 (Volume/Issue)
- [ ] 页码 (Pages)
- [ ] DOI
- [ ] 关键词 (Keywords)
- [ ] 摘要 (Abstract)

#### 数据补全方法
1. **缺失DOI**：通过CrossRef API查询
2. **缺失关键词**：从摘要中提取
3. **缺失引文信息**：从引文数据库补充

---

## 导出格式配置

### 1. VOSviewer所需格式

#### 1.1 Web of Science格式导出
```
Zotero导出设置：
格式：Web of Science (Tagged)
文件扩展名：.txt
编码：UTF-8

导出字段包括：
- PT (Publication Type)
- AU (Authors)  
- TI (Title)
- SO (Source)
- PY (Publication Year)
- AB (Abstract)
- DE (Keywords)
- ID (Keywords Plus)
- CR (Cited References)
```

#### 1.2 导出操作步骤
1. 选择要导出的文献集合
2. 右键选择"导出文献集合"
3. 选择格式："Web of Science (Tagged)"
4. 勾选"导出文件"和"导出注释"
5. 点击确定保存为.txt文件

#### 1.3 VOSviewer导入设置
```
文件类型：Web of Science
分析单位：
- Authors：作者合作网络
- Keywords：关键词共现网络
- Sources：期刊引用网络
- Organizations：机构合作网络

阈值设置：
- 最小出现次数：根据数据量调整(通常2-5次)
- 最小引用次数：根据研究需要设定
```

### 2. CiteSpace所需格式

#### 2.1 Web of Science核心合集格式
```
CiteSpace要求严格的WoS格式：
文件命名：download_1-500.txt, download_501-1000.txt...
每个文件最多500条记录

必需字段：
UT (Unique Article Identifier)
AU (Authors)
TI (Title)  
SO (Source)
PY (Publication Year)
CR (Cited References)
```

#### 2.2 从Zotero准备CiteSpace数据
```
方法1：重新从WoS下载
1. 根据Zotero中的文献列表
2. 重新到WoS检索相同文献
3. 按CiteSpace要求导出

方法2：格式转换
1. 从Zotero导出RIS格式
2. 使用转换工具转为WoS格式
3. 手动调整字段映射
```

### 3. 其他常用格式

#### 3.1 Bibliometrix (R包) 格式
```
导出格式：BibTeX
文件扩展名：.bib
用途：R语言文献计量分析
```

#### 3.2 Gephi格式
```
导出格式：CSV (自定义)
包含字段：
- Source (来源节点)
- Target (目标节点)  
- Weight (权重)
用途：复杂网络可视化
```

---

## VOSviewer数据准备

### 1. 数据文件准备

#### 1.1 标准WoS格式文件
```
文件要求：
- 格式：纯文本(.txt)
- 编码：UTF-8
- 字段分隔：制表符或特定标记

示例文件结构：
PT J
AU Smith, J; Johnson, M; Brown, K
TI Analysis of machine learning in healthcare
SO NATURE MEDICINE
PY 2023
DE machine learning; healthcare; artificial intelligence
ID DEEP LEARNING; NEURAL NETWORKS
```

#### 1.2 自定义CSV文件
```csv
Id,Label,Authors,Year,Source,Keywords
1,"Machine learning in healthcare","Smith J; Johnson M",2023,"Nature Medicine","machine learning; healthcare"
2,"AI applications in medicine","Brown K; Davis L",2023,"Science","artificial intelligence; medical diagnosis"
```

### 2. VOSviewer分析类型配置

#### 2.1 作者合作网络
```
分析设置：
- 单位：Authors
- 最小文档数：2
- 最小引用数：5
- 网络类型：Co-authorship
```

#### 2.2 关键词共现网络
```
分析设置：
- 单位：All keywords / Author keywords
- 最小出现次数：5
- 网络类型：Co-occurrence
- 标准化方法：Association strength
```

#### 2.3 期刊引用网络
```
分析设置：
- 单位：Sources
- 最小文档数：3
- 最小引用数：10
- 网络类型：Citation / Co-citation
```

---

## CiteSpace数据准备

### 1. 严格的WoS格式要求

#### 1.1 文件命名规范
```
正确命名：
download_1-500.txt
download_501-1000.txt
download_1001-1500.txt

每个文件包含字段：
FN Thomson Reuters Web of Science™
VR 1.0
PT J
AU [作者列表]
TI [标题]
SO [期刊名]
PY [年份]
CR [引文列表]
ER
EF
```

#### 1.2 引文格式标准
```
标准引文格式：
Author, Year, Journal, Volume, Page

示例：
SMITH J, 2020, NATURE, V580, P123
JOHNSON M, 2019, SCIENCE, V365, P456
```

### 2. CiteSpace项目设置

#### 2.1 项目创建
```
项目参数：
- Time Slicing：年份范围(如2019-2024)
- Years Per Slice：时间切片(通常1年)
- Text Processing：选择标题、摘要、关键词
- Node Types：选择分析节点类型
```

#### 2.2 常用分析参数
```
聚类分析：
- k=50 (网络剪裁参数)
- Top N=50 (每个时间片选择的节点数)
- Selection Criteria：g-index, Top N%, Top N

可视化设置：
- Show Merged Network：显示合并网络
- Cluster View：聚类视图
- Timeline View：时间线视图
```

---

## 实际操作示例

### 示例：人工智能医疗应用研究

#### 1. 检索策略
```
Web of Science检索式：
TS=("artificial intelligence" OR "machine learning" OR "deep learning") 
AND TS=("medicine" OR "medical" OR "healthcare" OR "clinical")
AND PY=(2019-2024)
AND DT=(Article OR Review)

预期结果：约2000-5000篇文献
```

#### 2. Zotero收集流程
```
步骤1：在WoS执行检索
步骤2：全选检索结果(分批处理，每批500篇)
步骤3：使用Zotero Connector导入
步骤4：在Zotero中创建"AI_Healthcare_2019-2024"集合
步骤5：检查导入完整性，手动补充缺失信息
```

#### 3. 数据预处理
```
清理checklist：
□ 去除重复文献（预计去重率10-15%）
□ 标准化作者姓名（重点关注高产作者）
□ 统一机构名称（重点关注知名医学院校）
□ 清理关键词（合并同义词，如AI和artificial intelligence）
□ 补全缺失的DOI和摘要信息
□ 标记文献质量等级（根据期刊影响因子）
```

#### 4. 导出用于VOSviewer
```
导出设置：
- 选择"AI_Healthcare_2019-2024"集合
- 导出格式：Web of Science (Tagged)
- 文件名：AI_Healthcare_WoS.txt
- 确保包含所有必要字段

VOSviewer分析计划：
1. 关键词共现网络：识别研究热点
2. 作者合作网络：找出核心研究团队
3. 机构合作网络：分析国际合作模式
4. 期刊共引网络：了解学科知识基础
```

#### 5. 导出用于CiteSpace
```
由于CiteSpace对格式要求严格，建议：
1. 重新到WoS下载相同文献的标准格式
2. 按500篇一个文件的要求分割
3. 确保引文信息完整

CiteSpace分析计划：
1. 关键词突现分析：识别前沿趋势
2. 作者共引分析：确定知识基础
3. 期刊双图叠加：理解学科交叉
4. 时间线图谱：追踪研究演进
```

---

## 常见问题解决

### 1. 文献导入问题

#### Q1：Zotero无法识别某些数据库的文献
**解决方案：**
```
方法1：手动添加
- 使用DOI添加功能
- 通过ISBN或PMID添加
- 手动输入元数据

方法2：格式转换
- 导出RIS/BibTeX格式
- 使用第三方转换工具
- 导入到Zotero后手动调整
```

#### Q2：PDF文件无法自动下载
**解决方案：**
```
检查项目：
□ 是否在机构网络内
□ 数据库访问权限是否正常
□ Zotero代理设置是否正确
□ 使用Sci-Hub等工具补充（注意版权问题）
```

### 2. 数据质量问题

#### Q3：作者姓名格式不统一
**解决方案：**
```
批量处理步骤：
1. 导出作者列表到Excel
2. 使用查找替换功能统一格式
3. 创建作者姓名对照表
4. 重新导入到Zotero

常用正则表达式：
- 姓名分离：(\w+),\s*(\w+)
- 缩写统一：(\w)\.\s*(\w)\.
```

#### Q4：关键词混乱、重复
**解决方案：**
```
清理流程：
1. 导出所有关键词
2. 转换为小写
3. 去除标点符号
4. 合并同义词
5. 删除无意义词汇（如"study", "analysis"）

同义词词典示例：
AI = artificial intelligence
ML = machine learning  
DL = deep learning
```

### 3. 导出格式问题

#### Q5：VOSviewer无法识别导出文件
**解决方案：**
```
检查项目：
□ 文件编码是否为UTF-8
□ 字段标记是否正确
□ 是否包含必需字段
□ 文件大小是否合理

重新导出步骤：
1. 检查Zotero导出设置
2. 选择正确的导出格式
3. 验证导出文件内容
4. 必要时手动调整格式
```

#### Q6：CiteSpace报告数据格式错误
**解决方案：**
```
CiteSpace格式要求：
1. 必须是原始WoS格式
2. 文件命名必须符合规范
3. 引文信息必须完整
4. 字段分隔符必须正确

建议做法：
- 直接从WoS下载数据
- 不要使用Zotero转换的格式
- 分批下载，每批不超过500条
```

---

## 学习资源推荐

### 1. 官方文档和教程

#### Zotero官方资源
```
- 官方网站：https://www.zotero.org/
- 用户文档：https://www.zotero.org/support/
- 视频教程：https://www.zotero.org/support/screencast_tutorials
- 论坛支持：https://forums.zotero.org/
```

#### VOSviewer学习资源
```
- 官方网站：https://www.vosviewer.com/
- 用户手册：https://www.vosviewer.com/documentation/Manual_VOSviewer_1.6.18.pdf
- 在线教程：https://www.vosviewer.com/getting-started
- YouTube频道：搜索"VOSviewer tutorial"
```

#### CiteSpace学习资源  
```
- 官方网站：https://citespace.podia.com/
- 用户手册：http://cluster.cis.drexel.edu/~cchen/citespace/CiteSpaceManual.pdf
- 在线课程：https://citespace.podia.com/courses
- 开发者博客：http://cluster.cis.drexel.edu/~cchen/
```

### 2. 中文学习资源

#### 书籍推荐
```
1. 《文献计量学》- 邱均平著
2. 《科学计量学与科学评价》- 刘念才著  
3. 《信息可视化：交互设计》- Colin Ware著
4. 《网络科学引论》- 汪小帆著
```

#### 在线教程
```
- B站搜索关键词：
  * "Zotero教程"
  * "VOSviewer使用方法"  
  * "CiteSpace教程"
  * "文献计量学分析"

- 知乎专栏：
  * "文献计量与科学计量"
  * "学术写作与文献管理"
  * "数据可视化实践"
```

#### 学术期刊
```
国际期刊：
- Journal of Informetrics
- Scientometrics  
- Journal of the American Society for Information Science and Technology

中文期刊：
- 情报学报
- 图书情报工作
- 情报理论与实践
- 现代图书情报技术
```

### 3. 实践练习建议

#### 初学者练习路径
```
第1周：Zotero基础操作
- 安装配置Zotero和浏览器插件
- 练习从不同数据库导入文献
- 学习文献管理和整理方法

第2周：数据预处理
- 练习文献去重和数据清洗
- 学习元数据标准化方法
- 掌握导出不同格式的技巧

第3周：VOSviewer入门
- 安装VOSviewer软件
- 练习基础网络分析
- 学习结果解读和可视化调整

第4周：CiteSpace进阶
- 安装配置CiteSpace
- 练习时间序列分析
- 学习突现检测和聚类分析
```

#### 进阶项目建议
```
项目1：某领域研究现状分析
- 选择熟悉的研究领域
- 收集近10年相关文献
- 进行全面的文献计量分析

项目2：作者合作网络研究
- 选择特定学术群体
- 分析合作模式和演化趋势
- 识别核心作者和研究团队

项目3：前沿技术发展追踪
- 选择新兴技术领域
- 分析关键词演化和突现
- 预测未来发展趋势
```

### 4. 社区和交流

#### 在线社区
```
- Reddit：r/Zotero, r/AcademicWriting
- 学术Twitter：关注相关研究者
- ResearchGate：加入文献计量学群组
- 微信群：搜索"文献计量学交流群"
```

#### 会议和培训
```
国际会议：
- ISSI (International Society for Scientometrics and Informetrics)
- STI Conference (Science and Technology Indicators)

国内会议：
- 中国科学计量学与科技评价会议
- 全国情报学博士生论坛

在线培训：
- Coursera相关课程
- edX数据科学课程
- 各大学图书馆培训项目
```

---

## 总结

这份指南涵盖了使用Zotero进行文献计量学研究的完整流程，从文献收集到数据预处理，再到为VOSviewer和CiteSpace准备数据。关键要点：

1. **系统性**：建立完整的工作流程，确保数据质量
2. **标准化**：严格按照各工具的格式要求处理数据
3. **质量控制**：在每个环节都要进行质量检查
4. **持续学习**：文献计量学工具在不断更新，需要持续关注新功能

记住，工具只是手段，重要的是理解文献计量学的原理和方法，这样才能做出有意义的分析和解释。

**最后建议**：从小规模项目开始练习，逐步积累经验，不要急于处理大规模数据集。每个步骤都要仔细验证结果，确保分析的可靠性和有效性。