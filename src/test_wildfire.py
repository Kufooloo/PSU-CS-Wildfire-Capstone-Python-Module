import wildfire as wf

wildfire_map = wf.wildfireMap()
wildfire_map.setDates(["1981-02-02"])
wildfire_map.setBounds(18.9, 71.3, -124.8, -66)
wildfire_map.createPlot()