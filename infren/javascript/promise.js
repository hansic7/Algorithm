// function isPositive(number, resolve, reject) {
//   setTimeout(() => {
//     if (typeof number == 'number') {
//       //성공 -> resolve
//       resolve(number >= 0 ? '양수' : '음수');
//     } else {
//       reject('주어진 값이 숫자형 값이 아닙니다');
//     }
//   }, 500);
// }

// isPositive(
//   'k',
//   (res) => {
//     console.log('성공적으로 수행됨 : ', res);
//   },
//   (res) => {
//     console.log(res);
//   }
// );

// ------------------------------------------------------------

// function isPositive(number) {
//   const executor = (resolve, rrr) => {
//     setTimeout(() => {
//       if (typeof number == 'number') {
//         //성공 -> resolve
//         resolve(number >= 0 ? '양수' : '음수');
//       } else {
//         rrr('주어진 값이 숫자형 값이 아닙니다');
//       }
//     }, 500);
//   };

//   const asyncTask = new Promise(executor);
//   return asyncTask;
// }

// const res = isPositive('k');
// res
//   .then((res) => {
//     console.log('작업성공 : ', res);
//   })
//   .catch((err) => {
//     console.log('작업 실패 : ', err);
//   });
// console.log(res);
// setTimeout(() => {
//   console.log(res);
// }, 500);

// ------------------------------------------------------------

// function taskA(a, b, cb) {
//   setTimeout(() => {
//     const res = a + b;
//     cb(res);
//   }, 2000);
// }

// function taskB(a, cb) {
//   setTimeout(() => {
//     const res = a * 2;
//     cb(res);
//   }, 500);
// }

// function taskC(a, cb) {
//   setTimeout(() => {
//     const res = a * -1;
//     cb(res);
//   }, 1000);
// }

// taskA(3, 4, (a_res) => {
//   console.log('A result : ', a_res);
//   taskB(a_res, (b_res) => {
//     console.log('B result : ', b_res);
//     taskC(b_res, (c_res) => {
//       console.log('C result : ', c_res);
//     });
//   });
// });

// ------------------------------------------------------------

function taskA(a, b) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const res = a + b;
      resolve(res);
    }, 500);
  });
}

function taskB(a) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const res = a * 2;
      resolve(res);
    }, 500);
  });
}

function taskC(a) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const res = a * -1;
      resolve(res);
    }, 500);
  });
}

// taskA(5, 1).then((a_res) => {
//   console.log('A result : ', a_res);
//   taskB(a_res).then((b_res) => {
//     console.log('B result : ', b_res);
//     taskC(b_res).then((c_res) => {
//       console.log('C result : ', c_res);
//     });
//   });
// });

// -then chinning 방법
taskA(5, 1)
  .then((a_res) => {
    console.log('A result : ', a_res);
    return taskB(a_res);
  })
  .then((b_result) => {
    console.log('B result :', b_result);
    return taskC(b_res);
  })
  .then((c_result) => {
    console.log('C result :', c_result);
  });
