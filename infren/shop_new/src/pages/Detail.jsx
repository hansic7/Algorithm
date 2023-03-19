import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import styled from 'styled-components';

// let YellowButton = styled.button`
//   background: ${(props) => props.bg};
//   color : ${(props) => (props.bg === 'blue' ? 'white' : 'black')},
//   padding: 10px;
// `;

// let NewBtn = styled.button(YellowButton)`
//   color : white
// `;

const Detail = (props) => {
  let { id } = useParams();
  let rr = props.shoes.find((x) => x.id == id);

  let [alert, setAlert] = useState(true);
  useEffect(() => {
    let a = setTimeout(() => {
      setAlert(false);
    }, 2000);
    console.log(2);
    return () => {
      // 다음번에 렌더링될때 전의 타이머 갖다버리는거
      console.log(1);
      clearTimeout(a);
    };
  }, []);

  return (
    <div className="container">
      {alert == true ? (
        <div className="alert alert-warning">2초이내 구매시 할인</div>
      ) : (
        ''
      )}

      {/* <YellowButton bg={'yellow'}>버튼</YellowButton>
      <YellowButton bg={'blue'}>버튼</YellowButton>
      <NewBtn bg={'blue'}>버f튼</NewBtn> */}
      <div className="row">
        <div className="col-md-6">
          <img
            src="https://codingapple1.github.io/shop/shoes1.jpg"
            width="100%"
            alt=""
          />
        </div>
        <div className="col-md-6">
          <h4 className="pt-5">{rr.title}</h4>
          <p>{rr.content}</p>
          <p>{rr.price}원</p>
          <button className="btn btn-danger">주문하기</button>
        </div>
      </div>
    </div>
  );
};

export default Detail;
