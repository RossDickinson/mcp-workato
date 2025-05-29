from workato_mcp.client import WorkatoClient
from workato_mcp.models import RecipeData, TestRecipeInput
from typing import Union, Optional, Dict, Any

workato_client = WorkatoClient()

def register_recipe_tools(mcp):
    @mcp.tool()
    async def list_recipes(include_tags: bool = False) -> str:
        """List all available recipes in Workato.

        Args:
            include_tags: Whether to include tags in the response.
        Returns:
            JSON string containing all recipes.
        """
        recipes = await workato_client.get_recipes(include_tags=include_tags)
        return f"Found {len(recipes)} recipes:\n\n{recipes}"

    @mcp.tool()
    async def get_recipe(recipe_id: Union[int, str]) -> str:
        """Get details for a specific recipe.

        Args:
            recipe_id: The ID of the recipe to retrieve.
        Returns:
            JSON string containing recipe details.
        """
        recipe = await workato_client.get_recipe_details(recipe_id)
        return f"Recipe details:\n\n{recipe}"

    @mcp.tool()
    async def start_recipe(recipe_id: Union[int, str]) -> str:
        """Start a recipe.

        Args:
            recipe_id: The ID of the recipe to start.
        Returns:
            Status message.
        """
        result = await workato_client.start_recipe(recipe_id)
        return f"Start recipe result: {result}"

    @mcp.tool()
    async def stop_recipe(recipe_id: Union[int, str]) -> str:
        """Stop a recipe.

        Args:
            recipe_id: The ID of the recipe to stop.
        Returns:
            Status message.
        """
        result = await workato_client.stop_recipe(recipe_id)
        return f"Stop recipe result: {result}"

    @mcp.tool()
    async def test_recipe(input: TestRecipeInput) -> str:
        """Test a recipe with optional input data.

        Args:
            input: Test recipe input parameters.
        Returns:
            Test results.
        """
        result = await workato_client.test_recipe(
            recipe_id=input.recipe_id,
            input_data=input.input_data
        )
        return f"Test recipe result: {result}"

    @mcp.tool()
    async def create_recipe(recipe: RecipeData) -> str:
        """Create a new recipe.

        Args:
            recipe: Recipe configuration data.
        Returns:
            Created recipe details.
        """
        recipe_data = recipe.dict(exclude_none=True)
        result = await workato_client.create_recipe(recipe_data)
        return f"Created recipe: {result}"

    @mcp.tool()
    async def update_recipe(recipe_id: Union[int, str], recipe: RecipeData) -> str:
        """Update an existing recipe.

        Args:
            recipe_id: The ID of the recipe to update.
            recipe: Updated recipe configuration data.
        Returns:
            Updated recipe details.
        """
        recipe_data = recipe.dict(exclude_none=True)
        result = await workato_client.update_recipe(recipe_id, recipe_data)
        return f"Updated recipe: {result}"

    @mcp.tool()
    async def delete_recipe(recipe_id: Union[int, str]) -> str:
        """Delete a recipe.

        Args:
            recipe_id: The ID of the recipe to delete.
        Returns:
            Status message.
        """
        result = await workato_client.delete_recipe(recipe_id)
        return f"Delete recipe result: {result}"

    @mcp.tool()
    async def copy_recipe(recipe_id: Union[int, str], folder_id: Optional[str] = None) -> str:
        """Copy a recipe to a new folder (optional).

        Args:
            recipe_id: The ID of the recipe to copy.
            folder_id: Optional folder ID for the copied recipe.
        Returns:
            Copy result details.
        """
        result = await workato_client.copy_recipe(recipe_id, folder_id)
        return f"Copy recipe result: {result}"

    @mcp.tool()
    async def reset_recipe_trigger(recipe_id: Union[int, str]) -> str:
        """Reset the trigger for a recipe.

        Args:
            recipe_id: The ID of the recipe to reset the trigger for.
        Returns:
            Reset result details.
        """
        result = await workato_client.reset_recipe_trigger(recipe_id)
        return f"Reset recipe trigger result: {result}"

    @mcp.tool()
    async def update_recipe_connection(recipe_id: Union[int, str], adapter_name: str, connection_id: int) -> str:
        """Update the connection for a stopped recipe.

        Args:
            recipe_id: The ID of the recipe to update the connection for.
            adapter_name: The internal name of the connector.
            connection_id: The ID of the new connection.
        Returns:
            Update result details.
        """
        result = await workato_client.update_recipe_connection(recipe_id, adapter_name, connection_id)
        return f"Update recipe connection result: {result}"

    @mcp.tool()
    async def poll_recipe_now(recipe_id: Union[int, str]) -> str:
        """Activate a polling trigger for a recipe.

        Args:
            recipe_id: The ID of the recipe to poll now.
        Returns:
            Poll result details.
        """
        result = await workato_client.poll_recipe_now(recipe_id)
        return f"Poll recipe now result: {result}"

    @mcp.tool()
    async def get_recipe_versions(recipe_id: Union[int, str], page: int = 1, per_page: int = 100) -> str:
        """Get all versions of a recipe.

        Args:
            recipe_id: The ID of the recipe to get versions for.
            page: Page number for pagination.
            per_page: Number of versions per page.
        Returns:
            Recipe versions details.
        """
        result = await workato_client.get_recipe_versions(recipe_id, page, per_page)
        return f"Recipe versions: {result}"

    @mcp.tool()
    async def get_recipe_version_details(recipe_id: Union[int, str], version_id: Union[int, str]) -> str:
        """Get details of a specific recipe version.

        Args:
            recipe_id: The ID of the recipe.
            version_id: The ID of the version to retrieve.
        Returns:
            Recipe version details.
        """
        result = await workato_client.get_recipe_version_details(recipe_id, version_id)
        return f"Recipe version details: {result}"

    @mcp.tool()
    async def update_recipe_version_comment(recipe_id: Union[int, str], version_id: Union[int, str], comment: str) -> str:
        """Update the comment for a specific recipe version.

        Args:
            recipe_id: The ID of the recipe.
            version_id: The ID of the version to update.
            comment: The new comment for the version.
        Returns:
            Update result details.
        """
        result = await workato_client.update_recipe_version_comment(recipe_id, version_id, comment)
        return f"Update recipe version comment result: {result}"

    # ...add more recipe tools here... 