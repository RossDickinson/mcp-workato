from workato_mcp.client import WorkatoClient
from typing import Union, Optional, Dict, Any

workato_client = WorkatoClient()

def register_custom_connector_sdk_tools(mcp):
    @mcp.tool()
    async def search_custom_connectors(title: str) -> str:
        """Search for custom connectors by title.

        Args:
            title: The case-sensitive title of the custom connector to search for.
        Returns:
            JSON string containing the search results.
        """
        result = await workato_client.search_custom_connectors(title)
        return f"Custom connector search result: {result}"

    @mcp.tool()
    async def get_custom_connector_code(connector_id: Union[int, str]) -> str:
        """Fetch code for a custom connector by ID.

        Args:
            connector_id: The ID of the custom connector.
        Returns:
            JSON string containing the connector code.
        """
        result = await workato_client.get_custom_connector_code(connector_id)
        return f"Custom connector code: {result}"

    @mcp.tool()
    async def generate_schema_from_json(sample: str) -> str:
        """Generate Workato schema from a stringified JSON sample.

        Args:
            sample: Stringified JSON sample document.
        Returns:
            JSON string containing the generated schema.
        """
        result = await workato_client.generate_schema_from_json(sample)
        return f"Generated schema from JSON: {result}"

    @mcp.tool()
    async def generate_schema_from_csv(sample: str, col_sep: Optional[str] = None) -> str:
        """Generate Workato schema from a stringified CSV sample.

        Args:
            sample: Stringified CSV sample document.
            col_sep: Optional column delimiter (comma, semicolon, space, tab, colon, pipe).
        Returns:
            JSON string containing the generated schema.
        """
        result = await workato_client.generate_schema_from_csv(sample, col_sep)
        return f"Generated schema from CSV: {result}"

    @mcp.tool()
    async def create_custom_connector(connector: Dict[str, Any]) -> str:
        """Create a custom connector.

        Args:
            connector: Dictionary representing the custom connector payload.
        Returns:
            JSON string containing the created connector.
        """
        result = await workato_client.create_custom_connector(connector)
        return f"Created custom connector: {result}"

    @mcp.tool()
    async def release_custom_connector(connector_id: Union[int, str]) -> str:
        """Release the latest version of a custom connector.

        Args:
            connector_id: The ID of the custom connector to release.
        Returns:
            JSON string containing the release result.
        """
        result = await workato_client.release_custom_connector(connector_id)
        return f"Release custom connector result: {result}"

    @mcp.tool()
    async def share_custom_connector(connector_id: Union[int, str]) -> str:
        """Share the most recently released version of a custom connector.

        Args:
            connector_id: The ID of the custom connector to share.
        Returns:
            JSON string containing the share result.
        """
        result = await workato_client.share_custom_connector(connector_id)
        return f"Share custom connector result: {result}"

    @mcp.tool()
    async def update_custom_connector(connector_id: Union[int, str], connector: Dict[str, Any]) -> str:
        """Update a custom connector.

        Args:
            connector_id: The ID of the custom connector to update.
            connector: Dictionary representing the updated connector payload.
        Returns:
            JSON string containing the updated connector.
        """
        result = await workato_client.update_custom_connector(connector_id, connector)
        return f"Updated custom connector: {result}" 