# Demand-Forecasting-App

## Project Overview

The **Demand Forecasting App** is designed to help optimize inventory and supply chain management by accurately predicting product demand. This app uses historical sales data to generate demand forecasts for the top-selling products over a 15-week period. The system provides key insights through visualizations, error histograms, and forecasts to aid in making informed inventory decisions.

### Features
- Displays the top 10 best-selling products based on historical sales data.
- Provides weekly demand forecasts for the next 15 weeks for each product.
- Allows users to view historical demand data, forecasted demand, and error distributions for model accuracy evaluation.
- An interactive web app built using **Streamlit** and deployed on **Heroku** for easy access.

## Data Sources
The system uses four main datasets:
1. **Transactional_data_retail_01.csv**: Sales transaction details including product codes, quantities, prices, and dates.
2. **Transactional_data_retail_02.csv**: Additional transaction details.
3. **CustomerDemographics.csv**: Information about customers.
4. **ProductInfo.csv**: Product details such as descriptions and categories.

## Project Structure

The following is a brief overview of the main files and directories in this project:

Demand-Forecasting-App/
│
├── app.py                  # Main Streamlit app for demand forecasting and visualization
├── data/
│   ├── Transactional_data_retail_01.csv       # Transactional data for analysis
│   ├── Transactional_data_retail_02.csv       # Additional transactional data
│   ├── CustomerDemographics.csv               # Customer demographic information
│   └── ProductInfo.csv                        # Information about each product
│
├── notebooks/
│   └── demand_forecasting.ipynb               # Jupyter notebook for data exploration and model development
│
├── requirements.txt        # Required libraries and dependencies for the app
├── Procfile                # Heroku configuration file for app deployment
├── README.md               # Project documentation and instructions

## Setup Instructions

To run the project locally, follow these steps:

### Prerequisites

1. **Python 3.7+**
2. **Git** (for version control)
3. **Anaconda** (optional, but recommended for managing environments)

### Step 1: Clone the Repository

#### bash
- git clone https://github.com/your-username/Demand-Forecasting-System.git
- cd Demand-Forecasting-System

## Step 2: Set Up a Virtual Environment
- Using Anaconda:

#### bash
- conda create -n demand_forecasting_env python=3.8
- conda activate demand_forecasting_env
- Or using venv:

#### bash
- python -m venv venv
- source venv/bin/activate  # On Windows, use: venv\Scripts\activate
  
## Step 3: Install Required Libraries
Install the dependencies listed in requirements.txt:

#### bash
- pip install -r requirements.txt
### Step 4: Run the Application
To launch the Streamlit app, run the following command:

#### bash
- streamlit run app.py
- This command will open a new browser window with the app interface.

### Usage
**Top 10 Products**: The app displays the top 10 products based on total sales.
**Historical and Forecast Plots**: Select a product to view both its historical demand data and forecasted demand for the next 15 weeks.
**Error Histogram**: Visualize the error distribution for the model’s training and test periods, giving insights into the accuracy of the forecasts.
### Example Commands for Jupyter Notebook
- To perform data preprocessing and build a forecasting model, open notebooks/demand_forecasting.ipynb and follow the instructions.

### Deployment on Heroku
- The app is deployed on Heroku for easy access. You can view the live app at: Your Heroku App Link

### To deploy your own instance on Heroku, follow these steps:

- Login to Heroku:

#### bash
- heroku login
- Create a new Heroku app:

#### bash
- heroku create your-app-name
- Push the code to Heroku:

#### bash
- git add .
- git commit -m "Deploying to Heroku"
- git push heroku main  # or git push heroku master
- Open the app in your browser:

#### bash
- heroku open
  
### Known Issues

**Data Format**: Ensure all date formats in the datasets are consistent. Use pd.to_datetime with errors='coerce' to handle discrepancies.

**Model Parameters**: The default ARIMA model parameters are (1,1,1). For better accuracy, consider tuning these parameters based on the dataset.

### Future Improvements

**User Authentication**: Add login functionality for secured access.

**Alternative Models**: Explore other time series forecasting models such as Prophet or LSTM.

**Dashboard Enhancements**: Add more visualizations and interactivity.
