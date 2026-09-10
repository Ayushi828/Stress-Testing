import numpy as np

def calculate_var_eq(close_price, w1)
  returns = np.log(close_price/ close_price.shift(1))
  returns = returns.dropna()
  
