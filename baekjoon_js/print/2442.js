("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `5
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let t = input();

for (let i = 0; i < t; i++) {
  for (let j = t - i; j > 1; j--) {
    process.stdout.write(" ");
  }
  for (let k = 0; k < 2 * i + 1; k++) {
    process.stdout.write("*");
  }
  console.log();
}
