import pytest
from unittest.mock import patch, AsyncMock
from workato_mcp.client import WorkatoClient
from server import (
    list_recipes, get_recipe, start_recipe, stop_recipe, 
    test_recipe, create_recipe, update_recipe, delete_recipe,
    list_jobs, get_job, list_folders, list_connections, get_connection,
    TestRecipeInput, RecipeData, JobFilter
)

# Sample test data
SAMPLE_RECIPES = [
    {"id": 1, "name": "Recipe 1"},
    {"id": 2, "name": "Recipe 2"}
]

SAMPLE_RECIPE_DETAILS = {
    "id": 1,
    "name": "Recipe 1",
    "description": "Test recipe"
}

@pytest.mark.asyncio
async def test_list_recipes():
    """Test list_recipes tool."""
    with patch("workato_mcp.client.WorkatoClient.get_recipes", new_callable=AsyncMock) as mock_get_recipes:
        mock_get_recipes.return_value = SAMPLE_RECIPES
        
        result = await list_recipes()
        
        mock_get_recipes.assert_called_once_with(include_tags=False)
        assert "Found 2 recipes" in result
        assert str(SAMPLE_RECIPES) in result

@pytest.mark.asyncio
async def test_get_recipe():
    """Test get_recipe tool."""
    with patch("workato_mcp.client.WorkatoClient.get_recipe_details", new_callable=AsyncMock) as mock_get_recipe:
        mock_get_recipe.return_value = SAMPLE_RECIPE_DETAILS
        
        result = await get_recipe(1)
        
        mock_get_recipe.assert_called_once_with(1)
        assert "Recipe details" in result
        assert str(SAMPLE_RECIPE_DETAILS) in result

@pytest.mark.asyncio
async def test_start_recipe():
    """Test start_recipe tool."""
    with patch("workato_mcp.client.WorkatoClient.start_recipe", new_callable=AsyncMock) as mock_start_recipe:
        mock_start_recipe.return_value = {"status": "started"}
        
        result = await start_recipe(1)
        
        mock_start_recipe.assert_called_once_with(1)
        assert "Start recipe result" in result
        assert "started" in result

@pytest.mark.asyncio
async def test_test_recipe():
    """Test test_recipe tool."""
    with patch("workato_mcp.client.WorkatoClient.test_recipe", new_callable=AsyncMock) as mock_test_recipe:
        mock_test_recipe.return_value = {"status": "success", "result": {"data": "test"}}
        
        input_data = TestRecipeInput(recipe_id=1, input_data={"param": "value"})
        result = await test_recipe(input_data)
        
        mock_test_recipe.assert_called_once_with(recipe_id=1, input_data={"param": "value"})
        assert "Test recipe result" in result
        assert "success" in result

@pytest.mark.asyncio
async def test_create_recipe():
    """Test create_recipe tool."""
    with patch("workato_mcp.client.WorkatoClient.create_recipe", new_callable=AsyncMock) as mock_create_recipe:
        mock_create_recipe.return_value = {"id": 3, "name": "New Recipe"}
        
        recipe_data = RecipeData(
            name="New Recipe",
            code='{"trigger": {"type": "webhook"}, "actions": []}',
            description="Test recipe"
        )
        result = await create_recipe(recipe_data)
        
        mock_create_recipe.assert_called_once()
        assert "Created recipe" in result
        assert "New Recipe" in result 