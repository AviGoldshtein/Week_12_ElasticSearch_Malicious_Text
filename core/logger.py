import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger("logger")

# logger.debug("debug")
# logger.info("info")
# logger.warning("warning")
# logger.critical("critical")
