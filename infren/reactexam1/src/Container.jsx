const Container = ({ children }) => {
  return (
    <div style={{ margin: 20, padding: 20, border: '1px solid gray' }}>
      {children}
    </div>
  );
};

/*  App.js에서 컨테이너 안에 있는 것들이 
    다 children props으로 전달을 받게됨 */

export default Container;
