from loguru import logger

from src.presence.const import EnemyConst, LocationConst
from src.settings.settings import game_settings


class LogAnalyzer:
    """Класс для получения информации из лога"""

    @staticmethod
    def __get_log_data() -> str:
        """Чтение лога"""
        json_log_path = game_settings.get_log_path()
        if not json_log_path:
            system_user = game_settings.get_system_user_name()
            logger.info(f"read log with system user: {system_user}")
            with open(rf'C:\Users\{system_user}\AppData\LocalLow\RedHook\Darkest Dungeon II\Player.log',
                      mode="r") as dd2_log_file:
                data = dd2_log_file.read()
            return data
        else:
            log_path = json_log_path.get("path")
            with open(rf'{log_path}', mode="r") as dd2_log_file:
                data = dd2_log_file.read()
            return data

    def get_game_state(self) -> str:
        """Получения состояния игры"""
        log_data = self.__get_log_data()
        log_split = log_data.split("\n")
        game_state_list = [string for string in log_split if
                           "Entering game mode" in string]
        game_state_len = len(game_state_list) - 1
        game_state = game_state_list[game_state_len].split(" ")[3]
        if game_state != "MAIN_MENU":
            game_mode_kingdoms = [string for string in log_split if
                                  "KingdomMapCameraBhv" in string]
            if game_mode_kingdoms:
                game_settings.set_global_game_mod("kingdoms")
        else:
            game_settings.set_global_game_mod("main")
        return game_state

    def get_location(self) -> dict | None:
        """Получение названия и кода текущей локации"""
        log_data = self.__get_log_data()
        log_split = log_data.split("\n")
        locations_list_embark = [string for string in log_split if
                                 "Embark: finished load scene" in string]
        if locations_list_embark:
            locations_len = len(locations_list_embark) - 1
            location_code = locations_list_embark[locations_len].split(" ")[5]
            location_data = LocationConst.locations_embark.get(location_code)
            return location_data
        else:
            locations_list_fog = [string for string in log_split if
                                  "FogSystem" in string]
            if locations_list_fog:
                locations_len = len(locations_list_fog) - 1
                location_code = locations_list_fog[locations_len].split(" ")[9]
                location_data = LocationConst.locations_fog.get(location_code)
                return location_data
            else:
                logger.info("cant find location in dict")
                logger.info(f"embark location: {locations_list_embark}")
                logger.info(f"fog location: {locations_list_fog}")
                return None

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
            return None


log_analyzer = LogAnalyzer()
