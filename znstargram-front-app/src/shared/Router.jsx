import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import AccountPage from "../pages/AccountPage";
import Login from "../components/Login";
import Signup from "../components/Signup";

function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<AccountPage />}>
          <Route path="/" element={<Login />}></Route>
          <Route path="/signup" element={<Signup />}></Route>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default Router;
