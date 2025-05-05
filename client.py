from mcp import ClientSession
from mcp.client.sse import sse_client


async def run():
    async with sse_client(url="http://localhost:8000/sse") as streams:
        async with ClientSession(*streams) as session:

            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print(tools)

            # Call a tool
            # result = await session.call_tool("get_pokemon_info", arguments={"pokemon_name_or_id": "pikachu"})
            result = await session.call_tool("get_pokemon_info", )
            print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
