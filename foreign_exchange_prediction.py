import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
import plotly.graph_objects as go
from datetime import timedelta

# Loading the data from CSV and formatting date columns
@st.cache_data
def load_data():
    df = pd.read_csv('HistoricalPrices.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)
    return df

# Training the Prophet model on the loaded data
@st.cache_resource
def train_model(df):
    model = Prophet()
    model.fit(df)
    return model

# Generating the forecast based on the specified period
def generate_forecast(model, years):
    try:
        # Attempting to generate a forecast for the full 10-year period (3650 days)
        future = model.make_future_dataframe(periods=years * 365)
        forecast = model.predict(future)
    except Exception as e:
        # Falling back to a shorter forecast period (e.g., 5 years) if an issue arises
        fallback_years = 5
        st.write(f"Warning: Forecast period limited to {fallback_years} years due to model constraints.")
        future = model.make_future_dataframe(periods=fallback_years * 365)
        forecast = model.predict(future)
    return forecast

# Setting up the Streamlit application with a title and description
st.title('USD/GBP Exchange Rate Forecast')
st.write('Developed by Solomon Odum')

# Displaying forecast options on the sidebar
st.sidebar.header("Forecast Options")
years = st.sidebar.slider('Select forecast period (years):', 1, 10, 5)
usd_input = st.sidebar.number_input('Enter current USD rate:', min_value=0.1, value=1.0, step=0.1)

# Loading the data and training the model
df = load_data()
model = train_model(df)

# Generating the forecast with user-specified parameters
forecast = generate_forecast(model, years)

# Adjusting forecast values based on the user-provided USD rate
forecast['yhat_adjusted'] = forecast['yhat'] * usd_input

# Initializing a plotly figure for the forecast visualization
fig = go.Figure()

# Adding a trace for the actual historical data
fig.add_trace(go.Scatter(
    x=df['ds'],
    y=df['y'],
    mode='lines',
    name='Actual Data',
    line=dict(color='royalblue')
))

# Adding a trace for the forecasted data based on the specified period
forecast_dates = forecast[forecast['ds'] > df['ds'].max()]['ds']
forecast_values = forecast[forecast['ds'] > df['ds'].max()]['yhat_adjusted']
fig.add_trace(go.Scatter(
    x=forecast_dates,
    y=forecast_values,
    mode='lines',
    name='Forecast',
    line=dict(color='orange')
))

# Updating layout properties and extending the x-axis to cover the full forecast range
end_date_manual = pd.to_datetime(df['ds'].max()) + timedelta(days=years * 365)
fig.update_layout(
    title=f'USD/GBP Exchange Rate - Actual vs Forecast ({years} Year Forecast)',
    xaxis=dict(
        title='Date',
        range=[df['ds'].min(), end_date_manual],
        tickformat="%Y",
        dtick="M12"
    ),
    yaxis=dict(title='Exchange Rate (Adjusted)'),
    hovermode='x'
)

# Displaying the forecast plot in Streamlit
st.plotly_chart(fig)

# Displaying trend and seasonality components based on user selection
st.subheader("Trend and Seasonality Components")
if st.checkbox("Show trend and seasonality components"):
    # Plotting the trend component
    trend_fig = go.Figure()
    trend_fig.add_trace(go.Scatter(
        x=forecast['ds'],
        y=forecast['trend'],
        mode='lines',
        name='Trend',
        line=dict(color='green')
    ))
    trend_fig.update_layout(title="Trend Component", xaxis_title="Date", yaxis_title="Trend")
    st.plotly_chart(trend_fig)

    # Plotting the yearly seasonality component if it exists in the forecast data
    if 'yearly' in forecast.columns:
        yearly_seasonality_fig = go.Figure()
        yearly_seasonality_fig.add_trace(go.Scatter(
            x=forecast['ds'],
            y=forecast['yearly'],
            mode='lines',
            name='Yearly Seasonality',
            line=dict(color='purple')
        ))
        yearly_seasonality_fig.update_layout(title="Yearly Seasonality", xaxis_title="Date", yaxis_title="Yearly Seasonality")
        st.plotly_chart(yearly_seasonality_fig)
    else:
        st.write("Yearly seasonality data not available for this forecast.")
