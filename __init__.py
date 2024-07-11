# init.py
from .ComfyUI_Live_Prompt_Interpolation import LivePromptInterpolation
from .ComfyUI_Prompt_Stack_Manager import PromptStackManager
from .DynamicAnimatedWeights import DynamicAnimatedWeightsHelper
from .FlorenceTravelHelper import FlorencePromptTravelHelper
from .MaskSequenceHelper import MaskSequenceHelper
from .PromptTravelHelper import promptTravelHelper
# Add any other necessary imports or initialization code here
# Mapping the class to its name for the node system
NODE_CLASS_MAPPINGS = {
    "LivePromptInterpolation": LivePromptInterpolation,
    "PromptStackManager": PromptStackManager,
    "DynamicAnimatedWeightsHelper": DynamicAnimatedWeightsHelper,
    "FlorencePromptTravelHelper": FlorencePromptTravelHelper,
    "MaskSequenceHelper": MaskSequenceHelper,
    "PromptTravelHelper": promptTravelHelper
}
# Display name mappings for the node system
NODE_DISPLAY_NAME_MAPPINGS = {
    "LivePromptInterpolation": "Live Prompt Interpolation",
    "PromptStackManager": "Prompt Stack Manager",
    "DynamicAnimatedWeightsHelper": "Dynamic Animated Weights",
    "FlorencePromptTravelHelper": "Florence Prompt Travel Helper",
    "MaskSequenceHelper": "Mask Sequence Helper",
    "PromptTravelHelper": "Prompt Travel Helper"
}