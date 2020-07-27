# VKVisualization (by myDiamondsDancing)

This package was created to visualize VK group data using Python, `matplotlib` and `pandas`. Get .xsl file from your VK group.

## DataSet
To use this class, import it from `vkvisualization.dataset`:
```python
from vkvisualization.dataset import DataSet
```

### Initialization
This class inherits `pandas.DataFrame` class and its constructor gets all arguments that `pandas.DataFrame constructor` has.
```python
import pandas as pd
from vkvisualization.dataset import DataSet

df = pd.read_csv('group.xls')
dataset = DataSet(df)
```

### Initialize from file
In this class defined two class methods - 'from_excel' and 'from_csv'. Both of these methods have one mandatory argument - path of file and kwargs for `pandas` reading function.
Example of using `from_excel` method:
```python
from vkvisualization.dataset import DataSet

dataset = DataSet.from_excel('group.xls')
```
Example of using `from_csv` method:
```python
from vkvisualization.dataset import DataSet

dataset = DataSet.from_csv('group.csv')
```
### Getting data
All methods described lower have two non-mandatory arguments - `start` and `end`. These arguments are responsible for start date and end date. If `start` is None, data will be selected from the minimum date in the sample (use `DataSet.start_date()` to get minimum date). If `end` is None, data will be selected from the start to the maximum date in the sample (use `DataSet.end_date()` to get maximum date). 

#### `DataSet.views(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.views(start='2020-01-01', end='2020-07-27'))
```

#### `DataSet.visitors(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.visitors(start='2020-01-01', end='2020-07-27'))
```

#### `DataSet.age(key='18-21', start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.age(start='2020-01-01', 
                  end='2020-07-27',
                  key='18-21'))
```
Raises `ValueError` if key is uknown. All available keys will be described in the description of `ValueError`.

#### `DataSet.gender(key='Ж', start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.gender(start='2020-01-01', 
                     end='2020-07-27',
                     key='Ж'))
```
Raises `ValueError` if key is unknown. `key` argument has to be 'М' or 'Ж'.

#### `DataSet.gender_age(gender='Ж', age='18-21', start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.gender_age(start='2020-01-01', 
                         end='2020-07-27',
                         gender='Ж',
                         age='18-21'))
```

#### `DataSet.city(city:str, start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.city('Москва',
                    start='2020-01-01', 
                    end='2020-07-27'))
```
Raises `ValueError` if `city` argument was declared invalid. To get all available names for `city` argument use `DataSet.available_cities()`.

#### `DataSet.country(country:str, start='None', end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.country('Российская Федерация',
                       start='2020-01-01', 
                       end='2020-07-27'))
```
Raises `ValueError` if `country` argument is unknown. To get all available names for `country` argument use `DataSet.available_countries()`.

#### `DataSet.discussions(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.discussions(start='2020-01-01', end='2020-07-27'))
```

#### `DataSet.audio(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.audio(start='2020-01-01', end='2020-07-27'))
```

#### `DataSet.videos(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.videos(start='2020-01-01', end='2020-07-27'))
```

#### `DataSet.photo_albums(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.photo_albums(start='2020-01-01', end='2020-07-27'))
```

#### `DataSet.likes(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.likes(start='2020-01-01', end='2020-07-27'))
```

#### `DataSet.comments(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.comments(start='2020-01-01', end='2020-07-27'))
```

#### `DataSet.told_friends(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.told_friend(start='2020-01-01', end='2020-07-27'))
```

#### `DataSet.new_members(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.new_members(start='2020-01-01', end='2020-07-27'))
```

#### `DataSet.exited_members(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.exited_members(start='2020-01-01', end='2020-07-27'))
```

#### `DataSet.reach(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.reach(start='2020-01-01', end='2020-07-27'))
```

#### `DataSet.reach_subscribers(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.reach_subscribers(start='2020-01-01', end='2020-07-27'))
```

#### `DataSet.reach_viral(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.reach_viral(start='2020-01-01', end='2020-07-27'))
```

#### `DataSet.reach_ads(start=None, end=None) -> np.ndarray`
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.reach_ads(start='2020-01-01', end='2020-07-27'))
```

### Other methods
#### `DataSet.start_date()`
Use this method to get minimum date in the sample.
#### `DataSet.end_date()`
Use this method to get maximum date in the sample.
#### `DataSet.available_cities() -> list`
Use this method to get all available values for `city` argument in `DataSet.city()`.
#### `DataSet.available_countries() -> list`
Use this method to get all available values for `country` argument in `DataSet.country()`.
