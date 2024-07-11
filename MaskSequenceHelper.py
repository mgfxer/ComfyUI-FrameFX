"""
@author: mgfxer
@title: FrameFX
@nickname: FrameFX 💫
@description: This extension provides various frame and mask sequence manipulation tools for animation workflows.
"""
import torch

class MaskSequenceHelper:
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
            }
        }

    # Define the return types for the function outputs
    RETURN_TYPES = ("IMAGE", "IMAGE", "STRING", "STRING", "INT")  # The function will return two image tensors, two strings, and an integer
    # Define the return names for the function outputs
    RETURN_NAMES = ("first_timeline", "second_timeline", "first_text_output", "second_text_output", "total_frames")
    # Name of the function to be executed
    FUNCTION = "generate_mask_definitions"
    # Category of the node
    CATEGORY = "advanced"

    def generate_mask_definitions(self, image_stream, num_images, hold_length, transition_length, padding_frames):
        # Initialize lists to hold the timelines and mask definitions
        first_timeline = []
        second_timeline = []
        first_text_output = ""
        second_text_output = ""

        # Calculate the total number of frames for each image and the total number of frames for the entire animation
        frame_distance = hold_length + transition_length
        total_frames = num_images * frame_distance + padding_frames

        # Get the actual number of images provided
        num_images_provided = image_stream.shape[0]

        # Generate the first timeline
        for i in range(num_images):
            index = i % num_images_provided
            repeated_images = image_stream[index:index+1].repeat(frame_distance, 1, 1, 1)
            first_timeline.append(repeated_images)

        # Concatenate the list of tensors into a single tensor
        first_timeline = torch.cat(first_timeline, dim=0)

        # Generate the second timeline
        for i in range(1, num_images):
            index = i % num_images_provided
            repeated_images = image_stream[index:index+1].repeat(frame_distance, 1, 1, 1)
            second_timeline.append(repeated_images)
        repeated_images = image_stream[0:1].repeat(frame_distance, 1, 1, 1)
        second_timeline.append(repeated_images)

        # Concatenate the list of tensors into a single tensor
        second_timeline = torch.cat(second_timeline, dim=0)

        # Initialize frame number and create mask text outputs
        frame = 0
        while frame < num_images * frame_distance:
            frame_end_hold = frame + hold_length - 1
            frame_start_transition = frame_end_hold + 1
            frame_end_transition = frame_start_transition + transition_length - 1

            first_text_output += f"{frame}:(1.0),\n"
            first_text_output += f"{frame_end_hold}:(1.0),\n"
            first_text_output += f"{frame_end_transition}:(0.0),\n"

            second_text_output += f"{frame}:(0.0),\n"
            second_text_output += f"{frame_end_hold}:(0.0),\n"
            second_text_output += f"{frame_end_transition}:(1.0),\n"

            frame = frame_end_transition + 1

        # Add padding frames if specified
        if padding_frames > 0:
            padding_start_frame = frame
            last_image_first_timeline = first_timeline[-1:]
            last_image_second_timeline = second_timeline[-1:]

            # Add padding frames to the timelines
            padding_images_first = last_image_first_timeline.repeat(padding_frames, 1, 1, 1)
            first_timeline = torch.cat((first_timeline, padding_images_first), dim=0)
            
            padding_images_second = last_image_second_timeline.repeat(padding_frames, 1, 1, 1)
            second_timeline = torch.cat((second_timeline, padding_images_second), dim=0)

            # Append padding frames to the text outputs
            for i in range(padding_frames):
                frame = padding_start_frame + i
                first_text_output += f"{frame}:(0.0),\n"
                second_text_output += f"{frame}:(1.0),\n"  # Set to 1.0 for the second timeline

        # Ensure the text output ends correctly
        first_text_output = first_text_output.strip().rstrip(',')
        second_text_output = second_text_output.strip().rstrip(',')

        # Return the generated timelines, text outputs, and total frames
        return first_timeline, second_timeline, first_text_output, second_text_output, total_frames

# Mapping the class to its name for the node system
NODE_CLASS_MAPPINGS = {
    "MaskSequenceHelper": MaskSequenceHelper  # Map the class name to the node system
}

# Display name mappings for the node system
NODE_DISPLAY_NAME_MAPPINGS = {
    "MaskSequenceHelper": "Mask Sequence Helper"  # Map the display name to the node system
}
