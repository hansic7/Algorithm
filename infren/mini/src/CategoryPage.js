import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { useParams } from 'react-router-dom';
import Categories from './Categories';
import MaiPage from './MaiPage';
import data from './dummydata';
import axios from 'axios';

const ItemListBlock = styled.div`
  box-sizing: border-box;
  padding-bottom: 3rem;
  width: 768px;
  margin: 0 auto;
  margin-top: 2rem;
  @media screen and (max-width: 768px) {
    width: 100%;
    padding-left: 1rem;
    padding-right: 1rem;
  }
`;

const ItemList = ({ category }) => {
  const [alcohol, setAlcohol] = useState(data);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    console.log('여기서 부터 막힘');
    console.log(alcohol);
    // async를 사용하는 함수 따로 선언
    const fetchData = async () => {
      // setLoading(true);
      // try {
      const response = await axios.get(
        alcohol.find((x) => x.product_category == category)
      );
      setAlcohol(response.alcohol);
      console.log('카테고리 별 추출');
      console.log(response);
      //   } catch (e) {
      //     console.log(e);
      //   }
      //   setLoading(false);
      // };
      // fetchData();
    };
  }, []);

  // 대기 중일 때
  if (loading) {
    return <ItemListBlock>대기 중...</ItemListBlock>;
  }

  // 값이 유효할 때
  return (
    <ItemListBlock>
      {alcohol.map((alcohol) => (
        //<BoardItem key={alcohol.product_num} alcohol={alcohol} />
        <MaiPage key={alcohol.product_num} alcohol={alcohol} />
      ))}
    </ItemListBlock>
  );
};

const CategoryPage = () => {
  const params = useParams();
  // 카테고리가 선택되지 않았으면 기본값 all로 사용
  const category = params.category || 'all';

  return (
    <>
      <Categories />
      <ItemList category={category} />
    </>
  );
};

export default CategoryPage;
