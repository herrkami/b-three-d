// import { Viewer, Timer } from "./three-cad-viewer.esm.js";

function write_config(viewer, config) {

  if ('viewer' in config) {
    for (const [key, value] of Object.entries(config.viewer)) {
      viewer[key] = value;
      console.debug(`Set viewer.${key} to ${viewer[key]}.`);
      // axes
      // axes0
      // grid
      // ortho
      // transparent
      // black_edges
      // collapse

      // clip_intersection
      // clip_plane_helpers
      // clip_normal
      // clip_slider
      // control
      // ticks

      // position
      // quaternion

      // zoom

      // pan_speed
      // rotate_speed
      // zoom_speed

      // timeit
      // zoom0
      // tools
    }
  }
  if ('display' in config) {
    for (const [key, value] of Object.entries(config.display)) {
      viewer.display[key] = value;
      console.debug(`Set viewer.display.${key} to ${display[key]}.`);
      // theme
      // cad_width
      // tree_width
      // height
      // pinning
      // glass
      // tools
      // keymap
    }
  }
  if ('render' in config) {
    for (const [key, value] of Object.entries(config.render)) {
      viewer.renderer[key] = value;
      console.debug(`Set viewer.renderer.${key} to ${render[key]}.`);
      // ambient_intensity
      // direct_intensity
      // metalness
      // roughness
      // default_opacity
      // edge_color
      // normal_len
      // measureTools
    }
  }
}

export { write_config };