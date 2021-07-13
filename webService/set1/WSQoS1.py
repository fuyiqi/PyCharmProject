import numpy as np    # Python中进行数值计算的库
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


class WebServiceQos():
    def __init__(self,path_str,type_str):
        self.path_str = path_str
        self.rawDF = pd.read_csv(self.path_str,delimiter='\t')


    def cognition(self):
        pass

    def qualityAnalysis(self):
        pass














if __name__ == "__main__":

    #rtMatrix = WebServiceQos('../../data/webService/dataset1/rtMatrix.txt')
    usersInfo = WebServiceQos('../../data/webService/dataset1/userlist.txt')
    print(usersInfo.rawDF)
