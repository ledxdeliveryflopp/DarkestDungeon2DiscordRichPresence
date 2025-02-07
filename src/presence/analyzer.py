import time

from loguru import logger

from src.presence.const import EnemyConst, LocationConst
from src.settings.settings import game_settings


class LogAnalyzer:
    """Класс для получения информации из лога"""

    @staticmethod
    @logger.catch
    def __get_log_data() -> str:
        """Чтение лога"""
        json_log_path = game_settings.get_log_path()
        try:
            if not json_log_path:
                system_user = game_settings.get_system_user_name()
                logger.info(f"read log with system user: {system_user}")
                with open(rf'C:\Users\{system_user}\AppData\LocalLow\RedHook\Darkest Dungeon II\Player.log',
                          mode="r", encoding='utf-8') as dd2_log_file:
                    data = dd2_log_file.read()
                return data
            else:
                log_path = json_log_path.get("path")
                with open(rf'{log_path}', mode="r", encoding='utf-8') as dd2_log_file:
                    data = dd2_log_file.read()
                return data
        except Exception as exc:
            logger.error(f"error while read dd2 log: {exc}")
            logger.info("close application")
            time.sleep(10)
            exit()

    @logger.catch
    def set_global_game_mode(self, log_split: list, game_state: str) -> None:
        """Установка режима игры"""
        game_mode_kingdoms = [string for string in log_split if
                              "KingdomMapCameraBhv" in string]
        if game_state == "MAIN_MENU" and game_settings.get_global_game_mod != "main":
            game_settings.set_global_game_mod("main", game_state)
        elif game_mode_kingdoms and game_settings.get_global_game_mod == "main" and game_state != "MAIN_MENU":
            game_settings.set_global_game_mod("kingdoms", game_state)

    @logger.catch
    def get_game_state(self) -> str:
        """Получения состояния игры"""
        log_data = self.__get_log_data()
        log_split = log_data.split("\n")
        game_state_list = [string for string in log_split if
                           "Entering game mode" in string]
        game_state_len = len(game_state_list) - 1
        game_state = game_state_list[game_state_len].split(" ")[3]
        self.set_global_game_mode(log_split, game_state)
        return game_state

    @staticmethod
    @logger.catch
    def get_embark_location(log_split: list) -> dict | None:
        """Получение название локации по Embark"""
        locations_list_embark = [string for string in log_split if
                                 "Embark: finished load scene" in string]
        if not locations_list_embark:
            return None
        locations_len = len(locations_list_embark) - 1
        location_code = locations_list_embark[locations_len].split(" ")[5]
        embark_location_data = LocationConst.locations_embark.get(location_code)
        if embark_location_data:
            return embark_location_data
        else:
            logger.info(f"cant find location in embark dict, embark code: {location_code}")
            return None

    @staticmethod
    @logger.catch
    def get_fog_location(log_split: list) -> dict | None:
        """Получение название локации по FogSystem"""
        locations_list_fog = [string for string in log_split if
                              "FogSystem" in string]
        if not locations_list_fog:
            return None
        locations_len = len(locations_list_fog) - 1
        location_code = locations_list_fog[locations_len].split(" ")[9]
        fog_location_data = LocationConst.locations_fog.get(location_code)
        if fog_location_data:
            return fog_location_data
        else:
            logger.info(f"cant find location in fog dict, fog code: {location_code}")
            return None

    @logger.catch
    def get_location(self) -> dict | None:
        """Получение названия и кода текущей локации"""
        log_data = self.__get_log_data()
        log_split = log_data.split("\n")
        embark_location = self.get_embark_location(log_split)
        if embark_location:
            return embark_location
        else:
            fog_location = self.get_fog_location(log_split)
            if fog_location:
                return fog_location
            else:
                return None

    @logger.catch
    def get_enemy(self) -> dict | None:
        """Получение типа врагов и их код"""
        log_data = self.__get_log_data()
        log_split = log_data.split("\n")
        enemy_list = [string for string in log_split if
                      "TimelinePropertyMapBhv" in string]
        if not enemy_list:
            return None
        enemy_len = len(enemy_list) - 1
        enemy_code = enemy_list[enemy_len].split(" ")[5]
        enemy_data = EnemyConst.enemy.get(enemy_code)
        if enemy_data:
            return enemy_data
        else:
            logger.info(f"cant find enemy in enemy dict, enemy code: {enemy_code}")
            return None


log_analyzer = LogAnalyzer()
