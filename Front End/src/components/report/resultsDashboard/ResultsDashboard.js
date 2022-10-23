import React, { useState, useEffect } from "react";
import styles from "./ResultsDashboard.module.css";
import BarChart from "./barChart/BarChart";
import DoughnutChart from "./doughnutChart/DoughnutChart";
import Parameters from "../parameters/Parameters";
import WaitingInformation from "../waitingInformation/WaitingInformation";

const ResultsDashboard = ({ event }) => {
  const [gender, setGender] = useState([]);
  const [tweets, setTweets] = useState([]);
  const [femalePercentage, setFemalePercentage] = useState();
  const [malePercentage, setMalePercentage] = useState();
  const [tweetWithoutBias, setTweetWithoutBias] = useState();
  const [negativeTweets, setNegativeTweets] = useState();
  const [positiveTweets, setPositiveTweets] = useState();
  const [neutralTweets, setNeutralTweets] = useState();
  const [mixedTweets, setMixedTweets] = useState();

  const getAllGender = () => {
    fetch("https://635337fca9f3f34c374f84f0.mockapi.io/gender")
      .then((response) => response.json())
      .then((gender) => {
        setGender(gender);
        setFemalePercentage(gender.map((item) => item.relatedToWomen));
        setMalePercentage(gender.map((item) => item.relatedToMen));
        setTweetWithoutBias(
          gender.map((item) => item.tweetPercentageWithoutBias)
        );
      });
  };

  const getAllTweets = () => {
    fetch("https://635337fca9f3f34c374f84f0.mockapi.io/tweetsFeelings")
      .then((response) => response.json())
      .then((tweets) => {
        setTweets(tweets);
        setNegativeTweets(tweets.map((item) => item.negativeTweets));
        setPositiveTweets(tweets.map((item) => item.positiveTweets));
        setNeutralTweets(tweets.map((item) => item.neutralTweets));
        setMixedTweets(tweets.map((item) => item.mixedTweets));
      });
  };

  useEffect(() => {
    getAllGender();
    getAllTweets();
  }, []);

  return (
    <>
      {event && (
        <div>
          <main>
            <section className={styles.result}>
              <h4>Tweets con sésgos de género</h4>
              <BarChart gender={gender} />
              <p>
                Los tweets encontrados tuvieron un porcentaje de sesgo hacia la
                mujer de <strong>{femalePercentage}%</strong>, un porcentaje de
                sesgo hacia el hombre de <strong>{malePercentage}%</strong> y un
                porcentaje de tweets sin sesgos de género del{" "}
                <strong>{tweetWithoutBias}%</strong>.
              </p>
            </section>

            <section className={styles.result}>
              <h4>Sentimiento en los tweets</h4>
              <DoughnutChart tweets={tweets} />
              <p>
                Los tweets encontrados tuvieron un porcentaje de sentimientos
                negativos del <strong>{negativeTweets}%</strong>, un porcentaje
                de sentimientos positivos del <strong>{positiveTweets}%</strong>
                , un porcentaje de tweets con sentimientos neutral del{" "}
                <strong>{neutralTweets}%</strong> y un porcentaje de tweets en
                un rango inconcluso del <strong>{mixedTweets}%</strong>.
              </p>
            </section>
          </main>

          <div className={styles.parameters}>
            <Parameters />
          </div>
        </div>
      )}
      {!event && (
        <div className={styles.resultsDashboard}>
          <WaitingInformation />
        </div>
      )}
    </>
  );
};

export default ResultsDashboard;
