function checkMood(mood, goodcallback, badcallback) {
  if (mood == 'good') {
    goodcallback();
  } else {
    badcallback();
  }
}
function cry() {
  console.log('Action :: cry');
}

function sing() {
  console.log('Action :: sing');
}
function dance() {
  console.log('Action :: dance');
}

checkMood('go', sing, dance);
