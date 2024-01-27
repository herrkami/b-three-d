import json
import logging as log

class Option():
        def __init__(
            self,
            name,
            value,
            type_,
            desc,
        ):
            self.name = name
            self._value = value
            self.default_value = value
            self.type = type_
            self.description = desc
            
            self._changed = False
            
        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, new_value):
            self._value = new_value
            self._changed = True
        
        def __str__(self):
            return 'Option'

def _populate_with_options(cl, options):
    
    for k, v in options.items():
        name = v['snake_cased']
        value = v['default']
        if type(value) is str:
            value = f'"{value}"'
        type_ = v['type']
        desc = v['description']
        
        doc_string = f'{name} : {type_} (default: {value})\n    '
        doc_string += desc
        doc_string += '\n\n'
        cl.__doc__ += doc_string
        
        option = Option(name, value, type_, desc)
        
        setattr(cl, name, option)

def _get_all_options(cl):
    options = []
    for a in dir(cl):
        opt = getattr(cl, a)
        if isinstance(opt, Option):
            options.append(opt)
    return options

class Display():
    def __init__(self):
        self.__doc__ = 'Backend representation of three-cad-viewer\'s display configuration\n\n'
        # Create attributes from options
        self.__doc__ += 'Attributes\n----------\n'
        
        with open('./options.json', 'r') as f:
            options = json.loads(f.read())
        _populate_with_options(self, options['display'])
        
        self._changed = []
        
        

class Renderer():
    def __init__(self):
        self.__doc__ = 'Backend representation of three-cad-viewer\'s render configuration \n\n'
        # Create attributes from options
        self.__doc__ += 'Attributes\n----------\n'
        
        with open('./options.json', 'r') as f:
            options = json.loads(f.read())
        _populate_with_options(self, options['render'])

        self._changed = []

class Viewer():
    def __init__(self):
        self.__doc__ = 'Backend representation of three-cad-viewer\'s viewer configuration\n\n'
        self.__doc__ += 'display : Display\nRepresentation of three-cad-viewer\'s display configuration\n\n'
        self.__doc__ += 'renderer : Renderer\nRepresentation of three-cad-viewer\'s render configuration\n\n'
        # Create attributes from options
        self.__doc__ += 'Attributes\n----------\n'

        self._changed = []
        
        self.display = Display()
        
        self.renderer = Renderer()
        
        with open('./options.json', 'r') as f:
            options = json.loads(f.read())
        _populate_with_options(self, options['viewer'])
        
    def get_config(self, select='all', format='snake_case'):
        options_viewer = _get_all_options(self)
        
        config = {}
        if select == 'all':
            config['viewer'] = {}
            for opt in options_viewer:
                key = opt.name
                val = opt.value
                config['viewer']['key'] = val
            
            options_display = _get_all_options(self.display)
            config['display'] = {}
            
            options_renderer = _get_all_options(self.renderer)
            config['renderer'] = {}
            
if __name__ == '__main__':
    v = Viewer()
    
            
