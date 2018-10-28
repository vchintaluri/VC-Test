import pandas as pd
import numpy as np

test_list = pd.DataFrame(np.arange(16).reshape(4,4), columns = list('ABCD'))

print test_list.head()