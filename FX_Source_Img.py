"""
@author: mgfxer
@title: FrameFX
@nickname: FrameFX 💫
@description: This extension provides various frame and mask sequence manipulation tools for animation workflows.
"""
import torch

class EdgeFXSourceImages:
    def __init__(self):
        pass  # This constructor does nothing but is required for class instantiation

    @classmethod
    def INPUT_TYPES(cls):
        # Define the input types for the node
        return {
            "required": {
                "image_stream": ("IMAGE",),  # Single image input for the stream of images
                "num_images": ("INT", {"default": 4, "min": 1}),  # Integer input for the number of images
                "hold_length": ("INT", {"default": 5, "min": 1}),  # Integer input for hold length with default 5 and minimum 1
                "transition_length": ("INT", {"default": 20, "min": 1}),  # Integer input for transition length with default 20 and minimum 1
                "padding_frames": ("INT", {"default": 0, "min": 0}),  # Integer input for padding frames with default 0 and minimum 0
                "push": ("INT", {"default": 0, "min": 0}),
                "retract": ("INT", {"default": 0, "min": 0}),
            }
        }

    # Define the return types for the function outputs
    RETURN_TYPES = ("IMAGE", "IMAGE", "STRING", "STRING", "INT")  # The function will return two image tensors, two strings, and an integer
    # Define the return names for the function outputs
    RETURN_NAMES = ("first_timeline", "second_timeline", "first_text_output", "second_text_output", "total_frames")
    # Name of the function to be executed
    FUNCTION = "generate_mask_definitions_v2"
    # Category of the node
    CATEGORY = "advanced"

    def generate_mask_definitions_v2(self, image_stream, num_images, hold_length, transition_length, padding_frames, push, retract):
        # Initialize lists to hold the timelines and mask definitions
        primary_timeline = []
        secondary_timeline = []
        primary_text_output = ""
        secondary_text_output = ""

        # Calculate the total number of frames for each image and the total number of frames for the entire animation
        frame_interval = hold_length + transition_length
        total_frame_count = num_images * frame_interval + padding_frames

        # Get the actual number of images provided
        provided_image_count = image_stream.shape[0]

        # Adjust hold value for the first cycle
        adjusted_initial_hold = hold_length - retract + push

        # Generate the primary timeline with adjusted initial hold value
        for i in range(num_images):
            index = i % provided_image_count
            current_hold_duration = adjusted_initial_hold if i == 0 else hold_length
            frame_interval = current_hold_duration + transition_length
            repeated_images = image_stream[index:index+1].repeat(frame_interval, 1, 1, 1)
            primary_timeline.append(repeated_images)

        # Concatenate the list of tensors into a single tensor
        primary_timeline = torch.cat(primary_timeline, dim=0)

        # Adjust padding length
        adjusted_padding_duration = padding_frames + retract - push

        # Generate the secondary timeline
        for i in range(1, num_images):
            index = i % provided_image_count
            repeated_images = image_stream[index:index+1].repeat(frame_interval, 1, 1, 1)
            secondary_timeline.append(repeated_images)
        repeated_images = image_stream[0:1].repeat(frame_interval, 1, 1, 1)
        secondary_timeline.append(repeated_images)

        # Concatenate the list of tensors into a single tensor
        secondary_timeline = torch.cat(secondary_timeline, dim=0)

        # Initialize frame number and create mask text outputs
        frame_counter = 0
        while frame_counter < num_images * frame_interval:
            hold_end_frame = frame_counter + hold_length - 1
            transition_start_frame = hold_end_frame + 1
            transition_end_frame = transition_start_frame + transition_length - 1

            primary_text_output += f"{frame_counter}:(1.0),\n"
            primary_text_output += f"{hold_end_frame}:(1.0),\n"
            primary_text_output += f"{transition_end_frame}:(0.0),\n"

            secondary_text_output += f"{frame_counter}:(0.0),\n"
            secondary_text_output += f"{hold_end_frame}:(0.0),\n"
            secondary_text_output += f"{transition_end_frame}:(1.0),\n"

            frame_counter = transition_end_frame + 1

        # Add padding frames if specified
        if adjusted_padding_duration > 0:
            padding_start_frame = frame_counter
            last_image_primary_timeline = primary_timeline[-1:]
            last_image_secondary_timeline = secondary_timeline[-1:]

            # Add padding frames to the timelines
            padding_images_primary = last_image_primary_timeline.repeat(adjusted_padding_duration, 1, 1, 1)
            primary_timeline = torch.cat((primary_timeline, padding_images_primary), dim=0)
            
            padding_images_secondary = last_image_secondary_timeline.repeat(adjusted_padding_duration, 1, 1, 1)
            secondary_timeline = torch.cat((secondary_timeline, padding_images_secondary), dim=0)

            # Append padding frames to the text outputs
            for i in range(adjusted_padding_duration):
                frame_counter = padding_start_frame + i
                primary_text_output += f"{frame_counter}:(0.0),\n"
                secondary_text_output += f"{frame_counter}:(1.0),\n"  # Set to 1.0 for the secondary timeline

        # Ensure the text output ends correctly
        primary_text_output = primary_text_output.strip().rstrip(',')
        secondary_text_output = secondary_text_output.strip().rstrip(',')

        # Return the generated timelines, text outputs, and total frames
        return primary_timeline, secondary_timeline, primary_text_output, secondary_text_output, total_frame_count

# Mapping the class to its name for the node system
NODE_CLASS_MAPPINGS = {
    "EdgeFXSourceImages": EdgeFXSourceImages  # Map the class name to the node system
}

# Display name mappings for the node system
NODE_DISPLAY_NAME_MAPPINGS = {
    "EdgeFXSourceImages": "EdgeFX Source Images"  # Map the display name to the node system
}
