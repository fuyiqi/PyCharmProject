#coding:utf8

import matplotlib.pyplot as plt
#正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
#显示符号
plt.rcParams['axes.unicode_minus'] = False
import pandas as pd

def get_txt_content(file_path_str):

    record_list = []
    with open(file_path_str,'r',encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            word_list = line.split('\t')
            record_list.append([word for word in word_list])

    return record_list


def get_dep_level_distribution(record_list):
    dep_level_distribution = {}
    for record in record_list:
        person = record[0]
        dep = record[1]
        level = record[4]
        dep_flag = dep_level_distribution.get(dep)
        if (dep_flag is None):
            dep_level_distribution[dep] = {}
            dep_level_distribution[dep][level] = []
            dep_level_distribution[dep][level].append(person)
        else:
            level_flag = dep_flag.get(level)
            if (level_flag is None):
                dep_level_distribution[dep][level] = []
                dep_level_distribution[dep][level].append(person)
            else:
                dep_level_distribution[dep][level].append(person)
    for k, v in dep_level_distribution.items():
        for level, people_list in v.items():
            sorted(people_list)

    return dep_level_distribution


def get_subject_level_distribution(record_list):
    distribution = {}
    for record in record_list:
        person = record[0]
        subject = record[3]
        level = record[4]
        subject_flag = distribution.get(subject)
        if (subject_flag is None):
            distribution[subject] = {}
            distribution[subject][level] = []
            distribution[subject][level].append(person)
        else:
            level_flag = subject_flag.get(level)
            if (level_flag is None):
                distribution[subject][level] = []
                distribution[subject][level].append(person)
            else:
                distribution[subject][level].append(person)
    for k, v in distribution.items():
        for level, people_list in v.items():
            sorted(people_list)

    return distribution


def str_list2str(str_list):
    res_str = ''
    if(str_list is None):
        return res_str
    for s in str_list:
        res_str+=s+','
    return res_str[:-1]

def count_strList(str_list):
    if(str_list is None):
        return 0
    else:
        return len(str_list)

def generate_Excel(record_list,dep_df,subject_df):


    output_dir_path = 'result/ditribition.xls'
    excel_writer = pd.ExcelWriter(output_dir_path)



    dep_df.to_excel(excel_writer, sheet_name='dep_distribution', index=False)
    subject_df.to_excel(excel_writer, sheet_name='subject_distibution', index=False)
    excel_writer.save()
    excel_writer.close()


if __name__ == '__main__':
    record_list = get_txt_content('data/pub.txt')

    dep_data = []
    for k, v in get_dep_level_distribution(record_list).items():
        tmp = []
        tmp.append(k)
        tmp.append(count_strList(v.get('初级')))#count_strList,str_list2str
        tmp.append(count_strList(v.get('中级')))
        tmp.append(count_strList(v.get('高级')))
        dep_data.append(tmp)
    dep_df = pd.DataFrame(dep_data, columns=['部门', '初级', '中级', '高级'])


    subject_data = []
    for k, v in get_subject_level_distribution(record_list).items():
        tmp = []
        tmp.append(k)
        tmp.append(count_strList(v.get('初级')))
        tmp.append(count_strList(v.get('中级')))
        tmp.append(count_strList(v.get('高级')))
        subject_data.append(tmp)

        '''

        low = v.get('初级')
        medium = v.get('中级')
        high = v.get('高级')
        low_num = 0 if low is None else len(low)
        medium_num = 0 if medium is None else len(medium)
        high_num = 0 if high is None else len(high)
        print(k + '@' + str(low_num) + '@' + str(medium_num) + '@' + str(high_num))
        '''
    subject_df = pd.DataFrame(subject_data, columns=['技术序列', '初级', '中级', '高级'])
    #generate_Excel(record_list,dep_df,subject_df)

    dep_df.plot(x='部门',y=['初级', '中级', '高级'], kind="bar")
    plt.show()