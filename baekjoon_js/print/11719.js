("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `    Hello

Baekjoon     
   Online Judge`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

// console.log(stdin);

stdin.forEach((element) => {
  console.log(element);
});

// for (let i = 0; i < 4; i++) {
//   let text = input();
//   console.log(text);
// }

// while (true) {
//   try {
//     let text = input();
//     console.log(text);
//   } catch {
//     break;
//   }
// }
