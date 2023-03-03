// import logo from './logo.svg';
// import './App.css';
import Myheader from './Myheader';
import Counter from './Counter';
import Container from './Container';

function App() {
  return (
    <Container>
      {/* <div className="App"> */}
      <Myheader />
      <Counter initialValue={5} />
      {/* </div> */}
    </Container>
  );
}

export default App;

/* <img src={logo} className="App-logo" alt="logo" />
  <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React </a> */
