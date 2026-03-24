# Claude API — Builder de Handlers MCP

## Prompt
```text
Act as an expert in building MCP (Model Context Protocol) handlers for Claude.

JARVIS MCP SERVER: src/mcp_server.py
EXISTING TOOLS: brain_analyze, gpu_info, system_info, memory_recall, lm_query, etc.

TASK: Create new MCP tool handlers that:
1. Follow the MCP spec (name, description, inputSchema, handler function)
2. Return structured JSON responses
3. Handle errors gracefully
4. Log to structured logging
5. Are async-compatible

TEMPLATE:
```python
@server.tool("tool_name")
async def tool_name(arguments: dict) -> str:
    """Tool description for Claude."""
    try:
        result = do_something(arguments)
        return json.dumps({"status": "ok", "data": result})
    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)})
```

Current count: 600+ handlers. Port: 8765 (WebSocket).
Respond in French.
```
