# USD/GBP Forex-exchange-forecast
This project was done to forecast USD/GBP closing rate for the next 10 years i.e 2033 using 2003 - June 14, 2023 historical data.
The study employed LSTM for this time series analysis and forecast
USD/GBP Exchange Rate Forecast
An interactive application that forecasts the USD/GBP exchange rate using historical data and Prophet for time-series modeling. Users can specify the forecast period, enter a current USD rate, and see projected GBP rates over time.

Developed by Solomon Odum.

Table of Contents
Project Overview
Features
Requirements
Setup Instructions
Usage
Application Demo
Customization
Acknowledgments
Project Overview
This application leverages the Facebook Prophet model to forecast the USD/GBP exchange rate for up to 10 years based on historical data. Users can adjust the forecast period and input a specific USD rate to see the projected GBP values over the chosen period.

The interactive dashboard, built with Streamlit, provides a dynamic visualization of the exchange rate forecast, including components for trends and seasonality.

Features
Forecast Adjustment: Users can set the forecast period up to 10 years.
Exchange Rate Simulation: Input a current USD rate to adjust the forecasted GBP values.
Interactive Visualization: View actual vs. forecasted exchange rates with hover functionality.
Trend and Seasonality Insights: Option to display underlying trend and seasonality components in the forecast.
Requirements
Python 3.8 or higher
The following Python libraries:
streamlit
pandas
numpy
prophet
plotly
You can install the required libraries using:

bash
Copy code
pip install streamlit pandas numpy prophet plotly
Setup Instructions
Clone the repository:

bash
Copy code
git clone <repository_url>
cd usd_gbp_forecast
Add Historical Data:

Place your historical exchange rate data file in CSV format in the root folder and name it HistoricalPrices.csv.
The CSV should have two columns: Date (dates of exchange rates) and Close (USD/GBP closing exchange rate).
Run the Application:

bash
Copy code
streamlit run app.py
Access the Application:

The app will open in your browser (usually at http://localhost:8501).
Usage
Select Forecast Period: Use the slider in the sidebar to set the forecast period (1 to 10 years).
Enter USD Rate: Input the current USD rate in the sidebar to adjust projected GBP values.
View Forecast: The main plot shows actual vs. forecasted values for the specified period.
Display Trend and Seasonality: Check the box below the plot to view additional trend and seasonality components if available.
Application Demo

In the visualization:

Blue Line: Represents historical USD/GBP exchange rate data.
Orange Line: Shows the forecasted exchange rate over the selected period.
Customization
Adjust Forecast Model: Modify the train_model function in app.py to customize Prophet parameters.
Data Source: Replace HistoricalPrices.csv with any other dataset, ensuring it has the required columns (Date, Close).
Forecast Period: Default forecast period is 5 years. Adjust this in the code or UI settings as needed.
Acknowledgments
Facebook Prophet: For time-series modeling.
Streamlit: For building an interactive and user-friendly interface.
Plotly: For dynamic data visualizations.
