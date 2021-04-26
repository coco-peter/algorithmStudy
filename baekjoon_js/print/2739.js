("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `2
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let t = input();

for (let i = 1; i < 10; i++) {
  console.log(`${t} * ${i} = ${t * i}`);
}
