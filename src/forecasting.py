from prophet import Prophet
import pandas as pd

def prepare_prophet_data(daily_df):
    """
    Prepare dataset for Prophet forecasting
    """

    prophet_df = daily_df[['date', 'confirmed']].copy()

    prophet_df.rename(
        columns={
            'date': 'ds',
            'confirmed': 'y'
        },
        inplace=True
    )

    return prophet_df


def train_prophet_model(prophet_df):
    """
    Train Prophet model
    """

    model = Prophet()

    model.fit(prophet_df)

    return model


def make_forecast(model, periods=7):
    """
    Generate future predictions
    """

    future = model.make_future_dataframe(
        periods=periods
    )

    forecast = model.predict(future)

    return forecast


 