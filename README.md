# Mini Quant Backtest – SMA Crossover (1-day build)

이 프로젝트는 **SMA(이동평균선) 크로스오버 전략**을 아주 간단한 파이썬 코드로 백테스트하는 예시입니다.  
지원서/면접용으로 “파이썬+금융데이터 다룰 줄 안다”를 보여주는 **작은 증빙** 역할을 합니다.

## 1) 실행 순서 (왜 이렇게 하나요?)
```bash
# (선택) 가상환경 만들기: 내 컴퓨터의 다른 파이썬 환경과 섞이지 않게 '독립 공간'을 만드는 단계
python -m venv .venv && source .venv/bin/activate   # (Windows: .venv\Scripts\activate)

# 필요한 패키지 설치: 아래 requirements.txt에 적힌 버전으로 설치 → 실행환경 '재현성' 보장
pip install -r requirements.txt

# ① 온라인 데이터 사용(yfinance가 야후파이낸스에서 가격을 받아옴)
python strategy_sma.py --ticker SPY --start 2015-01-01 --end 2025-09-25 --fast 50 --slow 200

# ② 오프라인 CSV 사용(회사 보안환경 등 외부접속 제한일 때) - sample_prices.csv 같은 로컬 파일로 테스트
python strategy_sma.py --csv sample_prices.csv --date_col date --price_col close --fast 20 --slow 50
