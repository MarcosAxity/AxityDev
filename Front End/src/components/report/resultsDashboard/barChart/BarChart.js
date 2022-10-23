import React from "react";
import { registerables, Chart as ChartJS, BarElement } from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(BarElement, ...registerables);

const BarChart = ({ gender }) => {
  // const [gender, setGender] = useState([]);
  // var baseUrl = "https://635337fca9f3f34c374f84f0.mockapi.io/gender";
  // var proxyUrl = "https://cors-anywhere.herokuapp.com/";
  // var apikey = ;

  // const getAllGender = () => {
  //     fetch("https://635337fca9f3f34c374f84f0.mockapi.io/gender")
  //       .then((response) => response.json())
  //       .then((gender) => {
  //         setGender(gender);
  //         console.log(gender);
  //       });
  //   };

  //   useEffect(() => {
  //     getAllGender();
  //   }, []);

  var data = {
    labels: ["Mujer", "Hombre", "Neutral"],
    datasets: [
      {
        label: "Sésgos de género",
        // label: `${gender.length} Gender Available`,
        // data: [70, 30],
        data: [
          gender.map((item) => item.relatedToWomen),
          gender.map((item) => item.relatedToMen),
          gender.map((item) => item.tweetPercentageWithoutBias),
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
    scales: {
      y: {
        beginAtZero: true,
      },
    },
    legend: {
      labels: {
        fontSize: 26,
      },
    },
  };
  return (
    <div>
      <Bar data={data} height={400} options={options} />
    </div>
  );
};

export default BarChart;
