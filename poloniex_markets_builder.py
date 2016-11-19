'''
Creates a panel object with the main crypto currencies available in poloniex.
'''
import poloniex 
import pandas as pd
import json
import time

key, secret='YU8DY6RN-4PVXEV7V-8329ZN4L-IS9H6ILV', '5f6192f1eb8151c2b283477b2e3f97a56969ec80d2b4c287bb685a15d679b8b152847feca01c2cc1d57696bc251b1cc9c8c6995f72be04124cbeda97e6e92430'

def get_market_data(candlestick_period = '7200', start = '0', end = time.time()):
        '''connects to poloniex and gets the chart data
        
        '''
        polo = poloniex.Poloniex(key,secret,extend=True)
        market_keys = list(polo.returnOpenOrders('all').keys())

        dd={}
        for x in market_keys:
                dd[x]=pd.DataFrame(polo.returnChartData(x, period, start, end)).set_index('date')

        return pd.Panel(dd)


def compute_indicators(mkts):
        


json.dump(markets,'/home/project/data/Poloniex/poloniex_markets.json')

if __name__ == "__main__":
        
        markets = get_market_data(start = '0') #markets variable panel of 2h-markets from the origin of time until now.

        while True:
                build_markets(start = str())
'''
TODO
1) Keep a file for each market
2) Make strategies with computations on files
3) Keep a file (dictionary) of strategies and performances.
4) Chose a strategy and connect the computer to Poloniex and run it on a small amount.
'''
