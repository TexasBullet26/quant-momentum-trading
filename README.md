# Quant Momentum Trading System — V3

Massive.com market-data layer + quantitative momentum research engine + Alpaca/Coinbase execution adapters.

**Safety:** paper trading is the default; live trading is disabled by default; hard max position notional defaults to $250.

## Architecture

Massive -> normalized data -> momentum factors -> cross-sectional ranking -> portfolio construction -> risk engine -> execution router -> Alpaca/Coinbase.

## Momentum model

Composite score:
- 35% 12-1 momentum
- 25% 6-1 momentum
- 15% 3-1 momentum
- 10% relative strength vs benchmark
- 10% trend strength
- 5% volatility-adjusted momentum

Signals are shifted in backtests so the close used to calculate a signal cannot also be used to receive that day's return.

## Install

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add credentials.

## Demo backtest

```bash
python scripts/backtest_demo.py
```

## CLI for your OHLCV universe

CSV columns: `date,symbol,open,high,low,close,volume`

```bash
python -m app.cli --csv universe.csv
```

## API

```bash
uvicorn app.api.main:app --reload
```

Endpoints: `/health`, `/config`.

## Providers

Massive is the primary research/market-data provider. It supports REST, WebSockets and bulk historical files across multiple asset classes. Alpaca is the primary equities execution adapter. Coinbase is retained as the crypto execution adapter.

Official docs:
- https://www.massive.com/docs
- https://docs.alpaca.markets/
- https://docs.cdp.coinbase.com/advanced-trade/docs/welcome

## Before live trading

Validate data quality, corporate actions, universe survivorship, slippage, commissions, borrow/short constraints, liquidity, market hours, order behavior, and out-of-sample/walk-forward results. Do not treat backtest results as expected future returns.
