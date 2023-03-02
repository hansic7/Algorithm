function taskA(a, b, cb) {
  setTimeout(() => {
    const res = a + b;
    cb(res);
  }, 2000);
}

function taskB(a, cb) {
  setTimeout(() => {
    const res = a * 2;
    cb(res);
  }, 500);
}

function taskC(a, cb) {
  setTimeout(() => {
    const res = a * -1;
    cb(res);
  }, 1000);
}

// taskA(3, 4, (output) => {
//   console.log('A Task result :', output);
// });
// taskC(14, (output) => {
//   console.log('C Task result :', output);
// });
// taskB(7, (output) => {
//   console.log('B Taksk result :', output);
// });

taskA(4, 5, (a_res) => {
  console.log('A result : ', a_res);
  taskB(a_res, (b_res) => {
    console.log('B result : ', b_res);
    taskC(b_res, (c_res) => {
      console.log('C result : ', c_res);
    });
  });
});

console.log('코드 끝');
