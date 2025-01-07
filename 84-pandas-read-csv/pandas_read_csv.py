import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())


import pandas as pd
df = pd.read_csv('data.csv')
print(df)


import pandas as pd
print(pd.options.display.max_rows)


import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)
