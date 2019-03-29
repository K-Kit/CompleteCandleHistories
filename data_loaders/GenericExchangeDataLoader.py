from typing import List
import ccxt.async_support as ccxt
import time
from database import db_session as session
from models.Candle import Candle
import asyncio

class GenericExchangeDataLoader:
    client = None

    def __init__(self, exchage_id: str, candle_intervals: List = None):
        self.exchange_id = exchage_id
        self.candle_intervals = candle_intervals
        self.client_class = getattr(ccxt, exchage_id)
        self.loop = asyncio.get_event_loop()

    def initialize_client(self):
        self.client = self.client_class({'enableRateLimit': True})

    async def load_historical_candles(self, symbol, endtime=None):
        raise NotImplementedError()

    async def load_many_candle_histories(self):
        tasks = [
            self.load_historical_candles('ADA/ETH', '1d'),
            self.load_historical_candles('ADA/BTC', '1d')
            ]
        await asyncio.gather(*tasks)
