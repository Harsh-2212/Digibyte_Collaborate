var chrt = document.getElementById("chartId").getContext("2d");
var chartId = new Chart(chrt, {
   type: 'doughnut',
   data: {
      labels: ["Academics", "Non-Academics", "Administration", "Cultural", "Others"],
      datasets: [{
      label: "Events  Attended",
      data: [20, 40, 13, 35, 20, 38],
      backgroundColor: ['yellow', 'aqua', 'pink', 'lightgreen', 'lightblue'],
      hoverOffset: 5
      }],
   },
   options: {
      responsive: false,
   },
});