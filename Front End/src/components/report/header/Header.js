import React from "react";
import styles from "./Header.module.css";

const Header = () => {
  return (
    <>
      <header>
        <section className={styles.logo}>
        <h1>Logo</h1>
        <h4>#AbrazaLaDiversidad</h4>
        </section>
        {/* <nav>
          <ul className={styles.navList}>
            <li>
              <a href="#">Reporte</a>
            </li>
            <li>
              <a href="#">Configuración</a>
            </li>
          </ul>
        </nav> */}
      </header>
    </>
  );
};

export default Header;
