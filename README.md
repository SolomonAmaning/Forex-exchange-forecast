# USD/GBP Exchange Rate Forecast Application

Developed by **Solomon Odum**

## Overview
This application forecasts the USD/GBP exchange rate for up to 10 years. Users can input a custom USD and GBP rate, and the forecast will start from today’s date with the user-defined rate. The application provides interactive visualization features, allowing users to view historical exchange rates, explore forecasted trends, and highlight specific years for detailed rate information.

## Features
1. **Forecast Customization**: 
   - Users can input the current USD and GBP values to personalize the forecast.
   - Forecast period adjustable from 1 to 10 years.
   
2. **Yearly Highlight Functionality**:
   - Select any year using a slider to view:
     - **Historical Years**: Actual closing rate and adjusted rate based on user input.
     - **Future Years**: Forecasted closing rate.
   - Selected year is highlighted on the visualization for better visibility.

3. **Detailed Data Visualization**:
   - Interactive graph shows actual historical data and forecasted trends.
   - Detailed trend and seasonality components are available for further insights.

## How to Use
1. **Input Custom USD and GBP Values**:
   - Enter the current USD and GBP values in the sidebar to adjust the forecast starting point.
   
2. **Adjust Forecast Period**:
   - Use the slider to select the forecast period (1 to 10 years).

3. **Select a Specific Year**:
   - Choose any year in the range to view detailed rate information.
   - The application will display either the actual or forecasted closing rate based on the year chosen.

4. **Toggle Trend and Seasonality**:
   - Enable detailed trend and seasonality views for insights into the forecasted data.

## Example Outputs
- **For Historical Years**: Displays the actual closing rate in USD for GBP, adjusted for the user-defined USD input.
- **For Future Years**: Shows the forecasted closing rate for GBP in the selected year.

## Installation and Setup

### Prerequisites
- Python 3.x
- Required libraries: `streamlit`, `pandas`, `numpy`, `prophet`, `plotly`

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/SolomonAmaning/Forex-exchange-forecast.git
    ```
2. Navigate to the project directory:
    ```bash
    cd forex-exchange-forecast
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Files
- **foreign-exchange-prediction.py**: Main application code for running the Streamlit app.
- **HistoricalPrices.csv**: Historical data for USD/GBP exchange rates.
- **README.md**: Project documentation.

## How It Works

### Data Processing
- The application loads historical data from `HistoricalPrices.csv`.
- Users can input custom USD and GBP values to begin the forecast from today’s date.
- The Prophet model retrains with the updated data and generates forecasts for up to 10 years.

### Interactive Features
- The app highlights the selected year on the plot, displaying detailed rate information:
    - **Historical Years**: Actual closing rate and adjusted rate based on the custom USD value.
    - **Future Years**: Forecasted closing rate.
- Components for trend and seasonality can be toggled to provide more insights.

## Visualization
- An interactive plot displays both historical and forecasted data.
- Hovering over the chart provides date-specific values, and selected years are highlighted for ease of use.

## Example Usage
- Select a forecast period, e.g., 5 years.
- Input current USD and GBP values, e.g., USD = 1.2, GBP = 0.8.
- Choose a year in the sidebar to view closing rates and adjusted rates.
- Enable trend and seasonality components to understand fluctuations and patterns in the forecast.

## Future Improvements
- Adding additional currency pairs for a broader forecast range.
- Enhancing interactive elements with daily, weekly, and monthly breakdowns.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
This project leverages Prophet and Streamlit for forecasting and visualization, respectively, providing an interactive platform for financial analysis.

