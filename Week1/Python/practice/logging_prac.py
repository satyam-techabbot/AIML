# logging to a file
# import logging
# logging.basicConfig(filename="app.log", level=0, encoding="utf-8", filemode="a", format="{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M")
# logging.debug("This is a debug log full_path")
# logging.info("This is a debug log full_path")
# logging.warning("This is a debug log full_path")
# logging.critical(f"This is a debug log {logging}")

# stack traces
# import logging
# logging.basicConfig(filename="error.log", encoding="utf-8", filemode="a", format="{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H/%M", level=10)
# try:
#     a = 1/0
# except ZeroDivisionError as z:
#     logging.error(z, exc_info=True)

import logging
def get_only_debug(record):
    return record.levelname == "ERROR"
logger1 = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_handler.setLevel("DEBUG")
console_handler.addFilter(get_only_debug)
logger1.addHandler(console_handler)
logger1.error("This is error")
logger1.critical("This is CRITICAL")
logger1.debug("This is debug")
logger1.info("This is info")
