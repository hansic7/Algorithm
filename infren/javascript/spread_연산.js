const cookie = {
  base: 'cookie',
  madeIn: 'Korea',
};

///...으로 하는것이 펼치는(spred) 연산임
const chocochipCookie = {
  ...cookie,
  toping: 'chocochip',
};

const blueberryCookie = {
  ...chocochipCookie,
  ...cookie,
  toping: 'blueberry',
};

const strawberryCookie = {
  ...cookie,
  toping: 'strawberry',
};
// console.log(blueberryCookie);

const noTopingCookie = ['촉촉한쿠키', '안촉촉한쿠키'];
const topingCookie = ['바나나', '초코', '딸기'];
const allCookies = [...noTopingCookie, ...topingCookie];
console.log(allCookies);
