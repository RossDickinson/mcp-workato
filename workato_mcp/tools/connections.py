from workato_mcp.client import WorkatoClient
from typing import Union, Optional, Dict, Any

workato_client = WorkatoClient()

def register_connection_tools(mcp):
    @mcp.tool()
    async def list_connections(folder_id: Optional[str] = None, parent_id: Optional[str] = None, external_id: Optional[str] = None, include_runtime_connections: Optional[str] = None, includes: Optional[list] = None) -> str:
        """List all connections for the authenticated user.

        Args:
            folder_id: Optional folder ID of the connection.
            parent_id: Optional parent ID of the connection.
            external_id: Optional external identifier for the connection.
            include_runtime_connections: 'true' to include runtime user connections.
            includes: Optional list of additional fields to include (e.g., ['tags']).
        Returns:
            JSON string containing all connections.
        """
        result = await workato_client.list_connections(folder_id, parent_id, external_id, include_runtime_connections, includes)
        return f"Connections: {result}"

    @mcp.tool()
    async def create_connection(connection: Dict[str, Any]) -> str:
        """Create a new connection.

        Args:
            connection: Dictionary representing the connection payload.
        Returns:
            JSON string containing the created connection.
        """
        result = await workato_client.create_connection(connection)
        return f"Created connection: {result}"

    @mcp.tool()
    async def update_connection(connection_id: Union[int, str], connection: Dict[str, Any]) -> str:
        """Update a connection.

        Args:
            connection_id: The ID of the connection to update.
            connection: Dictionary representing the updated connection payload.
        Returns:
            JSON string containing the updated connection.
        """
        result = await workato_client.update_connection(connection_id, connection)
        return f"Updated connection: {result}"

    @mcp.tool()
    async def disconnect_connection(connection_id: Union[int, str], force: bool = False) -> str:
        """Disconnect a connection.

        Args:
            connection_id: The ID of the connection to disconnect.
            force: Set to true to forcefully disconnect an active connection used by active recipes.
        Returns:
            JSON string containing the disconnect result.
        """
        result = await workato_client.disconnect_connection(connection_id, force)
        return f"Disconnect connection result: {result}"

    @mcp.tool()
    async def delete_connection(connection_id: Union[int, str]) -> str:
        """Delete a connection.

        Args:
            connection_id: The ID of the connection to delete.
        Returns:
            JSON string containing the delete result.
        """
        result = await workato_client.delete_connection(connection_id)
        return f"Delete connection result: {result}" 