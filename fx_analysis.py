import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. 환율 데이터 다운로드 (최근 1개월, 원/달러 환율)
df = yf.download("KRW=X", period="1mo", interval="1d")
df = df[['Close']].dropna()
df.rename(columns={'Close': 'KRW/USD'}, inplace=True)

# 2. 평균 환율
avg_rate = df['KRW/USD'].mean()

# 3. 변동성(연율화)
returns = df['KRW/USD'].pct_change().dropna()
volatility = returns.std() * np.sqrt(252)

# 4. 결과 출력
print("최근 1개월 평균 환율:", round(avg_rate, 2), "KRW/USD")
print("최근 1개월 연율화 변동성:", round(volatility*100, 2), "%")

# 5. 데이터 프레임에 수익률 컬럼 추가
df['Daily Return'] = returns
print("\n📊 최근 5일 데이터")
print(df.tail())

# 6. 그래프 시각화
plt.figure(figsize=(10,5))
plt.plot(df.index, df['KRW/USD'], label="KRW/USD 환율", color="blue")
plt.title("최근 1개월 원/달러 환율")
plt.xlabel("날짜")
plt.ylabel("KRW per USD")
plt.legend()
plt.grid(True)
plt.show()
