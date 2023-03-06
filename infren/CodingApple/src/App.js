/* eslint-disable */

import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {
  let [post, setPost] = useState([
    '남자 코트 추천',
    '강남 우동 맛집',
    '파이썬 독학',
  ]);
  // let [like, setLike] = useState(0);
  let [like, setLike] = useState([0, 0, 0]);
  let [modal, setModal] = useState(false);
  let [titleNum, setTitleNum] = useState(0);
  let [inputValue, setInputvalue] = useState('');

  return (
    <div className="App">
      <div className="black-nav">
        <h4>ReactBlog</h4>
      </div>

      <button
        onClick={() => {
          let copy = [...post];
          copy.sort();
          setPost(copy);
        }}
      >
        가나다순정렬
      </button>

      <button
        onClick={() => {
          let copy = [...post];
          copy[0] = '여자 코트 추천';
          setPost(copy);
        }}
      >
        변경하기
      </button>

      {post.map((a, i) => {
        return (
          <div className="list" key={i}>
            <h4
              onClick={() => {
                setModal(!modal);
                setTitleNum(i);
              }}
              className="cursor"
            >
              {post[i]}
            </h4>
            <span
              // className="cursor"
              onClick={() => {
                let copy = [...like];
                copy[i] = copy[i] + 1;
                setLike(copy);
              }}
            >
              👍
            </span>
            {like[i]}
            <p>2월 17일 발행</p>
            <button
              onClick={() => {
                let copy = [...post];
                copy.splice(i, 1);
                setPost(copy);
                let likeCopy = [...like];
                likeCopy.splice(i, 1);
                setLike(likeCopy);
              }}
            >
              삭제
            </button>
          </div>
        );
      })}

      <input
        onChange={(e) => {
          setInputvalue(e.target.value);
        }}
      />
      <button
        onClick={() => {
          let copy = [inputValue, ...post];
          setPost(copy);
          let copyLike = [0, ...like];

          setLike(copyLike);
        }}
      >
        글발행
      </button>

      {modal ? (
        <Modal post={post} setPost={setPost} titleNum={titleNum} />
      ) : null}
    </div>
  );
}

function Modal(props) {
  return (
    <div className="modal">
      <h4>{props.post[props.titleNum]}</h4>
      <p>날짜</p>
      <p>상세내용</p>
      <button
        onClick={() => {
          let copy = [...props.post];
          copy[0] = '여자 코트 추천';
          props.setPost(copy);
        }}
      >
        글수정
      </button>
    </div>
  );
}

export default App;
