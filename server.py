# server.py
from mcp.server.fastmcp import FastMCP
import requests

# Create an MCP server
mcp = FastMCP("PokeServer", "1.0.0")


# Add an addition tool
# @mcp.tool()
# def add(a: int, b: int) -> int:
#     """Add two numbers"""
#     return a + b


# # Add a dynamic greeting resource
# @mcp.resource("greeting://{name}")
# def get_greeting(name: str) -> str:
#     """Get a personalized greeting"""
#     return f"Hello, {name}!"

@mcp.tool("get_pokemon_info", "Get Pokemon Info from PokeAPI")
def get_pokemon_info(pokemon_name_or_id: str | int) -> dict:
    """
    Fetch Pokemon information from the PokeAPI
    
    Args:
        pokemon_name_or_id (str or int): Name or ID of the Pokemon
        
    Returns:
        dict: Pokemon data if successful, None if unsuccessful
    """
    # Convert input to lowercase if it's a string
    if isinstance(pokemon_name_or_id, str):
        pokemon_name_or_id = pokemon_name_or_id.lower()
    
    # Construct the API URL
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name_or_id}"
    
    try:
        # Make the API request
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

if __name__ == "__main__":
    mcp.run()