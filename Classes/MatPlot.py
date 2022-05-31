import matplotlib.pyplot as plt
import statistics as stat
from Classes.InitVars import InitVars as iv
from Classes.StringToFloat import StringToFloat

class MatPlot():
    def __init__(self) -> None:
        pass

    def simplePlot(plot_list: list) -> None:
        plt.figure(figsize=(18, 6))
        plt.gca().yaxis.grid(linestyle='-', linewidth=0.2)
        # plt.gca().yaxis.grid(True)
        plt.ylim(0, 0.03)
        plt.plot(plot_list, '.')
        plt.show()
        
        pass

    def multiFigurePlot(di_diff, mono_shuffle, di_shuffle, tri_shuffle) -> None:
        mono_float = StringToFloat().stringToFloat(mono_shuffle)
        mono_shuffle_mean = [stat.mean(item) for item in mono_float] 
        di_float = StringToFloat().stringToFloat(di_shuffle)
        di_shuffle_mean = [stat.mean(item) for item in di_float]
        tri_float = StringToFloat().stringToFloat(tri_shuffle)
        tri_shuffle_mean = [stat.mean(item) for item in tri_float]
        
        plt.figure(1, figsize=(18, 5))
        plt.title('Dinuc diff (blue) and seq shuffled by dinuc diff (red) of Archaea genomes')
        plt.gca().yaxis.grid(linestyle='-', linewidth=0.2)
        plt.ylim(-0.05, 0.3)
        plt.plot(di_diff, color='blue', linestyle='none', marker='.')
        plt.plot(di_shuffle_mean, color='red', linestyle='none', marker='|')
        
        plt.figure(2, figsize=(18, 3))
        plt.title('Seq shuffled by mononuc diff of Archaea genomes')
        plt.gca().yaxis.grid(linestyle='-', linewidth=0.2)
        plt.ylim(-0.015, 0.02)
        plt.plot(mono_shuffle_mean, color='black', linestyle='none', marker='|')
        plt.plot(di_diff, color='blue', linestyle='none', marker='.')

        plt.figure(3, figsize=(18, 3))
        plt.title('Seq shuffled by trinuc diff of Arcaea genomes')
        plt.gca().yaxis.grid(linestyle='-', linewidth=0.2)
        plt.ylim(-0.015, 0.02)
        plt.plot(tri_shuffle_mean, color='green', linestyle='none', marker='|')
        plt.plot(di_diff, color='blue', linestyle='none', marker='.')
        
        plt.show()    

        pass

    def subPlots(di_diff, mono_shuffle, di_shuffle, tri_shuffle):
        mono_float = StringToFloat().stringToFloat(mono_shuffle)
        mono_shuffle_mean = [stat.mean(item) for item in mono_float] 
        di_float = StringToFloat().stringToFloat(di_shuffle)
        di_shuffle_mean = [stat.mean(item) for item in di_float]
        tri_float = StringToFloat().stringToFloat(tri_shuffle)
        tri_shuffle_mean = [stat.mean(item) for item in tri_float]
        
        plt.rcParams['figure.figsize'] = [18, 8]
        fig, axs = plt.subplots(nrows=3, ncols=1)

        axs[0].set_title(f'Fig.1 Dinuc diff (blue) and seq shuffled by dinuc diff (red) of {iv.out_name} genomes')
        axs[0].grid()
        axs[0].plot(di_diff, color='blue', linestyle='none', marker='.')
        axs[0].plot(di_shuffle_mean, color='red', linestyle='none', marker='|')
        
        axs[1].set_title(f'Fig.2 Seq shuffled by mononuc diff of {iv.out_name} genomes')
        axs[1].grid()
        axs[1].plot(mono_shuffle_mean, color='black', linestyle='none', marker='|')
        axs[1].plot(di_diff, color='blue', linestyle='none', marker='.')
        
        axs[2].set_title(f'Fig.3 Seq shuffled by trinuc diff of {iv.out_name} genomes')
        axs[2].grid()
        axs[2].plot(tri_shuffle_mean, color='green', linestyle='none', marker='|')
        axs[2].plot(di_diff, color='blue', linestyle='none', marker='.')
        
        fig.tight_layout()
        plt.show()

        pass

    def dictPlot(di_dict: dict) -> None:
        dict_1st = {}
        dict_2nd = {}
        dict_1st_2nd = {}
        for key, value in di_dict.items():
            dict_1st[key] = value[0]
            dict_2nd[key] = value[1]
            dict_1st_2nd[key] = value[:-1]
        
        plt.rcParams['figure.figsize'] = [8, 10]
        plt.suptitle('E.coli dinuc diff in two frames')
        plt.plot(list(dict_1st.keys()), list(dict_1st.values()), 'b.', linestyle='none', label='1st frame')
        plt.plot(list(dict_2nd.keys()), list(dict_2nd.values()), 'r.', linestyle='none', label='2nd frame')
        plt.legend(loc='upper right')
        plt.show()

        pass
        
        