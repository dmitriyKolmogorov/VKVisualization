import matplotlib.pyplot as plt
import pandas as pd

from vkvisualization.dataset import DataSet


def visualize_views(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes views statistics with matplotlib'''

    data = dataset.views(start=start, 
                         end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes views statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        elif kind == 'barh':
            ax.barh(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist', 'bar' or 'barh'.")


    return plot


def visualize_visitors(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes visitors statistics with matplotlib'''

    data = dataset.visitors(start=start, 
                            end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes visitors statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_age(dataset:DataSet, key='18-21', start=None, end=None, intercept=0):
    '''Visualizes age statistics with matplotlib'''

    data = dataset.age(start=start, 
                       end=start,
                       key=key)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes age statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_gender(dataset:DataSet, key='Ж', start=None, end=None, intercept=0):
    '''Visualizes gender statistics with matplotlib'''

    data = dataset.gender(start=start, 
                          end=end,
                          key=key)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes gender statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_gender_age(dataset:DataSet, gender='Ж', age='18-21', start=None, end=None, intercept=0):
    '''Visualizes gender and age statistics with matplotlib'''

    data = dataset.views(start=start, 
                         end=end,
                         gender=gender,
                         age=age)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes gender and age statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_city(dataset:DataSet, city:str, start=None, end=None, intercept=0):
    '''Visualizes city statistics with matplotlib'''

    data = dataset.views(city,
                         start=start, 
                         end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes city statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_country(dataset:DataSet, country:str, start=None, end=None, intercept=0):
    '''Visualizes country statistics with matplotlib'''

    data = dataset.country(country,
                           start=start, 
                           end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes country statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_discussions(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes discussions statistics with matplotlib'''

    data = dataset.discussions(start=start, 
                               end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes discussions statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_audio(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes audio statistics with matplotlib'''

    data = dataset.audio(start=start, 
                         end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes audio statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_videos(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes videos statistics with matplotlib'''

    data = dataset.videos(start=start, 
                          end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes videos statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_photo_albums(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes photo albums statistics with matplotlib'''

    data = dataset.photo_albums(start=start, 
                                end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes photo albums statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_likes(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes likes statistics with matplotlib'''

    data = dataset.likes(start=start, 
                         end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not (isinstance(intercept, int) or intercept > 0):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes likes statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_comments(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes comments statistics with matplotlib'''

    data = dataset.comments(start=start, 
                            end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes comments statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_told_friends(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes told friends statistics with matplotlib'''

    data = dataset.told_friends(start=start, 
                                end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes told friends statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_new_members(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes new members statistics with matplotlib'''

    data = dataset.new_members(start=start, 
                               end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes new members statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_exited_members(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes exited members statistics with matplotlib'''

    data = dataset.exited_members(start=start, 
                                  end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes exited members statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_reach(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes reach statistics with matplotlib'''

    data = dataset.reach(start=start, 
                         end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes reach statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_reach_subscribers(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes reach subscribers statistics with matplotlib'''

    data = dataset.reach_subscribers(start=start, 
                                     end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes reach subscribers statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_reach_viral(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes reach viral statistics with matplotlib'''

    data = dataset.reach_viral(start=start, 
                               end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes reach viral statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot


def visualize_reach_ads(dataset:DataSet, start=None, end=None, intercept=0):
    '''Visualizes reach ads statistics with matplotlib'''

    data = dataset.reach_ads(start=start, 
                             end=end)

    x_axis = range(intercept, len(data) + intercept)

    if not isinstance(intercept, int):
        raise TypeError('Argument intercept expected to be integer.')


    def plot(ax, kind='plot', **kwargs):
        '''Visualizes reach ads statistics with matplotlib from start to end'''

        if kind == 'plot':
            ax.plot(x_axis, data, **kwargs)
        elif kind == 'hist':
            ax.hist(data, **kwargs)
        elif kind == 'bar':
            ax.bar(x_axis, data, **kwargs)
        else:
            raise ValueError("kind argument has to have values 'plot', 'hist' or 'bar'")


    return plot