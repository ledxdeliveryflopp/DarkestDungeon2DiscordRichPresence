import time

import psutil
from loguru import logger


def check_dd2_run_in_start() -> bool:
    """поиск процесса Darkest Dungeon II при запуске приложения"""
    process_name = "Darkest Dungeon II.exe"
    for proc in psutil.process_iter():
        if process_name in proc.name():
            return True


def check_dd2_run() -> None:
    """Проверка запущен ли Darkest Dungeon II"""
    process_name = "Darkest Dungeon II.exe"
    for proc in psutil.process_iter():
        if process_name in proc.name():
            return None
    logger.info("can't find darkest dungeon II process, close application")
    time.sleep(10)
    exit()
