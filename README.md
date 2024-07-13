## Dynamic Animated Weights
<img src="https://github.com/user-attachments/assets/2c571c21-5666-4d44-a71c-ca5bca106d03" style="max-width: 100%; height: auto;">
<img src="https://github.com/user-attachments/assets/68f96e4a-cd8f-4735-92f1-f75a1a5994a0" style="max-width: 100%; height: auto;">

Outputs operate on the principle Hold Frames + Transition Length + End Padding Frames. These values specify the length of the animation to be created.
Many of my nodes use these concepts and work in lockstep.

### Description
The Dynamic Animated Weights Helper is a versatile extension for animation workflows, providing various frame and mask sequence manipulation tools. This node facilitates the creation of complex animation effects with ease and flexibility.

## 12 Transition Slots
The user can choose up to 12 separate transition animations, and these are used as a list order. If only 4 transitions are needed the first 4 will be used, if more than 12 are needed, the list of transitions will repeat in a loop in the order listed. 

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
<img src="https://github.com/user-attachments/assets/ddb14de4-0539-4b81-a2f2-dcd270a543b0" style="width: 350px; height: auto;">

The Mask Sequence Helper node provides an efficient way to generate mask sequence codes across two opposing timelines to form a slideshow effect that loops. The node also outputs your images to match the hold, transition and padding counts set. These two timelines are then either masked by the codes, or by animated weights output. This node makes it easy to manage frame transitions in animation workflows. Its customizable parameters allow for precise control over the timing and sequence of frames, making it a valuable tool for animation projects.

# Prompt Travel Helper
<img src="https://github.com/user-attachments/assets/2562572c-a3a5-41f2-b602-756fe3702587" style="width: 350px; height: auto;">

<img src="https://github.com/user-attachments/assets/4cf5521a-e463-447f-9c13-01104f5a425d" style="max-width: 100%; height: auto;">

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
<img src="https://github.com/user-attachments/assets/122f8ea2-bf95-46c8-b6e3-f59fa7f1ed75" style="width: 350px; height: auto;">

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
<img src="https://github.com/user-attachments/assets/2509b268-a811-49b4-a00f-9e41bcfe93d1" style="width: 350px; height: auto;">

## Description
The EdgeFX Source Images node extends the functionality of the Mask Sequence Helper by adding push and retract features. This node allows for more dynamic control over the timing of the Edge FX animation sequence, enabling users to adjust the timeline by either pushing it forward in time or pulling it back in time, allowing you to resync the effect across the transition timeline. This is primarily useful for the 'lower ram' ipadapter option within the worflow, it's aimed at helping users with lower ram cards, who can barely run EFX. Otherwise the 2 Ipadapter solution should be used, and these push retract features are usually never needed.

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

## Dream Zoom Workflow 
(excerpt image only) The workflow file is in the workflows folder.
<img src="https://github.com/user-attachments/assets/b4564dff-febb-46e0-bd03-574f373e3fa7" style="max-width: 100%; height: auto;">

<img src="https://github.com/user-attachments/assets/a069efe1-dbfc-41a9-b448-91edd46c8c64" style="width: 650px; height: auto;">

## Prompt Stack Manager
The Prompt Stack Manager node is designed for the Dream Zoom Workflow with auto-queue functionality in ComfyUI. It manages a stack of prompts provided in a multiline text box and cycles through them based on the frame count derived from a seed input. This node outputs the current and previous prompts, facilitating live prompt interpolation and seamless transitions between different prompts during animation workflows.
This node was designed to work as a sister node for the following node:
## Attack Hold Weighted Prompt, 
Atomic Perception created as a collaboration effort for the Dream-zoom workflow on discord. Props to atom.p for inspiring me to get started on custom node creation. His effort on this node led to creating my own nodes.

<img src="https://github.com/user-attachments/assets/9560da78-2b22-4b2d-a5e9-7a613686ed57" style="width: 350px; height: auto;">

That node can be found here:
https://github.com/AtomicPerception/ap_Nodes/tree/main

## Live Prompt Interpolation
The Live Prompt Interpolation node is also part of the Dream Zoom Workflow with auto-queue functionality in ComfyUI. It enables live interpolation of prompts on the fly, allowing for dynamic and smooth transitions between prompts. This node takes a single prompt and interpolates from the previously typed prompt over a specified number of frames, It has nice trigger functions that make sure the prompt is only registered after a specified number of frames and characters difference, ensuring that prompt changes are handled in real-time, yet not too soon, providing a fluid animation experience.

All of my nodes were created with AI assistance from Chat GPT and Claude.
