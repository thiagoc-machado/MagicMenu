import { useState } from 'react'
import Logo from '../../assets/logo-main.jpg'
import '../../App.css'

function Client() {
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

export default Client