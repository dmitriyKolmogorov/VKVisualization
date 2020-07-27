# VKVisualization (by myDiamondsDancing)

This package was created to visualize VK group data using Python, `matplotlib` and `pandas`. Get .xsl file from your VK group.

## DataSet
To use this class, import it from `vkvisualization.dataset`:
```python
from vkvisualization.dataset import DataSet
```

#### Initialization
This class inherits `pandas.DataFrame` class and its constructor gets all arguments that `pandas.DataFrame constructor` has.
```python
import pandas as pd
from vkvisualization.dataset import DataSet

df = pd.read_csv('group.xls')
dataset = DataSet(df)
```

#### Initialize from file
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
#### Getting data
All methods described lower have two non-mandatory arguments - `start` and `end`. These arguments are responsible for start date and end date. If `start` is None, data will be selected from the minimum date in the sample. If `end` is None, data will be selected from the start to the maximum date in the sample. 

###### Dataset.views(start=None, end=None) -> np.ndarray
```python
dataset = DataSet.from_excel('group.xls)
print(dataset.views(end='2020-07-27'))
```

###### 
