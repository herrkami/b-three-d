
// import { WebSocket } from 'ws';
// WebSocket = require('ws');

const MessageType = {
  "DATA": 1,
  "CONFIG": 2,
  "BACKEND_RESPONSE": 3,
}

export class TCVController {

  constructor(b_three_d_host, b_three_d_port) {
    if (!b_three_d_host) {
      b_three_d_host = 'ws://localhost';
    }
    if (!b_three_d_port) {
      b_three_d_port = 9678;
    }
    this.b_three_d_host = b_three_d_host;
    this.b_three_d_port = b_three_d_port;
    
    const url = this.b_three_d_host + ':' + this.b_three_d_port + '/';
    this.socket = new WebSocket(url);
    
    this.socket.addEventListener('open', function (event) {
      console.debug('TCVController connected.');
    });
    
    this.socket.addEventListener('message', function (event) {
      console.debug(`Msg:\n[${event.data}]`);

      // // const f = document.getElementById("chatbox").contentDocument;
      // // let text = "";
      // const msg = JSON.parse(event.data);
      // // const time = new Date(msg.date);
      // // const timeStr = time.toLocaleTimeString();
      
      // // Message structure
      // // msg.type
      // // msg.action
      // // msg.data
      // console.log(`Raw message:\n${msg}`);
      // console.log(`Received message of type ${msg.type} with data\n${msg.data}`);
      // switch (msg.type) {
      //   case MessageType.DATA:
      //     const data = msg.data;
      //     handleDataReceived(data);
      //     break;
      //   case MessageType.CONFIG:
      //     const config = msg.data;
      //     handleConfigUpdate(config);
      //     break;
      //   case MessageType.BACKEND_RESPONSE:
      //     const response = msg.data;
      //     handleBackendResponse(response);
      //     break;
      // }
    });
  }
  
  isConnectected() {
    if (this.socket.readyState == this.socket.OPEN) {
      return true;
    }
  }

  sendRaw(msg) {
    this.socket.send(msg);
  }

  handleDataReceived(data) {
    console.debug("handleDataReceived called.")
    return;
  }

  handleConfigUpdate(config) {
    console.debug("handleConfigUpdate called.")
    return;
  }

  handleBackendResponse(response) {
    console.debug("handleBackendResponse called.")
    return;
  }

  // exampleSocket.onmessage = (event) => {

}

// const socket = new WebSocket('ws://localhost:9876');

// socket.addEventListener('open', function (event) {
//   socket.send('Connection Established');
// });

// socket.addEventListener('message', function (event) {
//   console.debug(event.data);
// });

// const pingTheServer = () => {
//   // console.log("Here we are.")
//   socket.send("Ping?");
// }
