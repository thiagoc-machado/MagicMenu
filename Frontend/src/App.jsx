import { BrowserRouter, Route, Routes } from 'react-router-dom';
import "./App.css";
import Login from "./components/Login/login";
import Client from "./components/Client_menu/client";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        MagicMenu
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/client" element={<Client />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
