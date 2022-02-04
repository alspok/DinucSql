from sys import stderr
from turtle import color
import matplotlib.pyplot as plt
import statistics as stat
import random

from Classes.StringToFloat import StringToFloat

def simplePlot(plot_list: list) -> None:
    # plot_list = []
    # for item in float_list:
    #     for plot_item in item:
    #         plot_list.append(plot_item)
            
    plt.figure(figsize=(18, 6))
    plt.gca().yaxis.grid(linestyle='-', linewidth=0.2)
    # plt.gca().yaxis.grid(True)
    plt.ylim(0, 0.03)
    plt.plot(plot_list, '.')
    plt.show()
    
    pass

def errorPlot(di_diff, mono_shuffle, di_shuffle, tri_shuffle) -> None:
    mono_float = StringToFloat().stringToFloat(mono_shuffle)
    mono_shuffle_mean = [stat.mean(item) for item in mono_float] 
    di_float = StringToFloat().stringToFloat(di_shuffle)
    di_shuffle_mean = [stat.mean(item) for item in di_float]
    tri_float = StringToFloat().stringToFloat(tri_shuffle)
    tri_shuffle_mean = [stat.mean(item) for item in tri_float]
    
    plt.figure(figsize=(18, 6))
    plt.gca().yaxis.grid(linestyle='-', linewidth=0.2)
    plt.ylim(-0.05, 0.3)
    # plt.boxplot(di_shuffle_diff)
    plt.plot(mono_shuffle_mean, color='black', linestyle='none', marker='|')
    plt.plot(di_shuffle_mean, color='red', linestyle='none', marker='|')
    plt.plot(tri_shuffle_mean, color='green', linestyle='none', marker='|')
    # x = range(0, len(di_shuffle_diff), 1)
    # y = di_shuffle_mean
    # plt.errorbar(x, y, yerr=0.06)
    plt.plot(di_diff, color='blue', linestyle='none', marker='.')
    # plt.plot(di_diff, 'g')
    # plt.plot(di_shuffle_mean, '.')
    # plt.plot(di_shuffle_std, '+')
    plt.show()    
    pass