from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="hello-server",
    stateless_http=True,
)

# If the module isn't found, use this direct attribute override 
# which works on older FastMCP versions to bypass host checks
try:
    from mcp.server.fastmcp.settings import TransportSecuritySettings
    mcp.settings.transport_security = TransportSecuritySettings(
        enable_dns_rebinding_protection=False
    )
except ImportError:
    # Fallback for older SDK versions
    if hasattr(mcp, "settings"):
        mcp.settings.host = "0.0.0.0"

@mcp.tool()
def  hello(name: str)-> str:
    return f"hi i am mcp tool {name}"

@mcp.tool()
def get_weather(city:str)-> str:
    """Get weather for a given city"""
    return f"The weather is sunny in {city}:"    

mcp_app = mcp.streamable_http_app() 

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MCP Server Running"}

app.mount("/", mcp_app)


# todo----------------------------------Sir Hamzah 1st Code -----------------------------------------
# ! Problem sirf ye hai ke FastMCP root / endpoint provide nahi karta.
# ! is leye not found araha tha, to fastapi ka endpoint add kia h, 

# mcp = FastMCP(name ="Hello mcp_server", stateless_http= True) # when True we don't need handshake.

# # stateless mtlb req,res k bad bhol jaye. gajni.

# @mcp.tool()
# def  hello(name: str)-> str:
#     return f"hi iam mcp tool {name}"

# @mcp.tool()
# def get_weather(city:str)-> str:
#     """Get weather for a given city"""
#     return f"The weather is sunny in {city}:"    

# mcp_app = mcp.streamable_http_app()