import React from "react";
import { Outlet } from "react-router-dom";
import { StAccountCon, StFormCon } from "../styles/Pages";

function AccountPage() {
  return (
    <>
      <StAccountCon>
        <StFormCon>
          <h2>
            <img src="https://static.cdninstagram.com/rsrc.php/v3/yS/r/ajlEU-wEDyo.png" />
          </h2>
          <Outlet />
        </StFormCon>
      </StAccountCon>
    </>
  );
}

export default AccountPage;
