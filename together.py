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

df = pd.DataFrame([address['date-time'], address['address-count'], blocksize['blocksize'], etherprice['price'],
      hashrate['global-hashrate'], marketcap['market-cap-value'], tx['amt-transactions-on-day']]).transpose()

df.to_csv('all_data.csv', index=False)
