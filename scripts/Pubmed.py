#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PubMed医学研究热点分析工具
作者：为医学生定制
功能：分析PubMed数据库中的研究热点和趋势
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
from datetime import datetime, timedelta
import time
import json
import jieba
from wordcloud import WordCloud
import numpy as np
from urllib.parse import quote
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

class PubMedHotspotAnalyzer:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.base_url = "https://pubmed.ncbi.nlm.nih.gov"
        self.results = []
        
    def search_pubmed(self, query, max_results=500, years_back=2):
        """搜索PubMed数据库"""
        print(f"正在搜索关键词: {query}")
        print(f"搜索范围: 最近{years_back}年，最多{max_results}条结果")
        
        # 构建时间范围
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365 * years_back)
        date_range = f"{start_date.year}:{end_date.year}"
        
        # 构建搜索URL - 使用更简单的格式
        encoded_query = quote(f'{query}')
        url = f"{self.base_url}/?term={encoded_query}&filter=years.{date_range}&sort=date&size=200"
        
        page = 1
        total_collected = 0
        
        while total_collected < max_results and page <= 10:  # 限制最大页数
            try:
                if page == 1:
                    page_url = url
                else:
                    page_url = f"{url}&page={page}"
                    
                print(f"正在爬取第{page}页: {page_url}")
                
                response = requests.get(page_url, headers=self.headers, timeout=15)
                response.raise_for_status()
                
                print(f"HTTP状态码: {response.status_code}")
                
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # 尝试多种可能的文章容器
                articles = (soup.find_all('article', class_='full-docsum') or 
                          soup.find_all('div', class_='docsum-wrap') or
                          soup.find_all('div', class_='rprt'))
                
                print(f"找到 {len(articles)} 个文章元素")
                
                if not articles:
                    # 如果没找到文章，打印页面部分内容用于调试
                    print("未找到文章，页面内容预览:")
                    page_text = soup.get_text()[:500]
                    print(page_text)
                    
                    # 尝试查找标题链接
                    title_links = soup.find_all('a', href=re.compile(r'/\d+/'))
                    print(f"找到 {len(title_links)} 个可能的标题链接")
                    
                    if title_links:
                        for i, link in enumerate(title_links[:5]):  # 处理前5个
                            if total_collected >= max_results:
                                break
                            title = link.get_text().strip()
                            if title and len(title) > 10:  # 确保是有意义的标题
                                # 尝试获取PMID
                                href = link.get('href', '')
                                pmid_match = re.search(r'/(\d+)/', href)
                                pmid = pmid_match.group(1) if pmid_match else f"link_{i}"
                                
                                self.results.append({
                                    'title': title,
                                    'authors': "未知",
                                    'journal_info': "未知",
                                    'abstract': "",
                                    'pmid': pmid,
                                    'search_query': query
                                })
                                total_collected += 1
                                print(f"找到文章: {title[:50]}...")
                    
                    if total_collected == 0:
                        break
                else:
                    # 处理找到的文章
                    for article in articles:
                        if total_collected >= max_results:
                            break
                            
                        try:
                            # 多种方式尝试提取标题
                            title_elem = (article.find('a', class_='docsum-title') or 
                                        article.find('a', class_='docsum-title') or
                                        article.find('h1') or 
                                        article.find('a', href=re.compile(r'/\d+/')))
                            
                            title = title_elem.text.strip() if title_elem else "无标题"
                            
                            if not title or title == "无标题" or len(title) < 10:
                                continue
                            
                            # 提取作者
                            authors_elem = (article.find('span', class_='docsum-authors') or
                                          article.find('div', class_='docsum-authors'))
                            authors = authors_elem.text.strip() if authors_elem else "无作者信息"
                            
                            # 提取期刊和日期
                            journal_elem = (article.find('span', class_='docsum-journal-citation') or
                                          article.find('div', class_='docsum-journal-citation'))
                            journal_info = journal_elem.text.strip() if journal_elem else "无期刊信息"
                            
                            # 提取摘要
                            abstract_elem = (article.find('div', class_='docsum-snippet') or
                                           article.find('p', class_='docsum-snippet'))
                            abstract = abstract_elem.text.strip() if abstract_elem else ""
                            
                            # 提取PMID
                            pmid = (article.get('data-pmid') or 
                                   article.get('data-uid') or
                                   f"unknown_{total_collected}")
                            
                            self.results.append({
                                'title': title,
                                'authors': authors,
                                'journal_info': journal_info,
                                'abstract': abstract,
                                'pmid': pmid,
                                'search_query': query
                            })
                            
                            total_collected += 1
                            print(f"收集文章 {total_collected}: {title[:50]}...")
                            
                        except Exception as e:
                            print(f"解析文章时出错: {e}")
                            continue
                
                print(f"第{page}页完成，已收集{total_collected}篇文章")
                
                if total_collected == 0 and page == 1:
                    print("第一页没有找到任何文章，可能是搜索词问题或网站结构变化")
                    break
                    
                page += 1
                time.sleep(2)  # 增加延时避免被封
                
            except Exception as e:
                print(f"请求第{page}页时出错: {e}")
                break
        
        print(f"搜索完成！共收集到{total_collected}篇相关文章")
        
        if total_collected == 0:
            print("建议检查:")
            print("1. 网络连接是否正常")
            print("2. 搜索词是否正确（建议使用英文）")
            print("3. PubMed是否可正常访问")
            
    def search_pubmed_api(self, query, max_results=500, years_back=2):
        """使用PubMed E-utilities API搜索（备用方法）"""
        print(f"使用API方式搜索关键词: {query}")
        
        # E-utilities base URLs
        esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        efetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        
        # 构建时间范围
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365 * years_back)
        date_filter = f"{start_date.year}:{end_date.year}[pdat]"
        
        # 构建搜索查询
        search_term = f"{query} AND {date_filter}"
        
        try:
            # 第一步：搜索获取PMID列表
            esearch_params = {
                'db': 'pubmed',
                'term': search_term,
                'retmax': min(max_results, 1000),  # API限制
                'retmode': 'json',
                'sort': 'pub+date',
                'usehistory': 'y'
            }
            
            print("正在搜索PMID...")
            search_response = requests.get(esearch_url, params=esearch_params, timeout=15)
            search_response.raise_for_status()
            
            search_data = search_response.json()
            
            if 'esearchresult' not in search_data:
                print("API搜索失败")
                return []
            
            pmid_list = search_data['esearchresult'].get('idlist', [])
            total_found = int(search_data['esearchresult'].get('count', 0))
            
            print(f"找到 {total_found} 篇相关文章，获取前 {len(pmid_list)} 篇详细信息")
            
            if not pmid_list:
                print("没有找到相关文章")
                return []
            
            # 第二步：批量获取文章详细信息
            batch_size = 50  # 每批处理50篇文章
            
            for i in range(0, len(pmid_list), batch_size):
                batch_pmids = pmid_list[i:i + batch_size]
                pmid_string = ','.join(batch_pmids)
                
                print(f"正在获取第 {i//batch_size + 1} 批文章信息 ({len(batch_pmids)} 篇)...")
                
                efetch_params = {
                    'db': 'pubmed',
                    'id': pmid_string,
                    'retmode': 'xml',
                    'rettype': 'abstract'
                }
                
                try:
                    fetch_response = requests.get(efetch_url, params=efetch_params, timeout=15)
                    fetch_response.raise_for_status()
                    
                    # 解析XML
                    soup = BeautifulSoup(fetch_response.content, 'xml')
                    articles = soup.find_all('PubmedArticle')
                    
                    for article in articles:
                        try:
                            # 提取PMID
                            pmid_elem = article.find('PMID')
                            pmid = pmid_elem.text if pmid_elem else "未知"
                            
                            # 提取标题
                            title_elem = article.find('ArticleTitle')
                            title = title_elem.text if title_elem else "无标题"
                            
                            # 提取作者
                            authors = []
                            author_list = article.find('AuthorList')
                            if author_list:
                                for author in author_list.find_all('Author'):
                                    lastname = author.find('LastName')
                                    forename = author.find('ForeName')
                                    if lastname:
                                        name = lastname.text
                                        if forename:
                                            name += f" {forename.text}"
                                        authors.append(name)
                            
                            authors_str = ', '.join(authors[:5]) if authors else "无作者信息"
                            if len(authors) > 5:
                                authors_str += " et al."
                            
                            # 提取期刊信息
                            journal_elem = article.find('Title')  # 期刊标题
                            pub_date = article.find('PubDate')
                            year = ""
                            if pub_date:
                                year_elem = pub_date.find('Year')
                                if year_elem:
                                    year = year_elem.text
                            
                            journal_info = ""
                            if journal_elem:
                                journal_info = journal_elem.text
                            if year:
                                journal_info += f" ({year})"
                            
                            # 提取摘要
                            abstract_elem = article.find('AbstractText')
                            abstract = abstract_elem.text if abstract_elem else ""
                            
                            self.results.append({
                                'title': title,
                                'authors': authors_str,
                                'journal_info': journal_info,
                                'abstract': abstract,
                                'pmid': pmid,
                                'search_query': query
                            })
                            
                        except Exception as e:
                            print(f"解析单篇文章时出错: {e}")
                            continue
                    
                except Exception as e:
                    print(f"获取第 {i//batch_size + 1} 批文章时出错: {e}")
                    continue
                
                time.sleep(1)  # API调用间隔
            
            print(f"API搜索完成！共收集到 {len(self.results)} 篇文章")
            return self.results
            
        except Exception as e:
            print(f"API搜索出错: {e}")
            return []
    
    def analyze_keywords(self, text_field='title'):
        """分析关键词频率"""
        if not self.results:
            print("没有数据可分析，请先运行搜索")
            return
        
        print(f"正在分析{text_field}中的关键词...")
        
        # 合并所有文本
        all_text = ""
        for result in self.results:
            text = result.get(text_field, "")
            if text:
                all_text += " " + text.lower()
        
        # 移除常见的停用词
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
            'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these',
            'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'study', 'studies',
            'research', 'analysis', 'results', 'conclusion', 'background', 'objective',
            'method', 'methods', 'discussion', 'patient', 'patients'
        }
        
        # 提取单词和短语
        words = re.findall(r'\b[a-zA-Z]{3,}\b', all_text)
        filtered_words = [word for word in words if word not in stop_words]
        
        # 统计词频
        word_freq = Counter(filtered_words)
        
        return word_freq.most_common(30)
    
    def analyze_journals(self):
        """分析热门期刊"""
        if not self.results:
            print("没有数据可分析，请先运行搜索")
            return
        
        print("正在分析期刊分布...")
        
        journals = []
        for result in self.results:
            journal_info = result.get('journal_info', '')
            if journal_info:
                # 提取期刊名称（通常在第一个点号之前）
                journal_name = journal_info.split('.')[0].strip()
                if journal_name and len(journal_name) > 3:
                    journals.append(journal_name)
        
        journal_freq = Counter(journals)
        return journal_freq.most_common(20)
    
    def generate_visualizations(self):
        """生成可视化图表"""
        if not self.results:
            print("没有数据可分析，请先运行搜索")
            return
        
        print("正在生成可视化图表...")
        
        # 创建图表
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('PubMed研究热点分析报告', fontsize=16, fontweight='bold')
        
        # 1. 关键词词频图
        keywords = self.analyze_keywords()
        if keywords:
            words, freqs = zip(*keywords[:15])
            axes[0, 0].barh(range(len(words)), freqs)
            axes[0, 0].set_yticks(range(len(words)))
            axes[0, 0].set_yticklabels(words)
            axes[0, 0].set_title('热门研究关键词 (Top 15)')
            axes[0, 0].set_xlabel('出现频次')
        
        # 2. 期刊分布图
        journals = self.analyze_journals()
        if journals:
            journal_names, journal_counts = zip(*journals[:10])
            # 截断过长的期刊名称
            short_names = [name[:30] + "..." if len(name) > 30 else name for name in journal_names]
            axes[0, 1].pie(journal_counts, labels=short_names, autopct='%1.1f%%')
            axes[0, 1].set_title('热门发表期刊 (Top 10)')
        
        # 3. 文章数量趋势（按年份）
        years = []
        for result in self.results:
            journal_info = result.get('journal_info', '')
            # 尝试提取年份
            year_match = re.search(r'20\d{2}', journal_info)
            if year_match:
                years.append(int(year_match.group()))
        
        if years:
            year_counts = Counter(years)
            sorted_years = sorted(year_counts.items())
            if sorted_years:
                years_list, counts_list = zip(*sorted_years)
                axes[1, 0].plot(years_list, counts_list, marker='o', linewidth=2, markersize=6)
                axes[1, 0].set_title('研究文章发表趋势')
                axes[1, 0].set_xlabel('年份')
                axes[1, 0].set_ylabel('文章数量')
                axes[1, 0].grid(True, alpha=0.3)
        
        # 4. 词云图
        keywords_dict = dict(self.analyze_keywords())
        if keywords_dict:
            wordcloud = WordCloud(width=400, height=300, 
                                background_color='white',
                                colormap='viridis').generate_from_frequencies(keywords_dict)
            axes[1, 1].imshow(wordcloud, interpolation='bilinear')
            axes[1, 1].axis('off')
            axes[1, 1].set_title('研究热点词云')
        
        plt.tight_layout()
        plt.savefig('pubmed_hotspot_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("图表已保存为: pubmed_hotspot_analysis.png")
    
    def generate_report(self):
        """生成分析报告"""
        if not self.results:
            print("没有数据可分析，请先运行搜索")
            return
        
        print("正在生成分析报告...")
        
        # 创建DataFrame
        df = pd.DataFrame(self.results)
        
        # 保存原始数据
        df.to_csv('pubmed_research_data.csv', index=False, encoding='utf-8-sig')
        
        # 生成报告
        report = []
        report.append("=" * 60)
        report.append("PubMed医学研究热点分析报告")
        report.append("=" * 60)
        report.append(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"总文章数: {len(self.results)}")
        report.append("")
        
        # 热门关键词
        keywords = self.analyze_keywords()
        if keywords:
            report.append("【研究热点关键词 Top 20】")
            report.append("-" * 40)
            for i, (word, freq) in enumerate(keywords[:20], 1):
                report.append(f"{i:2d}. {word:<20} ({freq}次)")
            report.append("")
        
        # 热门期刊
        journals = self.analyze_journals()
        if journals:
            report.append("【热门发表期刊 Top 15】")
            report.append("-" * 40)
            for i, (journal, count) in enumerate(journals[:15], 1):
                report.append(f"{i:2d}. {journal:<50} ({count}篇)")
            report.append("")
        
        # 最新热门文章
        report.append("【最新热门研究文章 Top 10】")
        report.append("-" * 40)
        for i, result in enumerate(self.results[:10], 1):
            report.append(f"{i:2d}. {result['title']}")
            report.append(f"    期刊: {result['journal_info']}")
            report.append(f"    PMID: {result['pmid']}")
            report.append("")
        
        # 保存报告
        report_text = "\n".join(report)
        with open('pubmed_hotspot_report.txt', 'w', encoding='utf-8') as f:
            f.write(report_text)
        
        print("分析报告已保存:")
        print("- 原始数据: pubmed_research_data.csv")
        print("- 分析报告: pubmed_hotspot_report.txt")
        print("- 可视化图表: pubmed_hotspot_analysis.png")
        
        return report_text

def main():
    """主函数 - 使用示例"""
    print("PubMed医学研究热点分析工具")
    print("=" * 50)
    
    analyzer = PubMedHotspotAnalyzer()
    
    # 定义医学研究热点领域
    research_areas = [
        "artificial intelligence medicine",
        "CRISPR gene editing",
        "immunotherapy cancer",
        "COVID-19 treatment",
        "personalized medicine",
        "machine learning diagnosis",
        "telemedicine",
        "precision medicine",
        "biomarkers",
        "stem cell therapy"
    ]
    
    print("预设研究领域:")
    for i, area in enumerate(research_areas, 1):
        print(f"{i:2d}. {area}")
    
    print("\n选择分析方式:")
    print("1. 选择预设研究领域")
    print("2. 输入自定义关键词")
    print("3. 分析多个领域对比")
    print("4. 测试简单搜索")
    
    def perform_search(query, max_results=300, years_back=2):
        """执行搜索的统一函数"""
        print(f"\n开始搜索: {query}")
        
        # 先尝试API方法
        print("尝试使用API方法...")
        results = analyzer.search_pubmed_api(query, max_results, years_back)
        
        if not results:
            print("API方法失败，尝试网页爬取方法...")
            results = analyzer.search_pubmed(query, max_results, years_back)
        
        if results:
            print(f"搜索成功！共找到 {len(results)} 篇文章")
            print("正在生成分析...")
            analyzer.generate_visualizations()
            analyzer.generate_report()
        else:
            print("搜索失败，没有找到任何数据")
            print("建议尝试:")
            print("- 使用更常见的英文关键词")
            print("- 检查网络连接")
            print("- 尝试简化搜索词")
    
    try:
        choice = input("\n请输入选择 (1-4): ").strip()
        
        if choice == "1":
            area_choice = int(input("请选择研究领域编号: ")) - 1
            if 0 <= area_choice < len(research_areas):
                query = research_areas[area_choice]
                perform_search(query)
            else:
                print("无效选择")
                
        elif choice == "2":
            query = input("请输入研究关键词 (英文): ").strip()
            if query:
                max_results = int(input("最大结果数 (建议200-500): ") or "300")
                years_back = int(input("分析年限 (建议1-3年): ") or "2")
                perform_search(query, max_results, years_back)
            else:
                print("关键词不能为空")
                
        elif choice == "3":
            print("多领域对比分析功能")
            selected_areas = []
            area_indices = input("请输入要对比的领域编号，用逗号分隔 (如: 1,3,5): ").strip()
            
            try:
                indices = [int(x.strip()) - 1 for x in area_indices.split(',')]
                for idx in indices:
                    if 0 <= idx < len(research_areas):
                        selected_areas.append(research_areas[idx])
                
                if selected_areas:
                    print(f"将分析以下领域: {', '.join(selected_areas)}")
                    
                    # 对每个领域进行小规模搜索
                    for area in selected_areas:
                        print(f"\n正在分析: {area}")
                        analyzer.search_pubmed_api(area, 100, 1)
                        if not analyzer.results:
                            analyzer.search_pubmed(area, 100, 1)
                    
                    if analyzer.results:
                        analyzer.generate_visualizations()
                        analyzer.generate_report()
                    else:
                        print("未找到任何数据")
                else:
                    print("未选择有效领域")
                    
            except ValueError:
                print("输入格式错误")
                
        elif choice == "4":
            print("测试简单搜索功能...")
            test_queries = ["cancer", "diabetes", "COVID-19"]
            
            for test_query in test_queries:
                print(f"\n测试搜索: {test_query}")
                results = analyzer.search_pubmed_api(test_query, 10, 1)
                
                if results:
                    print(f"成功找到 {len(results)} 篇文章")
                    for i, result in enumerate(results[:3], 1):
                        print(f"{i}. {result['title'][:80]}...")
                    break
                else:
                    print("未找到结果")
            
            if analyzer.results:
                print("测试成功！继续完整分析...")
                analyzer.generate_visualizations()
                analyzer.generate_report()
            else:
                print("测试失败，可能存在网络或配置问题")
        else:
            print("无效选择")
            
    except KeyboardInterrupt:
        print("\n\n程序被用户中断")
    except Exception as e:
        print(f"程序执行出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()