#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
读取Word文档内容的Python脚本
用于提取2021年11月系统架构师真题（综合知识+答案解析）.docx文件中的文本内容

依赖安装:
pip install python-docx
"""

import os
import sys
from docx import Document

def read_word_document(file_path):
    """
    读取Word文档内容
    
    Args:
        file_path (str): Word文档的文件路径
        
    Returns:
        str: 文档的文本内容
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")
        
        # 读取Word文档
        doc = Document(file_path)
        
        # 提取所有段落的文本
        full_text = []
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():  # 只添加非空段落
                full_text.append(paragraph.text)
        
        return '\n'.join(full_text)
    
    except Exception as e:
        print(f"读取文档时发生错误: {e}")
        return None

def save_text_to_file(text, output_path):
    """
    将提取的文本保存到文件
    
    Args:
        text (str): 要保存的文本内容
        output_path (str): 输出文件路径
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"文本内容已保存到: {output_path}")
    except Exception as e:
        print(f"保存文件时发生错误: {e}")

def main():
    """
    主函数
    """
    # Word文档路径
    word_file_path = "2021_first/2021年11月系统架构师真题（综合知识+答案解析）.docx"
    
    # 输出文本文件路径
    output_file_path = "2021_first/extracted_content.txt"
    
    print("开始读取Word文档...")
    print(f"文档路径: {word_file_path}")
    
    # 读取Word文档内容
    content = read_word_document(word_file_path)
    
    if content:
        print(f"成功读取文档，共提取 {len(content)} 个字符")
        print("\n--- 文档内容预览（前500字符）---")
        print(content[:500])
        print("\n--- 预览结束 ---\n")
        
        # 保存到文本文件
        save_text_to_file(content, output_file_path)
        
        # 显示一些统计信息
        lines = content.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        print(f"\n统计信息:")
        print(f"总行数: {len(lines)}")
        print(f"非空行数: {len(non_empty_lines)}")
        print(f"总字符数: {len(content)}")
        
    else:
        print("读取文档失败")
        sys.exit(1)

if __name__ == "__main__":
    main()