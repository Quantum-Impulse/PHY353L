from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


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


def foo1a():
    """
    Big gaussian curve
    """
    data = load_data("data/26Jan2024_RunT_240000s_WaitT_1000ms_Experiment1.lvm")
    #data = load_data("data/25Jan2024_RunT_2s_WaitT_2ms_Experiment3.lvm")
    
    # Histogram
    plt.hist(data[1],bins=np.arange( min(data[1]), max(data[1]) + 1, 1), density=True,ec='white')
    plt.hist(data[2],bins=np.arange( min(data[2]), max(data[2]) + 1, 1), density=True,ec='white')

    # Fit
    mu1, sigma1 = norm.fit(data[1])
    mu2, sigma2 = norm.fit(data[2])
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin,xmax,100)
    p1 = norm.pdf(x,mu1,sigma1)
    p2 = norm.pdf(x,mu2,sigma2)
    plt.plot(x,p1,'k',linewidth=1)
    plt.plot(x,p2,'k',linewidth=1)
    plt.show()


def foo1b():
    data = load_data("data/26Jan2024_RunT_240000s_WaitT_1000ms_Experiment1.lvm")
    
    # Histogram
    plt.hist(data[1],bins=np.arange( min(data[1]), max(data[1]) + 1, 1), align='right',density=True)
    plt.hist(data[2],bins=np.arange( min(data[2]), max(data[2]) + 1, 1), align='right',density=True)
    
    # Fit
    mu1, sigma1 = norm.fit(data[1])
    mu2, sigma2 = norm.fit(data[2])
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin,xmax,100)
    p1 = norm.pdf(x,mu1,sigma1)
    p2 = norm.pdf(x,mu2,sigma2)
    plt.plot(x,p1,'k',linewidth=1)
    plt.plot(x,p2,'k',linewidth=1)
    plt.show()


def foo2():
    data = load_data("data/25Jan2024_RunT_2s_WaitT_2ms_Experiment3.lvm")
    
    # Histogram
    plt.hist(data[1],bins=np.arange( min(data[1]), max(data[1]) + 1, 1), align='right',density=True)
    plt.hist(data[2],bins=np.arange( min(data[2]), max(data[2]) + 1, 1), align='right',density=True)
    
    # Fit
    mu1, sigma1 = norm.fit(data[1])
    mu2, sigma2 = norm.fit(data[2])
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin,xmax,100)
    p1 = norm.pdf(x,mu1,sigma1)
    p2 = norm.pdf(x,mu2,sigma2)
    plt.plot(x,p1,'k',linewidth=1)
    plt.plot(x,p2,'k',linewidth=1)
    plt.show()


def foo3():
    """
    Shows lead data (80 ms)
    """
    datas = [
        load_data("data/30Jan2024_No Cobalt_RunTime_300s_WaitTime_80s.lvm"),
        load_data("data/30Jan2024_1.530mm_RunTime_300s_WaitTime_80ms.lvm"),
        load_data("data/30Jan2024_3.060mm_RunTime_300s_WaitTime_80ms.lvm"),
        load_data("data/30Jan2024_5.860mm_RunTime_300s_WaitTime_80ms.lvm"),
        load_data("data/30Jan2024_8.670mm_RunTime_300s_WaitTime_80ms.lvm"),
        load_data("data/30Jan2024_14.500mm_RunTime_300s_WaitTime_80ms.lvm"),
        load_data("data/30Jan2024_20.300mm_RunTime_300s_WaitTime_80ms.lvm"),
        load_data("data/30Jan2024_29.000mm_RunTime_300s_WaitTime_80ms.lvm")]

    # Get bin numbers
    fig, axs = plt.subplots(2)
    for i in range(len(datas)):
        # Histogram
        axs[0].hist(datas[i][1],bins=np.arange( min(datas[i][1]), max(datas[i][1]) + 1, 1), align='right',density=True)
        axs[1].hist(datas[i][2],bins=np.arange( min(datas[i][2]), max(datas[i][2]) + 1, 1), align='right',density=True)

        # Fit
        mu1, sigma1 = norm.fit(datas[i][1])
        mu2, sigma2 = norm.fit(datas[i][2])
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin,xmax,100)
        p1 = norm.pdf(x,mu1,sigma1)
        p2 = norm.pdf(x,mu2,sigma2)
        axs[0].plot(x,p1)
        axs[1].plot(x,p2)
        axs[0].errorbar(x,p1,yerr=0.01,xerr=0.1)
    plt.show()


def foo4():
    """
    Shows lead data (40 ms)
    """
    datas = [
        load_data("data/30Jan2024_No Cobalt_RunTime_300s_WaitTime_40s.lvm"),
        load_data("data/30Jan2024_1.530mm_RunTime_300s_WaitTime_40ms.lvm"),
        load_data("data/30Jan2024_3.060mm_RunTime_300s_WaitTime_40ms.lvm"),
        load_data("data/30Jan2024_5.860mm_RunTime_300s_WaitTime_40ms.lvm"),
        load_data("data/30Jan2024_8.670mm_RunTime_300s_WaitTime_40ms.lvm"),
        load_data("data/30Jan2024_14.500mm_RunTime_300s_WaitTime_40ms.lvm"),
        load_data("data/30Jan2024_20.300mm_RunTime_300s_WaitTime_40ms.lvm"),
        load_data("data/30Jan2024_29.000mm_RunTime_300s_WaitTime_40ms.lvm")]

    # Get bin numbers
    fig, axs = plt.subplots(2)
    for i in range(len(datas)):
        # Histogram
        axs[0].hist(datas[i][1],bins=np.arange( min(datas[i][1]), max(datas[i][1]) + 1, 1), align='right',density=True,ec='white')
        axs[1].hist(datas[i][2],bins=np.arange( min(datas[i][2]), max(datas[i][2]) + 1, 1), align='right',density=True,ec='white')

        # Fit
        mu1, sigma1 = norm.fit(datas[i][1])
        mu2, sigma2 = norm.fit(datas[i][2])
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin,xmax,100)
        p1 = norm.pdf(x,mu1,sigma1)
        p2 = norm.pdf(x,mu2,sigma2)
        axs[0].plot(x,p1)
        axs[1].plot(x,p2)
        axs[0].errorbar(x,p1,yerr=0.01,xerr=0.1)
    plt.show()


def main():
    #foo1a()
    #foo1b()
    #foo2()
    #foo3()
    foo4()

if __name__=="__main__":
    main()
