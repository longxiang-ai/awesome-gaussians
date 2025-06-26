#!/usr/bin/env python3
"""搜索配置验证脚本"""

import json
import sys
from pathlib import Path

def validate_config():
    config_path = "data/search_config.json"
    print(f"🔍 验证搜索配置文件: {config_path}")
    
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config_data = json.load(f)
        
        search_config = config_data.get("search_config", {})
        both_keywords = search_config.get("both_abstract_and_title", [])
        abs_keywords = search_config.get("abstract_only", [])
        title_keywords = search_config.get("title_only", [])
        
        # 生成查询
        query_parts = []
        for keyword in both_keywords:
            query_parts.append(f'abs:"{keyword}"')
            query_parts.append(f'ti:"{keyword}"')
        for keyword in abs_keywords:
            query_parts.append(f'abs:"{keyword}"')
        for keyword in title_keywords:
            query_parts.append(f'ti:"{keyword}"')
        
        if query_parts:
            search_query = "(" + " OR ".join(query_parts) + ")"
            print("✅ 配置文件格式正确!")
            print(f"📊 关键词统计: 摘要和题目({len(both_keywords)}), 仅摘要({len(abs_keywords)}), 仅题目({len(title_keywords)})")
            print(f"🔍 生成的搜索查询: {search_query}")
            return True
        else:
            print("⚠️ 没有定义任何关键词")
            return False
            
    except Exception as e:
        print(f"❌ 验证失败: {e}")
        return False

if __name__ == "__main__":
    if validate_config():
        print("🎉 配置验证通过!")
    else:
        print("❌ 配置验证失败")
        sys.exit(1) 