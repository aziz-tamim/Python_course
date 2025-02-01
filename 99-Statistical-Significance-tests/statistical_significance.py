import numpy as np
from scipy.stats import ttest_ind
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1, v2)
print(res)


import numpy as np
from scipy.stats import ttest_ind
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1, v2).pvalue
print(res)


import numpy as np
from scipy.stats import kstest
v = np.random.normal(size=100)
res = kstest(v, 'norm')
print(res)


import numpy as np
from scipy.stats import describe
v = np.random.normal(size=100)
res = describe(v)
print(res)


import numpy as np
from scipy.stats import skew, kurtosis
v = np.random.normal(size=100)
print(skew(v))
print(kurtosis(v))
print(kurtosis(v))


import numpy as np
from scipy.stats import normaltest
v = np.random.normal(size=100)
print(normaltest(v))
