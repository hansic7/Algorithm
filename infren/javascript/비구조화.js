// let arr = ['one', ' two', 'three'];

// let one = arr[0];
// let two = arr[1];
// let three = arr[2];
// let [one, two, three] = arr; //위에랑 같은거임(= 배열의 비구조화 할당)
// let [one, two, three] = ['one', ' two', 'three']; //배열의 선언분리 비구조화할당
// console.log(one, two, three);

// let a = 10;
// let b = 20;
// [a, b] = [b, a]; //배열의 비구조 할당
// console.log(a, b);

let object = { one: 'one', two: ' two', three: 'three', name: '조한식' };

// let one = object.one;
// let two = object.two;
// let three = object.three;

let { name, one: the_first, two, three, abc = 'four' } = object; // 키값을 기준으로 가져옴 // 변수명 abc로 "four"를 새롭게 추가 할당
console.log(name, the_first, two, three, abc); // one:the_first로 one은 키값 the_first는 새롭게 지정할 변수명
