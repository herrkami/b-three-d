import json
import re

options = {
    "viewer": {
        "control": {
            "type": 'str',
            "default": "orbit",
            "description": 'Viewpoint control ["orbit", "trackball"] (use "orbit" for mouse)',
        },
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
        "clipNormal": {
            "type": '[[int, int, int], [int, int, int], [int, int, int]]',
            "default": [[-1, 0, 0], [0, -1, 0], [0, 0, -1]],
            "description": 'Normal directions for clipping',
        },
        "ticks": {
            "type": 'int',
            "default": 10,
            "description": 'Number of grid ticks',
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
        "panSpeed": {
            "type": 'float',
            "default": 0.5,
            "description": 'Pan speed',
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
        "zoom": {
            "type": 'float',
            "default": 1.0,
            "description": 'Camera zoom factor',
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
        "timeit": {
            "type": 'bool',
            "default": False,
            "description": 'Show timings in browser console',
        },
    },
    
    "display": {
        "cadWidth": {
            "type": 'int',
            "default": 800,
            "description": 'Width of the CAD canvas',
        },
        "height": {
            "type": 'int',
            "default": 600,
            "description": 'Height of the CAD canvas',
        },
        "treeWidth": {
            "type": 'int',
            "default": 250,
            "description": 'Width of the tree section',
        },
        "theme": {
            "type": 'str',
            "default": "light",
            "description": 'Theme ["light", "dark"]',
        },
    },
    
    "render": {
        "edgeColor": {
            "type": 'int',
            "default": 0x707070,
            "description": 'Default edge color in hex format',
        },
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
        "defaultOpacity": {
            "type": 'float',
            "default": 0.4,
            "description": 'Default opacity level in transparency mode',
        },
        "normalLen": {
            "type": 'float',
            "default": 0,
            "description": 'Show triangle normals when normalLen > 0',
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
    for group in options.keys():
        for opt in options[group].keys():
            options[group][opt]['snake_cased'] = camel_to_snake(opt)
            try:
                camel = snake_to_camel(options[group][opt]['snake_cased'])
                assert(opt == camel)
                options[group][opt]['camel_cased'] = camel
            except:
                e = 'Option key {} changes when camel cased: {}'.format(opt, camel)
                raise AssertionError(e)
    
    with open('options.json', 'w') as f:
        json.dump(options, f, indent=2)
    

