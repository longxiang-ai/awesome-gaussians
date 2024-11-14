import os
import sys
from pathlib import Path
from utils.logger import setup_logger

logger = setup_logger("test_workflow")

def check_file_exists(filepath: str) -> bool:
    """检查文件是否存在"""
    exists = Path(filepath).exists()
    logger.info(f"检查文件 {filepath}: {'存在' if exists else '不存在'}")
    return exists

def run_workflow():
    logger.info("开始测试工作流程")
    
    # 检查必要文件
    if not check_file_exists("README_template.md"):
        logger.error("README模板文件不存在")
        return False
    
    # 运行爬虫
    logger.info("运行爬虫...")
    result = os.system("python3 scripts/arxiv_crawler.py")
    if result != 0:
        logger.error("爬虫运行失败")
        return False
    
    # 检查爬虫输出
    data_files = list(Path("data").glob("papers_*.json"))
    if not data_files:
        logger.error("未找到爬虫生成的数据文件")
        return False
    logger.info(f"找到数据文件: {[f.name for f in data_files]}")
        
    # 运行README生成器
    logger.info("生成README...")
    result = os.system("python3 scripts/readme_generator.py")
    if result != 0:
        logger.error("README生成失败")
        return False
    
    # 检查生成的README
    if not check_file_exists("README.md"):
        logger.error("README.md未生成")
        return False
    
    logger.info("工作流程测试完成")
    return True

if __name__ == "__main__":
    success = run_workflow()
    sys.exit(0 if success else 1) 