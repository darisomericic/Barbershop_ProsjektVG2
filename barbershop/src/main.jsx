import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import style from './style/barber.module.css'
import Barber from './pages/barber'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Barber />
  </StrictMode>,
)
