import logging

logging.basicConfig(
    filename='login_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    filemode='a',
    encoding='utf-8'
)


logger = logging.getLogger("log_event")

def log_event(username: str, status: str):

    log_message = f"Login event - Username: {username}, Status: {status}"

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)