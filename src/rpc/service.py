from loguru import logger
from pypresence import Presence, DiscordNotFound, DiscordError


class RpcService(Presence):
    """Сервис Discord Rpc"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, client_id=1336769178849513503)

    def rpc_reconnect(self) -> None:
        """переподлючение к discord rpc"""
        logger.info("trying reconnect to discord rpc")
        try:
            self.connect()
            logger.info("reconnect successful")
        except (DiscordNotFound, DiscordError, BrokenPipeError) as exc:
            logger.error(f"reconnect to rpc error: {exc}")
            pass

    @staticmethod
    def connect_to_discord_rpc():
        """подлючение к discord rpc"""
        try:
            presence = rpc_service
            presence.connect()
            logger.info("connected to discord rpc")
        except Exception as exc:
            logger.error(f"error while connecting rpc: {exc}")
            logger.info("close application")
            exit()


rpc_service = RpcService()
