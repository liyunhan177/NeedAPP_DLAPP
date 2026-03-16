"""日志配置模块

提供统一的日志配置和管理功能
日志文件存放在 log/ 目录下
支持记录：用户操作、应用事件、错误信息、性能统计等
所有日志在单次运行中只写入一个文件
"""
import logging
import pathlib
import sys
from datetime import datetime

def setup_logger(name="NeedAPP_DLAPP", log_level=logging.INFO, use_shared_handler=False):
    """
    配置并返回一个日志记录器
    
    Args:
        name (str): 日志记录器名称
        log_level (int): 日志级别，默认为 INFO
        use_shared_handler (bool): 是否使用共享的日志文件 handler，默认为 True
    
    Returns:
        logging.Logger: 配置好的日志记录器对象
    """
    global _log_file_path
    
    # 获取项目根目录
    project_root = pathlib.Path(__file__).resolve().parents[2]
    
    # 创建 log 目录（如果不存在）
    log_dir = project_root / "log"
    log_dir.mkdir(exist_ok=True)
    
    # 如果是第一次调用或没有共享路径，生成新的日志文件名
    if _log_file_path is None or not use_shared_handler:
        # 生成日志文件名（包含日期时间）
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        _log_file_path = log_dir / f"{name}_{timestamp}.log"
    
    log_file = _log_file_path
    
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
    
    # 创建文件 handler（写入日志文件）- 只在主 logger 创建
    if use_shared_handler and _log_file_path:
        file_handler = logging.FileHandler(_log_file_path, encoding='utf-8')
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
    else:
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


# ========== 便捷日志记录函数 ==========

def log_user_click(button_name: str, page_name: str = "MainPage", details: str = ""):
    """
    记录用户点击事件
    
    Args:
        button_name (str): 被点击的按钮名称
        page_name (str): 当前页面名称
        details (str): 额外详情信息
    """
    logger = get_user_action_logger()
    if logger is None:
        logger = init_user_action_logger()
    
    msg = f"[用户点击] 页面：{page_name} | 按钮：{button_name}"
    if details:
        msg += f" | 详情：{details}"
    logger.info(msg)

def log_user_action(action_type: str, action_desc: str, page_name: str = "",
                    details: str = ""):
    """
    记录用户操作事件
    
    Args:
        action_type (str): 操作类型（如：打开窗口、关闭窗口、下载、取消等）
        action_desc (str): 操作描述
        page_name (str): 当前页面名称
        details (str): 额外详情信息
    """
    logger = get_user_action_logger()
    if logger is None:
        logger = init_user_action_logger()
    
    msg = f"[用户操作] 类型：{action_type} | 描述：{action_desc}"
    if page_name:
        msg += f" | 页面：{page_name}"
    if details:
        msg += f" | 详情：{details}"
    logger.info(msg)

def log_app_event(event_type: str, event_desc: str, details: str = ""):
    """
    记录应用事件（启动、关闭、网络状态变化等）
    
    Args:
        event_type (str): 事件类型
        event_desc (str): 事件描述
        details (str): 额外详情信息
    """
    logger = get_default_logger()
    
    msg = f"[应用事件] 类型：{event_type} | 描述：{event_desc}"
    if details:
        msg += f" | 详情：{details}"
    logger.info(msg)

def log_error(error_type: str, error_msg: str, page_name: str = "",
              traceback_info: str = ""):
    """
    记录错误信息
    
    Args:
        error_type (str): 错误类型
        error_msg (str): 错误消息
        page_name (str): 发生错误的页面
        traceback_info (str): 堆栈跟踪信息
    """
    logger = get_error_logger()
    if logger is None:
        logger = init_error_logger()
    
    msg = f"[错误] 类型：{error_type} | 描述：{error_msg}"
    if page_name:
        msg += f" | 页面：{page_name}"
    logger.error(msg)
    
    if traceback_info:
        logger.error(f"堆栈信息：\n{traceback_info}")

def log_warning(warning_type: str, warning_msg: str, page_name: str = "",
                details: str = ""):
    """
    记录警告信息
    
    Args:
        warning_type (str): 警告类型
        warning_msg (str): 警告消息
        page_name (str): 发生警告的页面
        details (str): 额外详情信息
    """
    logger = get_default_logger()
    
    msg = f"[警告] 类型：{warning_type} | 描述：{warning_msg}"
    if page_name:
        msg += f" | 页面：{page_name}"
    if details:
        msg += f" | 详情：{details}"
    logger.warning(msg)

def log_download_status(software_name: str, status: str, details: str = ""):
    """
    记录下载状态
    
    Args:
        software_name (str): 软件名称
        status (str): 下载状态（开始、成功、失败、取消等）
        details (str): 额外详情信息
    """
    logger = get_default_logger()
    
    msg = f"[下载状态] 软件：{software_name} | 状态：{status}"
    if details:
        msg += f" | 详情：{details}"
    logger.info(msg)

def log_performance(page_name: str, operation: str, duration: float):
    """
    记录性能数据
    
    Args:
        page_name (str): 页面名称
        operation (str): 操作名称
        duration (float): 耗时（秒）
    """
    logger = get_default_logger()
    
    msg = f"[性能] 页面：{page_name} | 操作：{operation} | 耗时：{duration:.3f}秒"
    logger.info(msg)

# 默认的全局 logger 实例
_default_logger = None

# 用户操作日志记录器（与主 logger 共用同一个文件 handler）
_user_action_logger = None

# 错误日志记录器（与主 logger 共用同一个文件 handler）
_error_logger = None

# 全局日志文件路径（确保同一次运行使用同一个文件）
_log_file_path = None

def init_default_logger(log_level=logging.INFO):
    """
    初始化默认的日志记录器
    
    Args:
        log_level (int): 日志级别
    
    Returns:
        logging.Logger: 默认日志记录器
    """
    global _default_logger
    _default_logger = setup_logger("NeedAPP_DLAPP", log_level, use_shared_handler=True)
    return _default_logger

def init_user_action_logger(log_level=logging.INFO):
    """
    初始化用户操作日志记录器，专门记录用户点击、交互等行为
    与主 logger 共用同一个日志文件
    
    Args:
        log_level (int): 日志级别
    
    Returns:
        logging.Logger: 用户操作日志记录器
    """
    global _user_action_logger
    if _user_action_logger is None:
        _user_action_logger = setup_logger("UserActions", log_level, use_shared_handler=True)
    return _user_action_logger

def init_error_logger(log_level=logging.ERROR):
    """
    初始化错误日志记录器，专门记录异常和错误信息
    与主 logger 共用同一个日志文件
    
    Args:
        log_level (int): 日志级别，默认为 ERROR
    
    Returns:
        logging.Logger: 错误日志记录器
    """
    global _error_logger
    if _error_logger is None:
        _error_logger = setup_logger("AppErrors", log_level, use_shared_handler=True)
    return _error_logger

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

def get_user_action_logger():
    """
    获取用户操作日志记录器
    
    Returns:
        logging.Logger: 用户操作日志记录器，如果不存在则返回 None
    """
    logger = logging.getLogger("UserActions")
    if logger.handlers:
        return logger
    return None

def get_error_logger():
    """
    获取错误日志记录器
    
    Returns:
        logging.Logger: 错误日志记录器，如果不存在则返回 None
    """
    logger = logging.getLogger("AppErrors")
    if logger.handlers:
        return logger
    return None
