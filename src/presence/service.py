import time
from dataclasses import dataclass

from loguru import logger
from pypresence import ActivityType, PipeClosed, DiscordNotFound, DiscordError

from src.presence.const import StateConst, ImagesConst
from src.presence.analyzer import log_analyzer
from src.rpc.service import rpc_service
from src.settings.settings import game_settings


@dataclass
class DD2PresenceService:
    """Класс для установки rich presence"""
    saved_time: float = None

    def set_presence(self) -> None:
        """установка присутствия"""
        try:
            game_state = log_analyzer.get_game_state()
            logger.info(f"game state: {game_state}")
            translated_state = StateConst.states.get(game_state)
            if not self.saved_time:
                self.saved_time = time.time()
            global_game_mode = game_settings.get_global_game_mod
            game_mode_image = ImagesConst.game_mode_images.get(global_game_mode)
            if game_state == "COMBAT":
                self.set_combat_presence(game_mode_image, translated_state)
            elif game_state == "DRIVING":
                self.set_driving_presence(game_mode_image, translated_state)
            else:
                self.set_basic_state(game_mode_image, translated_state)
        except (DiscordNotFound, DiscordError, BrokenPipeError, AssertionError, PipeClosed) as exc:
            logger.error(f"error while set presence: {exc}")
            rpc_service.rpc_reconnect()

    def set_combat_presence(self, game_mode_image: str, translated_state: str) -> None:
        """установка присутствия битвы"""
        enemy_data = log_analyzer.get_enemy()
        if enemy_data:
            enemy_name = enemy_data.get("enemy_name")
            enemy_code = enemy_data.get("enemy_code")
            builded_state = f"{translated_state} с {enemy_name}"
            rpc_service.update(activity_type=ActivityType.PLAYING, state=builded_state, start=self.saved_time,
                               large_image=game_mode_image, small_image=enemy_code, small_text=enemy_code)
        else:
            builded_state = f"{translated_state} с неизвестным врагом"
            rpc_service.update(activity_type=ActivityType.PLAYING, state=builded_state, start=self.saved_time,
                               large_image=game_mode_image)

    def set_driving_presence(self, game_mode_image: str, translated_state: str) -> None:
        """установка присутствия передвижения по локации"""
        location_data = log_analyzer.get_location()
        if location_data:
            location_name = location_data.get("location_name")
            location_code = location_data.get("location_code")
            builded_state = f"{translated_state} {location_name}"
            rpc_service.update(activity_type=ActivityType.PLAYING, state=builded_state, start=self.saved_time,
                               large_image=game_mode_image, small_image=location_code, small_text=location_code)
        else:
            builded_state = f"{translated_state} неизвестной локации"
            rpc_service.update(activity_type=ActivityType.PLAYING, state=builded_state, start=self.saved_time,
                               large_image=game_mode_image)

    def set_basic_state(self, game_mode_image: str, translated_state: str) -> None:
        """установка присутствия не требующего доп информации"""
        rpc_service.update(activity_type=ActivityType.PLAYING, state=translated_state, start=self.saved_time,
                           large_image=game_mode_image)


presence_service = DD2PresenceService()
