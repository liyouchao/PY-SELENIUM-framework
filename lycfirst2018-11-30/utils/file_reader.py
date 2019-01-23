import yaml,os
from xlrd import open_workbook

class YamlReader:
    def __init__(self,yamlf):
        if os.path.exists(yamlf):  #判断这个yamlf是否存在
            self.yamlf = yamlf
        else:
            raise FileExistsError("文件不存在！")
        self._data = None

    @property  #私有属性
    def data(self):
        # 如果是第一次调用data，读取yaaml文档，否则直接返回之前保存数据
        if not self._data:
            with open(self.yamlf,'rb') as f:  #已二进制文件只读形式打开文件赋值到f:，然后关闭 with open()...,打开后关闭
                #此方法的好处可以避免内存溢出
                self._data = list(yaml.safe_load_all(f)) #load后是个generator，用list组织成列表
                #yaml.load接受一个字节字符串，一个Unicode字符串，一个打开的二进制文件对象或一个打开的文本文件对象。加_all
                #是全部
        return self._data

class SheetTypeError(Exception):
    pass

class ExcelReader:
    """
       读取excel文件中的内容。返回list。

       如：
       excel中内容为：
       | A  | B  | C  |
       | A1 | B1 | C1 |
       | A2 | B2 | C2 |

       如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
       [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

       如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
       [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

       可以指定sheet，通过index或者name：
       ExcelReader(excel, sheet=2)
       ExcelReader(excel, sheet='BaiDuTest')
       """
    def __init__(self,excel,sheet=0,title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileExistsError('文件不存在！')
        self.sheet = sheet
        self.title_line = title_line
        self._data =list()

    @property
    def data(self):
        if not self._data: #如果不为空则执行
            workbook = open_workbook(self.excel) #打开这个Excel
            if type(self.sheet) not in [int,str]: #如果表格没有int,str类型
                raise SheetTypeError('please pass in int or str'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet) #如果是int通过索引获取
            else:
                s = workbook.sheet_by_name(self.sheet)#如果是str通过名字获取

            if self.title_line:
                title = s.row_values(0)  #如果首行位title则
                # excel表格如下:
                #  | title1 | title2 |
                #  | value1 | value2 |
                #  | value3 | value4 |
                #  如果title_line=True [{"title1": "value1", "title2": "value2"}, {"title1": "value3", "title2": "value4"}]
                #  如果title_line=False [["title1", "title2"], ["value1", "value2"], ["value3", "value4"]]

                for col in range(1,s.nrows):#依次里面其余行，与首行组成dict，拼到sele。_data中
                    self._data.append(dict(zip(title,s.row_values(col))))
            else:
                for col in range(0,s.nrows):#编历所有行，拼到SELF._DATA中
                    self._data.append(s.row_valuse(col))

        return  self._data

if __name__ == '__main__':
    y = 'E:\资料\自学资料\学习资料\py文件\lycfirst2018-11-30\config\config.yml'
    reader = YamlReader(y)
    print(reader.data)

    e = 'E:/资料/自学资料/学习资料/py文件/lycfirst2018-11-30/data/baidu.xlsx'
    reader = ExcelReader(e, title_line=True)
    print(reader.data)
    for d in reader.data:
        print(d['search'])

