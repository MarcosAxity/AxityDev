import React from "react";
import Header from "../report/header/Header";
import InputTopic from "./inputTopic/InputTopic";
import styles from "./ReportDashboard.module.css";

const ReportDashboard = () => {
  return (
    <>
      <section className={styles.resultBody}>
        <div className={styles.headerContainer}>
          <Header />
        </div>
        <div className={styles.inputTopic}>
          <InputTopic />
        </div>
      </section>
    </>
  );
};

export default ReportDashboard;
