from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, BigInteger, INTEGER, FLOAT
from sqlalchemy.orm import backref, relationship

from database import Base


class Candle(Base):
    __tablename__ = 'candle'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    symbol = Column(String)
    interval = Column(String)
    start_time = Column(BigInteger)
    exchange = Column(String)
    open = Column(FLOAT)
    high = Column(FLOAT)
    low = Column(FLOAT)
    close = Column(FLOAT)
    volume = Column(FLOAT)
