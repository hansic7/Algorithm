const productOption = [{ a: 11 }, { a: 22 }];

const mapping = (message) => {
  console.log(message);
};

productOption.map((a) => {
  mapping(a.a);
});
