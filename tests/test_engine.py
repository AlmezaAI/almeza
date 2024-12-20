import pytest
from almeza.core.engine import AlmezaEngine, EngineConfig

@pytest.fixture
def engine():
    config = EngineConfig(
        memory_size=1000,
        max_planning_depth=5,
        safety_checks=["input", "output"],
        neural_models={"test": "mock"},
        compute_resources={}
    )
    return AlmezaEngine(config)

async def test_engine_initialization(engine):
    assert isinstance(engine, AlmezaEngine)

async def test_basic_processing(engine):
    result = await engine.process({"test": "data"})
    assert isinstance(result, dict)
