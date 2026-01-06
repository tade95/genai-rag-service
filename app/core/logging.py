"""
Logging estructurado para la aplicación demo-genai-service.
"""
import logging
import json
from datetime import datetime

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name
        }
        return json.dumps(log_record)
    
def setup_logging(log_level: str):
    level = log_level.upper()

    if not hasattr(logging, level):
        raise ValueError(f"Invalid log level: {log_level}")
    
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())

    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, level))
    root_logger.handlers = [handler]
    root_logger.debug(f"Logging is set to {level} level with JSON format.")