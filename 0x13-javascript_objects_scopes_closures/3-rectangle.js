#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.print = function () {
        let char = '';
        for (w = this.width; w > 0; w--) {
          char += 'X';
        }
        for (h = this.height; h > 0; h--) {
          console.log(char);
        }
      };
    } else {
      constructor();
    }
  }
};
