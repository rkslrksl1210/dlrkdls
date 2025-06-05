import streamlit as st
st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHdyeXkzdmE5djZ5ZDBleHVnNXF4dXV5czc4aWQwejV2NHZoM29idCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriO0OEd9QIDdllqo/giphy.gif")


import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime, timedelta

# 페이지 설정
st.set_page_config(page_title="Global Top 10 Market Cap Stocks", layout="wide")
st.title("📈 글로벌 시가총액 TOP 10 기업의 10년 주가 변화")

# 시가총액 기준 글로벌 Top 10 (2024년 기준으로 업데이트 가능)
top10_tickers = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Saudi Aramco': '2222.SR',
    'Alphabet (Google)': 'GOOGL',
    'Amazon': 'AMZN',
    'Nvidia': 'NVDA',
    'Berkshire Hathaway': 'BRK-B',
    'Meta Platforms': 'META',
    'TSMC': 'TSM',
    'Eli Lilly': 'LLY'
}

# 기간 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365 * 10)

# 데이터 수집
@st.cache_data
def fetch_data(tickers):
    data = {}
    for name, symbol in tickers.items():
        df = yf.download(symbol, start=start_date, end=end_date)
        if not df.empty:
            df['Name'] = name
            df['Ticker'] = symbol
            data[name] = df
    return data

with st.spinner("데이터 불러오는 중..."):
    stock_data = fetch_data(top10_tickers)

# Plotly 시각화
fig = go.Figure()

for name, df in stock_data.items():
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['Adj Close'],
        mode='lines',
        name=name
    ))

fig.update_layout(
    title="글로벌 시가총액 TOP 10 기업의 Adjusted Close (지난 10년)",
    xaxis_title="날짜",
    yaxis_title="Adjusted Close 가격 (USD)",
    legend_title="기업명",
    template="plotly_dark",
    height=600
)

st.plotly_chart(fig, use_container_width=True)
