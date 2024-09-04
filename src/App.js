// App.js
import React, { useState } from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Footer from "./Components/Common/Footer";
import AboutPage from "./Pages/AboutPage";
import HomePage from "./Pages/HomePage";
import Dashboard from "./Components/Common/dashboard";
import ErrorPage from "./Components/Common/ErrorPage"; // Assuming you create this component

function App() {
  const [isPopupVisible, setIsPopupVisible] = useState(false);

  const triggerPopup = () => {
    setIsPopupVisible(true);
  };

  const closePopup = () => {
    setIsPopupVisible(false);
  };

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route 
            path="/" 
            element={<HomePage triggerPopup={triggerPopup} isPopupVisible={isPopupVisible} closePopup={closePopup} />} 
          />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="*" element={<ErrorPage />} /> {/* Handle 404 and other errors */}
        </Routes>
        <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;
