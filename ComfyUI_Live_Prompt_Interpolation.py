"""
@author: mgfxer
@title: FrameFX
@nickname: FrameFX 💫
@description: This extension provides various frame and mask sequence manipulation tools for animation workflows.
"""
import subprocess
from time import gmtime, strftime

# Live Prompt Interpolation
# A new node to execute python with text interpolation and character stability check.
# The resulting print() statement ends up as the output, if any.
# (c) 2024 Atom, ChatGPT, and mgfxer.

# Internal code to handle the interpolation and prompt logic
def internal_code():
    return """
def lerp(a: float, b: float, t: float) -> float:
    return (1 - t) * a + t * b

def generate_interpolated_prompt(prev_prompt: str, curr_prompt: str, t: float) -> str:
    if t == 0:
        return f"{prev_prompt}"
    elif t == 1:
        return f"{curr_prompt}"
    else:
        weighted_prev = f"({prev_prompt}:{1 - t:.2f})"
        weighted_curr = f"({curr_prompt}:{t:.2f})"
        return f"{weighted_prev} {weighted_curr}"

current_frame = PYTHON_CODE_BOX_SEED % (TOTAL_FRAMES + 1)

# Example previous and current prompts
previous_prompt = 'PREVIOUS_PROMPT'
current_prompt = 'CURRENT_PROMPT'

# Interpolation factor based on frame count
if current_frame > TOTAL_FRAMES:
    current_frame = TOTAL_FRAMES

t = current_frame / TOTAL_FRAMES

# Generate the interpolated prompt
interpolated_prompt = generate_interpolated_prompt(previous_prompt, current_prompt, t)

# Print the interpolated prompt
print(interpolated_prompt)
"""

class LivePromptInterpolation:
    RETURN_TYPES = ("STRING", "FLOAT", "FLOAT", "INT",)
    RETURN_NAMES = ("text", "current_strength", "previous_strength", "toggle_state",)
    
    FUNCTION = "node_update_with_text_v3"
    CATEGORY = "Scripting"
    
    def __init__(self):
        self.previous_prompt = ""
        self.current_prompt = ""
        self.current_frame = 0
        self.total_frames = 100
        self.update_cycle = 10
        self.char_stability_frames = 5
        self.stable_char_count_frame = 0
        self.last_char_count = 0
        self.toggle_state = 0  # Initialize the toggle state

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "new_prompt": ("STRING", {"default": "Enter your prompt here..."}),
                "seed": ("INT", {"default": 311, "step": 1, "display": "number"}),
                "total_frames": ("INT", {"default": 100, "step": 1, "display": "number"}),
                "update_cycle": ("INT", {"default": 10, "step": 1, "display": "number"}),
                "min_char_count": ("INT", {"default": 30, "step": 1, "display": "number"}),
                "char_stability_frames": ("INT", {"default": 5, "step": 1, "display": "number"})
            },
        }
   
    def node_update_with_text_v3(self, new_prompt, seed, total_frames, update_cycle, min_char_count, char_stability_frames):
        # Check if the new prompt is significant
        def is_significant_change(prev_prompt, new_prompt, min_char_count):
            char_count = len(new_prompt)
            return char_count >= min_char_count

        # Debug logging
        print(f"Current Frame: {self.current_frame}")
        print(f"Previous Prompt: {self.previous_prompt}")
        print(f"Current Prompt: {self.current_prompt}")
        print(f"New Prompt: {new_prompt}")
        print(f"Update Cycle: {update_cycle}")
        print(f"Character Stability Frames: {char_stability_frames}")

        self.update_cycle = update_cycle  # Update cycle dynamically
        self.char_stability_frames = char_stability_frames  # Update char stability frames dynamically

        # Check if character count has been stable
        if len(new_prompt) == self.last_char_count:
            self.stable_char_count_frame += 1
        else:
            self.stable_char_count_frame = 0
            self.last_char_count = len(new_prompt)

        # Check if it's time to update the prompt
        if (self.stable_char_count_frame >= self.char_stability_frames and 
            new_prompt != self.current_prompt and 
            is_significant_change(self.current_prompt, new_prompt, min_char_count)):
            
            self.previous_prompt = self.current_prompt
            self.current_prompt = new_prompt
            self.current_frame = 1  # Reset frame count for new interpolation
            self.stable_char_count_frame = 0  # Reset stability counter
            self.toggle_state = 1 - self.toggle_state  # Toggle the state between 0 and 1
            print("New prompt detected, resetting frames and toggling state.")
        elif self.current_frame < self.total_frames:
            self.current_frame += 1
            print("Update cycle not reached yet or prompt not stable long enough.")

        # Ensure current_frame doesn't exceed total_frames
        if self.current_frame > self.total_frames:
            self.current_frame = self.total_frames

        # Update total_frames dynamically
        self.total_frames = total_frames

        # Interpolation calculation
        t = self.current_frame / self.total_frames
        current_strength = t if self.toggle_state == 0 else 1 - t
        previous_strength = 1 - current_strength

        # Modify the code to include the previous and current prompts
        modified_code = internal_code().replace('PREVIOUS_PROMPT', self.previous_prompt).replace('CURRENT_PROMPT', self.current_prompt).replace('TOTAL_FRAMES', str(self.total_frames))
        code = f"import random; random.seed({seed}); PYTHON_CODE_BOX_SEED={self.current_frame}; {modified_code}"
        
        try:
            proc = subprocess.Popen(["python", "-c", code], stdout=subprocess.PIPE)
            code_result = proc.communicate(timeout=10)[0]  # Add timeout here
            # Fix up result.
            convert_result = code_result.decode().strip() 
        except subprocess.TimeoutExpired:
            proc.kill()
            print("Subprocess timed out and was killed.")
            convert_result = ""
        except Exception as e:
            print(f"Error during code execution: {e}")
            convert_result = ""

        t = strftime("%m-%d-%Y %H:%M:%S", gmtime())
        print(f"\033[36m[{t}] PCBv3--> {convert_result}\033[0m")

        return (convert_result, current_strength, previous_strength, self.toggle_state,)

    @classmethod
    def IS_CHANGED(cls, new_prompt, seed):
        return True
        
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {"LivePromptInterpolation": LivePromptInterpolation}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {"LivePromptInterpolation": "Live Prompt Interpolation"}
