import React, { useState, useCallback } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CategoryPage from './CategoryPage';
import data from './dummydata';
import MaiPage from './MaiPage';

function App() {
  const [alcohol, setAlcohol] = useState(data);
  const [item, setItem] = useState([
    {
      prodct_num: 0,
      product_writer: '',
      product_datetime: '',
      product_mainimage: '',
      product_name: '',
      product_introduction: '',
      product_category: '',
      product_percentage: '',
      product_volume: 0,
      product_price: 0,
      product_stock: 0,
    },
  ]);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<MaiPage alcohol={item} />} />
        <Route path="/:category" element={<CategoryPage />} />
      </Routes>
    </Router>
  );
}

export default App;
