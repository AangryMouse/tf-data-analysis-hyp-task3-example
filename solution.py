import pandas as pd
import numpy as np
import statsmodels.stats.weightstats as w


chat_id = 396317433

def solution(x, y) -> bool: 
    _, res = w.ztest(y, value=np.median(x), alternative='larger')
    return res <= 0.07
