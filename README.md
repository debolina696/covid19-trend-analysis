# 🦠 COVID-19 Trend Analysis & Forecasting

## 📌 Project Overview

This project analyzes global COVID-19 data to understand trends in confirmed cases, deaths, recoveries, and active cases.  
It also uses time-series forecasting to predict future confirmed cases using the Prophet model.

The project follows an industry-style modular structure using Python and Jupyter Notebook.

---

## 🎯 Objectives

- Clean and preprocess COVID-19 dataset
- Perform daily global aggregation
- Visualize trends of confirmed, deaths, recovered, and active cases
- Forecast future COVID-19 confirmed cases
- Build reusable modular code using Python scripts
- Generate professional outputs for analysis

---

## 📂 Project Structure

covid19_trend_analysis/
│
├── data/
│ ├── raw/ # Raw dataset
│ ├── processed/ # Cleaned & aggregated data
│
├── notebooks/
│ └── covid_analysis.ipynb # Main analysis notebook
│
├── outputs/
│ ├── plots/ # Visualization outputs
│ ├── predictions/ # Forecast outputs
│
├── src/
│ ├── data_loader.py # Data loading functions
│ ├── preprocessing.py # Data cleaning functions
│ ├── visualization.py # Plot functions
│ ├── forecasting.py # Forecast model functions
│
├── requirements.txt
├── README.md
├── .gitignore

---

## 📊 Dataset Information

The dataset contains global COVID-19 data with the following columns:

- Province/State
- Country/Region
- Latitude
- Longitude
- Date
- Confirmed Cases
- Death Cases
- Recovered Cases
- Active Cases
- WHO Region

Source: Public COVID-19 dataset.

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Prophet
- Matplotlib
- Jupyter Notebook

---

## 📈 Key Features

✔ Data Cleaning & Preprocessing  
✔ Daily Global Aggregation  
✔ Trend Visualization  
✔ Time-Series Forecasting  
✔ Modular Python Code Structure  
✔ Professional Output Storage  

---

## 📊 Visualizations Created

- Confirmed Cases Trend
- Death Cases Trend
- Recovery Trend
- Active Cases Trend
- Combined Global Trend Visualization

---

## 🔮 Forecasting

The Prophet model was used to:

- Train on historical confirmed cases
- Predict future confirmed cases
- Generate 7-day future forecast
- Visualize trend and seasonality components

---

## 📌 Key Insights

- Confirmed cases show continuous growth trend.
- Recovery cases increase significantly over time.
- Active cases fluctuate based on recovery and death rates.
- Forecast results indicate short-term increase in confirmed cases.

---

## ▶️ How to Run the Project

1. Clone repository

git clone <your-repository-link>


2. Install dependencies
3. pip install -r requirements.txt

3. Run Jupyter Notebook
4. jupyter notebook
5.  Open:
6.  notebooks/covid_analysis.ipynb
7.  
Run all cells to reproduce results.

---

## 📁 Outputs Generated

- Cleaned dataset
- Daily aggregated dataset
- Interactive trend plots
- Forecast prediction results
- Forecast visualization charts

---

## 📌 Future Improvements

- Country-level analysis
- Region-wise comparison
- Interactive dashboard integration
- Machine learning model comparison

---

## 👤 Author

**Debolina Sorkhel**

Data Analyst | Python | Data Visualization | Forecasting
















