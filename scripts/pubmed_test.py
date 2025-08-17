#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化版PubMed测试脚本
先测试基本功能是否正常
"""

import requests
from bs4 import BeautifulSoup
import json

def test_xml_parser():
    """测试XML解析器是否可用"""
    try:
        # 测试lxml
        from bs4 import BeautifulSoup
        test_xml = "<root><test>Hello</test></root>"
        soup = BeautifulSoup(test_xml, 'xml')
        print("✓ XML解析器测试成功")
        return True
    except Exception as e:
        print(f"✗ XML解析器测试失败: {e}")
        return False

def test_pubmed_api():
    """测试PubMed API连接"""
    print("测试PubMed API连接...")
    
    try:
        # 简单的API测试
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            'db': 'pubmed',
            'term': 'cancer',
            'retmax': 5,
            'retmode': 'json'
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        pmids = data.get('esearchresult', {}).get('idlist', [])
        
        if pmids:
            print(f"✓ API连接成功，找到PMIDs: {pmids[:3]}...")
            return pmids[:3]  # 返回前3个PMID用于进一步测试
        else:
            print("✗ API连接成功但没有找到结果")
            return []
            
    except Exception as e:
        print(f"✗ API连接失败: {e}")
        return []

def test_fetch_articles(pmids):
    """测试获取具体文章信息"""
    if not pmids:
        print("没有PMID可以测试")
        return
    
    print("测试获取文章详情...")
    
    try:
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        params = {
            'db': 'pubmed',
            'id': ','.join(pmids),
            'retmode': 'xml'
        }
        
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        
        # 尝试解析XML
        soup = BeautifulSoup(response.content, 'xml')
        articles = soup.find_all('PubmedArticle')
        
        print(f"✓ 成功获取 {len(articles)} 篇文章")
        
        # 显示第一篇文章的信息
        if articles:
            first_article = articles[0]
            
            # 获取标题
            title_elem = first_article.find('ArticleTitle')
            title = title_elem.text if title_elem else "无标题"
            
            # 获取PMID
            pmid_elem = first_article.find('PMID')
            pmid = pmid_elem.text if pmid_elem else "无PMID"
            
            print(f"第一篇文章:")
            print(f"PMID: {pmid}")
            print(f"标题: {title[:100]}...")
            
            return True
        else:
            print("✗ 没有解析到文章内容")
            return False
            
    except Exception as e:
        print(f"✗ 获取文章详情失败: {e}")
        return False

def test_web_scraping():
    """测试网页爬取方法"""
    print("测试网页爬取方法...")
    
    try:
        url = "https://pubmed.ncbi.nlm.nih.gov/?term=cancer&size=5"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 尝试多种可能的标题选择器
        title_selectors = [
            'a.docsum-title',
            'a[data-article-id]',
            'h1.heading-title',
            'a[href*="/"]'
        ]
        
        titles_found = []
        for selector in title_selectors:
            elements = soup.select(selector)
            if elements:
                for elem in elements[:3]:
                    text = elem.get_text().strip()
                    if len(text) > 20:  # 过滤掉太短的文本
                        titles_found.append(text)
                        
        if titles_found:
            print(f"✓ 网页爬取成功，找到 {len(titles_found)} 个标题")
            for i, title in enumerate(titles_found[:3], 1):
                print(f"{i}. {title[:80]}...")
            return True
        else:
            print("✗ 网页爬取失败，没有找到标题")
            # 显示页面内容片段用于调试
            page_text = soup.get_text()[:300]
            print(f"页面内容预览: {page_text}")
            return False
            
    except Exception as e:
        print(f"✗ 网页爬取失败: {e}")
        return False

def main():
    """主测试函数"""
    print("PubMed功能测试")
    print("=" * 40)
    
    # 1. 测试XML解析器
    xml_ok = test_xml_parser()
    print()
    
    # 2. 测试API连接
    pmids = test_pubmed_api()
    print()
    
    # 3. 如果有PMID，测试获取详情
    if xml_ok and pmids:
        fetch_ok = test_fetch_articles(pmids)
        print()
    else:
        fetch_ok = False
    
    # 4. 测试网页爬取
    web_ok = test_web_scraping()
    print()
    
    # 总结
    print("测试结果总结:")
    print(f"XML解析器: {'✓' if xml_ok else '✗'}")
    print(f"API连接: {'✓' if pmids else '✗'}")
    print(f"获取详情: {'✓' if fetch_ok else '✗'}")
    print(f"网页爬取: {'✓' if web_ok else '✗'}")
    
    if xml_ok and (pmids or web_ok):
        print("\n🎉 基本功能正常，可以运行完整程序！")
    else:
        print("\n🔧 需要解决以下问题:")
        if not xml_ok:
            print("- 安装XML解析器: pip install lxml")
        if not pmids and not web_ok:
            print("- 检查网络连接")
            print("- 可能需要VPN访问PubMed")

if __name__ == "__main__":
    main()