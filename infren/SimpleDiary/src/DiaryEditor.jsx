import { useRef } from 'react';
import { useState } from 'react';

const DiaryEditor = ({ onCreate }) => {
  const AuthorInput = useRef();
  const ContentInput = useRef();

  const [state, setState] = useState({
    Author: '',
    Content: '',
    Emotion: 1,
  });

  const handleChangeState = (e) => {
    setState({
      ...state,
      [e.target.name]: e.target.value,
    });
    // console.log(e.target.value);
    // console.log(e.target.name);
  };

  const handleSubmit = () => {
    // console.log(state);
    if (state.Author.length < 1) {
      AuthorInput.current.focus();
      return;
    }
    if (state.Content.length < 5) {
      ContentInput.current.focus();
      return;
    }

    onCreate(state.Author, state.Content, state.Emotion);
    // alert('저장성공');
    setState({
      Author: '',
      Content: '',
      Emotion: 1,
    });
  };

  return (
    <div className="DiaryEditor">
      <h2>오늘의 일기</h2>
      <div>
        <input
          ref={AuthorInput}
          name="Author"
          value={state.Author}
          onChange={handleChangeState}
          // onChange={(e) => setState({ Author: e.target.value })} //이렇게 하면 state에 author만 남음
        />
      </div>
      <br />

      <div>
        <textarea
          ref={ContentInput}
          name="Content"
          value={state.Content}
          onChange={handleChangeState}
        ></textarea>
      </div>
      <div>
        <select name="Emotion" onChange={handleChangeState}>
          <option value={1}>1</option>
          <option value={2}>2</option>
          <option value={3}>3</option>
          <option value={4}>4</option>
          <option value={5}>5</option>
        </select>
      </div>
      <div>
        <button onClick={handleSubmit}>저장하기</button>
      </div>
    </div>
  );
};

export default DiaryEditor;
