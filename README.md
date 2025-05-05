# mcp-pokemon

# MCP Pokemon Server

This repository contains an MCP server implementation for interacting with the PokeAPI.

## Prerequisites

1. **Python**: Ensure Python 3.12 or higher is installed.
2. **Dependencies**: Install the required dependencies using `pip`.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd mcp-pokemon

   ```

2. Create a virtual environment:

```
python3 -m venv mcppoke_venv
source mcppoke_venv/bin/activate  # On Windows, use `mcppoke_venv\Scripts\activate`
```

3. Install the required dependencies:

Running the Server
To run the MCP server, execute the following command:
mcp dev server.py - for inspector debugging
mcp run server.py - for running the server directly

Features
Tools: The server provides tools like get_pokemon_info to fetch data from the PokeAPI.
Resources: Extendable to include dynamic resources for interacting with clients.
Testing
You can test the server using the MCP Inspector or integrate it with compatible clients.

Additional Notes
Ensure the virtual environment is activated before running the server.
For more information on MCP, visit the Model Context Protocol documentation.
