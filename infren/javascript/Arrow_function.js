console.log(HelloB()); //hoisting돼서 이건 출력됨
// console.log(HelloA);

// let HelloA = function () {
//   return '안녕하세요';
// }; //함수 표현식

function HelloB() {
  return '안녕하세요';
} //함수 선언식

let HelloC = () => {
  return '안녕하냐?';
}; //함수 표현식

console.log(HelloC());
