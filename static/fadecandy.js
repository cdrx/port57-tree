!(function() {
  window.FadeCandy = function(canvas, server, token) {
    this.server = server;
    this.canvas = canvas;
    this.token = token;
    this.context = canvas.getContext("2d");
    this.drawing = false;
    this.color = new RColor();
    this.horizontalGridSpacing = 0;
    this.verticalGridSpacing = 0;
    this.points = [];
    //this.socket = null;

    this.ledsX = 32;
    this.ledsY = 64;

    this.init();
  };

  window.FadeCandy.prototype = {
    init: function() {
      this.drawGrid();

      // bind for drawing
      this.registerTouchEvents();
    },

    touchStart: function(e) {
      e.preventDefault();
      this.drawing = true;
    },

    draw: function(e) {
      e.preventDefault();
      if (!this.drawing) {
        return;
      }

      var x, y;

      if (e.offsetX) {
          x = e.offsetX;
          y = e.offsetY;
      } else if (e.layerX) {
          x = e.layerX;
          y = e.layerY;
      }

      // moved outside canvas
      if (typeof x == "undefined" || typeof y == "underfined") {
        return;
      }

      var gridX, gridY = 0;
      if (x > this.horizontalGridSpacing) {
        gridX = parseInt(x / this.horizontalGridSpacing);
      } else {
        gridX = 0
      }

      if (y > this.verticalGridSpacing) {
        gridY = parseInt(y / this.verticalGridSpacing);
      } else {
        gridY = 0;
      }

      // find our closest intersection
      var rgb = this.color.get();
      var rgb = this.randomRGB();
      var pixelX = gridX * this.horizontalGridSpacing;
      var pixelY = gridY * this.verticalGridSpacing;

      this.context.fillStyle = 'rgb('+rgb[0]+','+rgb[1]+','+rgb[2]+')';
      this.context.beginPath();
      this.context.rect(pixelX, pixelY, this.horizontalGridSpacing, this.verticalGridSpacing);
      this.context.closePath();
      this.context.fill();

      this.points[(((this.ledsX - 1) - gridX) * 64) + ((this.ledsY - 1) - gridY)] = {
        rgb: rgb
      };
    },

    sendToServer: function() {
      if (!this.drawing) {
        return;
      }

      var leds = this.ledsX * this.ledsY;

      var packet = new Uint8ClampedArray(leds * 3);

      for (var led in this.points) {
        if (this.points.hasOwnProperty(led)) {
          var dest = 4 + (parseInt(led) * 3)
            , point = this.points[led];

          packet[dest++] = point.rgb[0];
          packet[dest++] = point.rgb[1];
          packet[dest++] = point.rgb[2];
        }
      };

      var req = new XMLHttpRequest();
      req.open("POST", "http://10.0.57.25/draw/update/", true);
      req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
      req.send('token=' + this.token + '&data=' + packet.join(","));
    },

    touchEnd: function(e) {
      e.preventDefault();
      this.sendToServer();
      this.drawing = false;
    },

    drawGrid: function () {
      this.horizontalGridSpacing = this.canvas.clientWidth / this.ledsX;
      for (var x = 0; x <= this.canvas.clientWidth; x += this.horizontalGridSpacing) {
        this.context.moveTo(0.5 + x, 0);
        this.context.lineTo(0.5 + x, this.canvas.clientHeight);
      }

      this.verticalGridSpacing = this.canvas.clientHeight / this.ledsY;
      for (var x = 0; x <= this.canvas.clientHeight; x += this.verticalGridSpacing) {
        this.context.moveTo(0, 0.5 + x);
        this.context.lineTo(this.canvas.clientWidth, 0.5 + x);
      }

      this.context.strokeStyle = "rgba(255, 255, 255, 0.4)";
      this.context.stroke();
    },

    randomRGB: function() {
      var r, g, b;
      var h = Math.random(10);
      var i = ~~(h * 6);
      var f = h * 6 - i;
      var q = 1 - f;
      switch(i % 6) {
        case 0: r = 1, g = f, b = 0; break;
        case 1: r = q, g = 1, b = 0; break;
        case 2: r = 0, g = 1, b = f; break;
        case 3: r = 0, g = q, b = 1; break;
        case 4: r = f, g = 0, b = 1; break;
        case 5: r = 1, g = 0, b = q; break;
      }

      return [
        ("00" + (~ ~(r * 255))),
        ("00" + (~ ~(g * 255))),
        ("00" + (~ ~(b * 255)))
      ];
    },

    registerTouchEvents: function() {
        this.canvas.addEventListener("touchstart", this.touchStart.bind(this), false);
        this.canvas.addEventListener("mousedown", this.touchStart.bind(this), false);
        this.canvas.addEventListener("touchmove", this.draw.bind(this), false);
        this.canvas.addEventListener("mousemove", this.draw.bind(this), false);
        this.canvas.addEventListener("touchend", this.touchEnd.bind(this), false);
        this.canvas.addEventListener("mouseup", this.touchEnd.bind(this), false);

        //setInterval(this.sendToServer.bind(this), 1000 / 60);
    }
  };
})();
