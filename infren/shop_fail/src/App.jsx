import './App.css';
import { Container, Nav, Navbar, Row, Col } from 'react-bootstrap';
import { useState } from 'react';
import data from './data.js';

function App() {
  let [shoes] = useState(data);
  console.log(shoes[0].title);

  return (
    <div className="App">
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="#home">ShoeShop</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#features">Cart</Nav.Link>
          </Nav>
        </Container>
      </Navbar>

      <div className="main-bg"></div>
      <Row>
        {shoes.map((shoes, i) => {
          return <Card shoes={shoes} i={i} />;
        })}
      </Row>
    </div>
  );
}

const Card = (props) => {
  return (
    <Col sm>
      <img
        src={`https://codingapple1.github.io/shop/shoes${1 + props.i}.jpg`}
        width="80%"
        alt=""
      />
      <h4>{props.shoes.title}</h4> <p>{props.shoes.price}</p>
    </Col>
  );
};

export default App;
