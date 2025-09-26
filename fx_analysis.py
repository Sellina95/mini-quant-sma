import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# 1. 원/달러 환율 데이터 가져오기 (KRW=X)
df = yf.download("KRW=X", period="1mo", interval="1d")
df = df[['Close']].dropna()

# 2. 최근 1개월 평균 환율
avg_rate = df['Close'].mean()

# 3. 일간 수익률로 변동성(연율화) 계산
returns = df['Close'].pct_change().dropna()
volatility = returns.std() * np.sqrt(252)

df['Close'].plot(title="KRW/USD 최근 1개월 환율")


print("최근 1개월 평균 환율:", round(avg_rate, 2), "KRW/USD")
print("최근 1개월 연율화 변동성:", round(volatility*100, 2), "%")
plt.show()
