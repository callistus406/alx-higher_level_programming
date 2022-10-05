class Rectangle {
  constructor(w, h) {
    if (w > 0 || h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
    // console.log('X'.repeat(this.width) + ' \n' + 'X'.repeat(this.height));
  }
}

const rect = new Rectangle(7, 4);

rect.print();
