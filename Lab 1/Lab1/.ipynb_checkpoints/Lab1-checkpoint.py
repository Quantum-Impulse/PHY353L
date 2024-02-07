import numpy as np
import matplotlib.pyplot as plt
import math as m



def load_data(path):
    """
    Loads a file with only number columns and returns
    a 2D array, with the first array holding each column.
    """
    raw_data = np.loadtxt(path)
    data = [[] for i in range(len(raw_data[0]))]
    for i in range(len(data)):
        for j in range(len(raw_data)):
            data[i].append(raw_data[j][i])
    return data


def main():
    # Run time = 2 days, wait time = 1 s
    #data = load_data("data/26Jan2024_RunT_240000s_WaitT_1000ms_Experiment1.lvm")
    
    # Run time = 10 min, wait time = 32 ms
    #data = load_data("data/26Jan2024_RunT_600s_WaitT_32ms_Experiment1.lvm")
    
    # Run time = 5 min, wait time = 64 ms
    #data = load_data("data/26Jan2024_RunT_300s_WaitT_64ms_Experiment1.lvm")
    
    # Run time = 10 s, wait time = 2 ms
    #data = load_data("data/25Jan2024_RunT_10s_WaitT_2ms_Experiment4.lvm")
    
    # Run time = 20 s, wait time = 500 ms
    #data = load_data("data/25Jan2024_RunT_10s_WaitT_2ms_Experiment4.lvm")
    data2 = load_data("data/30Jan2024_1.530mm_RunTime_300s_WaitTime_80s.lvm")
    data1 = load_data("data/30Jan2024_No Cobalt_RunTime_300s_WaitTime_80s.lvm")
    
    # Print data
    #print(data)
    
    # Plot data + histogram
    """
    fig, axs = plt.subplots(4)
    axs[0].plot(data[0],data[1])
    axs[1].hist(data[1],bins='auto')
    axs[2].plot(data[0],data[2])
    axs[3].hist(data[2],bins='auto')
    """
    
    # Get bin numbers
    fig, axs = plt.subplots(2)
    axs[0].hist(data1[1],bins=np.arange( min(data1[1]), max(data1[1]) + 1, 1), align='right',density=True)
    axs[0].hist(data1[2],bins=np.arange( min(data1[2]), max(data1[2]) + 1, 1), align='right',density=True)
    #axs[0].locator_params(axis='x',integer=True)
    axs[1].hist(data2[1],bins=np.arange( min(data2[1]), max(data2[1]) + 1, 1), align='right',density=True)
    axs[1].hist(data2[2],bins=np.arange( min(data2[2]), max(data2[2]) + 1, 1), align='right',density=True)
    #axs[1].locator_params(axis='x',integer=True)
    plt.show()
    


if __name__=="__main__":
    main()
