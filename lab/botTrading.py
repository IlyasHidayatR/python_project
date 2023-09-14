import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import talib
import python_utils as utils

def main():
    ticker_data = utils.get_data(ticker, data_period, interval)

    if len(ticker_data) != 0:
        ticker_data['sar'] = talib.SAR(ticker_data['High'], ticker_data['Low'], acceleration=0.02, maximum=0.2)
        ticker_data['atr'] = talib.ATR(ticker_data['High'], ticker_data['Low'], ticker_data['Close'], timeperiod=14)
        ticker_data.dropna(inplace=True)

        trade_data = utils.create_trade_data(ticker_data, rr, str_mult)
        trade_data = utils.simulate_trade(trade_data, share_amount, initial_capital)
        trade_data_df = pd.DataFrame(trade_data)
        win_rate, sim_result_df, sim_fig, acum_profit_fig = utils.get_sim_summary(trade_data_df['p/1'].tolist(), share_amount, initial_capital)


if __name__ == '__main__':
    ticker =  st.sidebar.text_input('Ticker', value='AAPL', max_chars=5)
    is_train = st.sidebar.checkbox('Train', value=True)
    data_period = st.sidebar.text_input('Data Period', value='1y', max_chars=3)
    interval = st.sidebar.radio('Interval', ['1d', '1wk', '1mo'], index=0)
    rr = st.sidebar.slider('Risk Reward Ratio', min_value=1.0, max_value=10.0, value=2.0, step=0.5)
    str_mult = st.sidebar.slider('Stop Loss Multiplier', min_value=1.0, max_value=10.0, value=2.0, step=0.5)
    share_amount = st.sidebar.text_input('Share Amount', value='100', max_chars=5)
    initial_capital = st.sidebar.text_input('Initial Capital', value='10000', max_chars=10)

    st.header('Bot Trading')
    st.subheader('Data')
    main()