import React from "react";
import { StInput, StValidation } from "../styles/Components";

function Input({ type, name, value, placeHolder, onChange, message }) {
  return (
    <>
      <StInput
        name={name}
        type={type}
        value={value}
        placeholder={placeHolder}
        onChange={onChange}
      ></StInput>
      <StValidation>{message}</StValidation>
    </>
  );
}

export default Input;
