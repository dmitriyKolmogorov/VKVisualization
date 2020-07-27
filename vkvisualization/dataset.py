import os

import pandas as pd
import numpy as np


class DataSet(pd.DataFrame):
    def __init__(self, *args) -> None:

        # DataFrame sorted by date
        df = pd.DataFrame(*args).sort_values('Дата')

        df = df[df['Дата'] >= df['Дата'][df['Критерий'] == 'views'].min()]

        # DataFrame.__init__() 
        super(DataSet, self).__init__(df)

        # converting Дата column to datetime
        try:
            self['Дата'] = pd.to_datetime(self['Дата'])
        except Exception as ex:
            raise ValueError(f'Error converting Дата column ({ex}).')

        # start date
        self.__start = np.datetime64(self['Дата'].min())

        # end date
        self.__end = np.datetime64(self['Дата'].max()) 

        # available cities in DataSet
        self.__cities = self['Парам. №1'][self['Критерий'] == 'cities'].unique()

        # available countries in DataSet
        self.__countries = self['Парам. №1'][self['Критерий'] == 'countries'].unique()


    def start_date(self):
        '''Returns minimum date in dataset'''
        return self.__start

    
    def end_date(self):
        '''Return maximum date in dataset'''
        return self.__end


    def views(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with views from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self._preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'views')].values


    def visitors(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with visitors from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                               (self['Дата'] >= start) & 
                               (self['Критерий'] == 'visitors')].values

    
    def age(self, key='18-21', start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with age as key from start date to end date.'''

        keys = ['1-18', '18-21', '21-24', '24-27', '27-30', '30-35', '35-45', '45+']

        # preprocessing key argument
        if key not in keys:
            raise ValueError(f'Unknown key: {key}. Available keys are {keys}.')

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'age') & 
                                (self['Парам. №1'] == key)].values


    def gender(self, key='Ж', start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with gender as key from start date to end date.'''

        # preprocessing key argument
        if key not in ('М', 'Ж'):
            raise ValueError(f"Unknown key: {key}. Available keys are 'М', 'Ж'.")

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'gender') & 
                                (self['Парам. №1'] == key)].values


    def gender_age(self, gender='Ж', age='18-21', start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with gender and age as keys from start date to end date.'''

        # preprocessing gender argument
        if gender not in ('М', 'Ж'):
            raise ValueError(f"Unknown key: {g}. Available gender keys are 'М', 'Ж'.")

        keys = ['1-18', '18-21', '21-24', '24-27', '27-30', '30-35', '35-45', '45+']

        # preprocessing age argument
        if age not in keys:
            raise ValueError(f'Unknown key: {a}. Available age keys are {keys}.')

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'gender_age') & 
                                (self['Парам. №1'] == g) &
                                (self['Парам. №2'] == a)].values


    def city(self, city:str, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with city as key from start date to end date.'''

        # preprocessing city argument
        if city not in self.__cities:
            raise ValueError(f"Unknown city: {city}. Use Dataset.available_cities() to check available cities.")

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'cities') & 
                                (self['Парам. №1'] == city)].values


    def available_cities(self) -> list:
        '''Returns list with available cities.'''
        return list(self.__cities)

    
    def country(self, country:str, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with country as key from start date to end date.'''

        # preprocessing country argument
        if country not in self.__countries:
            raise ValueError(f"Unknown city: {city}. Use Dataset.available_countries() to check available cities.")

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                 (self['Дата'] >= start) & 
                                 (self['Критерий'] == 'countries') & 
                                 (self['Парам. №1'] == city)].values 


    def available_countries(self) -> list:
        '''Returns list with available countries.'''
        return list(self.__countries)   


    def discussions(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with discussions from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'sections') &
                                (self['Парам. №1'] == 'Обсуждения')].values   


    def audio(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with audio from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'sections') &
                                (self['Парам. №1'] == 'Аудиозаписи')].values                                
    

    def videos(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with videos from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'sections') &
                                (self['Парам. №1'] == 'Видеозаписи')].values

    
    def photo_albums(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with photo albums from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'sections') &
                                (self['Парам. №1'] == 'Фотоальбомы')].values


    def likes(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with likes from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'feedback') &
                                (self['Парам. №1'] == 'Нравится')].values

            
    def comments(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with comments from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'feedback') &
                                (self['Парам. №1'] == 'Комментарии')].values


    def told_friends(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with "told friends" category from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'feedback') &
                                (self['Парам. №1'] == 'Рассказали друзьям')].values


    def new_members(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with "new members" category from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'members') &
                                (self['Парам. №1'] == 'Новые участники')].values    


    def exited_members(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with "exited members" category from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'members') &
                                (self['Парам. №1'] == 'Вышедшие участники')].values

    
    def reach(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with reach from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'reach')].values

    
    def reach_subscribers(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with reach subscribers from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'reach_subscribers')].values


    def reach_viral(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with "reach viral" category from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self._preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'reach_viral')].values


    def reach_ads(self, start=None, end=None) -> np.ndarray:
        '''Returns np.ndarray with "reach ads" category from start date to end date.'''

        # preprocessing start argument
        start = self._preprocess_start(start)

        # preprocessing end argument
        end = self.__preprocess_end(end)

        # if start is greater than end
        if start >= end:
            raise ValueError('Start is greater than end or is equal to end.')

        # return np.ndarray
        return self['Значение'][(self['Дата'] <= end) & 
                                (self['Дата'] >= start) & 
                                (self['Критерий'] == 'reach_ads')].values


    @classmethod
    def from_excel(cls, path:str, **kwargs):
        '''
        Creating DataSet object with .xls file.
        Parameters:
            - path:str - .xls file's path;
            - **kwargs - parameters for pd.read_excel();
        '''

        # splitting path for file's extension
        filename, file_extension = os.path.splitext(path)

        # if input file is not .xls file
        if file_extension != '.xls':
            raise ValueError('Input file is not .xls file.')

        # creating DataFrame with read_excel()
        try:
            dataframe = pd.read_excel(path, **kwargs)
        except Exception as ex:
            raise FileExistsError(f'Error reading file ({ex}).')

        # creating DataSet object
        return cls(dataframe) 


    @classmethod
    def from_csv(cls, path:str, **kwargs):
        '''
        Creating DataSet object with .csv file.
        Parameters:
            - path:str - .csv file's path;
            - **kwargs - parameters for pd.read_csv();
        '''

        # splitting path for file's extension
        filename, file_extension = os.path.splitext(path)

        # if input file is not .csv file
        if file_extension != '.csv':
            raise ValueError('Input file is not .xls file.')

        # creating DataFrame with read_csv()
        try:
            dataframe = pd.read_csv(path, **kwargs)
        except Exception as ex:
            raise FileExistsError(f'Error reading file ({ex}).')

        # creating DataSet object
        return cls(dataframe) 


    def _preprocess_start(self, start=None):
        '''Preprocesses start date.'''

        if start:

            # if start is not str
            if not isinstance(start, str):
                raise TypeError(f'Start argument has to be str (found {type(start)} type).')

            # converting start to datetime
            try:
                start = np.datetime64(start)
            except Exception as ex:
                raise ValueError('Cannot convert start argument to date.')

            # if start is lower than self.__start
            if start < self.__start:
                raise ValueError(F'Start argument is lower than a valid date ({start} vs. {str(self.__start)[:10]}).')
        
        else:
            start = self.__start

        return start


    def _preprocess_end(self, end=None):
        '''Preprocesses end date.'''

        if end:

            # if end is not str
            if not isinstance(end, str):
                raise TypeError(f'Start argument has to be str (found {type(end)} type).')

            # converting end to datetime
            try:
                end = np.datetime64(end)
            except Exception as ex:
                raise ValueError('Cannot convert end argument to date.')

            # if end is greater than self.__end
            if end > self.__end:
                raise ValueError(F'End argument is greater than a valid date ({end} vs. {str(self.__end)[:10]}).')
        
        else:
            end = self.__end

        return end
