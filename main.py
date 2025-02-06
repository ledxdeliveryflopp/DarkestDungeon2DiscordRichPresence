import time

from loguru import logger

from src.presence.service import presence_service
from src.rpc.service import rpc_service
from src.settings.utils import check_dd2_run_in_start, check_dd2_run


def start_application() -> None:
    """ожидание запуска DD2 и подлючение к Discord rpc"""
    dd2_status = False
    while dd2_status is False:
        update_dd2_status = check_dd2_run_in_start()
        if update_dd2_status is True:
            dd2_status = True
        else:
            logger.info("cant find dd2 process, check again after 60 sec")
            time.sleep(60)
    logger.info("dd2 started, wait 30 sec")
    time.sleep(30)
    rpc_service.connect_to_discord_rpc()


if __name__ == '__main__':
    logger.add(rf"dd2-rich-presence.log", rotation="100 MB",
               format="{time:DD-MM-YYYY at HH:mm:ss} | {level} | {message}")
    start_application()
    while True:
        check_dd2_run()
        presence_service.set_presence()
        time.sleep(8)
