import pytest
from almeza.core.pipeline import Pipeline
from almeza.core.types import Request, Response

@pytest.mark.integration
class TestPipeline:
    @pytest.fixture
    async def pipeline(self, almeza_engine):
        """Create a test pipeline."""
        pipeline = Pipeline(almeza_engine.config)
        await pipeline.initialize()
        yield pipeline
        await pipeline.shutdown()
    
    async def test_basic_request_processing(self, pipeline, mock_request_context):
        request = Request(
            type="test",
            data={"message": "Hello, World!"},
            context=mock_request_context
        )
        
        response = await pipeline.process(request)
        
        assert isinstance(response, Response)
        assert response.status == "success"
    
    async def test_pipeline_error_handling(self, pipeline, mock_request_context):
        request = Request(
            type="invalid",
            data={},
            context=mock_request_context
        )
        
        with pytest.raises(ValueError):
            await pipeline.process(request)
