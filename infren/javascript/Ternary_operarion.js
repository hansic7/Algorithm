// let a = -3;
// if (a >= 0) {
//   console.log('양수');
// } else {
//   console.log('음수');
// } //너무 김 -> 삼항연산자 씀
// a >= 0 ? console.log('양수') : console.log('음수');

// let a = [];
// if (a.length == 0) {
//   console.log('빈 배열');
// } else {
//   console.log('안 빈 배열');
// }
// a.length == 0 ? console.log('빈 배열') : console.log('안 빈 배열');

// const empty = a.length == 0 ? '빈 배열' : '안 빈 배열';
// console.log(empty);

// let a;
// const result = a ? true : false;
// console.log(result);

// // 학점계산 프로그램
// // 90점 이상 A+
// // 50점 이상 b+
// // 둘다 아니면 F
let score = 40;

score >= 90
  ? console.log('A+')
  : score >= 50
  ? console.log('B+')
  : console.log('F');

//중첩 삼항연산은 가독성 떨어져서 if로 씀
if (score >= 90) {
  console.log('A+');
} else if (score >= 50) {
  console.log('B+');
} else {
  console.log('F');
}
