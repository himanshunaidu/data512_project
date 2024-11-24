# WildLand Fire Analysis for Indianapolis, IN

The purpose of this project is to examine the impact of wildfires on Indianapolis, IN. Specifically, we will analyze wildfire prevalence and air quality to assess smoke impacts over the past 60 years.

## How to Run

The entire code of the project resides in the following 3 Jupyter notebooks
- [wildfire_data_acquisition.ipynb](wildfire_data_acquisition.ipynb)\
The goal of this notebook is to help with the overall wildland fire analysis for Indianapolis, Indiana, by loading the WildLand Fire data as a geopandas GeoDataFrame, filtering the wildfire observations to those that occurred in the last 60 years, and are within 650 miles of Indianapolis.\
This notebook also performs the smoke estimation, which will be later compared to available AQI data, in the main analysis notebook. 
- [aqi_data_acquisition.ipynb](aqi_data_acquisition.ipynb)\
The goal of this notebook is to help with the overall wildland fire analysis for Indianapolis, Indiana, by loading the Air Quality Index (AQI) data.
- [wildfire_data_analysis.ipynb](wildfire_data_analysis.ipynb)\
The goal of this notebook is to perform the overall analysis wildland fires for Indianapolis, Indiana.


In order to run the notebook, start by setting up the Conda environment, using the [data512.yml](data512.yml).


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

Please note that an email is required to use the API. Steps for setting up the API Key were detailed in the notebook [aqi_data_acquisition.ipynb](aqi_data_acquisition.ipynb).

Create an email address & request an API key using the EPA endpoint and run the function `request_signup` in [aqi_data_acquisition.ipynb](aqi_data_acquisition.ipynb)


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

Path: `./data/Fire_Feature/Fire_Feature_Data.gdb`


### Running the Notebook

The notebooks do not need any additional configuration. Thus, you can run the code using the 'Run All' option.

Run the notebooks in the following order:
1. [wildfire_data_acquisition.ipynb](wildfire_data_acquisition.ipynb)
2. [aqi_data_acquisition.ipynb](aqi_data_acquisition.ipynb)
3. [wildfire_data_analysis.ipynb](wildfire_data_analysis.ipynb)

The entire code base takes ~15 minutes to run on the system used to develop this project, with the main bottleneck being the Geospatial Processing of the GeoDataFrame objects created from USGS Wildland Fire data.

Note: The system used to develop this project is equipped with a 12th Gen Intel® Core™ i7-12700H processor (2.30 GHz)


## Data

### Source Data

#### WildLand Fire Data

The cleaned and organized wildfire data used in this project was provided by the [Combined wildland fire datasets for the United States and certain territories, 1800s-Present (combined wildland fire polygons](https://www.sciencebase.gov/catalog/item/61aa537dd34eb622f699df81). The final geospatial dataset contains both a raw, merged dataset with duplicates and a "combined" dataset that is duplicate-free. This combined dataset includes both wildfires and prescribed fires from the mid-1800s to 2021, compiled from 40 original wildfire datasets. For analysis, we will use only the combined dataset located at [./data/Fire_Feature/Fire_Feature_Data.gdb](data/Fire_Feature/Fire_Feature_Data.gdb). Due to its large size, this file is not tracked on Git and is therefore unavailable in this repository.

The data is listed as public and can be cited as the following:

Welty, J.L., and Jeffries, M.I., 2021, Combined wildland fire datasets for the United States and certain territories, 1800s-Present: U.S. Geological Survey data release, https://doi.org/10.5066/P9ZXGFY3.

##### GeoPandas Usage

Instead of the GeoJSON file, we ended up using the ArcGIS GeoDatabase file (Wildland Fire Polygons Fire Feature Data ArcGIS Pro 2.8 Geodatabase). 

This is because GeoPandas had some issues with reading the GeoJSON file, mostly due to conversion issues that may have occurred while the authors translated the ArcGIS files to GeoJSON. GeoPandas has drivers to directly read the ArcGIS GeoDatabase files. 

#### Air Quality Index Data

This analysis required historical Air Quality Index (AQI) data for Indianapolis, IN, focusing on fire season (May 1 - October 31) each year from 1963 onward. The AQI measures daily air quality to indicate how healthy the air is, tracking pollutants like smog and smoke. Typically, an AQI between 0-50 reflects healthy, clean air, while 500 marks the upper limit for hazardous conditions.

For this project, we accessed data via the US Environmental Protection Agency (EPA) Air Quality Service (AQS) API. The [documentation](https://aqs.epa.gov/aqsweb/documents/data_api.html) explains the available call parameters and includes sample calls.

We used the highest daily average sensor readings from monitoring stations within Indianapolis, IN. These daily maximums were averaged over the fire season to create annual estimates for 1971-2024, as data prior to 1983 was unavailable. Identifying nearby stations requires the Federal Information Processing Series (FIPS) codes for the target city, county, and state, which we sourced [here](https://www.census.gov/library/reference/code-lists/ansi.html). 

### Output Data

1. [aqi_annual_estimates.csv](./final/aqi_annual_estimates.csv)\
This file ontains the final annual AQI estimates for Indianapolis, IN, during the fire season from 1971 to 2024. 

2. [fire_annual_smoke_estimates.csv](./final/fire_annual_smoke_estimates.csv)\
This file ontains the final calculated smoke estimates for Indianapolis, IN, during the fire season from 1964 to 2020. 
