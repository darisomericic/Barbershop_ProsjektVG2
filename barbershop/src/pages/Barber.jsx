import style from '../style/barber.module.css'

function Barber() {
  return (
    <div className={style.container}>
      <h1 className={style.title}>Barber Page</h1>
      <p className={style.text}>Welcome to the Barber page!</p>
    </div>
  );
}
export default Barber;