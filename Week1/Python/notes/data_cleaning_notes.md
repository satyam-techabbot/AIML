# Data Cleaning

## Dropping Columns in a DataFrame
```
df.drop(labels=3) # row
df.drop(columns=to_drop, inplace=True) # column
```

## Changing the Index of a DataFrame
```
df = df.set_index('calories') # Set the DataFrame index using existing columns.
```

## Cleaning the Entire Dataset Using the map Function

- map() : used to apply a Python function to every single element of a DataFrame individually. Works only for Dataframe not series.

```
df1 = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

format_func = lambda x: '%.2f' % x

df_formatted_map = df1.map(format_func)
print(df_formatted_map)
```
