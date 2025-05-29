import os
import json
import httpx
from typing import Dict, List, Optional, Any, Union
from dotenv import load_dotenv

class WorkatoClient:
    """Client for interacting with the Workato API."""
    
    def __init__(self, api_token: Optional[str] = None, base_url: Optional[str] = None):
        """Initialize the Workato API client.
        
        Args:
            api_token: The API token for authentication. If not provided, will try to load from environment.
            base_url: The base URL for Workato API. If not provided, will try to load from environment.
        """
        load_dotenv()
        
        self.api_token = api_token or os.getenv("WORKATO_API_TOKEN")
        if not self.api_token:
            raise ValueError("API token is required. Provide it as a parameter or set WORKATO_API_TOKEN environment variable.")
        
        self.base_url = base_url or os.getenv("WORKATO_BASE_URL", "https://www.workato.com/api")
        
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
    
    async def get_recipes(self, include_tags: bool = False) -> List[Dict[str, Any]]:
        """Get a list of all recipes.
        
        Args:
            include_tags: Whether to include tags in the response.
            
        Returns:
            List of recipe objects.
        """
        params = {}
        if include_tags:
            params["includes[]"] = "tags"
            
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/recipes",
                headers=self.headers,
                params=params
            )
            response.raise_for_status()
            return response.json()
    
    async def get_recipe_details(self, recipe_id: Union[int, str]) -> Dict[str, Any]:
        """Get details for a specific recipe.
        
        Args:
            recipe_id: The ID of the recipe to retrieve.
            
        Returns:
            Recipe object with details.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/recipes/{recipe_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
    
    async def start_recipe(self, recipe_id: Union[int, str]) -> Dict[str, Any]:
        """Start a recipe.
        
        Args:
            recipe_id: The ID of the recipe to start.
            
        Returns:
            Response object indicating success or failure.
        """
        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"{self.base_url}/recipes/{recipe_id}/start",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
    
    async def stop_recipe(self, recipe_id: Union[int, str]) -> Dict[str, Any]:
        """Stop a recipe.
        
        Args:
            recipe_id: The ID of the recipe to stop.
            
        Returns:
            Response object indicating success or failure.
        """
        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"{self.base_url}/recipes/{recipe_id}/stop",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
    
    async def test_recipe(self, recipe_id: Union[int, str], input_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Test a recipe with optional input data.
        
        Args:
            recipe_id: The ID of the recipe to test.
            input_data: Input data for testing the recipe.
            
        Returns:
            Test run results.
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/recipes/{recipe_id}/test_run",
                headers=self.headers,
                json=input_data or {}
            )
            response.raise_for_status()
            return response.json()
    
    async def create_recipe(self, recipe_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new recipe.
        
        Args:
            recipe_data: Recipe configuration data.
            
        Returns:
            Created recipe object.
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/recipes",
                headers=self.headers,
                json={"recipe": recipe_data}
            )
            response.raise_for_status()
            return response.json()
    
    async def update_recipe(self, recipe_id: Union[int, str], recipe_data: Dict[str, Any]) -> Dict[str, Any]:
        """Update an existing recipe.
        
        Args:
            recipe_id: The ID of the recipe to update.
            recipe_data: Recipe configuration data.
            
        Returns:
            Updated recipe object.
        """
        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"{self.base_url}/recipes/{recipe_id}",
                headers=self.headers,
                json={"recipe": recipe_data}
            )
            response.raise_for_status()
            return response.json()
    
    async def delete_recipe(self, recipe_id: Union[int, str]) -> Dict[str, Any]:
        """Delete a recipe.
        
        Args:
            recipe_id: The ID of the recipe to delete.
            
        Returns:
            Response object indicating success or failure.
        """
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{self.base_url}/recipes/{recipe_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
    
    async def get_jobs(self, recipe_id: Optional[Union[int, str]] = None, 
                       status: Optional[str] = None, 
                       limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get a list of jobs, optionally filtered by recipe ID and status.
        
        Args:
            recipe_id: Filter jobs by recipe ID.
            status: Filter jobs by status (e.g., "success", "error").
            limit: Maximum number of jobs to return.
            
        Returns:
            List of job objects.
        """
        params = {}
        if recipe_id:
            params["recipe_id"] = recipe_id
        if status:
            params["status"] = status
        if limit:
            params["limit"] = limit
            
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/jobs",
                headers=self.headers,
                params=params
            )
            response.raise_for_status()
            return response.json()
    
    async def get_job_details(self, job_id: Union[int, str]) -> Dict[str, Any]:
        """Get details for a specific job.
        
        Args:
            job_id: The ID of the job to retrieve.
            
        Returns:
            Job object with details.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/jobs/{job_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
    
    async def get_folders(self) -> List[Dict[str, Any]]:
        """Get a list of all folders.
        
        Returns:
            List of folder objects.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/folders",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
    
    async def get_connections(self) -> List[Dict[str, Any]]:
        """Get a list of all connections.
        
        Returns:
            List of connection objects.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/connections",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
    
    async def get_connection_details(self, connection_id: Union[int, str]) -> Dict[str, Any]:
        """Get details for a specific connection.
        
        Args:
            connection_id: The ID of the connection to retrieve.
            
        Returns:
            Connection object with details.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/connections/{connection_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
    
    async def copy_recipe(self, recipe_id: Union[int, str], folder_id: Optional[str] = None) -> Dict[str, Any]:
        payload = {}
        if folder_id:
            payload["folder_id"] = folder_id
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/recipes/{recipe_id}/copy",
                headers=self.headers,
                json=payload if payload else None
            )
            response.raise_for_status()
            return response.json()

    async def reset_recipe_trigger(self, recipe_id: Union[int, str]) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/recipes/{recipe_id}/reset_trigger",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()

    async def update_recipe_connection(self, recipe_id: Union[int, str], adapter_name: str, connection_id: int) -> Dict[str, Any]:
        payload = {"adapter_name": adapter_name, "connection_id": connection_id}
        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"{self.base_url}/recipes/{recipe_id}/connect",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()

    async def poll_recipe_now(self, recipe_id: Union[int, str]) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/recipes/{recipe_id}/poll_now",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()

    async def get_recipe_versions(self, recipe_id: Union[int, str], page: int = 1, per_page: int = 100) -> Dict[str, Any]:
        params = {"page": page, "per_page": per_page}
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/recipes/{recipe_id}/versions",
                headers=self.headers,
                params=params
            )
            response.raise_for_status()
            return response.json()

    async def get_recipe_version_details(self, recipe_id: Union[int, str], version_id: Union[int, str]) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/recipes/{recipe_id}/versions/{version_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()

    async def update_recipe_version_comment(self, recipe_id: Union[int, str], version_id: Union[int, str], comment: str) -> Dict[str, Any]:
        payload = {"comment": comment}
        async with httpx.AsyncClient() as client:
            response = await client.patch(
                f"{self.base_url}/recipes/{recipe_id}/versions/{version_id}",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()

    async def get_folder_assets(self, folder_id: Optional[int] = None, include_test_cases: bool = False, include_data: bool = False) -> dict:
        """View assets in a folder for export manifests."""
        params = {}
        if folder_id is not None:
            params["folder_id"] = folder_id
        if include_test_cases:
            params["include_test_cases"] = str(include_test_cases).lower()
        if include_data:
            params["include_data"] = str(include_data).lower()
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/export_manifests/folder_assets",
                headers=self.headers,
                params=params
            )
            response.raise_for_status()
            return response.json()

    async def create_export_manifest(self, export_manifest: dict) -> dict:
        """Create an export manifest."""
        payload = {"export_manifest": export_manifest}
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/export_manifests",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()

    async def update_export_manifest(self, manifest_id: Union[int, str], export_manifest: dict) -> dict:
        """Update an export manifest."""
        payload = {"export_manifest": export_manifest}
        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"{self.base_url}/export_manifests/{manifest_id}",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()

    async def get_export_manifest(self, manifest_id: Union[int, str]) -> dict:
        """View an export manifest."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/export_manifests/{manifest_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()

    async def delete_export_manifest(self, manifest_id: Union[int, str]) -> dict:
        """Delete an export manifest."""
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{self.base_url}/export_manifests/{manifest_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()

    async def export_package(self, manifest_id: Union[int, str]) -> dict:
        """Export a package based on a manifest."""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/packages/export/{manifest_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()

    async def import_package(self, folder_id: Union[int, str], file_bytes: bytes, restart_recipes: bool = False, include_tags: bool = False, folder_id_for_home_assets: Optional[str] = None) -> dict:
        """Import a package into a folder. file_bytes should be the content of the zip file."""
        params = {"restart_recipes": str(restart_recipes).lower(), "include_tags": str(include_tags).lower()}
        if folder_id_for_home_assets:
            params["folder_id_for_home_assets"] = folder_id_for_home_assets
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/packages/import/{folder_id}",
                headers={**self.headers, "Content-Type": "application/octet-stream"},
                params=params,
                content=file_bytes
            )
            response.raise_for_status()
            return response.json()

    async def get_package(self, package_id: Union[int, str]) -> dict:
        """Get details of an imported or exported package."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/packages/{package_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()

    async def download_package(self, package_id: Union[int, str]) -> bytes:
        """Download a package zip file by package ID. Returns the raw bytes."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/packages/{package_id}/download",
                headers=self.headers,
                follow_redirects=True
            )
            response.raise_for_status()
            return response.content

    async def search_custom_connectors(self, title: str) -> dict:
        """Search for custom connectors by title."""
        payload = {"title": title}
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/custom_connectors/search",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()

    async def get_custom_connector_code(self, connector_id: Union[int, str]) -> dict:
        """Fetch code for a custom connector by ID."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/custom_connectors/{connector_id}/code",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()

    async def generate_schema_from_json(self, sample: str) -> dict:
        """Generate Workato schema from a stringified JSON sample."""
        payload = {"sample": sample}
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/sdk/generate_schema/json",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()

    async def generate_schema_from_csv(self, sample: str, col_sep: Optional[str] = None) -> dict:
        """Generate Workato schema from a stringified CSV sample."""
        payload = {"sample": sample}
        if col_sep:
            payload["col_sep"] = col_sep
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/sdk/generate_schema/csv",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()

    async def create_custom_connector(self, connector: dict) -> dict:
        """Create a custom connector."""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/custom_connectors",
                headers=self.headers,
                json=connector
            )
            response.raise_for_status()
            return response.json()

    async def release_custom_connector(self, connector_id: Union[int, str]) -> dict:
        """Release the latest version of a custom connector."""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/custom_connectors/{connector_id}/release",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()

    async def share_custom_connector(self, connector_id: Union[int, str]) -> dict:
        """Share the most recently released version of a custom connector."""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/custom_connectors/{connector_id}/share",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()

    async def update_custom_connector(self, connector_id: Union[int, str], connector: dict) -> dict:
        """Update a custom connector."""
        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"{self.base_url}/custom_connectors/{connector_id}",
                headers=self.headers,
                json=connector
            )
            response.raise_for_status()
            return response.json()

    async def list_connections(self, folder_id: Optional[str] = None, parent_id: Optional[str] = None, external_id: Optional[str] = None, include_runtime_connections: Optional[str] = None, includes: Optional[list] = None) -> dict:
        """List all connections for the authenticated user."""
        params = {}
        if folder_id:
            params["folder_id"] = folder_id
        if parent_id:
            params["parent_id"] = parent_id
        if external_id:
            params["external_id"] = external_id
        if include_runtime_connections:
            params["include_runtime_connections"] = include_runtime_connections
        if includes:
            params["includes[]"] = includes
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/connections",
                headers=self.headers,
                params=params
            )
            response.raise_for_status()
            return response.json()

    async def create_connection(self, connection: dict) -> dict:
        """Create a new connection."""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/connections",
                headers=self.headers,
                json=connection
            )
            response.raise_for_status()
            return response.json()

    async def update_connection(self, connection_id: Union[int, str], connection: dict) -> dict:
        """Update a connection."""
        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"{self.base_url}/connections/{connection_id}",
                headers=self.headers,
                json=connection
            )
            response.raise_for_status()
            return response.json()

    async def disconnect_connection(self, connection_id: Union[int, str], force: bool = False) -> dict:
        """Disconnect a connection."""
        payload = {"force": force} if force else {}
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/connections/{connection_id}/disconnect",
                headers=self.headers,
                json=payload if payload else None
            )
            response.raise_for_status()
            return response.json()

    async def delete_connection(self, connection_id: Union[int, str]) -> dict:
        """Delete a connection."""
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{self.base_url}/connections/{connection_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()

    async def list_lookup_tables(self, page: int = 1, per_page: int = 100) -> list:
        """List all lookup tables for the authenticated user."""
        params = {"page": page, "per_page": per_page}
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/lookup_tables",
                headers=self.headers,
                params=params
            )
            response.raise_for_status()
            return response.json()

    async def list_lookup_table_rows(self, lookup_table_id: Union[int, str], page: int = 1, per_page: int = 500, filters: Optional[dict] = None) -> list:
        """List rows from a lookup table, with optional filters and pagination."""
        params = {"page": page, "per_page": per_page}
        if filters:
            params.update(filters)
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/lookup_tables/{lookup_table_id}/rows",
                headers=self.headers,
                params=params
            )
            response.raise_for_status()
            return response.json()

    async def lookup_table_row(self, lookup_table_id: Union[int, str], filters: dict) -> dict:
        """Find the first row matching the given criteria in the lookup table."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/lookup_tables/{lookup_table_id}/lookup",
                headers=self.headers,
                params=filters
            )
            response.raise_for_status()
            return response.json()

    async def get_lookup_table_row(self, lookup_table_id: Union[int, str], row_id: Union[int, str]) -> dict:
        """Get a row from the lookup table by row ID."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/lookup_tables/{lookup_table_id}/rows/{row_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()

    async def add_lookup_table_row(self, lookup_table_id: Union[int, str], data: dict) -> dict:
        """Add a row to the lookup table."""
        payload = {"data": data}
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/lookup_tables/{lookup_table_id}/rows",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()

    async def create_lookup_table(self, lookup_table: dict) -> dict:
        """Create a new lookup table."""
        payload = {"lookup_table": lookup_table}
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/lookup_tables",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()

    async def batch_delete_lookup_tables(self, ids: list) -> dict:
        """Delete lookup tables in batch."""
        payload = {"ids": ids}
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/lookup_tables/batch_delete",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()

    async def update_lookup_table_row(self, lookup_table_id: Union[int, str], row_id: Union[int, str], data: dict) -> dict:
        """Update a row in the lookup table."""
        payload = {"data": data}
        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"{self.base_url}/lookup_tables/{lookup_table_id}/rows/{row_id}",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()

    async def delete_lookup_table_row(self, lookup_table_id: Union[int, str], row_id: Union[int, str]) -> dict:
        """Delete a row from the lookup table."""
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{self.base_url}/lookup_tables/{lookup_table_id}/rows/{row_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json() 