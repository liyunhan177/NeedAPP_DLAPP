"""日志配置模块

提供统一的日志配置和管理功能
日志文件存放在 log/ 目录下
"""
import logging
import pathlib
import sys
from datetime import datetime

def setup_logger(name="NeedAPP_DLAPP", log_level=logging.INFO):
    """
    配置并返回一个日志记录器
    
    Args:
        name (str): 日志记录器名称
        log_level (int): 日志级别，默认为 INFO
    
    Returns:
        logging.Logger: 配置好的日志记录器对象
    """
    # 获取项目根目录
    project_root = pathlib.Path(__file__).resolve().parents[2]
    
    # 创建 log 目录（如果不存在）
    log_dir = project_root / "log"
    log_dir.mkdir(exist_ok=True)
    
    # 生成日志文件名（包含日期时间）
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"{name}_{timestamp}.log"
    
    # 创建 logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # 避免重复添加 handler
    if logger.handlers:
        return logger
    
    # 创建 formatter（日志格式）
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # 创建文件 handler（写入日志文件）
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    
    # 创建控制台 handler（输出到终端）
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)  # 控制台只显示 INFO 及以上级别
    console_handler.setFormatter(formatter)
    
    # 添加 handler 到 logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    # 记录日志开始信息
    logger.info("=" * 60)
    logger.info(f"应用程序启动 - {name}")
    logger.info(f"日志文件：{log_file}")
    logger.info(f"日志级别：{logging.getLevelName(log_level)}")
    logger.info("=" * 60)
    
    return logger

def get_logger(name="NeedAPP_DLAPP"):
    """
    获取已配置的日志记录器
    
    Args:
        name (str): 日志记录器名称
    
    Returns:
        logging.Logger: 日志记录器对象，如果不存在则返回 None
    """
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    return None

def cleanup_old_logs(max_logs=10):
    """
    清理旧的日志文件，只保留最新的 max_logs 个
    
    Args:
        max_logs (int): 保留的最大日志文件数量，默认为 10
    """
    project_root = pathlib.Path(__file__).resolve().parents[2]
    log_dir = project_root / "log"
    
    if not log_dir.exists():
        return
    
    # 获取所有日志文件
    log_files = list(log_dir.glob("*.log"))
    
    # 按修改时间排序
    log_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    
    # 删除旧文件
    for old_file in log_files[max_logs:]:
        try:
            old_file.unlink()
            print(f"已删除旧日志文件：{old_file.name}")
        except Exception as e:
            print(f"删除日志文件失败：{old_file.name} - {str(e)}")

# 默认的全局 logger 实例
_default_logger = None

def init_default_logger(log_level=logging.INFO):
    """
    初始化默认的日志记录器
    
    Args:
        log_level (int): 日志级别
    
    Returns:
        logging.Logger: 默认日志记录器
    """
    global _default_logger
    _default_logger = setup_logger("NeedAPP_DLAPP", log_level)
    return _default_logger

def get_default_logger():
    """
    获取默认的日志记录器
    
    Returns:
        logging.Logger: 默认日志记录器
    """
    global _default_logger
    if _default_logger is None:
        _default_logger = setup_logger("NeedAPP_DLAPP")
    return _default_logger
