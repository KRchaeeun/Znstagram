import { useState } from "react";

const useInput = () => {
  const [state, setState] = useState();

  const handleInputChange = (e) => {
    setState(e.target.value);
  };

  const resetState = () => {
    setState("");
  };

  return [state, handleInputChange, resetState];
};

export { useInput };
