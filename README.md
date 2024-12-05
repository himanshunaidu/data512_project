# WildLand Fire Analysis for Indianapolis, IN

The purpose of this project is to examine the health impact of wildfires on Indianapolis, IN. More specically, we will be assessing the impact of wildre smoke on respiratory health. Smoke exposure from wildfires can have significant repercussions on public health, especially concerning respiratory conditions, making it a critical issue for the community. The primary aim is to assess the impact of smoke on respiratory health within the healthcare system, including potential changes in morbidity and mortality related to respiratory diseases. The respiratory diseases of interest for this analysis are Asthma and COPD. 

Using data available at the state-level, we approximate the impact of wildland fire smoke on respiratory health on the city. Based on our smoke estimates and past trends in asthma and COPD, we notice a few interesting trends. For asthma, our results indicate that while Asthma incidence is expected to keep decreasing, the Asthma death rates are expected to slightly rise in the coming years. This comes off as quite surprising, as the initial intuition is that due to advances in medicine, Asthma should not prove as fatal in the coming years. For COPD on the other hand, both the incidence rate and death rate have been increasing over time, and these rates are expected to continue to increase, albeit at a lower rate in the coming years. 

The final report of the project can be found [here](reports/DATA_512_Final_Report.pdf).

This project's secondary objective is for students in the University of Washington's Autumn 2024 DATA 512 course to acquire the professionalism and repeatability skills necessary for practical data-driven analysis.

## How to Run

In order to run the project, start by setting up the Conda environment, using the [data512.yml](data512.yml):

### Python Environment

To set up the Conda environment for the project, using the [data512.yml](data512.yml) file, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the data512.yml file is located. For this project, it would be the data-512-homework_1 folder.

    Note: Switch to the main branch.

3. Run the following command to create the Conda environment:

    ```
    conda env create -f data512.yml
    ```

    This command will read the data512.yml file and create a new Conda environment with the specified dependencies.

4. Once the environment is created, activate it by running the following command:

    ```
    conda activate data512
    ```
    (If the name in data512.yml has been changed, update the above environment name accordingly)

5. You can now proceed with running your notebooks or any other tasks within the activated Conda environment.

Remember to deactivate the environment when you're done by running `conda deactivate`.


### Get API Key for EPA AQS API

Please note that an email is required to use the API. Steps for setting up the API Key were detailed in the notebook [2_aqi_data_acquisition.ipynb](2_aqi_data_acquisition.ipynb).

Create an email address & request an API key using the EPA endpoint and run the function `request_signup` in [2_aqi_data_acquisition.ipynb](2_aqi_data_acquisition.ipynb)


### Environment File for Credentials

The project uses the dotenv package to load credentials (mainly for the AQS API, further instructions in the notebook) from a file called '.env' in the same directory as this notebook. The file should look like this:

```
    EMAIL=<email>
    AQS_USERNAME=<aqs_username>
    AQS_KEY=<aqs_key>
```

The repository has a file called '.env.example' that you can copy to '.env' and fill in the values with your own credentials. 

### Data Setup

1. Download and unzip the ArcGIS Geodatabase file from the Wildland Fire Source Data

Link: [Combined wildland fire datasets for the United States and certain territories, 1800s-Present (combined wildland fire polygons](https://www.sciencebase.gov/catalog/item/61aa537dd34eb622f699df81)

File name (current): Fire_Feature_Data_Pro2_8_Geodatabase.zip
Description: “Wildland Fire Polygons Fire Feature Data ArcGIS Pro 2.8 Geodatabase”

2. Add the GeoDatabase file do the data folder

(Rename folder to Fire_Feature)\
Final Path: `./data/Fire_Feature`


### Running the Notebooks

The notebooks do not need any additional configuration. Thus, you can run the code using the 'Run All' option.

This project's code base is divided into the following notebooks for carrying out the analyses:
- [1_wildfire_data_acquisition.ipynb](1_wildfire_data_acquisition.ipynb)\
The goal of this notebook is to help with the overall wildland fire analysis for Indianapolis, Indiana, by loading the WildLand Fire data as a geopandas GeoDataFrame, filtering the wildfire observations to those that occurred in the last 60 years, and are within 650 miles of Indianapolis.\
This notebook also performs the smoke estimation, which will be later compared to available AQI data, in the main analysis notebook. 
- [2_aqi_data_acquisition.ipynb](2_aqi_data_acquisition.ipynb)\
The goal of this notebook is to help with the overall wildland fire analysis for Indianapolis, Indiana, by loading the Air Quality Index (AQI) data.
- [3_wildfire_data_analysis.ipynb](3_wildfire_data_analysis.ipynb)\
The goal of this notebook is to perform the overall analysis wildland fires for Indianapolis, Indiana.
- [4_healthcare_data_acquisition.ipynb](4_healthcare_data_acquisition.ipynb)\
The goal of this notebook is to help with the overall wildland fire analysis for Indianapolis, Indiana, by loading and exploring all the healthcare data.
The notebook also combines all the data into a single dataframe and save it for further analysis. 
- [5_wildfire_healthcare_data_analysis.ipynb](5_wildfire_healthcare_data_analysis.ipynb)\
This final notebook aims to examine the health impact of wildfires on Indianapolis, IN. More specically, in this notebook, we assess the impact of wildre smoke on respiratory health.\
We first perform an Expoloratory Data Analysis, by analysing the trends of the respiratory illness measures and their correlations with our smoke estimates. Finally, we utilize our current and forecasted smoke estimates along with the current respiratory illness data, to forecast the respiratory illness measures for the next 10 years. 

### Overall Codebase

- [utils](utils/)\
This module contains some utility functions to be used by the notebooks. 
    - [gdf_utils.py](utils/gdf_utils.py)\
    This sub-module contains functions to visualize Geodataframes. 

The entire code base takes ~15 minutes to run on the system used to develop this project, with the main bottleneck being the Geospatial Processing of the GeoDataFrame objects created from USGS Wildland Fire data.

Note: The system used to develop this project is equipped with a 12th Gen Intel® Core™ i7-12700H processor (2.30 GHz)


## Data

### Source Data

#### WildLand Fire Data

The cleaned and organized wildfire data used in this project was provided by the [Combined wildland fire datasets for the United States and certain territories, 1800s-Present (combined wildland fire polygons](https://www.sciencebase.gov/catalog/item/61aa537dd34eb622f699df81). The final geospatial dataset contains both a raw, merged dataset with duplicates and a "combined" dataset that is duplicate-free. This combined dataset includes both wildfires and prescribed fires from the mid-1800s to 2021, compiled from 40 original wildfire datasets. For analysis, we will use only the combined dataset located at [./data/Fire_Feature/Fire_Feature_Data.gdb](data/Fire_Feature/Fire_Feature_Data.gdb). Due to its large size, this file is not tracked on Git and is therefore unavailable in this repository (instructions for inserting the file correctly have been given in [Data Setup](#data-setup)).

Out of the 28 attributes present for each wildland fire in the geodatabase file, we utilize the following variables to get the relevant details:
- `USGS_Assigned_ID`: A unique ID for each wildland fire.
- `Assigned_Fire_Type`: The assigned type of the fire. Is one of following values: 'Wildfire', 'Likely Wildfire', 'Prescribed Fire', 'Unknown Likely Wildfire', and 'Unknown - Likely Prescribed Fire'.
- `Fire_Year`: The year of the fire.
- `Listed_Fire_Dates`: Contains a list of dates related to major events related to the specific wildland fire. Can contain dates such as 'Listed Ignition Date(s)', 'Prescribed Fire Start Date', 'Listed Wildfire Controlled Date(s)', 'Prescribed Fire End Date', but there is no specific schema to adhere. This column was used to extract possible start and end dates of the fire.
- `Shape_Length`: A system-generated field that automatically calculates and populates the length of the longest section in the polygon.
- `Shape_Area`: A system-generated field that automatically calculates and populates the area of the polygon.

We focus on a select subset of Wildland fires that satisfy the following conditions:
- Occurred in the last 60 years: [1964 - Present]:\
This is straightforward to filter and is intended to avoid potentially inaccurate data collected prior to the advent of satellite imaging
- Within 650 miles of Indianapolis, IN:\
We designate (39.7684, -86.1580) as the latitude and longitude coordinates representing the center of Indianapolis.\
For distance calculation, we go with `EPSG:5070` (Conus Albers / USA Contiguous Albers Equal Area Conic). This CRS is indeed well-suited for the contiguous United States and designed specifically to minimize distortion for both area and distance across this region.
- Occurred in the fire season (1st May - 31st October):\
We utilized the `Listed_Fire_Dates` attribute in the database to get the possible start and end dates for each wildland fire, and filtered out those that did not have an overlap with the fire season. 

The data is listed as public and can be cited as the following:

Welty, J.L., and Jeffries, M.I., 2021, Combined wildland fire datasets for the United States and certain territories, 1800s-Present: U.S. Geological Survey data release, https://doi.org/10.5066/P9ZXGFY3.

##### GeoPandas Usage

Instead of the GeoJSON file, we ended up using the ArcGIS GeoDatabase file (Wildland Fire Polygons Fire Feature Data ArcGIS Pro 2.8 Geodatabase). 

This is because GeoPandas had some issues with reading the GeoJSON file, mostly due to conversion issues that may have occurred while the authors translated the ArcGIS files to GeoJSON. GeoPandas has drivers to directly read the ArcGIS GeoDatabase files. 

#### Air Quality Index Data

This analysis required historical Air Quality Index (AQI) data for Indianapolis, IN, focusing on fire season (May 1 - October 31) each year from 1963 onward. The AQI measures daily air quality to indicate how healthy the air is, tracking pollutants like smog and smoke. Typically, an AQI between 0-50 reflects healthy, clean air, while 500 marks the upper limit for hazardous conditions.

For this project, we accessed data via the US Environmental Protection Agency (EPA) Air Quality Service (AQS) API. The [documentation](https://aqs.epa.gov/aqsweb/documents/data_api.html) explains the available call parameters and includes sample calls.

Out of the 32 attributes present for the aqi data, we utilize the following variables to get the relevant details:
- `site_number`: Number assigned to the site that contains the aqi sensor.
- `parameter_code`: 5-digit AQS parameter code assigned to the parameter being recorded.
- `poc`: Used when there are multiple sensors measuring the same pollutant at a site.
- `latitude`: Latitude of the sensor location.
- `longitude`: Longitude of the sensor location.
- `parameter`: Parameter being recorded. 
- `date_local`: Date of the measurement of the parameter.
- `aqi`: AQI value of the parameter. 

We used the above attributes to get the highest daily average sensor readings from monitoring stations within Indianapolis, IN. These daily maximums were averaged over the fire season to create annual estimates for 1971-2024, as data prior to 1983 was unavailable. Identifying nearby stations requires the Federal Information Processing Series (FIPS) codes for the target city, county, and state, which we sourced [here](https://www.census.gov/library/reference/code-lists/ansi.html). 

#### Respiratory Health Data

The following sources of data are utilized to extract respiratory health data in Indianapolis, IN. 

1. [Global Burden of Disease (GBD)](https://vizhub.healthdata.org/gbd-results/)

The data contained in this IHME (Institute for Health Metrics and Evaluation: Homepage) dashboard can be used to extract respiratory illness-related raw counts and rates (per 10,000) for incidence (new cases), prevalence (total cases), and deaths, from 1999-2021. 
The lowest level of granularity is state-level (Indiana).

From the dashboard, we can get access to the following dataset:
- IHME-GBD_2021_DATA-<uuid>.csv:
This CSV file contains all the aggregated data that is obtained from the dashboard.
    - `Measure`: (Deaths, Prevalence, Incidence)
    - `Metric`: (Percent, Rate, Number)
    - `Year`: Year in which the measured incident occurred.
    - `Value`: Value of the measurement according to the metric.

The datasets can be downloaded from the dashboard in zipped CSV les. The data is governed by the 
[IHME FREE-OF-CHARGE NON-COMMERCIAL USER AGREEMENT](https://www.healthdata.org/Data-tools-practices/data-practices/ihme-free-charge-non-commercial-user-agreement).

2. [MCPHD Environmental Public Health Tracking Dashboard](https://marionhealth.org/explore-data/)

The data contained in this dashboard tracks asthma and COPD-related ED (Emergency Department) visits and hospitalizations from 2016 - 2023. 
The main reason for the limited window of data is the fact that Marion County was only recently awarded a grant by the CDC (Centers for Disease Control and Prevention), in 2022. 

From the dashboard, we can get access to the following datasets:
- Asthma_ED_Yearly.csv / COPD_ED_Yearly.csv:
Tracks the ED visits for asthma from 2018 - 2023.
    - `Year`: Year for which the number of ED visits is being measured. 
    - `AgeAdjustedRatePer10K`: Number of ED visits per 10,000 people. 

- Asthma_Hosp_Yearly.csv / COPD_Hosp_Yearly.csv:
Tracks the Hospitalizations for asthma from 2016-2018
    - `Year`: Year for which the number of hospitalizations is being measured. 
    - `AgeAdjustedRatePer10K`: Number of hospitalizations per 10,000 people. 


The datasets can be downloaded in separate CSV files.

3. [Federal Reserve Economic Database (FRED)](https://fred.stlouisfed.org/series/CDC20N2U018097)

FRED is an online database that has more than 800,000 time series datasets from various sources. 
From this database, we will be utilizing the ‘Age-adjusted premature death rate’ for Marion County and Indiana.

We can access the following dataset from the link:
- CDC20N2UAA018097.csv:
This CSV file contains all the aggregated data for the age-adjusted premature deaths in Marion County that is obtained from the link.
    - `Year`: Year for which the number of premature deaths is being measured. 
    - `Count`: Number of premature deaths

- CDC20N2UAA042063.csv:
This CSV file contains all the aggregated data for the age-adjusted premature deaths in Indiana that is obtained from the link.
    - `Year`: Year for which the number of premature deaths is being measured. 
    - `Count`: Number of premature deaths

The dataset can be downloaded from the given link in CSV format. 
FRED explicitly mentions that all data can be freely utilized, as long as one mentions FRED as the service from which the data was retrieved from, and keep note of the copyright notices that appear on the data with FRED. 
Additional details for the terms of use can be found [here](https://fred.stlouisfed.org/legal/).


### Intermediate Data

#### Wildland Fire Data

We store the wildland fire data used for further analysis, in the following intermediate files:

1. [Fire_Feature_Distances.csv](./intermediate/Fire_Feature_Distances.csv)\
This csv file contains the distance of each wildland fire from Indianapolis, IN. The information from this file will be used to get the relevant subset of wildland fires to be used for further analysis. \
Due to its large size, this file is not tracked on Git, however, this can easily be created by running the notebook [1_wildfire_data_acquisition.ipynb](1_wildfire_data_acquisition.ipynb).\
Columns of note:
    - `Distance`: Distance of the wildland fire from Indianapolis.

2. [filtered_fire_features.geojson](./intermediate/filtered_fire_features.geojson)\
This geojson file contains the relevant subset of the wildland fires that will be used to calculate smoke estimates and perform further analysis. 
Due to its large size, this file is not tracked on Git, however, this can easily be created by running the notebook [1_wildfire_data_acquisition.ipynb](1_wildfire_data_acquisition.ipynb). \
Same schema as the source wildland fire file from [Wildland Fire Data](#wildland-fire-data)

3. [wildfire_smoke_estimates.json](./intermediate/wildfire_smoke_estimates.json)\
This json file contains the smoke estimates for each wildland fire, which will eventually be used to calculate overall smoke estimates. \
Due to its large size, this file is not tracked on Git, however, this can easily be created by running the notebook [1_wildfire_data_acquisition.ipynb](1_wildfire_data_acquisition.ipynb).\
Attributes of note:
    - `Fire_First_Date`: Estimated start date of the fire.
    - `Fire_Last_Date`: Estimated last date of the fire.
    - `smoke_estimate`: Smoke estimate of the fire. 


#### Air Quality Index Data

We store aqi-related data for further analysis, in the following file:

1. [aqi_daily_estimates.csv](./intermediate/aqi_daily_estimates.csv)\
This file contains the AQI estimate for each day in Indianapolis. This data will be further used to calculate the annual AQI estimates. 
The file contains the following columns:
    - `date_local`: Date for the AQI estimate. 
    - `aqi`: The annual estimate of the AQI for the year. 
    - `year`: Year for the AQI estimate.

### Output Data

1. [aqi_annual_estimates.csv](./final/aqi_annual_estimates.csv)\
This file contains the final annual AQI estimates for Indianapolis, IN, during the fire season from 1971 to 2024. 
The file contains the following columns:
    - `year`: Year for the AQI estimate.
    - `aqi`: The annual estimate of the AQI for the year. 

2. [fire_annual_smoke_estimates.csv](./final/fire_annual_smoke_estimates.csv)\
This file contains the final calculated smoke estimates for Indianapolis, IN, during the fire season from 1964 to 2020. 
The file contains the following columns:
    - `Fire_Year`: Year for the smoke estimate.
    - `smoke_estimate_annual`: The average smoke estimate for the year (the term _weighted is an artifact to signify that the estimate was calculated by doing a weighted sum of all the relevant fires for that year). 

3. [forecasted_smoke_estimates.csv](./final/forecasted_smoke_estimates.csv)\
This file contains the forecasted smoke estimates for Indianapolis, IN, for the next 25 years (2021 - 2045).
The file contains the following columns:
    - `Fire_Year`: Year for the smoke estimate.
    - `smoke_estimate_annual`: The average smoke estimate for the year (the term _weighted is an artifact to signify that the estimate was calculated by doing a weighted sum of all the relevant fires for that year).

4. [forecasted_asthma.csv](./final/forecasted_asthma.csv)\
This file contains the forecasted asthma metrics for Indianapolis, IN, for the next 25 years (2021 - 2045).
The file contains the following columns:
    - `Year`: Year for the asthma metric.
    - `Asthma_Incidence_Rate_State`: The forecasted asthma incidence rate for the year.
    - `Asthma_Death_Rate_State`: The forecasted asthma death rate for the year.

5. [forecasted_copd.csv](./final/forecasted_copd.csv)\
This file contains the forecasted COPD metrics for Indianapolis, IN, for the next 25 years (2021 - 2045).
The file contains the following columns:
    - `Year`: Year for the asthma metric.
    - `COPD_Incidence_Rate_State`: The forecasted COPD incidence rate for the year.
    - `COPD_Death_Rate_State`: The forecasted COPD death rate for the year.


## Special Considerations and Known Issues

1. Data Quality:

None of the data sources contain asthma-related data for all the years for which we did the smoke estimates. While data from FRED and IHME GBD at least contain data of more than 20 years, the data for MCPHD is only for 3-5 years. Due to the insufficiency of the data available for Marion County, we had to acquiesce in the decision to perform analysis at the state level using the IHME and FRED data. \
Fortunately this did not break any of our prior assumptions, thanks to the fact that Indianapolis is at the center of Indiana, with the maximum radius of the state not being more than 200 miles. Thus, the filtering of the wildfires according to distance was still valid. 

2. Smoke Estimation Methodology:

The approach to estimating the impact of smoke relies on a calculation method that incorporates the area of the fires, their distance from Indianapolis, and whether they are true wildfires or prescribed wildfires.

$$\text{Smoke} = \beta_0 + \beta_1 \frac{\text{Area}}{\text{Distance}^2} + \beta_2 Fire\_Type + \beta_3 \frac{\text{Area}}{\text{Distance}^2} Fire\_Type$$

For the given model, we will be giving the betas the following values (thus, accounting only for interaction among all the variables):
- $\beta_0$ = 0
- $\beta_1$ = 0
- $\beta_2$ = 0
- $\beta_3$ = 1

While this approach establishes a base framework for our analysis, it does have certain limitations that we must consider and adjust for in our analysis.

3. Weak correlation between Smoke Estimates and AQI levels

While the AQI level data is not the source of truth for our analysis, since AQI levels are related to several factors unrelated to wildland fires, the weak correlation between our smoke estimates and the AQI levels do present a cause for concern. 

4. Predictive Model Limitations

Both the ARIMA and VARMAX models we employed for predictive analysis depend strongly on accurate historical data and assumes that future trends will reflect past patterns. This dependency presents a limitation, as the model may fail to capture unexpected changes or anomalies in future data, which could impact its predictive accuracy and reduce the reliability of our forecasts.


## Conclusion

This analysis explored the health impacts of wildfire smoke on the residents of Indianapolis, Indiana, with a particular focus on asthma and COPD-related health outcomes. By leveraging data from various sources, including wildfire occurrences, air quality indices, and state-level respiratory health statistics, the study sought to understand the trends and potential future implications of smoke exposure on public health. Using human-centered data science principles, the research aimed to inform policy and intervention strategies for the city's public health response.

Key findings reveal a complex relationship between wildfire smoke estimates and respiratory health indicators. While the occurrence of wildfires and their associated smoke levels have increased over the past decades, correlations with state-level respiratory health metrics such as incidence and mortality rates were found to be weak. This suggests that other factors, including improved air quality control measures and advances in medical care, may be mitigating some of the potential health impacts in Indianapolis. Forecasting models predict a relatively stable trend in smoke estimates over the next 25 years, while certain respiratory outcomes, like asthma-related deaths, are projected to rise in the next 10 years, highlighting a need for targeted attention.

The findings of this study have important implications for public health and policymaking. Policymakers should prioritize the protection of vulnerable populations, such as children, the elderly, and individuals with pre-existing respiratory conditions, by implementing targeted interventions and increasing community awareness during wildfire seasons. Additionally, sustained investments in air quality monitoring and proactive health data collection at the local level can enhance Indianapolis’s resilience against future environmental challenges.

By applying a human-centered approach, this project demonstrates the value of integrating diverse data sources and analytical methods to address pressing public health issues. While the results serve as a foundational understanding of wildfire impacts in Indianapolis, they also highlight the need for continued research, collaboration, and action to safeguard the health and well-being of the city’s residents.
