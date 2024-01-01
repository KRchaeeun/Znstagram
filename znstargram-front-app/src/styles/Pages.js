import { styled } from "styled-components";
import { StFlexAll, StFlexCon } from "./GlobalStyles";

// AccountPage
export const StAccountCon = styled(StFlexAll)`
  width: 100%;
  height: 100vh;
  padding: 5% 0;
`

export const StFormCon = styled.div`
  width: 350px;
  height: auto;
  padding: 2.3rem;
  border: 1px solid #ccc;
  border-radius: 10px;

  h2 {
    width: 100%;
    height: 54px;
    margin-bottom: 10%;
    position: relative;
    overflow: hidden;
    display: flex;

    img {
      width: 175px;
      height: auto;
      display: block;
      position: absolute;
      top: -48px;
      left: 50%;
      transform: translateX(-50%);
    }
  }

  h4 {
    font-size: 17px;
    text-align: center;
    padding-bottom: 10%;
    color: #666;
  }

  p {
    font-size: 0.75rem;
    color: #666;
    padding: 5% 0;

    a {
      color: navy;
    }
  }
`;