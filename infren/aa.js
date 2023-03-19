const arr = [
  { name: 'banana', price: 3000 },
  { name: 'apple', price: 1000 },
  { name: 'orange', price: 500 },
];

const aa = [...arr];
aa.sort(function (a, b) {
  return a.price - b.price;
});

const bb = arr.slice(1, 2);

console.log(bb);
