# CSV翻译脚本使用说明（配置版）

## 功能介绍
此Python脚本可以读取CSV文件，调用DeepSeek API翻译其中指定的列，并将结果保存为Markdown格式文件。所有配置集中在脚本顶部，方便修改。

## 环境要求
- Python 3.12
- Windows系统

## 安装依赖包

在命令提示符或PowerShell中运行以下命令安装必需的依赖包：

```bash
pip install pandas requests
```

## 获取DeepSeek API密钥

1. 访问 [DeepSeek官网](https://platform.deepseek.com/)
2. 注册账号并登录
3. 在控制台中获取API密钥
4. 确保账户有足够的余额

## 使用方法

### 步骤1：配置脚本参数

在脚本顶部的配置区域修改以下参数：

```python
# ==================== 配置区域 ====================
# 在这里修改你的配置信息

# CSV文件路径
CSV_FILE_PATH = "data.csv"

# DeepSeek API密钥
API_KEY = "sk-your-api-key-here"

# 要翻译的列名（列表格式）
COLUMNS_TO_TRANSLATE = ["title", "description"]

# 输出文件名（不包含路径，将保存在CSV文件同一目录下）
OUTPUT_FILE_NAME = "translated_result.md"

# 源语言
SOURCE_LANGUAGE = "英文"

# 目标语言
TARGET_LANGUAGE = "中文"

# 请求间隔时间（秒，避免API限制）
REQUEST_DELAY = 1

# ==================== 配置区域结束 ====================
```

### 步骤2：修改配置示例

#### 配置示例1：英译中
```python
CSV_FILE_PATH = "D:/data/products.csv"  # 绝对路径
API_KEY = "sk-1234567890abcdef"
COLUMNS_TO_TRANSLATE = ["product_name", "description", "features"]
OUTPUT_FILE_NAME = "products_translated.md"
SOURCE_LANGUAGE = "英文"
TARGET_LANGUAGE = "中文"
REQUEST_DELAY = 2  # 每2秒一次请求
```

#### 配置示例2：中译英
```python
CSV_FILE_PATH = "./input/articles.csv"  # 相对路径
API_KEY = "sk-abcdef1234567890"
COLUMNS_TO_TRANSLATE = ["标题", "内容"]
OUTPUT_FILE_NAME = "articles_en.md"
SOURCE_LANGUAGE = "中文"
TARGET_LANGUAGE = "英文"
REQUEST_DELAY = 1
```

#### 配置示例3：其他语言
```python
CSV_FILE_PATH = "news.csv"
API_KEY = "sk-your-real-api-key"
COLUMNS_TO_TRANSLATE = ["headline", "summary"]
OUTPUT_FILE_NAME = "news_japanese.md"
SOURCE_LANGUAGE = "英文"
TARGET_LANGUAGE = "日文"
REQUEST_DELAY = 1.5  # 支持小数
```

### 步骤3：运行脚本

保存配置后，在命令提示符中运行：

```bash
python csv_translator.py
```

## 配置参数说明

| 参数 | 类型 | 说明 | 示例 |
|------|------|------|------|
| `CSV_FILE_PATH` | 字符串 | CSV文件的路径，支持相对路径和绝对路径 | `"data.csv"` 或 `"D:/files/data.csv"` |
| `API_KEY` | 字符串 | DeepSeek API密钥 | `"sk-1234567890abcdef"` |
| `COLUMNS_TO_TRANSLATE` | 列表 | 要翻译的列名列表 | `["title", "content"]` |
| `OUTPUT_FILE_NAME` | 字符串 | 输出的Markdown文件名 | `"result.md"` |
| `SOURCE_LANGUAGE` | 字符串 | 源语言 | `"英文"`, `"中文"`, `"日文"` 等 |
| `TARGET_LANGUAGE` | 字符串 | 目标语言 | `"中文"`, `"英文"`, `"日文"` 等 |
| `REQUEST_DELAY` | 数字 | 请求间隔时间（秒） | `1`, `1.5`, `2` |

## 路径配置说明

### 相对路径示例：
- `"data.csv"` - 脚本同目录下的文件
- `"./input/data.csv"` - 脚本目录下input文件夹中的文件
- `"../data.csv"` - 脚本上级目录中的文件

### 绝对路径示例：
- `"D:/projects/data.csv"` - Windows绝对路径
- `"C:/Users/用户名/Documents/data.csv"` - 含中文的路径

### 输出文件位置：
输出的Markdown文件将自动保存在CSV文件的同一目录下，文件名由 `OUTPUT_FILE_NAME` 参数指定。

## 运行示例

配置完成后运行脚本，输出如下：

```
=== CSV翻译工具 ===
正在使用以下配置进行翻译:
📁 CSV文件: data.csv
🔑 API密钥: 已配置
📝 翻译列: ['title', 'description']
💾 输出文件: translated_result.md
🌍 翻译: 英文 → 中文
⏱️ 请求间隔: 1 秒
--------------------------------------------------
成功读取CSV文件，共 3 行数据
CSV文件包含的列: ['id', 'title', 'description', 'category']
将要翻译的列: ['title', 'description']
翻译语言: 英文 → 中文

开始翻译列: title
正在翻译第 1/3 行: Hello World...
翻译结果: 你好世界...
正在翻译第 2/3 行: Python Guide...
翻译结果: Python指南...

开始翻译列: description
正在翻译第 1/3 行: This is a sample text...
翻译结果: 这是一个示例文本...

✅ 翻译完成! Markdown文件已保存到: data_translated.md
📊 总共翻译了 3 行数据，2 个列
```

## 输出结果

生成的Markdown文件包含：
- 翻译信息摘要
- 包含原文和译文的对比表格
- 所有非翻译列的原始数据

### 输出文件示例：
```markdown
# CSV翻译结果

**原文件**: data.csv
**翻译时间**: 2024-12-19 10:30:00
**翻译语言**: 英文 → 中文
**翻译列**: title, description
**总行数**: 3 行

| id | title | title_translated | description | description_translated | category |
| --- | --- | --- | --- | --- | --- |
| 1 | Hello World | 你好世界 | This is a sample text | 这是一个示例文本 | Tech |
| 2 | Python Guide | Python指南 | Learn Python programming | 学习Python编程 | Education |
```

## 注意事项

1. **配置检查**：运行前确保所有配置参数正确
2. **API密钥**：必须替换默认的API密钥，否则无法运行
3. **列名准确性**：确保 `COLUMNS_TO_TRANSLATE` 中的列名与CSV文件完全匹配
4. **文件路径**：支持中文路径，建议使用绝对路径避免路径问题
5. **请求间隔**：根据API限制调整 `REQUEST_DELAY`，避免请求过于频繁

## 常见错误及解决方法

| 错误信息 | 原因 | 解决方法 |
|----------|------|----------|
| `请先在脚本中配置您的API密钥` | 未修改默认API密钥 | 在配置区域设置真实的API密钥 |
| `CSV文件不存在` | 文件路径错误 | 检查 `CSV_FILE_PATH` 是否正确 |
| `以下列在CSV文件中不存在` | 列名不匹配 | 检查 `COLUMNS_TO_TRANSLATE` 中的列名 |
| `API请求错误` | 网络或API问题 | 检查网络连接和API密钥有效性 |

## 进阶配置

如需自定义更多参数，可以修改 `DeepSeekTranslator` 类中的以下设置：

- `temperature`: 翻译的创造性（0-1之间，默认0.1）
- `max_tokens`: 最大返回长度（默认1000）
- `timeout`: 请求超时时间（默认30秒）

这种配置方式让你可以快速批量处理多个翻译任务，只需要修改配置参数即可。