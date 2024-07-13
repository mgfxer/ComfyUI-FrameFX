## Dynamic Animated Weights Helper

### Description
The Dynamic Animated Weights Helper is a versatile extension for animation workflows, providing various frame and mask sequence manipulation tools. This node facilitates the creation of complex animation effects with ease and flexibility.

### Features
- Supports multiple animation types including directional transitions, circle growth/shrink, fades, spins, and venetian blinds.
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
Below is an example of the output:
![Imgur Image](http://i.imgur.com/a/6FY96b2.gif)
