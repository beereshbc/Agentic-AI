from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
def get_weather(location:str) -> str:
    """Get the weather location."""
    return "It's alwasy rain at in Bengaluru"

if __name__ == "__main__":
     mcp.run(transport="streamable-http")