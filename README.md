# [Chicago Crime](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2)
Exploratory data analysis on Chicago Crimes from 2001 to present.
### Data
The data can be downloaded using `download.py`. Description of main dataset can be found at [Chicago's open data portal](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2). Except main dataset script will download census data, locations of  police stations and boundaries of community areas and police districts.
### Main findings:
* The number of crimes decreased about 50% from 2001 till 2015. After that number of incident is almost constant.
* The percentage of arrests for serious offence is 3 times smaller than for non serious. It's only 12%.
* The further the incident from police station, the less likely the arrest.
* During years location of crime has changed. Number of incidents on streets decreased, but increased in apartments.
* During hotter season there are more incidents. 
* There is increment in larceny and fraud and decrement in drug abuse and aggravated battery during years.
* There are more crimes on New Year than on casual day.
### Interactive maps
Some of the maps made with [plotly](https://plot.ly/). They can be seen properly through [Nbviewer page](https://nbviewer.jupyter.org/github/belkasanek/eda_chicago_crime_data/blob/master/chicago_crimes_eda.ipynb).
