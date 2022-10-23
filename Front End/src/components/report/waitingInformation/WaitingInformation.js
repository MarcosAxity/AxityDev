import React from "react";
import imgComponent from "../../../img/imgComponent.png";
import styles from "./WaitingInformation.module.css";

const WaitingInformation = () => {
  return (
    <>
      <section className={styles.imgComponent}>
        <img
          src={imgComponent}
          alt="imgComponent"
          className={styles.imgPeople}
        />
      </section>
    </>
  );
};

export default WaitingInformation;
