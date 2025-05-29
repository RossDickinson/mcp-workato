from workato_mcp.client import WorkatoClient
from typing import Union, Optional, Dict, Any

workato_client = WorkatoClient()

def register_recipe_lifecycle_tools(mcp):
    @mcp.tool()
    async def get_folder_assets(folder_id: Optional[int] = None, include_test_cases: bool = False, include_data: bool = False) -> str:
        """View assets in a folder for export manifests.

        Args:
            folder_id: The ID of the folder containing the asset. Defaults to root folder.
            include_test_cases: Not supported, defaults to false.
            include_data: Whether to include data from the list of assets. Defaults to false.
        Returns:
            JSON string containing folder assets.
        """
        result = await workato_client.get_folder_assets(folder_id, include_test_cases, include_data)
        return f"Folder assets: {result}"

    @mcp.tool()
    async def create_export_manifest(export_manifest: Dict[str, Any]) -> str:
        """Create an export manifest.

        Args:
            export_manifest: Dictionary representing the export manifest payload.
        Returns:
            JSON string containing the created export manifest.
        """
        result = await workato_client.create_export_manifest(export_manifest)
        return f"Created export manifest: {result}"

    @mcp.tool()
    async def update_export_manifest(manifest_id: Union[int, str], export_manifest: Dict[str, Any]) -> str:
        """Update an export manifest.

        Args:
            manifest_id: The ID of the export manifest to update.
            export_manifest: Dictionary representing the updated export manifest payload.
        Returns:
            JSON string containing the updated export manifest.
        """
        result = await workato_client.update_export_manifest(manifest_id, export_manifest)
        return f"Updated export manifest: {result}"

    @mcp.tool()
    async def get_export_manifest(manifest_id: Union[int, str]) -> str:
        """View an export manifest.

        Args:
            manifest_id: The ID of the export manifest to view.
        Returns:
            JSON string containing the export manifest details.
        """
        result = await workato_client.get_export_manifest(manifest_id)
        return f"Export manifest: {result}"

    @mcp.tool()
    async def delete_export_manifest(manifest_id: Union[int, str]) -> str:
        """Delete an export manifest.

        Args:
            manifest_id: The ID of the export manifest to delete.
        Returns:
            JSON string containing the delete result.
        """
        result = await workato_client.delete_export_manifest(manifest_id)
        return f"Delete export manifest result: {result}"

    @mcp.tool()
    async def export_package(manifest_id: Union[int, str]) -> str:
        """Export a package based on a manifest.

        Args:
            manifest_id: The ID of the export manifest to use for export.
        Returns:
            JSON string containing the export package result.
        """
        result = await workato_client.export_package(manifest_id)
        return f"Export package result: {result}"

    @mcp.tool()
    async def import_package(folder_id: Union[int, str], file_bytes: bytes, restart_recipes: bool = False, include_tags: bool = False, folder_id_for_home_assets: Optional[str] = None) -> str:
        """Import a package into a folder.

        Args:
            folder_id: The ID of the folder to import into.
            file_bytes: The content of the zip file to import.
            restart_recipes: Whether to restart running recipes during import.
            include_tags: Whether to preserve tags assigned to assets.
            folder_id_for_home_assets: Optional folder for home assets.
        Returns:
            JSON string containing the import package result.
        """
        result = await workato_client.import_package(folder_id, file_bytes, restart_recipes, include_tags, folder_id_for_home_assets)
        return f"Import package result: {result}"

    @mcp.tool()
    async def get_package(package_id: Union[int, str]) -> str:
        """Get details of an imported or exported package.

        Args:
            package_id: The ID of the package.
        Returns:
            JSON string containing the package details.
        """
        result = await workato_client.get_package(package_id)
        return f"Package details: {result}"

    @mcp.tool()
    async def download_package(package_id: Union[int, str]) -> bytes:
        """Download a package zip file by package ID.

        Args:
            package_id: The ID of the package to download.
        Returns:
            The raw bytes of the downloaded package zip file.
        """
        result = await workato_client.download_package(package_id)
        return result 