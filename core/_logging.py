"""
[v2.5] 结构化日志模块

统一日志格式，支持：
- 控制台彩色输出（开发环境）
- JSON 格式输出（CI/生产环境）
- 日志级别过滤
- 时间戳和模块名

用法：
    from core._logging import get_logger
    logger = get_logger(__name__)
    logger.info("Processing %d nodes", count)
"""

import logging
import sys
import json
from datetime import datetime
from typing import Optional


class StructuredFormatter(logging.Formatter):
    """JSON 结构化日志格式器"""
    
    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
            "message": record.getMessage(),
        }
        
        # 添加额外字段
        if hasattr(record, "node_count"):
            log_entry["node_count"] = record.node_count
        if hasattr(record, "duration_ms"):
            log_entry["duration_ms"] = record.duration_ms
        if hasattr(record, "stage"):
            log_entry["stage"] = record.stage
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
        
        return json.dumps(log_entry, ensure_ascii=False)


class ColorFormatter(logging.Formatter):
    """控制台彩色日志格式器"""
    
    COLORS = {
        "DEBUG": "\033[36m",     # Cyan
        "INFO": "\033[32m",      # Green
        "WARNING": "\033[33m",   # Yellow
        "ERROR": "\033[31m",     # Red
        "CRITICAL": "\033[35m",  # Magenta
    }
    RESET = "\033[0m"
    
    def format(self, record: logging.LogRecord) -> str:
        color = self.COLORS.get(record.levelname, "")
        timestamp = datetime.fromtimestamp(record.created).strftime("%H:%M:%S")
        
        # 简化模块名
        module = record.module
        if module.startswith("_"):
            module = module[1:]
        
        msg = f"{color}[{timestamp}] [{record.levelname[0]}] {module}: {record.getMessage()}{self.RESET}"
        
        if record.exc_info:
            msg += "\n" + self.formatException(record.exc_info)
        
        return msg


def setup_logging(
    level: str = "INFO",
    json_format: bool = False,
    log_file: Optional[str] = None,
) -> None:
    """
    配置全局日志系统
    
    Args:
        level: 日志级别 (DEBUG/INFO/WARNING/ERROR/CRITICAL)
        json_format: 是否使用 JSON 格式（适用于 CI/生产环境）
        log_file: 可选的日志文件路径
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    
    # 清除现有处理器
    root_logger.handlers.clear()
    
    # 控制台处理器
    console_handler = logging.StreamHandler(sys.stderr)
    if json_format:
        console_handler.setFormatter(StructuredFormatter())
    else:
        console_handler.setFormatter(ColorFormatter())
    root_logger.addHandler(console_handler)
    
    # 文件处理器（可选）
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(StructuredFormatter())
        root_logger.addHandler(file_handler)
    
    # 降低第三方库日志级别
    logging.getLogger("asyncio").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("aiohttp").setLevel(logging.WARNING)


def get_logger(name: str) -> logging.Logger:
    """获取指定名称的 logger"""
    return logging.getLogger(name)


# 自动初始化（如果未配置）
if not logging.root.handlers:
    setup_logging()
