import os

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(usecwd=True))

config = DEFAULT_CONFIG.copy()
config["llm_provider"] = os.getenv("LLM_PROVIDER", "openai")
config["deep_think_llm"] = os.getenv("DEEP_THINK_LLM", "gpt-5.4-mini")
config["quick_think_llm"] = os.getenv("QUICK_THINK_LLM", "gpt-5.4-mini")
config["max_debate_rounds"] = int(os.getenv("MAX_DEBATE_ROUNDS", "1"))
config["data_vendors"] = {
    "core_stock_apis": os.getenv("CORE_STOCK_APIS", "yfinance"),
    "technical_indicators": os.getenv("TECHNICAL_INDICATORS", "yfinance"),
    "fundamental_data": os.getenv("FUNDAMENTAL_DATA", "yfinance"),
    "news_data": os.getenv("NEWS_DATA", "yfinance"),
}

ta = TradingAgentsGraph(debug=True, config=config)

_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)
