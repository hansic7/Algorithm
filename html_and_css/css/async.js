function work3(callback) {
  setTimeout(() => {
    const start = Date.now();
    // Data.now() : 현재 날짜를 숫자 형태로 표시해주는 javascript 내장 함수
    for (let i = 0; i < 1000000000; i++) {}
    const end = Date.now();
    console.log(end - start + 'ms');
    callback(end - start);
  }, 0);
}
// 실행결과
// 작업 시작

console.log('작업 시작');
work3((ms) => {
  console.log('작업이 끝났어요!');
  console.log(ms + 'ms 걸렸다고 해요.');
});
console.log('다음 작업');
