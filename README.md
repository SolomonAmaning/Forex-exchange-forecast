# USD/GBP Forex-exchange-forecast
An interactive application that forecasts the USD/GBP exchange rate using historical data and Prophet for time-series modeling. Users can specify the forecast period, enter a current USD rate, and see projected GBP rates over time.

## Developed by Solomon Odum.

<!-- Table of Contents
- Project Overview
- Features
- Requirements
- Setup Instructions
- Usage
- Application Demo
- Customization
- Acknowledgments -->

## Project Overview
This application leverages the Facebook Prophet model to forecast the USD/GBP exchange rate for up to 10 years based on historical data. Users can adjust the forecast period and input a specific USD rate to see the projected GBP values over the chosen period.

The interactive dashboard, built with Streamlit, provides a dynamic visualization of the exchange rate forecast, including components for trends and seasonality.

## Features
- **Forecast Adjustment**: Users can set the forecast period up to 10 years.
- **Exchange Rate Simulation**: Input a current USD rate to adjust the forecasted GBP values.
- **Interactive Visualization**: View actual vs. forecasted exchange rates with hover functionality.
- **Trend and Seasonality Insights**: Option to display underlying trend and seasonality components in the forecast.

## Requirements
- Python 3.8 or higher
- The following Python libraries:
  - `streamlit`
  - `pandas`
  - `numpy`
  - `prophet`
  - `plotly`

**You can install the required libraries using:**

```bash
pip install streamlit pandas numpy prophet plotly
