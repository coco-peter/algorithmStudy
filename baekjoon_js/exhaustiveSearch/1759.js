("use strict");

const fs = require("fs");

const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `4 6
a t c i s w
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [L, C] = input().split(" ").map(Number);
let wordList = input().split(" ").sort();
let isVisited = Array(C).fill(false);

// console.log(L, C);
let m_word = ["a", "e", "i", "o", "u"];
let m_cnt = 0;
let j_cnt = 0;

DFS(0, 0, wordList);

function setPrint() {
  for (let i = 0; i < wordList.length; i++) {
    if (isVisited[i] === true) {
      process.stdout.write(`${String(wordList[i])}`);
    }
  }
  console.log(" ");
}

function DFS(idx, start, wordList) {
  if (start === L) {
    m_cnt = 0;
    j_cnt = 0;
    for (let i = 0; i < wordList.length; i++) {
      if (isVisited[i] === true) {
        if (m_word.find((e) => e === wordList[i]) === undefined) j_cnt++;
        else m_cnt++;
      }
    }
    if (m_cnt >= 1 && j_cnt >= 2) {
      setPrint();
      return;
    }
  }
  //   console.log(q, wordList.length, isVisited);
  for (let i = idx; i < wordList.length; i++) {
    if (isVisited[i] === false) {
      isVisited[i] = true;
      //   q.push(wordList[i]);
      DFS(i, start + 1, wordList);
      //   q.pop();
      isVisited[i] = false;
    }
  }
}
