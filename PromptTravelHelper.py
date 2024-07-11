# Prompt Travel Helper
# Version: 2.2

import re
from collections import defaultdict

class promptTravelHelper:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "bulk_text_input": ("STRING", {
                    "multiline": True,
                    "default": "",
                }),
                "hold_length": ("INT", {
                    "default": 5,
                    "min": 0
                }),
                "transition_length": ("INT", {
                    "default": 5,
                    "min": 0
                }),
                "end_padding_frames": ("INT", {
                    "default": 10,
                    "min": 0
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("formatted_prompts",)
    FUNCTION = "process_bulk_text"
    CATEGORY = "advanced"

    def process_bulk_text(self, bulk_text_input="", hold_length=5, transition_length=5, end_padding_frames=10):
        if not bulk_text_input.strip():
            return ("", )

        # Split the bulk input into individual prompts
        prompts = [prompt.strip() for prompt in bulk_text_input.strip().split('\n') if prompt.strip()]

        frames = []
        current_frame = 0

        # Create frames based on hold and transition lengths
        for prompt in prompts:
            prompt = prompt.replace('"', '\\"')  # Escape quotes
            frames.append((current_frame, prompt))
            current_frame += hold_length
            frames.append((current_frame, prompt))
            current_frame += transition_length

        # Add the first prompt again at the end to create a loop
        if prompts:
            first_prompt = prompts[0].replace('"', '\\"')
            frames.append((current_frame, first_prompt))
            current_frame += end_padding_frames

            # Add the final piece of the travel schedule
            frames.append((current_frame, first_prompt))

        frame_dict = defaultdict(tuple)

        for frame, text in frames:
            frame_dict[frame] += (text,)

        formatted_prompts = []
        for frame in sorted(frame_dict.keys()):
            formatted_prompts.append(f'"{frame}": "{", ".join(frame_dict[frame])}"')

        return (',\n'.join(formatted_prompts), )

NODE_CLASS_MAPPINGS = {
    "PromptTravelHelper": promptTravelHelper
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptTravelHelper": "Prompt Travel Helper"
}
