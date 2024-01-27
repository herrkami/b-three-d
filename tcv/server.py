import asyncio
import websockets
import threading
import logging as log
from typing import Callable

class Server():
    def __init__(
        self,
        host: str='localhost',
        port: int=9678,
        callback: Callable=None,
    ):
        self.host = host
        self.port = port
        
        self.clients = []
        self._server = None
        self.is_running = False
        
        if callback == None:
            self._callback = lambda msg: print(
                f'Callback not yet set. Received message:\n[{msg}]'
            )
        else:
            self._callback = callback
        
    async def _client_handler(self, client, path):
        # Register new client
        log.info(f'WebSocket client connected: {client}')
        self.clients.append(client)
        
        while True:
            try:
                msg = await client.recv()
                self._callback(msg)
            except Exception as e:
                clients.remove(client)
                log.info(f'WebSocket client disconnected: {client}')
                break
            
    def set_callback_function(func):
        self._callback = func

    def start(self):
        try:
            _loop = asyncio.new_event_loop()
            asyncio.set_event_loop(_loop)

            self._server = websockets.serve(
                self._client_handler, 
                self.host, 
                self.port
            )

            asyncio.get_event_loop().run_until_complete(self._server)
            threading.Thread(target=asyncio.get_event_loop().run_forever).start()
            log.info(f'WebSocket server started. Listening on {self.host}:{self.port}')
            self.is_running = True
        except Exception as e:
            raise e

    def get_clients(self):
        return self.clients.copy()

    def send_data_to_client(self, client, data):
        try:
            asyncio.run(client.send(data))
        except Exception as e:
            # Clients might have disconnected during the messaging process,
            # just ignore that, they will have been removed already.
            log.info(f'Ignoring exception {e}')
            pass
        
    def send_data_to_all_clients(self, data):
        for client in self.clients.copy():
            self.send_data_to_client(client, data)
        
    def ping_client(self, client):
        try:
            # asyncio.run(self._ping_client(client))
            asyncio.run(client.ping())
            log.info(f'PING {client}\nLatency: {client.latency * 1e3} ms')
        except Exception as e:
            log.info(f'Caught exception {e}, removing client...')
            self.clients.remove(client)
            log.info(f'WebSocket client disconnected: {client}')


if __name__ == "__main__":
    log.basicConfig(level=log.INFO)
    
    import time
    server = Server()
    server.start()

    try:
        if get_ipython().__class__.__name__ == 'TerminalInteractiveShell':
            pass
    except:
        # Enter infinite loop if not called from in interactive shell
        while True:
            clients = server.get_clients()
            for c in clients:
                server.ping_client(c)
            time.sleep(2)
            msg = f'Server speaking on {time.asctime()}'
            server.send_data_to_all_clients(msg)
            time.sleep(2)
