# scripts/ —— 科研小工具

这里放着三个**互相独立的工具链**，加一个通用工具。
每个工具链有独立文件夹，运行结果默认输出到其下的 `output/`（已在 `.gitignore` 中忽略）。

| 文件夹 | 工具链 | 入口 |
|---|---|---|
| `pubmed_hotspot/` | ① PubMed 研究热点分析 + CSV 翻译 | `Pubmed.py` |
| `paper_reading/` | ② 单篇英文文献精读 | `English_research_read.py` |
| `model_playground/` | ③ API 调用 / BioGPT 小实验 | `*.py` |
| `download_datasets.py` | 通用：下载数据集（MedNIST 等） | — |

---

## ① pubmed_hotspot —— PubMed 热点分析 + 翻译

```
pubmed_test.py           环境自检（可选）
      ↓
Pubmed.py                爬取 PubMed → 分析 → 出图/报告   → output/<主题>/
      ↓  (把 output/ 里的 csv 交给翻译脚本)
Translate_csv.py         翻译 → output/translated_result.md
```

```bash
# 1) 自检环境（可选）
python scripts/pubmed_hotspot/pubmed_test.py

# 2) 分析（默认输出到本工具 output/，用 --topic 分主题）
python scripts/pubmed_hotspot/Pubmed.py --topic specific_phobia

# 3) 翻译（需先在脚本里填 API Key）
python scripts/pubmed_hotspot/Translate_csv.py
```

- `Pubmed.spec`：PyInstaller 打包配置
- 详细用法见同目录 `pubmed_usage_guide.md` / `translate_usage_guide.md`

## ② paper_reading —— 单篇文献精读

读一个 PDF，调用大模型生成中文大纲 + 阅读指导，输出到本工具 `output/`。

```bash
python scripts/paper_reading/English_research_read.py
# 先编辑脚本顶部「用户配置区域」：PDF_FILE_PATH / RESEARCH_TOPIC / API_KEY / MODEL
```

## ③ model_playground —— 小实验（与上面两条线无关）

| 文件 | 作用 |
|---|---|
| `AI调用test.ipynb` | 测试 OpenRouter API 能否调通 |
| `test.py` | BioGPT 按英语水平给单词造句 |
| `test2.py` | BioGPT 续写医学文本 |
| `test.ipynb` | 上述实验的 notebook 版 |

## 通用工具

```bash
python scripts/download_datasets.py    # 下载 MedNIST 等数据集 → data/raw/datasets/
```

## 约定

- **API 密钥**：脚本里是占位符（如 `sk-your-api-key-here`），用自己的密钥替换，**不要提交真实密钥**。
- **运行结果**：统一写到各工具的 `output/` 目录，不进 Git。
