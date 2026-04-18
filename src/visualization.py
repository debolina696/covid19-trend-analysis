import plotly.express as px
import plotly.graph_objects as go

def plot_confirmed_trend(daily_df):
    fig = px.line(
        daily_df,
        x='date',
        y='confirmed',
        title="Global COVID-19 Confirmed Cases Over Time"
    )

    return fig


def plot_combined_trends(daily_df):

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=daily_df['date'],
        y=daily_df['confirmed'],
        mode='lines',
        name='Confirmed'
    ))

    fig.add_trace(go.Scatter(
        x=daily_df['date'],
        y=daily_df['deaths'],
        mode='lines',
        name='Deaths'
    ))

    fig.add_trace(go.Scatter(
        x=daily_df['date'],
        y=daily_df['recovered'],
        mode='lines',
        name='Recovered'
    ))

    fig.add_trace(go.Scatter(
        x=daily_df['date'],
        y=daily_df['active'],
        mode='lines',
        name='Active'
    ))

    fig.update_layout(
        title="Global COVID-19 Trends Overview",
        xaxis_title="Date",
        yaxis_title="Cases"
    )

    return fig
