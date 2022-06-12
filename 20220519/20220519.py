from seaborn import *
from matplotlib.pyplot import *
from numpy import *
from pandas import *


def log1():
    set_style('dark')  # darkgrid,whitegrid,dark,white,ticks
    log = read_csv('tips.csv')
    cols = ['total_bill','sex','day','time']
    norm_log = log[cols]
    print(norm_log[:5])
    distplot(norm_log['total_bill'], kde=True,bins=30)
    show()


def jointplot1():
    log = read_csv('fandango_scores.csv')
    cols = ['FILM', 'IMDB', 'RottenTomatoes', 'Fandango_Stars']
    set_style('dark')
    norm_log = log[cols]
    jointplot(x=norm_log['IMDB'],y=norm_log['RottenTomatoes'],kind="hex",data=norm_log,color='Green')
    show()



