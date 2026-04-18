import pandas as pd

def clean_data(df):
    """
    Clean COVID dataset
    """

    # Clean column names
    df.columns = df.columns.str.strip() \
                           .str.replace("/", "_") \
                           .str.replace(" ", "_") \
                           .str.lower()

    # Convert date column
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)

    # Fill missing province/state
    df['province_state'] = df['province_state'].fillna("Unknown")

    # Remove duplicates
    df = df.drop_duplicates()

    return df


def create_daily_data(df):
    """
    Create daily aggregated dataset
    """

    daily_df = df.groupby('date')[[
        'confirmed',
        'deaths',
        'recovered',
        'active'
    ]].sum().reset_index()

    return daily_df


    