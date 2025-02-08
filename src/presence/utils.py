from loguru import logger

from src.presence.const import StateConst, EnemyConst, LocationConst, ProposalConst
from src.settings.settings import game_settings


class StateBuilder:
    """Класс для создания описания статуса"""

    @staticmethod
    @logger.catch
    def get_translated_state(state: str) -> str:
        """Получение состояние игры на нужном языке"""
        state: dict = StateConst.states.get(state)
        translated_state = state.get(game_settings.get_presence_lang)
        return translated_state

    @staticmethod
    @logger.catch
    def get_enemy_image_code(enemy_name: str) -> str | None:
        """Получение кода изображения врага"""
        if enemy_name:
            enemy_data: dict = EnemyConst.enemy.get(enemy_name)
            if enemy_data:
                enemy_code = enemy_data.get("enemy_code")
                return enemy_code
            else:
                return None
        else:
            return None

    @staticmethod
    @logger.catch
    def get_translated_enemy(enemy_code: str) -> str | None:
        """Получение названия врага на нужном языке"""
        if enemy_code:
            enemy_data: dict = EnemyConst.enemy.get(enemy_code)
            if enemy_data:
                translated_enemy = enemy_data.get(game_settings.get_presence_lang)
                return translated_enemy
            else:
                logger.info(f"cant find enemy in enemy dict, enemy code: {enemy_code}")
                return None
        else:
            logger.info(f"empty enemy code")
            return None

    @staticmethod
    @logger.catch
    def get_location_image_code(location_code: str) -> str | None:
        """Получение кода изображения локации"""
        if location_code:
            location_data: dict = LocationConst.locations_embark.get(location_code)
            if location_data:
                location_code = location_data.get("location_code")
                return location_code
            else:
                return None
        else:
            return None

    @staticmethod
    @logger.catch
    def get_translated_location(location_code: str) -> str | None:
        """Получение названия локации на нужном языке"""
        if location_code:
            location_data_embark: dict = LocationConst.locations_embark.get(location_code)
            location_data_fog: dict = LocationConst.locations_fog.get(location_code)
            if location_data_embark:
                translated_location_embark = location_data_embark.get(game_settings.get_presence_lang)
                if translated_location_embark:
                    return translated_location_embark
            else:
                logger.info(f"cant find embark location in location embark dict, location embark code: {location_code}")
                translated_location_fog = location_data_fog.get(game_settings.get_presence_lang)
                if translated_location_fog:
                    return translated_location_fog
                else:
                    logger.info(f"cant find fog location in location fog dict, location fog code: {location_code}")
                    return None
        else:
            logger.info(f"empty location code")
            return None

    @logger.catch
    def build_presence_proposal(self, state: str, translated_info: str) -> str:
        """Получение строки с текущей активностью на нужном языке"""
        translated_state = self.get_translated_state(state)
        if translated_info is not None:
            return f"{translated_state} {translated_info}"
        else:
            proposal_end: dict = ProposalConst.proposal.get(state)
            proposal_end_translated: dict = proposal_end.get(game_settings.get_presence_lang)
            return f"{translated_state} {proposal_end_translated}"


state_builder = StateBuilder()
