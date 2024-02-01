
// import { WebSocket } from 'ws';
// WebSocket = require('ws');
import { Viewer, Timer } from "./three-cad-viewer.esm.js";
import { write_config } from "./viewer_interface.js";

const MessageType = {
  "DATA": "D",
  "CONFIG": "C",
  // "RESPONSE_FROM_BACKEND": "B",
  // "RESPONSE_FROM_FRONTEND": "F",
}

export class TCVController {

  // const host, port = 'localhost', 3123;
  // const callback = null;
  // viewer = new Viewer(container, options, callback);
  // controller = TCVController(host, port, viewer);

  constructor(
    b_three_d_host,  // WebSocket to b-three-e backend
    b_three_d_port,  
    viewer,  // viewer instance running the frontend
  ) {

    // WebSocket configuration 
    if (!b_three_d_host) {
      b_three_d_host = 'ws://localhost';
    }
    if (!b_three_d_port) {
      b_three_d_port = 9678;
    }
    this.b_three_d_host = b_three_d_host;
    this.b_three_d_port = b_three_d_port;

    
    // Get viewer instance
    if (!viewer) {
      console.error("You must provide a viewer instance, otherwise there's nothing to control.")
    } else {
      this.viewer = viewer;
      // Check if a callback function has previously been set and notify the
      // user if so.
      if (this.viewer.notifyCallback) {
        console.warn('Overwriting existing viewer.notifyCallback');
      }
      this.viewer.notifyCallback = this.viewer_callback;
    }
    
    // Initialization

    // Create a WebSocket connection and assign event handlers
    const url = this.b_three_d_host + ':' + this.b_three_d_port + '/';
    this.socket = new WebSocket(url);

    // On open
    this.socket.addEventListener('open', (event) => {
      console.debug('TCVController connected.');
    });

    // On message
    this.socket.addEventListener('message', (event) => {
      const raw_data = event.data;
      
      var msg = {
        'type':raw_data.substring(0, 1), 
        'data': raw_data.toString().substring(2),
      };

      switch (msg.type) {
        case MessageType.CONFIG:
          this.#handleConfigReceived(msg.data);
          break;
        
        case MessageType.DATA:
          this.#handleDataReceived(msg.data);
          break;
      }
    });
  }

  // WebSocket
  isConnectected() {
    if (this.socket.readyState == this.socket.OPEN) {
      return true;
    }
  }

  sendRaw(msg) {
    this.socket.send(msg);
  }

  viewer_callback(changed) {
    // Viewer parses an object that contains all things that changed, e.g.
    // { clip_normal_0: { old: null, new: this.clipNormal0 } }
    console.log('Callback received:', changed);
  }

  // Controller
  #handleConfigReceived(data) {
    console.debug("#handleConfigReceived called.");
    var config = JSON.parse(data);
    console.debug("Received config:", config);
    write_config(this.viewer, config);
    // Structure
    // component.option.value
    // switch (config[0]) {
    //   case 'viewer':
    //     console.debug("Configuring viewer:", config['viewer']);

    //     // axes
    //     // axes0
    //     // grid
    //     // ortho
    //     // transparent
    //     // black_edges
    //     // collapse
        
    //     // clip_intersection
    //     // clip_plane_helpers
    //     // clip_normal
    //     // clip_slider
    //     // control
    //     // ticks
        
    //     // position
    //     // quaternion
        
    //     // zoom
        
    //     // pan_speed
    //     // rotate_speed
    //     // zoom_speed
        
    //     // timeit
    //     // zoom0
    //     // tools
    //     break;
    //   case 'display':
    //     console.debug("Configuring display:", config['display']);
    //     // theme
    //     // cad_width
    //     // tree_width
    //     // height
    //     // pinning
    //     // glass
    //     // tools
    //     // keymap
    //     break;
    //     case 'render':
    //     console.debug("Configuring renderer:", config['render']);
    //     // ambient_intensity
    //     // direct_intensity
    //     // metalness
    //     // roughness
    //     // default_opacity
    //     // edge_color
    //     // normal_len
    //     // measureTools

    //     break;
    // }
    // console.log('Received config:', config);
  }


  #handleDataReceived(data) {
    console.debug("#handleDataReceived called.");
    return;
  }
}