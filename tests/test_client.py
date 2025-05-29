import pytest
import os
import json
from unittest.mock import patch, AsyncMock
from workato_mcp.client import WorkatoClient

# Sample test data
SAMPLE_RECIPES = [
    {"id": 1, "name": "Recipe 1"},
    {"id": 2, "name": "Recipe 2"}
]

SAMPLE_RECIPE_DETAILS = {
    "id": 1,
    "name": "Recipe 1",
    "description": "Test recipe",
    "code": json.dumps({"trigger": {"type": "webhook"}, "actions": []})
}

SAMPLE_JOBS = [
    {"id": 101, "recipe_id": 1, "status": "success"},
    {"id": 102, "recipe_id": 1, "status": "error"}
]

SAMPLE_FOLDERS = [
    {"id": 201, "name": "Folder 1"},
    {"id": 202, "name": "Folder 2"}
]

SAMPLE_CONNECTIONS = [
    {"id": 301, "name": "Connection 1"},
    {"id": 302, "name": "Connection 2"}
]

@pytest.fixture
def client():
    """Create a WorkatoClient instance for testing."""
    with patch.dict(os.environ, {"WORKATO_API_TOKEN": "test_token", "WORKATO_BASE_URL": "https://test.workato.com/api"}):
        return WorkatoClient()

@pytest.mark.asyncio
async def test_get_recipes(client):
    """Test getting recipes."""
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_response = AsyncMock()
        mock_response.json.return_value = SAMPLE_RECIPES
        mock_response.raise_for_status = AsyncMock()
        mock_get.return_value = mock_response
        
        recipes = await client.get_recipes()
        
        mock_get.assert_called_once_with(
            "https://test.workato.com/api/recipes",
            headers=client.headers,
            params={}
        )
        assert recipes == SAMPLE_RECIPES

@pytest.mark.asyncio
async def test_get_recipe_details(client):
    """Test getting recipe details."""
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_response = AsyncMock()
        mock_response.json.return_value = SAMPLE_RECIPE_DETAILS
        mock_response.raise_for_status = AsyncMock()
        mock_get.return_value = mock_response
        
        recipe = await client.get_recipe_details(1)
        
        mock_get.assert_called_once_with(
            "https://test.workato.com/api/recipes/1",
            headers=client.headers
        )
        assert recipe == SAMPLE_RECIPE_DETAILS

@pytest.mark.asyncio
async def test_create_recipe(client):
    """Test creating a recipe."""
    recipe_data = {
        "name": "New Recipe",
        "description": "Test recipe",
        "code": json.dumps({"trigger": {"type": "webhook"}, "actions": []})
    }
    
    with patch("httpx.AsyncClient.post") as mock_post:
        mock_response = AsyncMock()
        mock_response.json.return_value = {**recipe_data, "id": 3}
        mock_response.raise_for_status = AsyncMock()
        mock_post.return_value = mock_response
        
        result = await client.create_recipe(recipe_data)
        
        mock_post.assert_called_once_with(
            "https://test.workato.com/api/recipes",
            headers=client.headers,
            json={"recipe": recipe_data}
        )
        assert result["id"] == 3
        assert result["name"] == "New Recipe"

@pytest.mark.asyncio
async def test_get_jobs(client):
    """Test getting jobs."""
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_response = AsyncMock()
        mock_response.json.return_value = SAMPLE_JOBS
        mock_response.raise_for_status = AsyncMock()
        mock_get.return_value = mock_response
        
        jobs = await client.get_jobs(recipe_id=1, status="success", limit=10)
        
        mock_get.assert_called_once_with(
            "https://test.workato.com/api/jobs",
            headers=client.headers,
            params={"recipe_id": 1, "status": "success", "limit": 10}
        )
        assert jobs == SAMPLE_JOBS 