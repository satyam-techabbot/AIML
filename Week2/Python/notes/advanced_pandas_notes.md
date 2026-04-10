# Advanced Pandas

## Group by: split-apply-combine

By “group by” we are referring to a process involving one or more of the following steps:
- Splitting the data into groups based on some criteria.
- Applying a function to each group independently.
- Combining the results into a data structure.

```python
speeds = pd.DataFrame(
    [
        ("bird", "Psittaciformes", 24.0),
        ("bird", "Falconiformes", 389.0),
        ("mammal", "Carnivora", 80.2),
        ("mammal", "Primates", np.nan),
        ("mammal", "Carnivora", 58),
    ],
    index=["falcon", "parrot", "lion", "monkey", "leopard"],
    columns=("class", "order", "max_speed"),
)

speeds
grp_by_obj = speeds.groupby("class")
grp_by_obj.max_speed.sum()
```

## Splitting an object into groups

### GroupBy sorting
By default the group keys are sorted during the groupby operation. Use sort=false in param to stop sorting the data while using groupby.

```python
grp_by_obj = speeds.groupby("class", sort=False)

# get group by value of specific grp
speeds.groupby("class", sort=False).get_group('bird')
```

#### GroupBy dropna
By default NA values are excluded from group keys during the groupby operation. To get NaN values using groupby use dropna=False.

```python
speeds.groupby("class", sort=False, dropna=False).get_group('mammal')
```

### GroupBy object attributes

- groups: 
    groups attribute of a GroupBy object is a dictionary that maps each unique group key to the index labels belonging to that group.
    
    ```python
    grp_by_obj.groups
    ```

- getting len of sorted df:
    ```python
    len(grp_by_obj)
    ```

### GroupBy with MultiIndex
```python
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'SubCategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Values': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data).set_index(['Category', 'SubCategory'])

# Group by the first level ('Category') and sum the 'Values'
grouped_data = df.groupby(level='Category')['Values'].sum()

print(grouped_data)
```

### Grouping DataFrame with Index levels and columns
A DataFrame may be grouped by a combination of columns and index levels. We can specify both column and index names, or use a Grouper.

```python
df.groupby([pd.Grouper(level=0), "SubCategory"])['Values'].sum()
```

### DataFrame column selection in GroupBy
```python
grouped = df.groupby(["A"])
```


## Iterating through groups
We can use any loop like for loops or something two iterate through the group obj.

```python
for x, y in df.groupby('SubCategory'):
    print(x)
    print(y)
```

## Selecting a group
A single group can be selected using DataFrameGroupBy.get_group().

```python
df.groupby('Category').get_group('A')
# or
df.groupby(['Category', 'SubCategory']).get_group(('A', 'Y'))
```

## Aggregation
An aggregation is a GroupBy operation that reduces the dimension of the grouping object. Example, sum of each column of a group.

```python
df.groupby(level=['Category'])['Values'].sum()
```

### Built-in aggregation methods

- any() : computes whether any value in groups are truthy
- all() : Compute whether all of the values in the groups are truthy
- count() : Compute the number of non-NA values in the groups
- cov() * : Compute the covariance of the groups
- first() : Compute the first occurring value in each group
- idxmax() : Compute the index of the maximum value in each group
- idxmin() : Compute the index of the minimum value in each group
- last() : Compute the last occurring value in each group
- max() : Compute the maximum value in each group
    ```python
    df.groupby('Category', sort=False).max()
    ```
- mean() : Compute the mean of each group

- median() : Compute the median of each group
- min() : Compute the minimum value in each group
    ```python
    df.groupby('Category', sort=False).min()
    ```
- describe() : gives statistics of data
    ```python
    df.groupby('Category', sort=False).describe()
    ```
- nunique() : Compute the number of unique values in each group
- prod() : Compute the product of the values in each group
- quantile() : Compute a given quantile of the values in each group
- sem() : Compute the standard error of the mean of the values in each group
- size() : Compute the number of values in each group. Includes NaN values.
- skew() * : Compute the skew of the values in each group
- std() : Compute the standard deviation of the values in each group
- sum() : Compute the sum of the values in each group
- var() : Compute the variance of the values in each group

### aggregate() method
Any reduction method that pandas implements can be passed as a string to aggregate(). We can also use shorthand agg(). We can Apply different functions to DataFrame columns.

```python
df.groupby('Category', sort=False).agg("sum")
```

### Aggregation with user-defined functions
Users can also provide their own User-Defined Functions (UDFs) for custom aggregations.

```python
df.groupby('Category', sort=False).agg(lambda x : set(x))
```

> Applying multiple functions at once: ```grouped["C"].agg(["sum", "mean", "std"])```

### Named aggregation
To support column-specific aggregation with control over the output column names, pandas accepts the special syntax in DataFrameGroupBy.agg() and SeriesGroupBy.agg(), known as “named aggregation”

```python
df.groupby('Category', sort=False).agg(min_value = pd.NamedAgg(column='Values', aggfunc="min"))
```


## Transformation
A transformation is a GroupBy operation whose result is indexed the same as the one being grouped.

#### Methods
- bfill() : Back fill NA values within each group
- cumcount() : Compute the cumulative count within each group
- cummax() : Compute the cumulative max within each group
- cummin() : Compute the cumulative min within each group
- cumprod() : Compute the cumulative product within each group
- cumsum() : Compute the cumulative sum within each group
- diff() : Compute the difference between adjacent values within each group
- ffill() : Forward fill NA values within each group

- pct_change() : Compute the percent change between adjacent values within each group
- rank() : Compute the rank of each value within each group
- shift() : Shift values up or down within each group

### transform() method
similar to aggregate method and also pass the udf.

```python
grouped.transform("sum")
# or
print(grouped.transform(lambda x : x+1))
```

### Window and resample operations

- resample() : 
- rolling() : Return a rolling grouper, providing rolling functionality per group.
    
    ```python
    print(df_re.groupby('A').rolling(2).B.mean())
    ```
- expanding() : will accumulate a given operation (sum() in the example) for all the members of each particular group. 
    
    ```python
    df_re.groupby("A").expanding().sum()
    ```

## Filtration

### Built-in filtrations
- head() : Select the top row(s) of each group. ```df_re.groupby('A').head(4)```

- nth() : Select the nth row(s) of each group. ```df_re.groupby('A').nth(4)```

- tail() : Select the bottom row(s) of each group. ```df_re.groupby('A').tail(4)```

### filter() method
takes udf and filters.

```python
df_re.groupby('A').filter(lambda x : len(x)>9)
```

## Flexible apply
Some operations on the grouped data might not fit into the aggregation, transformation, or filtration categories. For these, you can use the apply function.

```python
df_re.groupby('A').apply(lambda x : x.describe())
```

### Control grouped column(s) placement with group_keys
To control whether the grouped column(s) are included in the indices, you can use the argument group_keys which defaults to True.

```python
df.groupby("A", group_keys=False).apply(lambda x: x)
```

## Other usefull features

#### Exclusion of non-numeric columns
```python
df.groupby("A").std(numeric_only=True)
```

## Piping function calls
Allows you to apply one or more functions to the DataFrame object.

```python
def change_age(x):
  x["age"]=[10, 20, 30]
  return x

data = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}

df = pd.DataFrame(data)
df.pipe(change_age)
print(df)
```



