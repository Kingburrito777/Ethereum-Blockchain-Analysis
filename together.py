# a script to piece all data sets together

import numpy as np
import pandas as pd

# read files
address = pd.read_csv('./input/address.csv')
blocksize = pd.read_csv('./input/blocksize.csv')
etherprice = pd.read_csv('./input/etherprice.csv')
hashrate = pd.read_csv('./input/hashrate.csv')
marketcap = pd.read_csv('./input/marketcap.csv')
tx = pd.read_csv('./input/tx.csv')
supply = pd.read_csv('./input/ethersupplygrowth.csv')

df = pd.DataFrame([address['timestamp'], address['total_addresses'], blocksize['blocksize'], etherprice['price_USD'],
      hashrate['hashrate'], supply['total_eth_growth'] ,marketcap['market-cap-value'], tx['transactions']]).transpose()

df.to_csv('./input/all_data.csv', index=False)
