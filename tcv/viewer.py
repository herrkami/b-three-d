import json
import logging as log

class Option():
        def __init__(
            self,
            name,
            value,
            type_,
            desc,
            name_fe,
        ):
            self.name = name
            self.name_fe = name_fe
            self._value = value
            self.default_value = value
            self.type = type_
            self.description = desc
            
            self._changed = False
        
        def __str__(self):
            string = self.__repr__()
            string += '\n\n'
            string += '{}\n\n'.format(self.description)
            string += 'Frontend name: {}\n'.format(self.name_fe)
            string += 'Type: {}\n'.format(self.type)
            string += 'Value: {}\n'.format(self.value)
            string += 'Default value: {}'.format(self.default_value)
            return string
        
        def has_changed(self):
            return self._changed
        
        def _reset_changed(self):
            self._changed = False

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, new_value):
            self._value = new_value
            self._changed = True

def _populate_with_options(cl, options):
    
    for k, v in options.items():
        name = v['snake_cased']
        name_fe = v['camel_cased']
        value = v['default']
        if type(value) is str:
            value = f'"{value}"'
        type_ = v['type']
        desc = v['description']
        
        doc_string = f'{name} : {type_} (default: {value})\n    '
        doc_string += desc
        doc_string += '\n\n'
        cl.__doc__ += doc_string
        
        option = Option(name, value, type_, desc, name_fe)
        
        setattr(cl, name, option)

def _get_all_options(cl):
    options = []
    for a in dir(cl):
        opt = getattr(cl, a)
        if isinstance(opt, Option):
            options.append(opt)
    return options

def _get_changed_options(cl):
    options = []
    for a in dir(cl):
        opt = getattr(cl, a)
        if isinstance(opt, Option):
            if opt.has_changed():
                options.append(opt)
    return options

def _reset_changed(self):
    for a in dir(cl):
        opt = getattr(cl, a)
        if isinstance(opt, Option):
            opt._reset_changed()

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
        
    def get_config(self, select='all', format='backend'):
        
        def options_to_dict(options):
            dic = {}
            for opt in options:
                if format == 'backend':
                    key = opt.name
                elif format == 'frontend':
                    key = opt.name_fe
                else:
                    e = '{} is not a valid format.'.format(format)
                    raise KeyError(e)
                    
                val = opt.value
                dic[key] = val
            return dic

        if select == 'all':
            option_getter = _get_all_options
        elif select == 'changed':
            option_getter = _get_changed_options
        else:
            e = '{} is not a valid selector.'.format(select)
            raise KeyError(e)
        
        config = {}
        
        config['viewer'] = options_to_dict(
            option_getter(self))
        config['display'] = options_to_dict(
            option_getter(self.display))
        config['renderer'] = options_to_dict(
            option_getter(self.renderer))
            
        return config
            
if __name__ == '__main__':
    v = Viewer()
    
    
            
