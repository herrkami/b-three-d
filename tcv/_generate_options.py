import json
import re

options = {
    "viewer": {
        "axes": {
            "type": 'bool',
            "default": False,
            "description": 'Show X-, Y-, and Z-axes',
        },
        "axes0": {
            "type": 'bool',
            "default": False,
            "description": 'Show axes at [0,0,0] or at object center (target)',
        },
        "grid": {
            "type": '[bool, bool, bool]',
            "default": [False, False, False],
            "description": 'Initial grid setting for all three axes',
        },
        "ortho": {
            "type": 'bool',
            "default": True,
            "description": 'Use orthographic (true) or vanishing point perspective (False)',
        },
        "transparent": {
            "type": 'bool',
            "default": False,
            "description": 'Show CAD objects transparently',
        },
        "blackEdges": {
            "type": 'bool',
            "default": False,
            "description": 'Show edges in black and instead of edgeColor',
        },
        "collapse": {
            "type": 'int',
            "default": 0,
            "description": 'Tree collapse level (0 .. 3)',
        },

        "clipIntersection": {
            "type": 'bool',
            "default": False,
            "description": 'Use intersection clipping',
        },
        "clipPlaneHelpers": {
            "type": 'bool',
            "default": False,
            "description": 'Show clipping planes',
        },
        "clipNormal": {  # clipNormal<0,1,2>
            "type": '[[int, int, int], [int, int, int], [int, int, int]]',
            "default": [[-1, 0, 0], [0, -1, 0], [0, 0, -1]],
            "description": 'Normal directions for clipping',
        },
        "clipSlider": {  # clipSlider<0,1,2>
            "type": '[int, int, int]',
            "default": [-1, -1, -1],
            "description": "Clipping slider value (will be trimmed to slider's min/max limits)",
        },
        "control": {
            "type": 'str',
            "default": "orbit",
            "description": 'Viewpoint control ["orbit", "trackball"] (use "orbit" for mouse)',
        },
        # up
        "ticks": {
            "type": 'int',
            "default": 10,
            "description": 'Number of grid ticks',
        },

        "position": {
            "type": '[float, float, float]',
            "default": None,
            "description": 'Camera position [x, y, z]',
        },
        "quaternion": {
            "type": '[float, float, float, float]',
            "default": None,
            "description": 'Camera rotation as 4-dim quaternion array [x, y, z, w]',
        },
        # target

        "zoom": {
            "type": 'float',
            "default": 1.0,
            "description": 'Camera zoom factor',
        },

        "panSpeed": {
            "type": 'float',
            "default": 0.5,
            "description": 'Pan speed',
        },
        "rotateSpeed": {
            "type": 'float',
            "default": 1.0,
            "description": 'Rotation speed',
        },
        "zoomSpeed": {
            "type": 'float',
            "default": 0.5,
            "description": 'Zoom speed',
        },
        "timeit": {
            "type": 'bool',
            "default": False,
            "description": 'Show timings in browser console',
        },

        "zoom0": {
            "type": 'float',
            "default": 1.0,
            "description": 'Initial zoom factor',
        },
        "tools": {
            "type": 'bool',
            "default": True,
            "description": 'Show/hide all tools',
        },
    },
    
    "display": {
        "theme": {
            "type": 'str',
            "default": "light",
            "description": 'Theme ["light", "dark"]',
        },
        "cadWidth": {
            "type": 'int',
            "default": 800,
            "description": 'Width of the CAD canvas',
        },
        "treeWidth": {
            "type": 'int',
            "default": 250,
            "description": 'Width of the tree section',
        },
        "height": {
            "type": 'int',
            "default": 600,
            "description": 'Height of the CAD canvas',
        },
        "pinning": {
            "type": 'bool',
            "default": False,
            "description": 'Show/hide the pinning button',
        },
        "glass": {
            "type": 'bool',
            "default": False,
            "description": 'Enable/disable glass mode (i.e. transparent tree)',
        },
        "tools": {
            "type": 'bool',
            "default": True,
            "description": 'Show/hide CAD tools',
        },
        "keymap": {
            "type": 'dict',
            "default": { "shift": "shiftKey", "ctrl": "ctrlKey", "meta": "metaKey" },
            "description": 'Keymap configuration for the modifier keys',
        },
    },
    
    "render": {
        "ambientIntensity": {
            "type": 'float',
            "default": 0.5,
            "description": 'Ambient light intensity',
        },
        "directIntensity": {
            "type": 'float',
            "default": 0.3,
            "description": 'Direct light intensity',
        },
        "metalness": {
            "type": 'float',
            "default": 0.7,
            "description": 'Metalness of the CAD object',
        },
        "roughness": {
            "type": 'float',
            "default": 0.7,
            "description": 'Roughness of the CAD object',
        },
        "defaultOpacity": {
            "type": 'float',
            "default": 0.4,
            "description": 'Default opacity level in transparency mode',
        },
        "edgeColor": {
            "type": 'int',
            "default": 0x707070,
            "description": 'Default edge color in hex format (might be displayed in decimal here: hex(7368816) = 0x707070)',
        },
        "normalLen": {
            "type": 'float',
            "default": 0,
            "description": 'Show triangle normals when normalLen > 0',
        },
        "measureTools": {
            "type": 'bool',
            "default": False,
            "description": 'Show/hide measurement tools',
        },
    }
}

def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def snake_to_camel(name):
    camel = ''
    for i, word in enumerate(name.split('_')):
        if i == 0:
            camel += word.lower()
        else:
            camel += word.title()
    return camel

if __name__ == '__main__':
    for component in options.keys():
        for opt in options[component].keys():
            options[component][opt]['snake_cased'] = camel_to_snake(opt)
            try:
                camel = snake_to_camel(options[component][opt]['snake_cased'])
                assert(opt == camel)
                options[component][opt]['camel_cased'] = camel
            except:
                e = 'Option key {} changes when camel cased: {}'.format(opt, camel)
                raise AssertionError(e)
    
    with open('options.json', 'w') as f:
        json.dump(options, f, indent=2)

    with open('options.md', 'w') as f:
        content = '# Available options\n\n'
        for component in options.keys():
            content += f'## `{component}`\n\n'
            for opt in options[component].keys():
                content += f'- `{options[component][opt]["snake_cased"]}`: {options[component][opt]["type"]} (default: {options[component][opt]["default"]})<br>'
                content += f'  {options[component][opt]["description"]}\n'
            content += '\n'
                
        f.write(content)
    

