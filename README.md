# enviro Overview :thermometer:
## Environmental Monitoring on Raspberry Pi with Bosch BME680 sensor in Python
This script reads data from a Raspberry Pi [Bosch BME680](https://amzn.to/2DJoFqr) module and writes it to:

- [x] terminal
- [x] CSV file
- [x] SQL database
- [ ] Grafana

I couldn't find code that offered all these options so I've cobbled this together from documentation, examples, and partial implementations found elsewhere.

For those unfamiliar with the Bosch BME680 sensor, it is a available as a breakout board for the Raspberry Pi and has the following sensors:
* Temperature (default is degrees Celsius)
* Humidity (percentage)
* Barometric Pressure (default is Pascals)
* Air Quality (measurement of [Volatile Organic Compounds](https://www.epa.gov/indoor-air-quality-iaq/volatile-organic-compounds-impact-indoor-air-quality)/VOC)

The script itself and the documentation is work-in-progress. However, feel free to open issues for your questions and ideas or contribute to improve the code!

## Roadmap
The following improvements are planned for this project.

### Visualizations
Develop a PHP web file to read from SQL database and plot sensor readings, likely with [Google Chart Library](https://developers.google.com/chart) or [Chart.js](https://www.chartjs.org/), for viewing the data remotely within a web browser. It would assume the pre-existing installation of a [LAMP stack](https://lamp.sh/).

### Grafana/InfluxDB
To better scale with multiple devices, my next step is to transmit the data to an InfluxDB instance for displaying in a Grafana dashboard. 

### BME280 Support
The [Bosch BME280](https://amzn.to/2DL0Tud) is a recently released and more affordable breakout board that has temperature, humidity, and barometric pressure sensors (i.e. everything but air quality). It was not available when I started this project but will likely be bought for my second monitoring device. 

Note: The even cheaper [BM**P**280](https://amzn.to/3bFpIV2) has sensors only for barometric pressure and altitude (i.e. no temperature and humidity)

# Credits
Thank you to all the folks who have trailblazed much of the initialization, configuration, and implementation of the sensor with the Raspberry Pi in Python. In particular, the folks at [Pimoroni](https://github.com/pimoroni) for their [tutorial for the BME680](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-bme680-breakout) and [bme680 python lib](https://github.com/pimoroni/bme680). Also many thanks to [ayeks](https://github.com/ayeks) in advance for his Grafana/InfluxDB implementation that I hope to be able to tailor.
