let person = {
  name: '이정환',
  age: 25,
  tall: 175,
};

const persoKeys = Object.keys(person);

// console.log(persoKeys);

for (let i = 0; i < persoKeys.length; i++) {
  const curKey = person[persoKeys[i]];
  console.log(persoKeys[i] + ' : ' + person[persoKeys[i]]);
}
