import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

from collections import defaultdict
from pprint import pprint

def histogram(results):
    counts = defaultdict(lambda : 0)
    for trial, trial_measurements in results.items():
        counts[tuple(trial_measurements.values())] += 1
    #pprint(counts)
    predata = defaultdict(list)
    for k, v in counts.items():
        measured = ''.join(map(str, tuple(k)))
        for _ in range(v):
            predata['measurement'].append(measured)
        #predata['count'].append(v)
    data = pd.DataFrame(predata)
    print(data)
    sns.countplot(x='measurement', data=data)
    plt.show()
