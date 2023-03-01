// let arr = [1, 2, 3, 4];

// arr.forEach((elm) => console.log(elm));
// arr.forEach(function (elm) {
//   console.log(elm);
// }); //위에랑 똑같은 거임

// const newArr = arr.map((elm) => {
//   return elm * 2;
// });
// console.log(newArr);

// let number = 3;
// arr.forEach((num) => {
//   if (num == number) console.log(num + ' true');
// });

// const arr = [
//   { num: 1, color: 'red' },
//   { num: 2, color: 'black' },
//   { num: 3, color: 'blue' },
//   { num: 4, color: 'green' },
// ];
// console.log(arr.findIndex((e) => e.color == 'black')); //둘은 같음
// console.log(
//   arr.findIndex((elm) => {
//     return elm.color == 'blue';
//   })
// );
// console.log(
//   ///find 함수
//   arr.find((elm) => {
//     return elm.color == 'blue';
//   })
// );

// var arr = [
//   { num: 1, color: 'red' },
//   { num: 2, color: 'black' },
//   { num: 3, color: 'blue' },
//   { num: 4, color: 'green' },
//   { num: 5, color: 'blue' },
// ];

// console.log(arr.filter((elm) => elm.color == 'blue')); //조건 true인거 배열로 반환함
// console.log(
//   arr.slice(
//     arr.findIndex((elm) => elm.color == 'red'),
//     arr.findIndex((elm) => elm.color == 'green')
//   )
// );

// var arr1 = [
//   { num: 1, color: 'red' },
//   { num: 2, color: 'black' },
//   { num: 3, color: 'blue' },
// ];
// var arr2 = [
//   { num: 4, color: 'green' },
//   { num: 5, color: 'blue' },
// ];
// console.log(arr1.concat(arr2));

// let chars = ['나', '다', '가'];
// chars.sort();
// console.log(chars);

let numbers = [0, 1, 3, 2, 10, 30, 20];

const compare = (a, b) => {
  // 1. 같다
  // 2. 작다
  // 3. 같다
  if (a > b) return 1;
  if (a < b) return -1;
  if (a == b) return 0;
};

numbers.sort(compare);
console.log(numbers);
