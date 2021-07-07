("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `9
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = Number(input());

let starArr = Array(N)
  .fill(" ")
  .map(() => Array(N).fill(" "));

function printStar(x, y, N) {
  //   console.log(x, y, N);
  if (N == 1) {
    starArr[y][x] = "*";
  } else {
    let nextSize = parseInt(N / 3);
    for (yy = 0; yy < 3; yy++) {
      for (xx = 0; xx < 3; xx++) {
        // [nx, ny] = [(N / 3) * xx, (N / 3) * yy];
        if (xx != 1 || yy != 1) {
          console.log(x + xx * nextSize, y + yy * nextSize, nextSize);
          printStar(x + xx * nextSize, y + yy * nextSize, nextSize);
        }
        console.log(x + xx * nextSize, y + yy * nextSize, nextSize);
      }
    }
  }
}

printStar(0, 0, N);

for (let y = 0; y < N; y++) {
  for (let x = 0; x < N; x++) {
    process.stdout.write(String(starArr[y][x]));
  }
  console.log();
}

// console.log(starArr);
