#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;

      // prints rectangle using character `X`
      this.print = function () {
        let char = '';
        for (w = this.width; w > 0; w--) {
          char += 'X';
        }
        for (h = this.height; h > 0; h--) {
          console.log(char);
        }
      };

      // exchanges the width and height of the rectangle
      this.rotate = function () {
        const tmp = this.height;
        this.height = this.width;
        this.width = tmp;
      };

      // multiplies the width and height by 2
      this.double = function () {
        this.height *= 2;
        this.width *= 2;
      };
    } else {
      constructor();
    }
  }
};
