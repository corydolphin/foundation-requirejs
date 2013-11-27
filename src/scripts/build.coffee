require.config
  name: "../../bower_components/almond/almond"
  include: ["app"] # main entry point for your application.
  paths:
    jquery: "../../bower_components/jquery/jquery"
    modernizr: "../../bower_components/modernizr/"
    foundation: "../../bower_components/foundation/js/foundation/foundation"
    "foundation.abide": "../../bower_components/foundation/js/foundation/foundation.abide"
    "foundation.accordion": "../../bower_components/foundation/js/foundation/foundation.accordion"
    "foundation.alert": "../../bower_components/foundation/js/foundation/foundation.alert"
    "foundation.clearing": "../../bower_components/foundation/js/foundation/foundation.clearing"
    "foundation.dropdown": "../../bower_components/foundation/js/foundation/foundation.dropdown"
    "foundation.interchange": "../../bower_components/foundation/js/foundation/foundation.interchange"
    "foundation.joyride": "../../bower_components/foundation/js/foundation/foundation.joyride"
    "foundation.magellan": "../../bower_components/foundation/js/foundation/foundation.magellan"
    "foundation.offcanvas": "../../bower_components/foundation/js/foundation/foundation.offcanvas"
    "foundation.orbit": "../../bower_components/foundation/js/foundation/foundation.orbit"
    "foundation.reveal": "../../bower_components/foundation/js/foundation/foundation.reveal"
    "foundation.tab": "../../bower_components/foundation/js/foundation/foundation.tab"
    "foundation.tooltip": "../../bower_components/foundation/js/foundation/foundation.tooltip"
    "foundation.topbar": "../../bower_components/foundation/js/foundation/foundation.topbar"

  shim:
    jquery:
      exports: "jquery"

    foundation:
      deps: ["jquery"]

    "foundation.abide":
      deps: ["foundation"]

    "foundation.accordion":
      deps: ["foundation"]

    "foundation.alert":
      deps: ["foundation"]

    "foundation.clearing":
      deps: ["foundation"]

    "foundation.dropdown":
      deps: ["foundation"]

    "foundation.interchange":
      deps: ["foundation"]

    "foundation.joyride":
      deps: ["foundation"]

    "foundation.magellan":
      deps: ["foundation"]

    "foundation.offcanvas":
      deps: ["foundation"]

    "foundation.orbit":
      deps: ["foundation"]

    "foundation.reveal":
      deps: ["foundation"]

    "foundation.tab":
      deps: ["foundation"]

    "foundation.tooltip":
      deps: ["foundation"]

    "foundation.topbar":
      deps: ["foundation"]
