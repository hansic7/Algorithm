import DiaryItem from './Diaryitem';

const DiaryList = ({ onEdit, onRemove, diaryList }) => {
  // console.log(diaryList);
  return (
    <div className="DiaryList">
      <h2>일기리스트</h2>
      <h4>{diaryList.length}개의 일기가 있습니다.</h4>
      <div>
        {diaryList.map((it) => (
          <DiaryItem key={it.id} {...it} onEdit={onEdit} onRemove={onRemove} />
        ))}
      </div>
    </div>
  );
};

DiaryList.defaultProps = {
  diaryList: [],
}; //이거 작동 안되는데 왠지 모르겠음

export default DiaryList;
