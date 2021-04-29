("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `3
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let num = 2;

console.log(parseInt(num, 8).toString(2));
