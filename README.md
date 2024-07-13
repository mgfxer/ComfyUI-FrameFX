## Dynamic Animated Weights

Outputs operate on the princple Hold Frames + Transition Length + End Padding Frames. These values specify the length of the animation to be created.
** (many of my nodes use these concepts and work in lockstep)**

### Description
The Dynamic Animated Weights Helper is a versatile extension for animation workflows, providing various frame and mask sequence manipulation tools. This node facilitates the creation of complex animation effects with ease and flexibility.

### Features
- Supports multiple animation types including directional and diagonal transitions, circle growth/shrink, fades, square spins, and venetian blinds.
- Includes options for easing, blur effects, and frame transitions.
- Allows for generation modes like QR, Edge-FX, and combined outputs.
- Random animation type selection with options to exclude specific types.
- Customizable parameters for frame dimensions, transition and hold frames, padding, Gaussian blur, edge effects, and more.

### Input Parameters
- `animation_type_1` to `animation_type_12`: Select the animation type for each sequence.
- `transition_easing` and `blur_easing`: Choose the easing function for transitions and blurs.
- `frame_width` and `frame_height`: Set the dimensions for each frame.
- `hold_frames`, `transition_frames`, `padding_frames`, and `input_frames`: Configure the number of frames for holding, transitioning, padding, and input sequences.
- `gaussian_blur_amount`: Adjust the amount of Gaussian blur applied.
- `edge_fx_thickness`, `push_fx`, `retract_fx`: Parameters for edge effects.
- `fx_cull_white_frames`: Set the threshold for culling white frames in edge effects.
- `qr_greyness`: Adjust the greyness for QR generation mode.
- `random_seed`: Seed for randomization.
- `edgeFade_contrast` and `edgeFade_blur`: Parameters for edge fade effects.
- `generation_mode`: Select the generation mode (Only Transitions, Generate QR, Generate Edge-FX, Generate All).
- `edge_fx_fade_balance`: Balance for edge fade effects.
- `venetian_bars`: Number of bars for Venetian blinds animation.

### Usage
This node is designed to be integrated into animation workflows within the ComfyUI environment. The node can generate animations based on various types and apply a range of effects such as transitions, blurs, and edge enhancements.

## Mask Sequence Helper
The Mask Sequence Helper node provides an efficient way to generate mask sequence codes across two opposing timelines to form a slideshow effect that loops. The node also outputs your images to match the hold, transition and padding counts set. These two timelines are then either masked by the codes, or by animated weights output. This node makes it easy to manage frame transitions in animation workflows. Its customizable parameters allow for precise control over the timing and sequence of frames, making it a valuable tool for animation projects.

# Prompt Travel Helper

## Description
The Prompt Travel Helper node assists in transforming a stream of BLIP (Bootstrapped Language-Image Pre-training) captions into a prompt travel format. This node operates on the principles of hold, transition, and padding lengths to create a structured sequence of prompts for animation workflows.

## Features
- **Stream of BLIP Captions:** Converts a bulk input of BLIP captions into a formatted sequence.
- **Customizable Hold and Transition Lengths:** Define the number of frames for holding and transitioning between prompts.
- **End Padding Frames:** Add padding frames to ensure smooth transitions at the end of the sequence.
- **Formatted Output:** Generates a structured prompt sequence suitable for prompt-travel animation workflows.

## Input Parameters
- `bulk_text_input`: A multiline string input for the bulk text of BLIP captions.
- `hold_length`: Integer input for the number of frames to hold each caption (default: 5).
- `transition_length`: Integer input for the number of frames to transition between captions (default: 5).
- `end_padding_frames`: Integer input for the number of padding frames at the end of the sequence (default: 10).

## Return Values
- `formatted_prompts`: A single string containing the formatted sequence of prompts.

## Usage
This node is designed to be integrated into animation workflows within the ComfyUI environment. It processes a stream of BLIP captions and generates a formatted sequence of prompts based on the specified hold, transition, and padding lengths.

# Florence Prompt Travel Helper

## Description
The Florence Prompt Travel Helper node assists in transforming a stream of Florence captions into a prompt travel format. This node operates on the principles of hold, transition, and padding lengths to create a structured sequence of prompts for animation workflows, similar to the BLIP Travel Helper but specifically designed for Florence captions.

## Features
- **Stream of Florence Captions:** Converts a bulk input of Florence captions into a formatted sequence.
- **Customizable Hold and Transition Lengths:** Define the number of frames for holding and transitioning between prompts.
- **End Padding Frames:** Add padding frames to ensure smooth transitions at the end of the sequence.
- **Formatted Output:** Generates a structured prompt sequence suitable for animation workflows.

## Input Parameters
- `bulk_text_input`: A multiline string input for the bulk text of Florence captions.
- `hold_length`: Integer input for the number of frames to hold each caption (default: 5).
- `transition_length`: Integer input for the number of frames to transition between captions (default: 5).
- `end_padding_frames`: Integer input for the number of padding frames at the end of the sequence (default: 10).

## Return Values
- `formatted_prompts`: A single string containing the formatted sequence of prompts.


# EdgeFX Source Images

## Description
The EdgeFX Source Images node extends the functionality of the Mask Sequence Helper by adding push and retract features. This node allows for more dynamic control over the animation sequence, enabling users to adjust the hold lengths for specific frames to create smoother transitions and effects.

## Features
- **Generate Edge FX Image Sequences:** Create detailed mask sequences with customizable hold and transition lengths.
- **Timeline Generation:** Produce two separate timelines of repeated images, useful for comparison or alternating effects.
- **Padding Frames:** Add padding frames to ensure smooth transitions.
- **Push and Retract Features:** Adjust the hold length for the first cycle of images to create dynamic effects:
  - **Push:** Increase the hold length for the first frame, useful for extending the visibility of the initial image.
  - **Retract:** Decrease the hold length for the first frame, useful for shortening the visibility of the initial image.

## Input Parameters
- `image_stream`: The stream of images to be processed.
- `num_images`: Number of images in the sequence.
- `hold_length`: Number of frames to hold each image.
- `transition_length`: Number of frames for the transition between images.
- `padding_frames`: Number of padding frames to add at the end.
- `push`: Increase the hold length for the first frame.
- `retract`: Decrease the hold length for the first frame.

## Return Values
- `first_timeline`: The first sequence of images with transitions and holds.
- `second_timeline`: The second sequence of images, offset by one image from the first.
- `first_text_output`: Text output for the first mask sequence.
- `second_text_output`: Text output for the second mask sequence.
- `total_frames`: Total number of frames generated, including padding.
## Prompt Stack Manager
The Prompt Stack Manager node is designed for the Dream Zoom Workflow with auto-queue functionality in ComfyUI. It manages a stack of prompts provided in a multiline text box and cycles through them based on the frame count derived from a seed input. This node outputs the current and previous prompts, facilitating live prompt interpolation and seamless transitions between different prompts during animation workflows.

## Live Prompt Interpolation
The Live Prompt Interpolation node is also part of the Dream Zoom Workflow with auto-queue functionality in ComfyUI. It enables live interpolation of prompts on the fly, allowing for dynamic and smooth transitions between prompts. This node takes a single prompt and interpolates it over a specified number of frames, ensuring that prompt changes are handled in real-time, providing a fluid animation experience.
