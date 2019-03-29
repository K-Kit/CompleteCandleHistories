import asyncio
import os
import sys
from pprint import pprint
import time
import ccxt.async_support as ccxt  # noqa: E402
import pandas as pd
import sys
sys.setrecursionlimit(99999999)
import os
import psutil
process = psutil.Process(os.getpid())
import models.Candle
from sqlalchemy.orm import Session



if __name__ == '__main__':
    import database
    from data_loaders.BinanceDataLoader import BinanceDataLoader
    dl = BinanceDataLoader('binance')
    database.init_db()
    asyncio.run(dl.load_many_candle_histories())
    from models.Candle import Candle
    print(len(database.db_session.query(Candle).all()))
