import numpy as np
from matplotlib import pyplot as plt
    
def pca(X, no_dims=50):
    ''' 
        使用PCA预降维到no_dims维
    '''
    (n, d) = X.shape
    X = X - np.tile(np.mean(X, 0), (n, 1))
    (l, M) = np.linalg.eig(np.dot(X.T, X))
    print(M.shape)
    Y = np.dot(X, M[:, 0:no_dims])
    return Y

def cal_pairwise_dist(x):
    '''
        计算X_i,X_j的距离
        (Xi - Xj)^2 = Xi^2 + Xj^2 - 2XiXj
    '''
    sum_x = np.sum(np.square(x), 1)
    dist = np.add( np.add(-2 * np.dot(x, x.T), sum_x ).T, sum_x )
    return dist

def cal_perplexity(dist, idx=0, beta=1.0):
    '''
    计算perplexity
    @dist：计算出的距离矩阵，
    @idx：指dist中自己的位置
    @beta：是高斯分布参数
    '''
    pass

if __name__ == "__main__":
    X = np.loadtxt("mnist2500_X.txt")
    labels = np.loadtxt("mnist2500_labels.txt")
    print(X.shape)
    X = pca(X, 50).real
    print(X.shape)
