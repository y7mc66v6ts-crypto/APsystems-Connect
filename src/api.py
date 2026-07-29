"""Client functions for the APsystems OpenAPI."""

import requests

from auth import build_headers
from config import API_BASE_URL, SID


def get_system_details() -> dict:
    """Return the registered details for the configured APsystems system."""
    if not SID:
        raise RuntimeError("SID must be set in .env")

    request_path = f"/user/api/v2/systems/details/{SID}"
    response = requests.get(
        f"{API_BASE_URL}{request_path}",
        headers=build_headers("GET", request_path),
        timeout=20,
    )
    response.raise_for_status()
    return response.json()


def get_system_summary() -> dict:
    """Return today, month, year and lifetime energy for the system."""
    if not SID:
        raise RuntimeError("SID must be set in .env")

    request_path = f"/user/api/v2/systems/summary/{SID}"
    response = requests.get(
        f"{API_BASE_URL}{request_path}",
        headers=build_headers("GET", request_path),
        timeout=20,
    )
    response.raise_for_status()
    return response.json()
