import os
import logging
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from workato_mcp.client import WorkatoClient
from workato_mcp.models import RecipeData, TestRecipeInput
from workato_mcp.tools.recipes import register_recipe_tools
from workato_mcp.tools.recipe_lifecycle_management import register_recipe_lifecycle_tools
from workato_mcp.tools.custom_connector_sdk import register_custom_connector_sdk_tools
from workato_mcp.tools.connections import register_connection_tools
from workato_mcp.tools.lookup_tables import register_lookup_table_tools
# (add other tool registrations as needed)

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("workato_mcp")

# Initialize the MCP server
mcp = FastMCP(
    "Workato MCP Server",
    description="MCP Server for interacting with Workato APIs to manage recipes and jobs",
    dependencies=["httpx", "python-dotenv", "pydantic"]
)

# Validate environment variables
required_env_vars = ["WORKATO_API_TOKEN", "WORKATO_BASE_URL"]
missing_vars = [var for var in required_env_vars if not os.getenv(var)]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

# Register tools
register_recipe_tools(mcp)
register_recipe_lifecycle_tools(mcp)
register_custom_connector_sdk_tools(mcp)
register_connection_tools(mcp)
register_lookup_table_tools(mcp)
# (register other tool sets here)

if __name__ == "__main__":
    logger.info("Starting Workato MCP server (FastMCP mode)")
    logger.info("MCP server is running and waiting for client connections via stdio")
    mcp.run()

