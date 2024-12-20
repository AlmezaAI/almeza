import pytest
import asyncio
from typing import Dict, Any
from almeza.core.engine import AlmezaEngine
from almeza.config.manager import ConfigManager

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
def config_manager():
    """Create a config manager instance."""
    test_config = {
        'test': True,
        'database': {
            'url': 'sqlite:///:memory:'
        },
        'redis': {
            'url': 'redis://localhost:6379/0'
        }
    }
    return ConfigManager(sources={}, defaults=test_config)

@pytest.fixture
async def almeza_engine(config_manager):
    """Create an Almeza engine instance for testing."""
    engine = AlmezaEngine(config_manager.config)
    await engine.initialize()
    yield engine
    await engine.shutdown()

@pytest.fixture
def mock_request_context():
    """Create a mock request context."""
    return {
        'user_id': 'test_user',
        'session_id': 'test_session',
        'timestamp': '2024-01-01T00:00:00Z'
    }
