import os

import pandas as pd

from common.const import RESOURCES_PATH
from common.quotes import client

HFQ_PATH = os.path.join(RESOURCES_PATH, 'hfq')


def get_hfq_kline(symbol, ts=None):
    csv_file = os.path.join(HFQ_PATH, f'{symbol}.csv')
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file, parse_dates=['date'], index_col='date')
        if ts and df.iloc[-1].name < ts:
            df = client.k(symbol=symbol, begin="1990-01-01", end="2100-01-01", adjust='hfq')
            df.to_csv(csv_file, index=False)
    else:
        df = client.k(symbol=symbol, begin="1990-01-01", end="2100-01-01", adjust='hfq')
        df.to_csv(csv_file, index=False)

    return df



