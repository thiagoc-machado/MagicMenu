import { useState } from 'react'
import Logo from './assets/logo-main2.png'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://react.dev" target="_blank">
          <img src={Logo} className="logo" alt="logo" />
        </a>
      </div>
      <h1></h1>
      <div className="card">
      </div>
    </>
  )
}

export default App
