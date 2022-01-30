import matplotlib.pyplot as plt

def matPlot(float_list: list) -> None:
    plot_list = []
    for item in float_list:
        for plot_item in item:
            plot_list.append(plot_item)
            
    plt.figure(figsize=(18, 6))
    plt.scatter(plot_list[700:])
    plt.show()
    
    pass