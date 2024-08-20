This directory contains a slightly modified version of https://github.com/joeyhng/trainplot

# TrainPlotter

Generate JSON files for plots in during training networks.

## Usage
```lua
require 'TrainPlotter'
local plotter = TrainPlotter.new('plot-data/exp.json')
plotter:add('Accracy', 'Train', 1, 0.5)
plotter:add('Accracy', 'Train', 2, 0.7)
plotter:add('Accracy', 'Train', 3, 0.8)
plotter:add('Accracy', 'Test', 1, 0.45)
plotter:add('Accracy', 'Test', 2, 0.6)
plotter:add('Accracy', 'Test', 3, 0.7)
```

## Seeing Plots
Start a HTTP server by
```

python -m SimpleHTTPServer
```

Open showplots.html in browser to change the JSON path, or 
apt-get install openssh-client

create a folfer plot-data/UCF101 in trainPlot folder and paste plot.json
specify with query string like
```

http://10.200.4.35:8001/trainplot/showplots.html?path=plot-data/FlowJHMDB/Full16FlowRGB_FlowJHMDB_Batch30.json

```
copied trainplot-0.1-1.rockspec in ltc-master
executed luarocks install trainplot-0.1-1.rockspec
and inside showplots.html replace line 6 with <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

