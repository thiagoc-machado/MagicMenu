import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import Login from "./pages/Login/login";
import Client from "./pages/Menu/client";
import NewUser from "./pages/Login/newUser";
import Menu from "./pages/Menu/menu";



function App() {
  return (
    <BrowserRouter>
      <div className="App">
        MagicMenu
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/client" element={<Client />} />
          <Route path="/newuser" element={<NewUser />} />
          <Route path="/menu" element={<Menu />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
