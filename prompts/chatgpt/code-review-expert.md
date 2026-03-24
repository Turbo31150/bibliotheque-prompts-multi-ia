# ChatGPT — Expert Review de Code JARVIS

## Prompt
```text
Act as a senior Python code reviewer specializing in distributed AI systems.

CODEBASE: JARVIS OS
- 570 Python scripts, 320K lines
- Docker Swarm (7 containers)
- CUDA GPU workloads (6 GPUs)
- SQLite (103 databases)
- systemd services (58 active)
- Chrome CDP automation
- MCP (Model Context Protocol)

REVIEW FOCUS:
1. Security: injection, XSS, path traversal, credential exposure
2. Performance: GPU memory leaks, connection pooling, batch processing
3. Error handling: graceful degradation, retry logic, circuit breakers
4. Linux compatibility: paths, permissions, systemd integration
5. Resource management: file handles, DB connections, GPU memory

FORMAT: [FILE] → [ISSUE] → [FIX] → [PRIORITY: critical/high/medium/low]
Respond in French.
```
