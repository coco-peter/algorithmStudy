// 9 9 8 8 7 7 6 6 5 5 4 4 3 3 2 2 1 1 0 0
// 5 5 4 3 2 1
const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `5
5
4
3
2
1
`
).split("\n");

console.log(stdin);

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let t = input();
let a = new Array(t);
for (let i = 0; i < t; i++) {
  a[i] = parseInt(input());
}

// console.log(a.sort());

// 선택정렬
// for (let i = 0; i < t; i++) {
//   for (let j = i; j < t; j++) {
//     if (a[i] > a[j]) {
//       temp = a[i];
//       a[i] = a[j];
//       a[j] = temp;
//     }
//   }
// }

// console.log(a);

// 삽입정렬

// for (let i = a.length - 1; i > -1; i--) {
//   for (let j = i; j > -1; j--) {
//     if (a[i] < a[j]) {
//       temp = a[i];
//       a[i] = a[j];
//       a[j] = temp;
//     }
//   }
// }

// console.log(a);

// 계수정렬

// let maxArray = Math.max.apply(null, a);
// let check = Array.from({ length: maxArray + 1 }, () => 0);
// for (let i = 0; i < a.length; i++) {
//   check[a[i]] += 1;
// }
// for (let i = 0; i < check.length; i++) {
//   while (check[i] > 0) {
//     // 자동 줄바꿈 안하게 하는법...
//     process.stdout.write(String(i));
//     process.stdout.write(" ");

//     // console.log(i);
//     check[i] -= 1;
//   }
// }

// quick sort
function quickSort(arr, start, end) {
  //   console.log(arr, start, end);
  if (start >= end) return;

  let pivot = start;
  let left = start + 1;
  let right = end;

  while (left <= right) {
    while (left <= arr.length - 1 && arr[left] < arr[pivot]) left += 1;
    while (right > 0 && arr[right] > arr[pivot]) right -= 1;

    let temp = 0;
    if (left > right) {
      temp = arr[right];
      arr[right] = arr[pivot];
      arr[pivot] = temp;
    } else {
      temp = arr[right];
      arr[right] = arr[left];
      arr[left] = temp;
    }
  }

  quickSort(arr, start, right - 1);
  quickSort(arr, right + 1, end);
}

quickSort(a, 0, a.length - 1);

console.log(a);
