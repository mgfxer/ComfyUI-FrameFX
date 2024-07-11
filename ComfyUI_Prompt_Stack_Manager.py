"""
@author: mgfxer
@title: FrameFX
@nickname: FrameFX 💫
@description: This extension provides various frame and mask sequence manipulation tools for animation workflows.
"""
class PromptStackManager:
    def __init__(self):
        self.prompts = []
        self.current_index = 0

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt_stack": ("STRING", {"multiline": True, "dynamicPrompts": False, "default": "Prompt 1\nPrompt 2\nPrompt 3"}),
                "frames_per_prompt": ("INT", {"default": 1, "min": 1, "max": 1000, "step": 1}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 1000000, "step": 1}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "INT")
    RETURN_NAMES = ("current_prompt", "previous_prompt", "current_frame")
    FUNCTION = "manage_prompts"
    CATEGORY = "Prompt Management"
    DESCRIPTION = """
    Manages a stack of prompts from a multiline text box and outputs the current and previous prompts.
    The node cycles through the prompts based on the frame count derived from the seed input.
    """

    def manage_prompts(self, prompt_stack, frames_per_prompt, seed):
        self.prompts = prompt_stack.strip().split("\n")
        num_prompts = len(self.prompts)

        if num_prompts == 0:
            return ("", "", 0)

        # Calculate the current frame based on the seed
        current_frame = seed % (frames_per_prompt * num_prompts)

        # Determine the current and previous prompt indices
        self.current_index = current_frame // frames_per_prompt
        previous_index = (self.current_index - 1) if self.current_index > 0 else (num_prompts - 1)

        current_prompt = self.prompts[self.current_index]
        previous_prompt = self.prompts[previous_index] if self.current_index > 0 else current_prompt

        return (current_prompt, previous_prompt, current_frame)

    @classmethod
    def IS_CHANGED(cls, prompt_stack, frames_per_prompt, seed):
        return True

NODE_CLASS_MAPPINGS = {"PromptStackManager": PromptStackManager}
NODE_DISPLAY_NAME_MAPPINGS = {"PromptStackManager": "Prompt Stack Manager"}
