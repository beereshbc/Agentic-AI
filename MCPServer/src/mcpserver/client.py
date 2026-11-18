from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio


async def main():
    client = MultiServerMCPClient(
         {
            "math": {
                "command": "python",
                "args": [
                    r"E:\Beeresh's Project\AgenticAI\MCPServer\src\mcpserver\mathserver.py"
                ],
                "transport": "stdio",
            },
            "weather":{
               "url": "http://127.0.0.1:8000/mcp",
                "transport":"streamable_http"
            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tool = await client.get_tools()
    model = ChatGroq(model="openai/gpt-oss-120b")
    agent = create_agent(
       model=model,
       tools=tool
    )

    math_response = await agent.ainvoke(
        {
            "messages":[
                {
                    "role":"user",
                    "content":"what's the (3+5) X 12 ?"
                }
            ]
        }
    )

    print("Math Response: ", math_response['messages'][-1].content)


asyncio.run(main())