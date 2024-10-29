# WildLand Fire Analysis for Indianapolis, IN

The purpose of this project is to examine the impact of wildfires on Indianapolis, IN. Specifically, we will analyze wildfire prevalence and air quality to assess smoke impacts over the past 60 years. A secondary objective is to build reproducibility and professional skills essential for conducting data-driven analysis, as part of the Autumn 2024 DATA 512 course at the University of Washington.

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


### Running the Notebook

The notebook does not need any additional configuration. Thus, you can run the code using the 'Run All' option.

The entire code base takes ~15 minutes to run on the system used to develop this project, with the main bottleneck being the Geospatial Processing of the GeoDataFrame objects created from USGS Wildland Fire data.

Note: The system used to develop this project is equipped with a 12th Gen Intel® Core™ i7-12700H processor (2.30 GHz)


## Data

### Source Data


### Output Data