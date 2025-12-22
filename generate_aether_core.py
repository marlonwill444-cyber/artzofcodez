"""
AETHER CORE — Sky Breather Image Generator
This script generates images for the "Aether Core — Sky Breather" character using
the Leonardo API with the Phoenix 1.0 model. It implements specific prompt details
for aerial poster compositions with glide poses and vent FX.
"""

import json
from typing import Dict, Any

import requests


API_KEY = "cd8d7691-5ec5-48e1-9c6b-7160900f59a5"
"""
Your Leonardo Production API key. Keep this value secret. You can also set
this value via an environment variable (e.g., LEONARDO_API_KEY) and read
`os.environ["LEONARDO_API_KEY"]` instead of hard‑coding it here.
"""

PHOENIX_MODEL_ID = "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3"
ANIME_XL_MODEL_ID = "e71a1c2f-4f80-4800-934f-2c68979d8cc8"


def _make_headers() -> Dict[str, str]:
    """Builds the authorization headers for API requests."""
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }


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
    response = requests.post(
        "https://cloud.leonardo.ai/api/rest/v1/generations",
        headers=_make_headers(),
        data=json.dumps(payload),
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # AETHER CORE — Sky Breather character prompt
    # Task: Aerial poster + glide poses + vent FX
    # Context: Plume legibility; foreshortening
    # Style: Bengus-style; sky-blue & yellow; titanium base
    # Pose/Scene: Glide/dive; mist; no capes
    # Design: Air valves; membrane wings; ankle vanes
    # Output: Poster A/B, FX plumes
    # Avoid: Bloom, clutter, bad foreshortening
    
    prompt_aether_core = (
        "Ultra-detailed Bengus-style anime character adult 25-35, AETHER CORE Sky Breather, "
        "aerial poster composition, dynamic glide pose diving through mist, "
        "crisp angular anatomy with clean foreshortening, "
        "sky-blue and yellow color scheme with titanium base armor, "
        "air valves and vent systems with visible FX plumes, "
        "translucent membrane wings extending from back, ankle vanes for aerial control, "
        "sharp cel-shaded rendering with firm outer contours, "
        "legible vapor trails and atmospheric effects, "
        "no capes, no bloom, no clutter, no bad foreshortening, "
        "no text, no logos, no watermarks, "
        "heroic proportions, negative-space design, material separation via value contrast."
    )
    
    result = generate_images_phoenix(prompt_aether_core)
    print(json.dumps(result, indent=2))
