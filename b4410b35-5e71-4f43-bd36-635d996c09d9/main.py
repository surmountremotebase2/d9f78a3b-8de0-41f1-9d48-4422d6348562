from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import RSI
from surmount.data import Asset

class TradingStrategy(Strategy):
    def __init__(self):
        # Asset ticker symbol
        self.tickers = ["AAPL"]
    
    @property
    def interval(self):
        # Using daily data for our analysis
        return "1day"

    @property
    def assets(self):
        # Define the assets that this strategy is interested in
        return self.tickers

    def run(self, data):
        # Initialize an empty allocation
        allocation_dict = {ticker: 0 for ticker in self.tickers}
        
        # Calculate the RSI for AAPL
        rsi_values = RSI("AAPL", data["ohlcv"], length=14)  # Using a standard 14-day RSI

        if not rsi_values:
            # Return empty allocation if RSI values are unavailable
            return TargetAllocation(allocation_dict)

        # Get the latest RSI value
        current_rsi = rsi_values[-1]

        # Determine trade signal based on RSI
        if current_rsi > 70:
            # RSI > 70 could indicate that AAPL is overbought, potential sell signal, but we only adjust allocation to 0 here
            allocation_dict["AAPL"] = 0  # Adjust allocation for selling or neutral stance
        elif current_rsi < 30:
            # RSI < 30 could indicate that AAPL is oversold, potential buy signal
            allocation_dict["AAPL"] = 1  # Full allocation towards buying

        # Return the target allocation based on RSI analysis
        return TargetAllocation(allocation_dict)