import pandas as pd
import numpy as np
import statsmodels.stats.weightstats as weightstats


chat_id = 396317433

def solution(x, y) -> bool: 
    _, res = weightstats.ztest(y, value=np.median(x), alternative='larger')
    return res <= 0.07
