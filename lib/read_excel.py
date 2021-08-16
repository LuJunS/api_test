import xlrd
import sys
sys.path.append('..')

# wb = xlrd.open_workbook("test_dop_data.xlsx")  # 打开excel
# sh = wb.sheet_by_name("TestCreateGroup")  # 按工作簿名定位工作表
# print(sh.nrows)  # 有效数据行数
# print(sh.ncols)  # 有效数据列数
# print(sh.cell(0, 0).value)  # 输出第一行第一列的值`case_name`
# print(sh.row_values(0))  # 输出第1行的所有值（列表格式）
#
# # 将数据和标题组装成字典，使数据更清晰
# print(dict(zip(sh.row_values(0), sh.row_values(1))))
#
# # 遍历excel,打印所有的数据
# for i in range(sh.nrows):
#    print(sh.row_values(i))

def excel_to_list(data_file,sheet):
    data_list = [] #新建个空列表，承装所有数据
    wb = xlrd.open_workbook(data_file) #打开excel
    sh = wb.sheet_by_name(sheet) #获取工作簿
    header = sh.row_values(0) #获取标题行数据
    for i in range(1,sh.nrows):  #跳过标题行，从第二行获取数据
        d = dict(zip(header,sh.row_values(i)))  #将标题和每行数据组装成字典
        data_list.append(d)
    return data_list

def get_test_data(data_list,case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:
            return case_data

if __name__ == '__main__':   # 测试一下自己的代码
    data_list = excel_to_list("../data/test_dop_data.xlsx", "TestCreateGroup")  # 读取excel，TestCreateGroup工作簿的所有数据
    case_data = get_test_data(data_list, 'test_create_Group_ture')  # 查找用例'test_create_Group_turel'的数据
    print(case_data)