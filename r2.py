
from sklearn.metrics import r2_score
import pandas as pd

df = pd.read_csv('/Users/jiabozhu/Desktop/20221208allSitenew.csv')
y_true = [1, 2, 4]
y_pred = [1.3, 2.5, 3.7]
r2_score(y_true, y_pred)