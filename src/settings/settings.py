import json
import subprocess
from typing import Any

from loguru import logger


class GameSettings:
    """Настройки игры"""
    global_game_mode: str = "main"

    @staticmethod
    @logger.catch
    def get_log_path() -> Any | None:
        """получение пути к лог файлу из json"""
        try:
            with open("settings.json", mode="rb") as settings:
                json_settings = json.load(settings)
            return json_settings
        except Exception as exc:
            logger.error(f"error while get settings from json: {exc}")
            return None

    @staticmethod
    @logger.catch
    def get_system_user_name() -> str | None:
        """получение имени текущего пользователя в ОС"""
        try:
            cmd = subprocess.run(["echo", "%USERNAME%"], stdout=subprocess.PIPE, text=True,
                                 creationflags=subprocess.CREATE_NO_WINDOW, shell=True)
            user_name = cmd.stdout.split("\n")[0]
            return user_name
        except Exception as exc:
            logger.info(f"error while run subprocess: {exc}")
            return None

    @property
    def get_global_game_mod(self) -> str:
        """получение режима игры"""
        return self.global_game_mode

    @logger.catch
    def set_global_game_mod(self, mode: str, state: str) -> None:
        """установка режима игры"""
        logger.info(f"update global game mode, state - {state}, mode - {mode}")
        self.global_game_mode = mode


game_settings = GameSettings()
