#!/usr/bin/env python3
"""
GitHub Actions 工作流测试脚本

模拟 GitHub Actions 环境来测试工作流中的 Python 脚本部分
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """运行命令并处理结果"""
    print(f"\n🔄 {description}")
    print(f"📝 运行命令: {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.stdout:
            print(f"📤 输出:\n{result.stdout}")
        
        if result.stderr:
            print(f"⚠️ 错误输出:\n{result.stderr}")
        
        if result.returncode == 0:
            print(f"✅ {description} - 成功")
            return True
        else:
            print(f"❌ {description} - 失败 (退出码: {result.returncode})")
            return False
            
    except Exception as e:
        print(f"❌ {description} - 异常: {e}")
        return False

def check_file_exists(filepath, description):
    """检查文件是否存在"""
    print(f"\n📁 检查文件: {filepath}")
    if Path(filepath).exists():
        print(f"✅ {description} - 文件存在")
        return True
    else:
        print(f"❌ {description} - 文件不存在")
        return False

def main():
    print("🤖 GitHub Actions 工作流测试")
    print("=" * 50)
    
    # 检查当前目录
    current_dir = Path.cwd()
    print(f"📂 当前目录: {current_dir}")
    
    # 1. 验证必要文件
    print("\n📋 步骤 1: 验证必要文件")
    files_ok = True
    files_ok &= check_file_exists("data/keywords.json", "关键词配置文件")
    files_ok &= check_file_exists("data/search_config.json", "搜索配置文件")
    files_ok &= check_file_exists("scripts/arxiv_crawler.py", "爬虫脚本")
    files_ok &= check_file_exists("scripts/validate_search_config.py", "配置验证脚本")
    
    if not files_ok:
        print("❌ 必要文件检查失败")
        return False
    
    # 2. 验证搜索配置
    print("\n📋 步骤 2: 验证搜索配置")
    if not run_command("python scripts/validate_search_config.py", "搜索配置验证"):
        return False
    
    # 3. 运行爬虫（少量结果用于测试）
    print("\n📋 步骤 3: 运行爬虫测试")
    if not run_command("python scripts/arxiv_crawler.py --max-results 3", "爬虫测试运行"):
        return False
    
    # 4. 验证爬虫输出
    print("\n📋 步骤 4: 验证爬虫输出")
    data_files = list(Path("data").glob("papers_*.json"))
    if data_files:
        print(f"✅ 找到论文数据文件: {[f.name for f in data_files]}")
    else:
        print("❌ 没有找到论文数据文件")
        return False
    
    # 5. 检查 README 生成器
    print("\n📋 步骤 5: 检查 README 生成器")
    if check_file_exists("scripts/readme_generator.py", "README 生成器"):
        print("💡 README 生成器存在，但跳过运行以避免修改文件")
    else:
        print("⚠️ README 生成器不存在")
    
    # 6. 总结
    print("\n🎉 测试总结")
    print("=" * 50)
    print("✅ 所有核心组件测试通过")
    print("✅ GitHub Actions 工作流应该可以正常运行")
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎊 GitHub Actions 工作流测试完成 - 一切正常！")
        sys.exit(0)
    else:
        print("\n💥 GitHub Actions 工作流测试失败 - 请检查配置")
        sys.exit(1) 