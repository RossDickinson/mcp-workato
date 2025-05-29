from workato_mcp.client import WorkatoClient
from workato_mcp.models import RecipeData, TestRecipeInput
from typing import Union, Optional, Dict, Any

workato_client = WorkatoClient()

def register_tools(mcp):
    @mcp.tool()
    async def list_recipes(include_tags: bool = False) -> str:
        """List all available recipes in Workato."""
        recipes = await workato_client.get_recipes(include_tags=include_tags)
        return f"Found {len(recipes)} recipes:\n\n{recipes}"

    # ... (other @mcp.tool() functions here, unchanged) 