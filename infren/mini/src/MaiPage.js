import './App.css';
import { Container, Nav, Navbar, Row, Col } from 'react-bootstrap';
import { useState, useEffect } from 'react';
// import data from ‘./data.js’;
// import { Route, Routes, Link, useNavigate, Outlet } from ‘react-router-dom’;
// import Detail from ‘./pages/Detail’;
import axios from 'axios';
import data from './dummydata';
import Categories from './Categories';
import './hoho.jpg';

const MaiPage = ({ alcohol }) => {
  /* { 맨 처음에 데이터 받아옴 } */
  /* { 문제생겨서 일단 주석 처리함 } */
  return (
    <div>
      {/* <div className=“main-bg”></div> */}
      {/* {console.log("ani", props.alcohList)}
      <img src={bg} alt="" style={{ backgroundSize: "cover" }} />
      <div style={{ backgroundImage: "url(bg)" }}></div>
      <br />
      <br /> */}
      <Categories />
      <Row>
        {console.log('맵함수 전')}
        {console.log(alcohol)}
        {useEffect(() => {
          alcohol.map((alcohol) => {
            return <Card alcohol={alcohol} />;
          });
        }, [])}
      </Row>
      <button
        onClick={() => {
          // axios
          //   // .get(‘https://codingapple1.github.io/shop/data2.json’)
          //   .get(‘./dummydata.json’)
          //   .then((res) => {
          //     const copy = [...alcohList.shoes, ...res.data];
          //     setAlcohList(copy);
          //   })
          //   .catch(() => {
          //     console.log(‘실패하였음‘);
          //   });
        }}
      >
        더보기
      </button>
    </div>
  );
};

const Card = (props) => {
  return (
    <div className="container">
      <Col sm={4}>
        {/* <img
        src={`https://codingapple1.github.io/shop/shoes${1 + props.i}.jpg`}
        width=“80%”
        alt=“”
      /> */}
        <img src="./hoho.jpg" width="80%" alt="" />
        <h4>{props.alcohol.product_name}</h4>
        <p>{props.alcohol.product_price}</p>
      </Col>
    </div>
  );
};
// const MaiPage = () => {
//   return (
//     <div>
//       <h5>asdkfhjjdsaj</h5>
//     </div>
//   );
// };
export default MaiPage;
