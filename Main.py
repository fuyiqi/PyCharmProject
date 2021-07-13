#coding:utf8

class DataProcess:
    def __init__(self,path_str):
        self.rawDF = self.load(path_str);

    #0 数据的读入
    def load(self,path_str):
        pass

#********************************************************#
    '''
    1. 数据探索
    '''
    #1.1 数据整体认识，旨在搞清变量和变量间的关系
    def cognition(self):
        pass
    #1.2 数据质量分析，旨在关注缺失值、重复值、异常值、歧义值、正负样本比例
    def qualityAnalysis(self):
        pass
    #1.3 数据统计量分析，旨在对单变量、俩变量、多变量进行统计分析
    def staticsAnalysis(self):
        pass
    #1.4 数据分布分析，旨在频数，时间、空间进行统计分布
    def distributionAnalysis(self):
        pass

#********************************************************#
    '''
    2. 数据预处理
    '''
    #2.1 数据清洗
    def pure(self):
        pass
    #2.2 数据集成
    def integration(self):
        pass
    #2.3 数据重采样
    def resample(self):
        pass
    #2.4 数据变换
    def alternation(self):
        pass
    #2.5 数据规范化
    def normalization(self):
        pass

#********************************************************#
    '''
    3. 特征构造
    '''
#********************************************************#
    '''
    4. 特征选择
    '''
#********************************************************#
    '''
    5. 模型选择
    '''
#********************************************************#
    '''
    6. 模型融合
    '''

if __name__ == "__main__":
    pass
