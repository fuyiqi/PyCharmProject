import numpy as np    # Python中进行数值计算的库
from matplotlib import pyplot as plt
import matplotlib
import pandas as pd    # Python中进行数据处理的库
import warnings
warnings.filterwarnings('ignore') #  忽略弹出的warnings

#显示所有列(参数设置为None代表显示所有行，也可以自行设置数字)
pd.set_option('display.max_columns',None)
#显示所有行
pd.set_option('display.max_rows',None)
#设置数据的显示长度，默认为50
pd.set_option('max_colwidth',200)
#禁止自动换行(设置为Flase不自动换行，True反之)
pd.set_option('expand_frame_repr', False)


class QoSMatrix():
    def __init__(self,path_str):
        self.path_str = path_str
        self.DF = self.markNull_rawDF()

    def markNull_rawDF(self):
        rawDF = pd.read_csv(self.path_str, delimiter='\t')
        bool_array = rawDF.applymap(lambda x: x!=-1 )
        return rawDF[bool_array]

class QoSItem():
    def __init__(self,path_str):
        self.path_str = path_str
        self.DF = self.load_items()

    def load_items(self):
        rawDF = pd.read_csv(self.path_str, delimiter='\t')
        # 删除第一列
        rawDF = rawDF.drop([0]).reset_index(drop=True)
        # 列名修饰
        rawDF.rename(columns=lambda x:x.replace('[','').replace(']',''),inplace=True)
        return rawDF










if __name__ == "__main__":

    '''
    rtMatrix = QoSMatrix('../../data/webService/dataset1/rtMatrix.txt')
    print(rtMatrix.DF)
    '''
    users = QoSItem('../../data/webService/dataset1/userlist.txt');

    #print(users.DF)

    #users.DF['Country'].value_counts().plot()
    webServices = QoSItem('../../data/webService/dataset1/wslist.txt');
    print(webServices.DF)


