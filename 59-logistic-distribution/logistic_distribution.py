from numpy import random
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')
plt.show()

