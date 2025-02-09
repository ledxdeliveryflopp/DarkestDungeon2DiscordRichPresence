import json
import subprocess
import sys
import time
from json import JSONDecodeError

from loguru import logger


class GameSettings:
    """Настройки игры"""
    global_game_mode: str = "main"
    presence_lang: str = "en"
    log_path: str = None

    @logger.catch
    def test_log_path(self) -> None:
        """Проверка на то что лог DD2 существует и его возможно прочитать"""
        logger.info("testing dd2 log file")
        try:
            with open(rf'{self.log_path}', mode="r", encoding='utf-8') as dd2_log_file:
                dd2_log_file.read()
            logger.info("dd2 log test success")
        except Exception as exc:
            logger.error(f"error while testing dd2 log file: {exc}")
            logger.info("close application")
            time.sleep(10)
            sys.exit()

    @logger.catch
    def set_log_path(self) -> None:
        """Установка пути к лог файлу из json"""
        try:
            with open("settings.json", mode="rb") as settings:
                json_settings = json.load(settings)
            log_path = json_settings["path"]
            self.log_path = log_path
        except (JSONDecodeError, KeyError, FileNotFoundError) as exc:
            logger.error(f"error while parse settings: {exc}")
            logger.info("trying set basic log path")
            os_username = self.get_system_user_name()
            logger.info(f"os username: {os_username}")
            basic_log_path = rf"{os_username}\AppData\LocalLow\RedHook\Darkest Dungeon II\Player.log"
            self.log_path = basic_log_path

    @logger.catch
    def set_presence_lang(self) -> None:
        """Установка языка активностей"""
        try:
            with open("settings.json", mode="rb") as settings:
                json_settings: dict = json.load(settings)
            settings_lang = json_settings.get("lang")
            if settings_lang == "ru" or settings_lang == "en":
                self.presence_lang = settings_lang
                logger.info(f"set {settings_lang} lang code")
        except Exception as exc:
            logger.error(f"error while get lang from json: {exc}")
            logger.info("set basic lang")
            return None

    @staticmethod
    @logger.catch
    def get_system_user_name() -> str | None:
        """получение имени текущего пользователя в ОС"""
        try:
            cmd = subprocess.run(["echo", "%systemdrive%%homepath%"], stdout=subprocess.PIPE, text=True,
                                 creationflags=subprocess.CREATE_NO_WINDOW, shell=True)
            user_name = cmd.stdout.split("\n")[0]
            return user_name
        except Exception as exc:
            logger.info(f"error while run subprocess: {exc}")
            return None

    @property
    def get_log_path(self) -> str:
        """Получить путь к логу DD2"""
        return self.log_path

    @property
    def get_global_game_mod(self) -> str:
        """получение режима игры"""
        return self.global_game_mode

    @logger.catch
    def set_global_game_mod(self, mode: str, state: str) -> None:
        """установка режима игры"""
        logger.info(f"update global game mode, state - {state}, mode - {mode}")
        self.global_game_mode = mode

    @property
    def get_presence_lang(self) -> str:
        """получение режима игры"""
        return self.presence_lang

    def set_settings(self) -> None:
        """Установка первоначальных настроек"""
        self.set_log_path()
        self.test_log_path()
        self.set_presence_lang()
        logger.info(f"Settings inited, log: {self.log_path}, lang: {self.presence_lang}")


game_settings = GameSettings()
