import React, { useState, useEffect } from 'react';

const UnmountTest = () => {
  useEffect(() => {
    console.log(`mount`);
  }, []);
  return <div>Unmount Testing Component</div>;
};

const LifeCycle = () => {
  const [isVisible, setIsVisible] = useState();
  const toggle = () => {
    setIsVisible(!isVisible);
  };

  return (
    <div style={{ padding: '20px' }}>
      <button onClick={toggle}>ON/OFF</button>
      {isVisible && <UnmountTest />}
    </div>
  );
};

export default LifeCycle;
