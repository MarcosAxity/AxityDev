import React from "react";
import {
  registerables,
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";
import { Doughnut } from "react-chartjs-2";

ChartJS.register(Tooltip, Legend, ArcElement, ...registerables);

const DoughnutChart = ({ tweets }) => {
  var data = {
    labels: ["Positivo", "Negativo", "Neutral"],
    datasets: [
      {
        label: "Hilos de tweets",
        data: [
          tweets.map((item) => item.positiveTweets),
          tweets.map((item) => item.negativeTweets),
          tweets.map((item) => item.neutralTweets),
        ],
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)",
          "rgba(255, 159, 64, 0.2)",
        ],
        borderColor: [
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)",
          "rgba(255, 159, 64, 1)",
        ],
        borderWidth: 1,
      },
    ],
  };

  var options = {
    responsive: false,
    maintainAspectRatio: false,
    legend: {
      labels: {
        fontSize: 26,
      },
    },
  };

  return (
    <div>
      <Doughnut data={data} height={400} options={options} />
    </div>
  );
};

export default DoughnutChart;
