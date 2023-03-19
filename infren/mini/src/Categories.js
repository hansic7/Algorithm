import React, { useState } from "react";
import styled, { css } from "styled-components";
import { NavLink } from "react-router-dom";

const categories = [
  {
    name: "all",
    text: "메인",
  },
  {
    name: "탁주",
    text: "탁주",
  },
  {
    name: "증류주",
    text: "증류주",
  },
  {
    name: "과실주",
    text: "과실주",
  },
];

const CategoriesBlock = styled.div`
  display: flex;
  padding: 1rem;
  width: 768px;
  margin: 0 auto;
  @media screen and (max-width: 768px) {
    width: 100%;
    overflow-x: auto;
  }
`;

const Category = styled(NavLink)`
  font-size: 1.125rem;
  cursor: pointer;
  white-space: pre;
  text-decoration: none;
  color: inherit;
  padding-bottom: 0.25rem;

  &:hover {
    color: #495057;
  }

  &.active {
    font-weight: 600;
    border-bottom: 2px solid #22b8cf;
    color: #22b8cf;
    &:hover {
      color: #3bc9db;
    }
  }
  & + & {
    margin-left: 1rem;
  }
`;
const Categories = () => {
  return (
    <CategoriesBlock>
      <div>
        {categories.map((c) => (
          <Category
            key={c.name}
            classNames={({ isActive }) => (isActive ? "active" : undefined)}
            to={c.name === "all" ? "/" : `/${c.name}`}
          >
            {c.text}
          </Category>
        ))}
      </div>
      {console.log("카테고리")}
    </CategoriesBlock>
  );
};

export default Categories;
