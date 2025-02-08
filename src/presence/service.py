import time
from dataclasses import dataclass

from loguru import logger
from pypresence import ActivityType, PipeClosed, DiscordNotFound, DiscordError

from src.presence.const import ImagesConst
from src.presence.analyzer import log_analyzer
from src.presence.utils import state_builder

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
            if not self.saved_time:
                self.saved_time = time.time()
            global_game_mode = game_settings.get_global_game_mod
            game_mode_image = ImagesConst.game_mode_images.get(global_game_mode)
            if game_state == "COMBAT":
                self.set_combat_presence(game_mode_image)
            elif game_state == "DRIVING":
                self.set_driving_presence(game_mode_image)
            else:
                self.set_basic_state(game_mode_image, game_state)
        except (DiscordNotFound, DiscordError, BrokenPipeError, AssertionError, PipeClosed) as exc:
            logger.error(f"error while set presence: {exc}")
            rpc_service.rpc_reconnect()

    def set_combat_presence(self, game_mode_image: str) -> None:
        """установка присутствия битвы"""
        enemy_code = log_analyzer.get_enemy()
        enemy_image = state_builder.get_enemy_image_code(enemy_code)
        translated_enemy = state_builder.get_translated_enemy(enemy_code)
        presence_proposal = state_builder.build_presence_proposal("COMBAT", translated_enemy)
        rpc_service.update(activity_type=ActivityType.PLAYING, state=presence_proposal, start=self.saved_time,
                           large_image=game_mode_image, small_image=enemy_image, small_text=translated_enemy)

    def set_driving_presence(self, game_mode_image: str) -> None:
        """установка присутствия передвижения по локации"""
        location_code = log_analyzer.get_location()
        location_image = state_builder.get_location_image_code(location_code)
        translated_location = state_builder.get_translated_location(location_code)
        presence_proposal = state_builder.build_presence_proposal("DRIVING", translated_location)
        rpc_service.update(activity_type=ActivityType.PLAYING, state=presence_proposal, start=self.saved_time,
                           large_image=game_mode_image, small_image=location_image, small_text=translated_location)

    def set_basic_state(self, game_mode_image: str, state: str) -> None:
        """установка присутствия не требующего доп информации"""
        translated_state = state_builder.get_translated_state(state)
        rpc_service.update(activity_type=ActivityType.PLAYING, state=translated_state, start=self.saved_time,
                           large_image=game_mode_image)


presence_service = DD2PresenceService()
