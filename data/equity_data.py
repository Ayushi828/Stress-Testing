import pandas as pd
import yfinance as yf


def get_equity_prices(start, end, eqt):
  adj_close_price_eq = pd.DataFrame()
    
  for eq in equity:
    eq_data_df = yf.download(equity, start = start, end = end)
    
    if not eq_data_df.empty:
      adj_close_price_eq[equity] = eq_data_df['Close']
    else:
      print("Data isn't available for equitites")
      
  return adj_close_price_eq


    


