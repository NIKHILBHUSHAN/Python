import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S"
)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

stream_h=logging.StreamHandler()
file_h=logging.FileHandler("app.log")

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter=logging.Formatter("%(name)s - %(levelname)s - %(message)s")

stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

try:
    a=[1,2,3]
    val=a[4]
except IndexError:
    logger.error("Index error occurred",exc_info=True)

from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler

rot_handler=RotatingFileHandler("rot_app.log",maxBytes=2000,backupCount=5)

timed_handler=TimedRotatingFileHandler("timed_app.log",when="s",interval=5,backupCount=5)