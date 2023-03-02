/// async

function delay(ms) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve();
    }, ms);
  });
}

/* asyn함수는 항상 반환값이 promise임 */
// async function helloAsync() {
//   return delay(500).then(() => {
//     return 'Hello Async';
//   });
// }

// 밑에것 == 위에것

async function helloAsync() {
  await delay(500);
  return 'Hello Async';
} /*await은 async밑에서만 쓰일 수 있고, 비동기 함수를 동기함수처럼 전개하게 한다*/

helloAsync().then((res) => {
  console.log(res);
});
