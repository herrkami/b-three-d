import logging as log
import orjson

from ocp_tessellate.ocp_utils import (
    is_topods_shape,
    is_toploc_location,
    serialize,
    loc_to_tq,
)

from viewer import Viewer
from server import Server

class MessageType:
    DATA = 'D:'.encode('utf-8')
    CONFIG = 'C:'.encode('utf-8')
    # RESPONSE_FROM_BACKEND = 'B:'.encode('utf-8')
    # RESPONSE_FROM_FRONTEND = 'F:'.encode('utf-8')

def serializer(obj):
    """Default JSON serializer."""
    if is_topods_shape(obj):
        return base64.b64encode(serialize(obj)).decode("utf-8")
    elif is_toploc_location(obj):
        return loc_to_tq(obj)
    elif isinstance(obj, enum.Enum):
        return obj.value
    elif isinstance(obj, dict):
        return obj
    else:
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


class Controller():
    '''
    three-cad-viewer controller
        
    TCVController is a backend representation and interface of a
    three-cad-viewer (TCV) instance. It runs a server and is connected to the
    frontend TCV controller ('tcv_controller.js') via a websocket connection.
    
    - Starts per default after the first call of a rendering method (show(),
      etc.)
    - Can be disabled (rendering methods then return TCV objects)
    - Runs a websocket server which
        - serves the entire frontend and communicates with the TCV controller
          (frontend)
        → exchange commands, data, config, etc. 
    - Offers an API to users and the b-three-d controller that allows 
        - controlling and exchanging data and config with TCV
        - provides a callback interface for async messages from TCV
    '''
    
    def __init__(
        self,
        host='localhost',
        port=9678,
    ):
        
        self.host = host
        self.port = port
        
        self.server = Server(
            host=self.host, 
            port=self.port, 
            callback=self._on_recv
        )

        self.viewer = Viewer()
        
    def start_server(self):
        if not self.server.is_running:
            self.server.start()
            
    def _send(self, data, message_type):
        if not self.server.is_running:
            self.start_server()
        msg = message_type + orjson.dumps(data, default=serializer)
        msg = msg.decode()
        log.info(f'Sending message:\n{msg}')
        self.server.send_data_to_all_clients(msg)
        
    def _on_recv(self, msg):
        log.info(f'Received message:\n[{msg}]')
        
    def send_config(self, select='changed'):
        config = self.viewer.get_config(select=select, format='backend')
        self._send(config, MessageType.CONFIG)
    

if __name__ == '__main__':
    import time
    import numpy as np
    log.basicConfig(level=log.INFO)
    
    tcv = Controller(host='localhost', port=9678)
    tcv.start_server()
    
    while True:
        tcv.viewer.display.cad_width.value = np.random.randint(0, 1000)
        tcv.send_config('changed')
        time.sleep(2)
    