from binance.client import Client
from binance.enums import *
import time
import logging

# Configure logging to console and file
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', handlers=[
    logging.FileHandler("trading_bot.log"),
    logging.StreamHandler()
])

class BinanceTradingBot:
    def __init__(self, api_key, api_secret, symbol='BTCUSDT', trade_quantity=0.001):
        self.client = Client(api_key, api_secret)
        self.symbol = symbol
        self.trade_quantity = trade_quantity
        logging.info(f"Initialized bot for {symbol} with qty {trade_quantity}")

    def get_current_price(self):
        ticker = self.client.get_symbol_ticker(symbol=self.symbol)
        price = float(ticker['price'])
        logging.info(f"Current price for {self.symbol}: {price}")
        return price

    def place_order(self, side, quantity):
        try:
            order = self.client.create_order(
                symbol=self.symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"Order placed: {side} {quantity} {self.symbol}")
            return order
        except Exception as e:
            logging.error(f"Failed to place order: {e}")
            return None

    def simple_strategy(self):
        # Simple demo strategy:
        # If price is below a threshold, buy; if above, sell
        price = self.get_current_price()
        buy_threshold = 25000  # Example threshold
        sell_threshold = 30000

        if price < buy_threshold:
            logging.info(f"Price {price} below {buy_threshold}, BUYING")
            self.place_order(SIDE_BUY, self.trade_quantity)
        elif price > sell_threshold:
            logging.info(f"Price {price} above {sell_threshold}, SELLING")
            self.place_order(SIDE_SELL, self.trade_quantity)
        else:
            logging.info(f"Price {price} in neutral zone, holding position.")

    def run(self):
        logging.info("Starting trading bot loop...")
        while True:
            self.simple_strategy()
            time.sleep(60)  # Check every minute

if __name__ == "__main__":
    import os

    API_KEY = os.getenv("BINANCE_API_KEY")
    API_SECRET = os.getenv("BINANCE_API_SECRET")

    if not API_KEY or not API_SECRET:
        logging.error("Please set BINANCE_API_KEY and BINANCE_API_SECRET environment variables.")
        exit(1)

    bot = BinanceTradingBot(API_KEY, API_SECRET)
    bot.run()

