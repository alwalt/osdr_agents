from mcp.server.fastmcp import FastMCP, Image
import httpx
import matplotlib.pyplot as plt
from io import StringIO
import os
import pandas as pd

mcp = FastMCP("OSDR_FETCH_SERVER")

import os
import json
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("osdr_data_fetch")

@mcp.tool(description="Fetch dataset metadata from the NASA OSDR API and save as JSON for downstream use.")
async def osdr_fetch_metadata(dataset_id: str) -> dict:
    """
    Fetch minimal metadata for a given dataset and save it to a local file.
    """
    url = f"https://visualization.osdr.nasa.gov/biodata/api/v2/dataset/{dataset_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()

    metadata = data.get(dataset_id, {}).get("metadata", {})

    cleaned = {
        "dataset_id": dataset_id,
        "title": metadata.get("study title", "N/A"),
        "organism": metadata.get("organism", "N/A"),
        "mission": ", ".join(metadata.get("mission", {}).get("name", [])) or "N/A",
        "protocols": metadata.get("study protocol name", []),
        "assay_type": metadata.get("study assay technology type", "N/A"),
        "platform": metadata.get("study assay technology platform", "N/A"),
        "funding": metadata.get("study funding agency", "N/A"),
    }

    # Save to JSON file
    filename = f"{dataset_id}_metadata.json"
    with open(filename, "w") as f:
        json.dump(cleaned, f, indent=2)

    cleaned["metadata_file"] = os.path.abspath(filename)
    return cleaned


if __name__ == "__main__":
    mcp.run(transport='stdio')
    
