from mcp.server.fastmcp import FastMCP


mcp = FastMCP(name ="Hello mcp_server", stateless_http= True) # when True we don't need handshake.

# stateless mtlb req,res k bad bhol jaye. gajni.

@mcp.tool()
def  hello(name: str)-> str:
    return f"hi iam mcp tool {name}"

@mcp.tool()
def get_weather(city:str)-> str:
    """Get weather for a given city"""
    return f"The weather is sunny in {city}:"    

mcp_app = mcp.streamable_http_app()