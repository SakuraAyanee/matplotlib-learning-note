from matplotlib.pyplot import show, subplots
from seaborn import *
from pandas import *


def seaborn1():
    set_style('darkgrid')
    log = read_csv('tips.csv')
    line = ['total_bill','tip','size']
    log2 = log[line]
    distplot(log2["total_bill"],kde=True,bins=20)
    show()


def seaborn2():
    set_style('darkgrid')
    log = read_csv('fandango_scores.csv')
    data = DataFrame(log,columns=['IMDB','RT_norm'])
    jointplot(x='IMDB',y='RT_norm',kind='hex',data=data,color='k')
    show()

def seaborn3():
    set_style('darkgrid')
    log = read_csv('fandango_scores.csv',nrows=20)
    fig,ax1 = subplots(2,2,figsize=(10,10),sharex=True)
    despine(left=True)
    violinplot(x='RottenTomatoes_User', y='RottenTomatoes',data=log,palette='CMRmap', ax=ax1[1, 0])
    violinplot(x='Metacritic_User', y='Metacritic', data=log, palette='husl', ax=ax1[0, 0])
    violinplot(x='IMDB', y='Fandango_Stars', data=log, palette='husl', ax=ax1[0, 1])
    violinplot(x='IMDB', y='Fandango_Ratingvalue', data=log, palette='CMRmap', ax=ax1[1, 1])
    show()

seaborn3()
seaborn2()
seaborn1()