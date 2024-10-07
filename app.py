import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from statsmodels.tsa.arima.model import ARIMA  # Example forecasting model
from datetime import timedelta
from sklearn.metrics import mean_absolute_error

# Load datasets
def load_data():
    data1 = pd.read_csv('Transactional_data_retail_01.csv')
    data2 = pd.read_csv('Transactional_data_retail_02.csv')
    data = pd.concat([data1, data2], ignore_index=True)
    return data

# Function to calculate top 10 products
def get_top_products(data):
    data['TotalSales'] = data['Quantity'] * data['Price']
    top_products = data.groupby('StockCode')['TotalSales'].sum().reset_index()
    top_products = top_products.sort_values(by='TotalSales', ascending=False).head(10)
    return top_products

# Function to get historical demand
def get_historical_demand(data, stock_code):
    historical_data = data[data['StockCode'] == stock_code].copy()
    historical_data['InvoiceDate'] = pd.to_datetime(historical_data['InvoiceDate'], errors='coerce')
    demand = historical_data.groupby('InvoiceDate').agg({'Quantity': 'sum'}).reset_index()
    return demand

# Function to forecast demand for the next 15 weeks
def forecast_demand(historical_demand):
    # Split the data into training and test sets
    train_size = int(len(historical_demand) * 0.8)
    train, test = historical_demand[:train_size], historical_demand[train_size:]

    # Fit ARIMA model
    model = ARIMA(train['Quantity'], order=(1, 1, 1))
    model_fit = model.fit()

    # Forecasting for the test set
    forecast_steps = len(test)
    forecast = model_fit.forecast(steps=forecast_steps)
    
    # Add forecast to test data for error calculation
    test['Forecast'] = forecast.values
    
    # Calculate errors
    test['Error'] = test['Quantity'] - test['Forecast']
    
    return train, test

# Main function to run the app
def main():
    st.title("Top 10 Products")
    
    # Load the data
    data = load_data()

    # Get top products
    top_products = get_top_products(data)
    st.subheader("Top 10 Products by Sales")
    st.write(top_products)

    # Create a selectbox for stock code
    stock_code_input = st.selectbox("Select a Stock Code from the Top 10 Products", top_products['StockCode'])

    if stock_code_input:
        # Get historical demand for the selected stock code
        historical_demand = get_historical_demand(data, stock_code_input)
        
        # Forecast demand and get train/test sets
        train, test = forecast_demand(historical_demand)

        # Plotting the historical and forecasted demand
        fig = go.Figure()
        # Historical Demand Plot
        fig.add_trace(go.Scatter(x=historical_demand['InvoiceDate'], y=historical_demand['Quantity'],
                                 mode='lines+markers', name='Historical Demand', line=dict(color='blue')))
        
        # Forecast Demand Plot
        fig.add_trace(go.Scatter(x=test['InvoiceDate'], y=test['Forecast'],
                                 mode='lines+markers', name='Forecasted Demand', line=dict(color='orange')))
        
        # Update layout
        fig.update_layout(title=f'Demand Forecast for {stock_code_input}',
                          xaxis_title='Date',
                          yaxis_title='Quantity Sold',
                          legend_title='Legend')
        
        # Display the plot
        st.plotly_chart(fig)

        # Plotting error distribution histograms
        st.subheader("Error Histogram for Test Dataset")
        fig_error = go.Figure()
        
        # Histogram for forecast errors
        fig_error.add_trace(go.Histogram(x=test['Error'], nbinsx=20, name='Forecast Error',
                                          marker_color='indianred', opacity=0.75))
        
        fig_error.update_layout(title='Error Distribution',
                                xaxis_title='Error',
                                yaxis_title='Frequency',
                                bargap=0.2)

        # Display the error histogram
        st.plotly_chart(fig_error)

if __name__ == "__main__":
    main()
