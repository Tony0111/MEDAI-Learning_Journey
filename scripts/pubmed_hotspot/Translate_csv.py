import pandas as pd
import requests
import json
import time
import sys
from pathlib import Path


'''
看这里！
看这里！
看这里！
看这里！
看这里！
看这里！

使用时，替换为可用的API Key

看这里！
看这里！
看这里！
看这里！
看这里！
看这里！
'''

# ==================== 配置区域 ====================
# 在这里修改你的配置信息

# CSV文件路径（默认为本工具 output/ 目录下的 PubMed 分析结果）
CSV_FILE_PATH = str(Path(__file__).resolve().parent / "output" / "pubmed_research_data.csv")

# DeepSeek API密钥（请替换为你自己的密钥）
API_KEY = "sk-your-api-key-here"

# 要翻译的列名（列表格式）
COLUMNS_TO_TRANSLATE = ["title", "abstract"]

# 输出文件名（不包含路径，将保存在CSV文件同一目录下）
OUTPUT_FILE_NAME = "translated_result.md"

# 源语言
SOURCE_LANGUAGE = "英文"

# 目标语言
TARGET_LANGUAGE = "中文"

# 请求间隔时间（秒，避免API限制）
REQUEST_DELAY = 4

# ==================== 配置区域结束 ====================


class DeepSeekTranslator:
    def __init__(self, api_key, base_url="https://api.deepseek.com/v1/chat/completions"):
        """
        初始化DeepSeek翻译器
        
        Args:
            api_key (str): DeepSeek API密钥
            base_url (str): API基础URL
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def translate_text(self, text, target_language="中文", source_language="英文"):
        """
        翻译单个文本
        
        Args:
            text (str): 要翻译的文本
            target_language (str): 目标语言
            source_language (str): 源语言
            
        Returns:
            str: 翻译后的文本
        """
        if not text or pd.isna(text):
            return ""
        
        prompt = f"请将以下{source_language}文本翻译成{target_language}，只返回翻译结果，不要添加任何解释：\n{text}"
        
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.1,
            "max_tokens": 1000
        }
        
        try:
            response = requests.post(self.base_url, headers=self.headers, json=data, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            translated_text = result['choices'][0]['message']['content'].strip()
            return translated_text
        
        except requests.exceptions.RequestException as e:
            print(f"API请求错误: {e}")
            return text  # 翻译失败时返回原文
        except KeyError as e:
            print(f"响应解析错误: {e}")
            return text
        except Exception as e:
            print(f"未知错误: {e}")
            return text

def translate_csv_to_markdown():
    """
    根据配置翻译CSV文件并生成Markdown文件
    """
    
    # 检查配置
    if API_KEY == "sk-your-api-key-here":
        print("错误: 请先在脚本中配置您的API密钥")
        return
    
    # 检查CSV文件是否存在
    csv_path = Path(CSV_FILE_PATH)
    if not csv_path.exists():
        print(f"错误: CSV文件 '{CSV_FILE_PATH}' 不存在")
        return
    
    # 读取CSV文件
    try:
        df = pd.read_csv(CSV_FILE_PATH, encoding='utf-8')
        print(f"成功读取CSV文件，共 {len(df)} 行数据")
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(CSV_FILE_PATH, encoding='gbk')
            print(f"使用GBK编码读取CSV文件，共 {len(df)} 行数据")
        except Exception as e:
            print(f"读取CSV文件失败: {e}")
            return
    except Exception as e:
        print(f"读取CSV文件失败: {e}")
        return
    
    # 显示CSV文件的列信息
    print(f"CSV文件包含的列: {list(df.columns)}")
    
    # 检查要翻译的列是否存在
    missing_columns = [col for col in COLUMNS_TO_TRANSLATE if col not in df.columns]
    if missing_columns:
        print(f"错误: 以下列在CSV文件中不存在: {missing_columns}")
        print(f"可用的列: {list(df.columns)}")
        return
    
    print(f"将要翻译的列: {COLUMNS_TO_TRANSLATE}")
    print(f"翻译语言: {SOURCE_LANGUAGE} → {TARGET_LANGUAGE}")
    print(f"请求间隔: {REQUEST_DELAY} 秒")
    
    # 初始化翻译器
    translator = DeepSeekTranslator(API_KEY)
    
    # 创建翻译后的数据框副本
    translated_df = df.copy()
    
    # 翻译指定列
    for column in COLUMNS_TO_TRANSLATE:
        print(f"\n开始翻译列: {column}")
        translated_column_name = f"{column}_translated"
        translated_df[translated_column_name] = ""
        
        for index, row in df.iterrows():
            original_text = str(row[column])
            print(f"正在翻译第 {index + 1}/{len(df)} 行: {original_text[:50]}...")
            
            translated_text = translator.translate_text(
                original_text, 
                target_language=TARGET_LANGUAGE, 
                source_language=SOURCE_LANGUAGE
            )
            
            translated_df.at[index, translated_column_name] = translated_text
            print(f"翻译结果: {translated_text[:50]}...")
            
            # 添加延迟避免API限制
            if REQUEST_DELAY > 0:
                time.sleep(REQUEST_DELAY)
    
    # 确定输出文件路径（与CSV文件在同一目录）
    output_path = csv_path.parent / OUTPUT_FILE_NAME
    
    # 生成Markdown内容
    markdown_content = []
    markdown_content.append(f"# CSV翻译结果\n")
    markdown_content.append(f"**原文件**: {CSV_FILE_PATH}")
    markdown_content.append(f"**翻译时间**: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    markdown_content.append(f"**翻译语言**: {SOURCE_LANGUAGE} → {TARGET_LANGUAGE}")
    markdown_content.append(f"**翻译列**: {', '.join(COLUMNS_TO_TRANSLATE)}")
    markdown_content.append(f"**总行数**: {len(df)} 行\n")
    
    # 创建表格
    all_columns = []
    for col in df.columns:
        all_columns.append(col)
        if col in COLUMNS_TO_TRANSLATE:
            all_columns.append(f"{col}_translated")
    
    # 表格标题行
    header_row = "| " + " | ".join(all_columns) + " |"
    separator_row = "| " + " | ".join(["---"] * len(all_columns)) + " |"
    
    markdown_content.append(header_row)
    markdown_content.append(separator_row)
    
    # 表格数据行
    for index, row in translated_df.iterrows():
        data_row = []
        for col in df.columns:
            cell_content = str(row[col]) if not pd.isna(row[col]) else ""
            # 转义Markdown特殊字符
            cell_content = cell_content.replace('|', '\\|').replace('\n', '<br>').replace('\r', '')
            data_row.append(cell_content)
            
            if col in COLUMNS_TO_TRANSLATE:
                translated_col = f"{col}_translated"
                translated_content = str(row[translated_col]) if not pd.isna(row[translated_col]) else ""
                translated_content = translated_content.replace('|', '\\|').replace('\n', '<br>').replace('\r', '')
                data_row.append(translated_content)
        
        markdown_row = "| " + " | ".join(data_row) + " |"
        markdown_content.append(markdown_row)
    
    # 写入Markdown文件
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(markdown_content))
        print(f"\n✅ 翻译完成! Markdown文件已保存到: {output_path}")
        print(f"📊 总共翻译了 {len(df)} 行数据，{len(COLUMNS_TO_TRANSLATE)} 个列")
    except Exception as e:
        print(f"❌ 保存Markdown文件失败: {e}")

def main():
    """
    主函数
    """
    print("=== CSV翻译工具 ===")
    print("正在使用以下配置进行翻译:")
    print(f"📁 CSV文件: {CSV_FILE_PATH}")
    print(f"🔑 API密钥: {'已配置' if API_KEY != 'sk-your-api-key-here' else '❌ 未配置'}")
    print(f"📝 翻译列: {COLUMNS_TO_TRANSLATE}")
    print(f"💾 输出文件: {OUTPUT_FILE_NAME}")
    print(f"🌍 翻译: {SOURCE_LANGUAGE} → {TARGET_LANGUAGE}")
    print(f"⏱️ 请求间隔: {REQUEST_DELAY} 秒")
    print("-" * 50)
    
    translate_csv_to_markdown()

if __name__ == "__main__":
    main()