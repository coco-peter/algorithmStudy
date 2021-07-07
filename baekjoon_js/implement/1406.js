const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `dmih
11
B
B
P x
L
B
B
B
P y
D
D
P z
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let wordListFront = input().split("").map(String);
let wordListEnd = [];

let N = Number(input());

for (let i = 0; i < N; i++) {
  let command = input().split(" ").map(String);
  console.log(command[0], command[1]);
  if (command[0] === "L") {
    if (wordListFront) wordListEnd.push(wordListFront.pop());
    else continue;
  } else if (command[0] === "D") {
    if (wordListEnd) wordListFront.push(wordListEnd.pop());
    else continue;
  } else if (command[0] === "B") {
    if (wordListFront) wordListFront.pop();
    else continue;
  } else if (command[0] === "P") {
    wordListFront.push(command[1]);
  }
}

// console.log(["a", "b"].reverse().join(""));
console.log(wordListFront.join("") + wordListEnd.reverse().join(""));
