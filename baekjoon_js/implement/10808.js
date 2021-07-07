("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `baekjoon
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let word = input();
let alphabet = Array(26).fill(Number(0));

for (let i = 0; i < word.length; i++) {
  //   console.log(word.charCodeAt(i) - 97);
  alphabet[word.charCodeAt(i) - 97]++;
}

alphabet.forEach((element) => {
  process.stdout.write(String(element));
  process.stdout.write(" ");
});
