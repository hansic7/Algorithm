// let a = 'd';

// if (a) {
//   console.log('True');
// } else {
//   console.log('False');
// }
// function gerName(person) {
//   return person.name;
// }

const getName = (person) => {
  if (!pers) return '객체가 아닙니다';
  else return person.name;
};
// let pers = { name: '조한식' };
let pers;
const name = getName(pers);
console.log(name);
