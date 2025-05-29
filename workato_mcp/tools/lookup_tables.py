from workato_mcp.client import WorkatoClient
from typing import Union, Optional, Dict, Any, List

workato_client = WorkatoClient()

def register_lookup_table_tools(mcp):
    @mcp.tool()
    async def list_lookup_tables(page: int = 1, per_page: int = 100) -> str:
        """List all lookup tables for the authenticated user.
        Args:
            page: Page number (default 1).
            per_page: Page size (default 100, max 100).
        Returns:
            JSON string containing all lookup tables.
        """
        result = await workato_client.list_lookup_tables(page, per_page)
        return f"Lookup tables: {result}"

    @mcp.tool()
    async def list_lookup_table_rows(lookup_table_id: Union[int, str], page: int = 1, per_page: int = 500, filters: Optional[Dict[str, Any]] = None) -> str:
        """List rows from a lookup table, with optional filters and pagination.
        Args:
            lookup_table_id: The ID of the lookup table.
            page: Page number (default 1).
            per_page: Page size (default 500, max 1000).
            filters: Optional dictionary of filter criteria (e.g., {"by[code]": "US"}).
        Returns:
            JSON string containing the rows.
        """
        result = await workato_client.list_lookup_table_rows(lookup_table_id, page, per_page, filters)
        return f"Lookup table rows: {result}"

    @mcp.tool()
    async def lookup_table_row(lookup_table_id: Union[int, str], filters: Dict[str, Any]) -> str:
        """Find the first row matching the given criteria in the lookup table.
        Args:
            lookup_table_id: The ID of the lookup table.
            filters: Dictionary of lookup criteria (e.g., {"by[code]": "US"}).
        Returns:
            JSON string containing the found row or 404 if not found.
        """
        result = await workato_client.lookup_table_row(lookup_table_id, filters)
        return f"Lookup table row: {result}"

    @mcp.tool()
    async def get_lookup_table_row(lookup_table_id: Union[int, str], row_id: Union[int, str]) -> str:
        """Get a row from the lookup table by row ID.
        Args:
            lookup_table_id: The ID of the lookup table.
            row_id: The ID of the row.
        Returns:
            JSON string containing the row.
        """
        result = await workato_client.get_lookup_table_row(lookup_table_id, row_id)
        return f"Lookup table row: {result}"

    @mcp.tool()
    async def add_lookup_table_row(lookup_table_id: Union[int, str], data: Dict[str, Any]) -> str:
        """Add a row to the lookup table.
        Args:
            lookup_table_id: The ID of the lookup table.
            data: Dictionary containing the row data.
        Returns:
            JSON string containing the added row.
        """
        result = await workato_client.add_lookup_table_row(lookup_table_id, data)
        return f"Added lookup table row: {result}"

    @mcp.tool()
    async def create_lookup_table(lookup_table: Dict[str, Any]) -> str:
        """Create a new lookup table.
        Args:
            lookup_table: Dictionary containing the lookup table definition (name, project_id, schema, etc).
        Returns:
            JSON string containing the created lookup table.
        """
        result = await workato_client.create_lookup_table(lookup_table)
        return f"Created lookup table: {result}"

    @mcp.tool()
    async def batch_delete_lookup_tables(ids: List[Union[int, str]]) -> str:
        """Delete lookup tables in batch.
        Args:
            ids: List of lookup table IDs to delete.
        Returns:
            JSON string containing the batch delete result.
        """
        result = await workato_client.batch_delete_lookup_tables(ids)
        return f"Batch delete result: {result}"

    @mcp.tool()
    async def update_lookup_table_row(lookup_table_id: Union[int, str], row_id: Union[int, str], data: Dict[str, Any]) -> str:
        """Update a row in the lookup table.
        Args:
            lookup_table_id: The ID of the lookup table.
            row_id: The ID of the row to update.
            data: Dictionary containing the updated row data.
        Returns:
            JSON string containing the updated row.
        """
        result = await workato_client.update_lookup_table_row(lookup_table_id, row_id, data)
        return f"Updated lookup table row: {result}"

    @mcp.tool()
    async def delete_lookup_table_row(lookup_table_id: Union[int, str], row_id: Union[int, str]) -> str:
        """Delete a row from the lookup table.
        Args:
            lookup_table_id: The ID of the lookup table.
            row_id: The ID of the row to delete.
        Returns:
            JSON string containing the delete result.
        """
        result = await workato_client.delete_lookup_table_row(lookup_table_id, row_id)
        return f"Delete lookup table row result: {result}" 