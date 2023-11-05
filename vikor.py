# -*-coding:utf-8-*-
# -*-this is a python script -*-
import numpy as np
class Vikor(object):
    def __init__(self,**kwargs):
        self.args=kwargs
        self.w=[0.4,0.3,0.3]#权重
        self.v=0.5
        self.norm_type=['min','min','min']#全为成本指标
    #step:1 确定标准化矩阵
    def normal_matrix(self,a):
        r_matrix=np.zeros(a.shape)
        x_matrix=np.zeros((a.shape[0],2))#
        for i in range(r_matrix.shape[1]):
            x_matrix[i,0]=a.min(axis=0)[i]#找到第i列的最小值
            x_matrix[i, 1] = a.max(axis=0)[i]
        for i in range(r_matrix.shape[0]):
            for j in range(r_matrix.shape[1]):
                t=self.norm_type[j]
                if t=='min':
                    r_matrix[i,j]=(x_matrix[j,1]-a[i,j])/(x_matrix[j,1]-x_matrix[j,0])
                elif t=='max':
                    r_matrix[i, j] = (a[i, j]-x_matrix[j,0]) / (x_matrix[j, 1] - x_matrix[j, 0])

        return r_matrix

    def compute_S_R(self,r_matrix):
        S,R=np.zeros(r_matrix.shape[0]),np.zeros(r_matrix.shape[0])
        b_matrix=np.zeros((r_matrix.shape[0],2))
        for i in range(r_matrix.shape[1]):
            b_matrix[i, 0] = r_matrix.max(axis=0)[i]
            b_matrix[i, 1] = r_matrix.min(axis=0)[i]
        for i in range(r_matrix.shape[0]):
            s,r=0,0
            for j in range(r_matrix.shape[1]):
                k=self.w[j]*(b_matrix[j,0]-r_matrix[i,j])/(b_matrix[j,0]-b_matrix[j,1])
                s+=k
                if k > r:
                    r = k  # 求最大遗憾值
                    R[i] = r
            S[i]=s
        return S,R

    def compute_Q(self,s,r,v):
        Q=np.zeros(r.shape[0])
        S_matrix,R_matrix=np.zeros(2),np.zeros(2)
        S_matrix[0],S_matrix[1]=s.max(axis=0),s.min(axis=0)
        R_matrix[0], R_matrix[1] = r.max(axis=0), r.min(axis=0)
        for i in range(Q.shape[0]):
            Q[i]=self.v*(s[i]-S_matrix[1])/(S_matrix[0]-S_matrix[1])+(1-self.v)*(r[i]-R_matrix[1])/(R_matrix[0]-R_matrix[1])
        return Q

    def get_plan(self,Q):

        return Q.argmin()

    def vikor(self):
        normal_matrix=np.array(self.args['load_matrix'])
        r_matrix=self.normal_matrix(normal_matrix)#标准化
        s,r=self.compute_S_R(r_matrix=r_matrix)#获取个体遗憾与最大群体效应
        Q_order=self.compute_Q(s=s,r=r,v=self.v)#排序
        return self.get_plan(Q_order)#迁移方案的编号,Q的指标值越小越好


