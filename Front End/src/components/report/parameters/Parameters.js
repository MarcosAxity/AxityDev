import React from "react";
import styles from "./Parameters.module.css";
import Fade from 'react-reveal/Fade';
const Parameters =() => {

        return ( <Fade>
          <div className={styles.parameters}>
            
            <section className={styles.text}>
              <h1 className={styles.title} >Parametros</h1>
              <ul className={styles.points}>
              <li >Identificamos en los tweets diferentes géneros relacionados con el tema ingresado.</li>
              <li>Los géneros son asociados negativa, positiva o neutralmente según el contexto del tweet.</li>
             </ul>
             </section>
            
          </div>
          </Fade>
        );
};
export default Parameters;