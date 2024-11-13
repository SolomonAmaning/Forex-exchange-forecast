# Forex Exchange Rate Forecasting

This project uses a machine learning model to forecast the USD/GBP exchange rate over a specified period. It includes a Streamlit app for user interaction, allowing users to input a current USD rate and visualize projected GBP rates for up to 10 years.

## Project Structure

- `foreign_exchange_prediction.py`: The main application code for the Streamlit dashboard.
- `HistoricalPrices.csv`: The dataset of historical exchange rates used for model training.
- `README.md`: Project documentation.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/...
    cd 
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the Streamlit app, run:
```bash
streamlit run foreign_exchange_prediction.py
