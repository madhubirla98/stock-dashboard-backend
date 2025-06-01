import yfinance as yf
import logging
from typing import List
from cachetools import TTLCache, cached
from cachetools.keys import hashkey

# Set up logging for debugging purposes
logger = logging.getLogger(__name__)

# Create an in-memory cache to store results for 10 minutes (600 seconds)
stock_cache = TTLCache(maxsize=100, ttl=600)

class StockService:
    @staticmethod
    def get_interval_for_timeframe(timeframe: str) -> str:
        """
        Maps user-defined timeframe strings to yfinance-supported interval strings.
        
        Returns:
            A valid interval string that yfinance accepts.
        """
        return {
            "1D": "5m",     # Intraday for single-day view
            "1W": "60m",    # Hourly data for 1 week
            "1M": "1d",     # Daily data for 1 month
            "3M": "1d",     # Daily data for 3 months
            "1Y": "1d",     # Daily data for 1 year
            "YTD": "1d",    # Year-To-Date daily data
            "MTD": "1d",    # Month-To-Date daily data
        }.get(timeframe, "1d")  # Default to daily if unrecognized

    @staticmethod
    @cached(
        stock_cache,
        key=lambda tickers, start, end, timeframe: hashkey(tuple(tickers), start, end, timeframe)
    )
    def fetch_stock_data(tickers, start_date, end_date, timeframe='1d'):
        """
        Fetches historical stock data for one or more tickers from Yahoo Finance,
        using caching to reduce redundant API calls.

        Args:
            tickers (list): List of stock ticker symbols (e.g., ["AAPL", "GOOGL"]).
            start_date (str): Start date for fetching data (e.g., "2024-01-01").
            end_date (str): End date for fetching data (e.g., "2024-05-30").
            timeframe (str): Timeframe string to determine the data granularity.

        Returns:
            dict: A dictionary with each ticker as the key and a list of daily data entries.
        """
        # Determine appropriate interval based on the given timeframe
        interval = StockService.get_interval_for_timeframe(timeframe)

        # Download the stock data from Yahoo Finance
        raw_data = yf.download(
            tickers,
            start=start_date,
            end=end_date,
            interval=interval,
            group_by='ticker',
            progress=False
        )

        data = {}

        for ticker in tickers:
            # Check if the ticker exists in the downloaded data
            if ticker not in raw_data.columns.levels[0]:
                data[ticker] = []  # Return empty list for missing data
                continue

            # Extract the DataFrame for the specific ticker
            df = raw_data[ticker]
            ticker_data = []

            # Convert each row to a dictionary with native Python types
            for idx, row in df.iterrows():
                day = {'Date': idx.strftime('%Y-%m-%d')}
                for col in df.columns:
                    val = row[col]
                    if hasattr(val, 'item'):  # Convert numpy data types to native Python types
                        val = val.item()
                    day[col] = val
                ticker_data.append(day)

            # Store the formatted data for the ticker
            data[ticker] = ticker_data

        return data
