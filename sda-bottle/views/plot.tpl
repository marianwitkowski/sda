
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

</head>
<body>

<div id="chart" style="width:90%;height:600px;"></div>

<script>

    var trace1 = {
      x: [ {{!dates}} ],
      y: [ {{closes}} ],
      type: 'scatter'
    };

    var trace2 = {
      x: [ {{!dates}} ],
      y: [ {{volumes}}  ],
      yaxis: 'y2',
      type: 'bar'
    };

    var data = [trace1, trace2];

    var layout = {
      title: 'Notowania {{ticker}}',
      yaxis: {title: 'Kurs zamknięcia [PLN]'},
      yaxis2: {
        title: 'Wolumen [szt.]',
        overlaying: 'y',
        side: 'right'
      },
      xaxis:{
        title: 'Dni notowań',
        type: 'category'
      },
    };

    Plotly.newPlot('chart', data, layout);


</script>


</body>
</html>