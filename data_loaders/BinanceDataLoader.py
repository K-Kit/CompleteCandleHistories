from data_loaders.GenericExchangeDataLoader import GenericExchangeDataLoader, time, session, Candle, List
from typing import List
import asyncio

class BinanceDataLoader(GenericExchangeDataLoader):

    def __init__(self,candle_intervals: List = None):
        super().__init__( 'binance', candle_intervals=candle_intervals)

    async def load_historical_candles(self, symbol:str, interval:str, endtime=None):
        if self.client is None:
            self.initialize_client()
        if endtime is None:
            endtime = int(time.time() * 1000)

        candles = await self.client.fetch_ohlcv(symbol, interval, params={"endTime": endtime})

        for candle in candles:
            session.add(Candle(
                symbol=symbol,
                interval='1d',
                start_time=candle[0],
                open=candle[1],
                high=candle[2],
                low=candle[3],
                close=candle[4],
                volume=candle[5]
            ))
        session.commit()
        # returns an empty list when history not in range
        if candles == []:
            return
        else:
            # candles[0][0] is the oldest candle in the list
            return await self.load_historical_candles(symbol, interval, endtime=candles[0][0]-1)


