# tests/agent_core/utils/test_logging.py

from agent_core.utils.logging import get_logger

def test_logger_output():
    logger = get_logger("test_logger")
    assert logger.name == "test_logger"
    logger.info("Logger is working.")
