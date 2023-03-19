import React, { useState } from 'react';
import OddEvenResult from './OddEvenResult';

const Counter = (props) => {
  const [count, setCount] = useState(props.initialValue);
  // var count = 0; //useState 안쓰면 렌더링 한번만 하는듯?

  const onIncrease = () => {
    setCount(count + 1);
  };
  const onDecrease = () => {
    setCount(count - 1);
  };

  return (
    <div>
      <h2>{count}</h2>
      <button onClick={onIncrease}>+</button>
      <button onClick={onDecrease}>-</button>

      <OddEvenResult count={count} />
    </div>
  );
};

Counter.deafaultProps = {
  //혹시 props가 전달이 안되었을때
  initialValue: 0,
};

export default Counter;
