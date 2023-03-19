import './App.css';
import { Container, Nav, Navbar, Row, Col } from 'react-bootstrap';
import { useState, useEffect } from 'react';
import data from './data.js';
import { Route, Routes, Link, useNavigate, Outlet } from 'react-router-dom';
import Detail from './pages/Detail';
import axios from 'axios';

function App() {
  let [shoes, setShoes] = useState(data);
  let navigate = useNavigate();

  return (
    <div className="App">
      {/* 네비게이션 바임 */}
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="#home">ShoeShop</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link
              onClick={() => {
                navigate('/');
              }}
            >
              Home
            </Nav.Link>
            <Nav.Link
              onClick={() => {
                navigate('/detail/1');
              }}
            >
              Detail
            </Nav.Link>
          </Nav>
        </Container>
      </Navbar>

      {/* 라우트임 */}
      <Routes>
        <Route
          path="/"
          element={<MainPage shoes={shoes} setShoes={setShoes} />}
        />
        <Route path="/detail/:id" element={<Detail shoes={shoes} />} />
        <Route path="*" element={<div>없는페이지요</div>} />

        <Route path="/about" element={<About />}>
          <Route path="members" element={<div>멤버임</div>} />
          <Route path="location" element={<div>위치임</div>} />
          <Route />
        </Route>

        <Route path="/event" element={<Today />}>
          <Route
            path="one"
            element={<div>첫 주문시 양배추즙 서비스</div>}
          ></Route>
          <Route path="two" element={<div>생일기념 쿠폰받기</div>}></Route>
        </Route>
      </Routes>
    </div>
  );
}

const Today = () => {
  return (
    <>
      <h4>오늘의 이벤트</h4>
      <Outlet></Outlet>
    </>
  );
};

const About = () => {
  return (
    <div>
      <h4>회사정보임</h4>
      <Outlet></Outlet>
    </div>
  );
};

const MainPage = (props) => {
  return (
    <div>
      <div className="main-bg"></div>
      <Row>
        {props.shoes.map((shoes, i) => {
          return <Card shoes={shoes} i={i} />;
        })}
      </Row>
      <button
        onClick={() => {
          axios
            .get('https://codingapple1.github.io/shop/data2.json')
            .then((res) => {
              const copy = [...props.shoes, ...res.data];
              props.setShoes(copy);
            })
            .catch(() => {
              console.log('실패하였음');
            });
        }}
      >
        더보기
      </button>
    </div>
  );
};

const Card = (props) => {
  return (
    // <div className='"container'>
    <Col sm={4}>
      <img
        src={`https://codingapple1.github.io/shop/shoes${1 + props.i}.jpg`}
        width="80%"
        alt=""
      />
      <h4>{props.shoes.title}</h4>
      <p>{props.shoes.price}</p>
    </Col>
    // </div>
  );
};

// const Card = (props) => {
//   return (
//     <div className='"container' style={{ display: 'inline' }}>
//       <div className="row">
//         <div className="col-md-4">
//           <img
//             src={`https://codingapple1.github.io/shop/shoes${1 + props.i}.jpg`}
//             width="80%"
//             alt=""
//           />
//           <h4>{props.shoes.title}</h4>
//           <p>{props.shoes.price}</p>
//         </div>
//       </div>
//     </div>
//   );
// };
export default App;
