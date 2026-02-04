"""
Generate images for Aether Core — Sky Breather character.
This script uses the Leonardo API to generate images based on the specific
character brief for Aether Core with aerial poster, glide poses, and vent FX.
"""

import json
import os
from typing import Dict, Any, Optional

import requests


API_KEY = os.environ.get("LEONARDO_API_KEY", "cd8d7691-5ec5-48e1-9c6b-7160900f59a5")
"""
Your Leonardo Production API key. Keep this value secret. Set via the
LEONARDO_API_KEY environment variable. Falls back to a default key for
backwards compatibility.
"""

PHOENIX_MODEL_ID = "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3"
ANIME_XL_MODEL_ID = "e71a1c2f-4f80-4800-934f-2c68979d8cc8"

# Request timeout in seconds (connection timeout, read timeout)
REQUEST_TIMEOUT = (10, 30)

# Cached authorization headers to avoid repeated dict allocation
_HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

# Reusable session for connection pooling
_session: Optional[requests.Session] = None


def _get_session() -> requests.Session:
    """Returns a reusable requests session with connection pooling."""
    global _session
    if _session is None:
        _session = requests.Session()
    return _session


def generate_images_phoenix(prompt: str, width: int = 1216, height: int = 1520,
                             num_images: int = 4, contrast: float = 3.5,
                             style_uuid: str = "a5632c7c-ddbb-4e2f-ba34-8456ab3ac436",
                             alchemy: bool = True) -> Dict[str, Any]:
    """
    Generates images using the Phoenix 1.0 model with the specified prompt.

    :param prompt: The text prompt describing the image.
    :param width: Width of the image (512–1536, multiple of 8).
    :param height: Height of the image (512–1536, multiple of 8).
    :param num_images: Number of images to generate.
    :param contrast: Contrast parameter required for Phoenix (e.g. 1.0–4.5).
    :param style_uuid: Optional style UUID for stylistic control.
    :param alchemy: Whether to enable Alchemy (enables upscaling beyond input size).
    :return: The JSON response from the API with generation details.
    """
    payload = {
        "modelId": PHOENIX_MODEL_ID,
        "prompt": prompt,
        "width": width,
        "height": height,
        "num_images": num_images,
        "contrast": contrast,
        "alchemy": alchemy,
        "styleUUID": style_uuid,
    }
    session = _get_session()
    response = session.post(
        "https://cloud.leonardo.ai/api/rest/v1/generations",
        headers=_HEADERS,
        json=payload,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # Aether Core — Sky Breather character prompt
    # Task: Aerial poster + glide poses + vent FX
    # Context: Plume legibility; foreshortening
    # Style: Bengus-style; sky-blue & yellow; titanium base
    # Pose/Scene: Glide/dive; mist; no capes
    # Design: Air valves; membrane wings; ankle vanes
    # Output: Poster A/B, FX plumes
    # Avoid: Bloom, clutter, bad foreshortening
    
    prompt_aether_core = (
        "Ultra-detailed aerial poster, anime female adult 25-35, Bengus-style anatomy, "
        "glide dive pose with clean foreshortening, neon teal primary glow with yellow accent highlights, "
        "titanium metal base armor with charcoal graphite panels, crisp angular lines, "
        "air valves on torso, membrane wings extended, ankle vanes visible, "
        "vent FX plumes with high legibility, atmospheric mist background, "
        "no capes, no bloom, no clutter, sharp mechanical details, "
        "two-value cel shading, hard-edged rim light on shadow side, clean silhouette separation."
    )
    
    result = generate_images_phoenix(prompt_aether_core)
    print(json.dumps(result, indent=2))
