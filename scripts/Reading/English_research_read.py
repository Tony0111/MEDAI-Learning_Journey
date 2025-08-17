#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
医学文献阅读助手
用于帮助医学生高效阅读和分析英文医学文献

需要安装的依赖包:
pip install PyPDF2 requests
"""

# ====================================
# 📝 用户配置区域 - 请在这里修改你的设置
# ====================================

# PDF文件路径 - 填写你要分析的PDF文件完整路径
PDF_FILE_PATH = "D:\AI\Rsearch\Reading\App_of_AI_form2009to2024.pdf"  # 使用正斜杠

# 研究主题 - 描述你当前的研究方向或感兴趣的领域
# 心血管疾病的药物治疗机制
RESEARCH_TOPIC = "对medical image analyze产生整体性的认识"

# OpenRouter API配置
API_KEY = "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"  # 请填写你的OpenRouter API密钥
BASE_URL = "https://openrouter.ai/api/v1"  # 一般不需要修改

# 使用的AI模型 - 根据需求和预算选择
# 推荐选项：
# - "anthropic/claude-3-haiku" (便宜，速度快，适合日常使用)
# - "anthropic/claude-3-sonnet" (中等价格，质量好，推荐)
# - "anthropic/claude-3-opus" (最贵但质量最高，用于重要论文)
# - "openai/gpt-4o" (OpenAI的模型)
# google/gemini-2.5-flash-lite
# anthropic/claude-3.7-sonnet
MODEL = "google/gemini-2.5-flash-lite"

# ====================================
# 以下为程序代码，一般不需要修改
# ====================================

import pypdf
import requests
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime

class MedicalPaperReader:
    """医学文献阅读助手主类"""
    
    def __init__(self, api_key: str, base_url: str = "https://openrouter.ai/api/v1"):
        """
        初始化阅读助手
        
        Args:
            api_key: OpenRouter API密钥
            base_url: API基础URL
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """
        从PDF文件提取文本内容
        
        Args:
            pdf_path: PDF文件路径
            
        Returns:
            提取的文本内容
        """
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = pypdf.PdfReader(file)
                text = ""
                
                for page_num, page in enumerate(pdf_reader.pages):
                    try:
                        page_text = page.extract_text()
                        text += f"\n--- 第{page_num + 1}页 ---\n{page_text}\n"
                    except Exception as e:
                        print(f"警告: 第{page_num + 1}页提取失败: {e}")
                        continue
                
                return text
        
        except Exception as e:
            raise Exception(f"PDF文件读取失败: {e}")
    
    def split_text_into_chunks(self, text: str, max_chunk_size: int = 6000) -> List[str]:
        """
        将长文本分割成适合API处理的小块
        
        Args:
            text: 完整文本
            max_chunk_size: 每块最大字符数
            
        Returns:
            文本块列表
        """
        # 优先按段落分割
        paragraphs = text.split('\n\n')
        chunks = []
        current_chunk = ""
        
        for paragraph in paragraphs:
            if len(current_chunk) + len(paragraph) + 2 <= max_chunk_size:
                current_chunk += paragraph + "\n\n"
            else:
                if current_chunk.strip():
                    chunks.append(current_chunk.strip())
                current_chunk = paragraph + "\n\n"
        
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def call_openrouter_api(self, prompt: str, model: str = "anthropic/claude-3-haiku") -> str:
        """
        调用OpenRouter API
        
        Args:
            prompt: 提示词
            model: 使用的模型
            
        Returns:
            API响应内容
        """
        url = f"{self.base_url}/chat/completions"
        
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.3,
            "max_tokens": 4000
        }
        
        try:
            response = requests.post(url, headers=self.headers, json=payload, timeout=60)
            response.raise_for_status()
            
            result = response.json()
            return result['choices'][0]['message']['content']
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"API请求失败: {e}")
        except KeyError as e:
            raise Exception(f"API响应格式错误: {e}")
    
    def analyze_paper_structure(self, text: str, research_topic: str, model: str) -> Dict[str, str]:
        """
        分析论文结构并生成中文大纲
        
        Args:
            text: 论文文本
            research_topic: 研究主题
            model: 使用的模型
            
        Returns:
            包含大纲和分析结果的字典
        """
        prompt = f"""
作为一名资深医学教授，请分析以下英文医学文献，用户的研究主题是：{research_topic}

请提供以下分析：

1. **论文基本信息**
   - 标题（中英文）
   - 主要作者和机构
   - 发表期刊和时间
   - 研究类型（如：随机对照试验、系统评价、病例报告等）

2. **中文结构大纲**
   按照论文原有结构，提供详细的中文大纲，包括：
   - 各主要章节标题的中文翻译
   - 每个章节的主要内容概述
   - 重要的子章节

3. **与研究主题的关联性分析**
   - 该文献与用户研究主题的相关程度
   - 对用户研究有价值的具体内容
   - 可能的局限性

请用中文回答，格式清晰，便于医学生理解。

论文内容：
{text[:8000]}...
"""
        
        return {
            "outline": self.call_openrouter_api(prompt, model),
            "research_topic": research_topic
        }
    
    def generate_reading_guide(self, text: str, research_topic: str, model: str) -> str:
        """
        生成针对性阅读指导
        
        Args:
            text: 论文文本
            research_topic: 研究主题
            model: 使用的模型
            
        Returns:
            阅读指导内容
        """
        prompt = f"""
作为医学导师，请为正在研究"{research_topic}"的医学生提供这篇文献的阅读指导。

请提供：

1. **阅读策略建议**
   - 建议的阅读顺序
   - 应该重点关注的章节
   - 可以快速浏览的部分

2. **关键概念解释**
   - 文中重要的医学术语（英文+中文）
   - 关键的研究方法和统计概念
   - 需要补充的背景知识

3. **批判性思维引导**
   - 评估研究设计的要点
   - 结果解释的注意事项
   - 临床应用的考量

4. **与你研究的关联**
   - 这篇文献如何支持或挑战你的研究方向
   - 可以借鉴的研究方法
   - 值得进一步探讨的问题

请用通俗易懂的中文表达，适合医学生理解。

论文内容（部分）：
{text[:6000]}...
"""
        
        return self.call_openrouter_api(prompt, model)
    
    def generate_reading_questions(self, text: str, research_topic: str, model: str) -> str:
        """
        生成阅读问题
        
        Args:
            text: 论文文本
            research_topic: 研究主题
            model: 使用的模型
            
        Returns:
            阅读问题列表
        """
        prompt = f"""
基于这篇医学文献和用户的研究主题"{research_topic}"，请设计一系列阅读问题来帮助医学生深入理解和批判性分析这篇论文。

请提供以下类型的问题：

1. **理解性问题（5-6个）**
   - 检验对论文主要内容的理解
   - 包括研究目的、方法、结果、结论

2. **分析性问题（4-5个）**
   - 引导学生分析研究设计的优缺点
   - 评估证据质量和结论的可靠性

3. **应用性问题（3-4个）**
   - 如何将研究结果应用到临床实践
   - 对用户研究主题的启示

4. **批判性问题（3-4个）**
   - 研究的局限性和偏倚风险
   - 与其他研究的比较
   - 未来研究方向

每个问题都应该：
- 用中文表述
- 具有一定的思考深度
- 与研究主题相关

论文内容（部分）：
{text[:6000]}...
"""
        
        return self.call_openrouter_api(prompt, model)
    
    def identify_key_paragraphs(self, text: str, research_topic: str, model: str) -> str:
        """
        识别需要精读的关键段落
        
        Args:
            text: 论文文本
            research_topic: 研究主题
            model: 使用的模型
            
        Returns:
            关键段落推荐
        """
        prompt = f"""
作为医学文献分析专家，请从这篇论文中识别出最值得精读的段落，特别是与研究主题"{research_topic}"最相关的部分。

请提供：

1. **最重要的5-8个段落**
   对每个段落：
   - 简要说明段落位置（如"摘要第2段"、"讨论部分第3段"）
   - 解释为什么这个段落重要
   - 与研究主题的关联性
   - 阅读时应该注意的要点

2. **精读建议**
   - 这些段落的最佳阅读顺序
   - 需要对照阅读的段落组合
   - 阅读时应该做的笔记要点

3. **跳读建议**
   - 可以快速浏览的部分
   - 与当前研究主题关联度较低的章节

请用中文回答，并且具体指出段落内容的前几个词，便于定位。

论文内容：
{text[:8000]}...
"""
        
        return self.call_openrouter_api(prompt, model)
    
    def generate_comprehensive_report(self, pdf_path: str, research_topic: str, 
                                    model: str = "anthropic/claude-3-haiku") -> Dict[str, str]:
        """
        生成完整的文献分析报告
        
        Args:
            pdf_path: PDF文件路径
            research_topic: 研究主题
            model: 使用的模型
            
        Returns:
            包含所有分析结果的字典
        """
        print("正在提取PDF文本...")
        full_text = self.extract_text_from_pdf(pdf_path)
        
        if len(full_text.strip()) == 0:
            raise Exception("PDF文件中没有提取到文本内容，请检查文件是否为扫描版PDF")
        
        print(f"文本提取完成，共 {len(full_text)} 个字符")
        
        # 如果文本太长，使用前半部分进行分析
        analysis_text = full_text[:12000] if len(full_text) > 12000 else full_text
        
        results = {}
        
        print("正在生成论文大纲...")
        outline_data = self.analyze_paper_structure(analysis_text, research_topic, model)
        results["outline"] = outline_data["outline"]
        
        print("正在生成阅读指导...")
        results["reading_guide"] = self.generate_reading_guide(analysis_text, research_topic, model)
        
        print("正在生成阅读问题...")
        results["reading_questions"] = self.generate_reading_questions(analysis_text, research_topic, model)
        
        print("正在识别关键段落...")
        results["key_paragraphs"] = self.identify_key_paragraphs(analysis_text, research_topic, model)
        
        results["metadata"] = {
            "pdf_path": pdf_path,
            "research_topic": research_topic,
            "model_used": model,
            "analysis_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "text_length": len(full_text)
        }
        
        return results
    
    def save_report_to_file(self, results: Dict[str, str], output_path: str):
        """
        将分析结果保存到文件
        
        Args:
            results: 分析结果字典
            output_path: 输出文件路径
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# 医学文献阅读分析报告\n\n")
            f.write(f"**分析时间**: {results['metadata']['analysis_date']}\n")
            f.write(f"**PDF文件**: {results['metadata']['pdf_path']}\n")
            f.write(f"**研究主题**: {results['metadata']['research_topic']}\n")
            f.write(f"**使用模型**: {results['metadata']['model_used']}\n")
            f.write(f"**文本长度**: {results['metadata']['text_length']} 字符\n\n")
            f.write("---\n\n")
            
            f.write("## 📋 论文大纲\n\n")
            f.write(results["outline"])
            f.write("\n\n---\n\n")
            
            f.write("## 📚 阅读指导\n\n")
            f.write(results["reading_guide"])
            f.write("\n\n---\n\n")
            
            f.write("## ❓ 阅读问题\n\n")
            f.write(results["reading_questions"])
            f.write("\n\n---\n\n")
            
            f.write("## 🎯 精读段落推荐\n\n")
            f.write(results["key_paragraphs"])
            f.write("\n\n")


def main():
    """主函数"""
    # 检查配置
    if not PDF_FILE_PATH or PDF_FILE_PATH == "example_paper.pdf":
        print("❌ 请在脚本顶部的配置区域设置PDF_FILE_PATH")
        print("📝 编辑脚本，找到'用户配置区域'，填写正确的PDF文件路径")
        sys.exit(1)
    
    if not API_KEY or API_KEY == "sk-or-your-api-key-here":
        print("❌ 请在脚本顶部的配置区域设置API_KEY")
        print("📝 编辑脚本，找到'用户配置区域'，填写你的OpenRouter API密钥")
        sys.exit(1)
    
    if not RESEARCH_TOPIC:
        print("❌ 请在脚本顶部的配置区域设置RESEARCH_TOPIC")
        print("📝 编辑脚本，找到'用户配置区域'，描述你的研究主题")
        sys.exit(1)
    
    # 检查PDF文件是否存在
    pdf_path = Path(PDF_FILE_PATH)
    if not pdf_path.exists():
        print(f"❌ 错误: PDF文件 '{PDF_FILE_PATH}' 不存在")
        print("📝 请检查文件路径是否正确")
        sys.exit(1)
    
    # 生成输出文件路径（与输入文件相同目录）
    output_path = pdf_path.parent / f"{pdf_path.stem}_阅读分析_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    
    try:
        # 初始化阅读助手
        reader = MedicalPaperReader(API_KEY, BASE_URL)
        
        print("🏥 医学文献阅读助手")
        print("=" * 60)
        print(f"📄 PDF文件: {PDF_FILE_PATH}")
        print(f"🔬 研究主题: {RESEARCH_TOPIC}")
        print(f"🤖 使用模型: {MODEL}")
        print(f"💾 输出文件: {output_path}")
        print("=" * 60)
        
        # 生成分析报告
        results = reader.generate_comprehensive_report(
            PDF_FILE_PATH, 
            RESEARCH_TOPIC, 
            MODEL
        )
        
        # 保存结果
        reader.save_report_to_file(results, str(output_path))
        
        print(f"\n✅ 分析完成！")
        print(f"📁 分析报告已保存到: {output_path}")
        print("\n📋 生成的内容包括:")
        print("  • 📊 中文论文大纲")
        print("  • 📚 个性化阅读指导") 
        print("  • ❓ 深度思考问题")
        print("  • 🎯 精读段落推荐")
        print("\n💡 提示: 可以用Markdown编辑器或笔记软件打开分析报告")
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        print("\n🔧 常见解决方案:")
        print("  • 检查网络连接和API密钥")
        print("  • 确认PDF文件不是扫描版")
        print("  • 尝试使用更便宜的模型（如claude-3-haiku）")
        sys.exit(1)


if __name__ == "__main__":
    main()