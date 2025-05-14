# 🧠 OSDR Parallel Workflow (MCP)

This repository demonstrates a parallel agent-based workflow using the [Model Context Protocol (MCP)](https://modelcontext.org/) to analyze NASA OSDR (Open Science Data Repository) biological datasets.

Specifically, it uses a fan-out/fan-in agent design to:
- 🛰 Fetch metadata for a given study
- 🧬 Analyze unnormalized RNA-seq counts and generate a top-10 gene plot
- 📄 Generate a clean, human-readable summary report

The agents are orchestrated in parallel using a `ParallelLLM` workflow and run on top of a local MCP runtime.

---

### `first_example/`
A simple agent that uses two official MCP servers:
- `mcp-server-fetch` (headless browser)
- `mcp-server-filesystem`

### `osdr_mcp/`
Custom MCP server exposing tools for interacting with OSDR data:
- `osdr_fetch_metadata`: Fetches metadata for a given OSDR dataset
- `osdr_find_by_organism`: Filters studies by organism
- Additional tools (e.g. RNA analysis) live in `osdr_viz_tools`

### `parallel_example/`
The parallel agent configuration is defined in `main.py` and demonstrates a fan-out/fan-in model using three distinct agents:
- **metadata_agent**: Fetches dataset metadata via the `osdr_data_fetch` server.
- **quant_analysis_agent**: Analyzes unnormalized RNA-seq count data using `osdr_viz_tools`.
- **summary_writer_agent**: Merges both outputs and writes a Markdown summary to disk.


Uses custom MCP servers:  
- `osdr_data_fetch`  
- `osdr_viz_tools`

## ⚙️ Configuration

The `cp_agent.config.yaml` file controls:
- LLM backend (e.g. Ollama, OpenAI)
- MCP server connections
- Tool availability
- System prompts / metadata

## 🚀 Getting Started

1. Clone this repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run an example:
   ```bash
   python first_example/main.py
   ```

Or launch the MCP server directly:
```bash
python osdr_mcp/main_simple.py
```

## 🧩 Integration Notes

This architecture is built for flexibility. You can toggle between document Q&A, RAG search, or custom analysis tools. A mode switch or UI toggle is ideal for user-facing integration. Support for Milvus-based RAG via MCP is on the roadmap.

## 📚 Resources

- [Model Context Protocol](https://modelcontext.org/)
- [NASA OSDR API](https://visualization.osdr.nasa.gov/biodata/api/v2/dataset/)
