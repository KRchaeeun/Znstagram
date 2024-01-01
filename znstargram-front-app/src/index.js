import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { QueryClient, QueryClientProvider } from "react-query";
import { CookiesProvider } from "react-cookie";

const queryClient = new QueryClient();
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <QueryClientProvider client={queryClient}>
    <CookiesProvider>
      <React.StrictMode>
        <App />
      </React.StrictMode>
    </CookiesProvider>
  </QueryClientProvider>
);