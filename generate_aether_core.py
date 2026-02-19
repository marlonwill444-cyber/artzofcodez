"""
Generate images for Aether Core — Sky Breather character.
This script uses the Leonardo API to generate images based on the specific
character brief for Aether Core with aerial poster, glide poses, and vent FX.
"""

import json

from mdigitalartz_leonardo import generate_images_phoenix


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
