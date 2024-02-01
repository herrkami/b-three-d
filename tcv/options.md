# Available options

## `viewer`

- `axes`: bool (default: False)<br>  Show X-, Y-, and Z-axes
- `axes0`: bool (default: False)<br>  Show axes at [0,0,0] or at object center (target)
- `grid`: [bool, bool, bool] (default: [False, False, False])<br>  Initial grid setting for all three axes
- `ortho`: bool (default: True)<br>  Use orthographic (true) or vanishing point perspective (False)
- `transparent`: bool (default: False)<br>  Show CAD objects transparently
- `black_edges`: bool (default: False)<br>  Show edges in black and instead of edgeColor
- `collapse`: int (default: 0)<br>  Tree collapse level (0 .. 3)
- `clip_intersection`: bool (default: False)<br>  Use intersection clipping
- `clip_plane_helpers`: bool (default: False)<br>  Show clipping planes
- `clip_normal`: [[int, int, int], [int, int, int], [int, int, int]] (default: [[-1, 0, 0], [0, -1, 0], [0, 0, -1]])<br>  Normal directions for clipping
- `clip_slider`: [int, int, int] (default: [-1, -1, -1])<br>  Clipping slider value (will be trimmed to slider's min/max limits)
- `control`: str (default: orbit)<br>  Viewpoint control ["orbit", "trackball"] (use "orbit" for mouse)
- `ticks`: int (default: 10)<br>  Number of grid ticks
- `position`: [float, float, float] (default: None)<br>  Camera position [x, y, z]
- `quaternion`: [float, float, float, float] (default: None)<br>  Camera rotation as 4-dim quaternion array [x, y, z, w]
- `zoom`: float (default: 1.0)<br>  Camera zoom factor
- `pan_speed`: float (default: 0.5)<br>  Pan speed
- `rotate_speed`: float (default: 1.0)<br>  Rotation speed
- `zoom_speed`: float (default: 0.5)<br>  Zoom speed
- `timeit`: bool (default: False)<br>  Show timings in browser console
- `zoom0`: float (default: 1.0)<br>  Initial zoom factor
- `tools`: bool (default: True)<br>  Show/hide all tools

## `display`

- `theme`: str (default: light)<br>  Theme ["light", "dark"]
- `cad_width`: int (default: 800)<br>  Width of the CAD canvas
- `tree_width`: int (default: 250)<br>  Width of the tree section
- `height`: int (default: 600)<br>  Height of the CAD canvas
- `pinning`: bool (default: False)<br>  Show/hide the pinning button
- `glass`: bool (default: False)<br>  Enable/disable glass mode (i.e. transparent tree)
- `tools`: bool (default: True)<br>  Show/hide CAD tools
- `keymap`: dict (default: {'shift': 'shiftKey', 'ctrl': 'ctrlKey', 'meta': 'metaKey'})<br>  Keymap configuration for the modifier keys

## `render`

- `ambient_intensity`: float (default: 0.5)<br>  Ambient light intensity
- `direct_intensity`: float (default: 0.3)<br>  Direct light intensity
- `metalness`: float (default: 0.7)<br>  Metalness of the CAD object
- `roughness`: float (default: 0.7)<br>  Roughness of the CAD object
- `default_opacity`: float (default: 0.4)<br>  Default opacity level in transparency mode
- `edge_color`: int (default: 7368816)<br>  Default edge color in hex format (might be displayed in decimal here: hex(7368816) = 0x707070)
- `normal_len`: float (default: 0)<br>  Show triangle normals when normalLen > 0
- `measure_tools`: bool (default: False)<br>  Show/hide measurement tools

