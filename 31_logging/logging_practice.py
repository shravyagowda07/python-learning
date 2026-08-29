import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

print("=== LOGGING PRACTICE ===")

logging.debug("This is debug information")

logging.info("Program started successfully")

logging.warning("This is a warning message")

logging.error("This is an error message")

logging.critical("This is a critical message")

print("Program finished")