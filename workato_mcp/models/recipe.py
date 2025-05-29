from pydantic import BaseModel, Field
from typing import Optional, Union, Dict, Any

class RecipeData(BaseModel):
    name: str = Field(..., description="Name of the recipe")
    code: str = Field(..., description="Recipe code in JSON format")
    folder_id: Optional[int] = Field(None, description="ID of the folder to place the recipe in")
    description: Optional[str] = Field(None, description="Description of the recipe")

class TestRecipeInput(BaseModel):
    recipe_id: Union[int, str] = Field(..., description="ID of the recipe to test")
    input_data: Optional[Dict[str, Any]] = Field(None, description="Input data for testing the recipe") 