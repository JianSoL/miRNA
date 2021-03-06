import numpy as np
import pandas as pd
##########################


def preprocess_data(mRNA_num):
    miRNA = pd.read_csv("Data_all/miRNA.csv")
    mRNA = pd.read_csv("Data_all/mRNA.csv")
    print(miRNA.iloc[:, :])
    print(mRNA.iloc[:, :])

    miRNA_np = miRNA.iloc[:, :].to_numpy()
    mRNA_np = mRNA.iloc[:,:].to_numpy()
    # print(miRNA_np)
    # print(mRNA_np)
    data = np.concatenate((mRNA_np, miRNA_np), 0)
    # print(data.shape)
    data = data.T
    print(data.shape)

    mask = np.ones(data.shape, dtype=np.float32)
    mask[:, mRNA_num:] = 0
    print(mask)
    Data_X = data*mask
    Data_Y = data[:,mRNA_num:]
    print(Data_X.shape)
    print(Data_Y.shape)
    return Data_X,Data_Y

