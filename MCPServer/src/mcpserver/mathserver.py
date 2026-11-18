from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")


@mcp.tool()
def add(a:int, b:int) -> int:
    """
    _Summury_ 
    add two numbers
    """
    return a+b


@mcp.tool()
def multiple(a:int, b:int) -> int:
    """
    MUltiply of Two Numbers
    """
    return a*b

#the transport="stdio" argument tells the server to:
#use the standard input/output to recieve and respond to tool function call


if __name__ =="__main__":
    mcp.run(transport="stdio")