import os
from enum import Enum
from dotenv import load_dotenv
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class EnvType(Enum):
    TEST = 'test'
    DEVELOPMENT = 'development'
    PRODUCTION = 'production'

class EnvManager:
    _instance = None

    def __new__(cls, app_name=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize(app_name)
        return cls._instance

    def _initialize(self, app_name):
        """Initialize environment with optional application context"""
        # Load base configuration
        load_dotenv(dotenv_path='.env', override=False)
        
        # Set environment type
        self._set_environment_type()
        
        # Load environment-specific configuration
        self._load_environment_config()
        
        # Load application-specific configuration if provided
        self.app_name = app_name
        if self.app_name:
            self._load_app_specific_config()

    def _set_environment_type(self):
        """Determine and validate environment type"""
        env_value = os.getenv('ENV', 'development').lower()
        try:
            self.env_type = EnvType(env_value)
        except ValueError:
            logger.warning(f"Invalid ENV value '{env_value}'. Defaulting to development.")
            self.env_type = EnvType.DEVELOPMENT

    def _load_environment_config(self):
        """Load environment-specific .env file"""
        env_file = f".env.{self.env_type.value}"
        if Path(env_file).exists():
            load_dotenv(dotenv_path=env_file, override=True)
        else:
            logger.warning(f"Environment file '{env_file}' not found.")

    def _load_app_specific_config(self):
        """Load application-specific configuration"""
        app_env_path = Path("apps") / self.app_name / f".env.{self.env_type.value}"
        if app_env_path.exists():
            load_dotenv(dotenv_path=app_env_path, override=True)
            logger.info(f"Loaded application-specific config from {app_env_path}")
        else:
            logger.warning(f"Application environment file {app_env_path} not found.")

    @classmethod
    def get(cls, key: str, default=None):
        """Get environment value with singleton access"""
        # Initialize instance if not already created
        cls()
        return os.getenv(key, default)