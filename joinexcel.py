import pandas as pd
import os

# 设定工作路径和输出的excel文件名，默认输出的excel就在工作路径中
workpath='C:\\Users\\89638\\Desktop\\退库\\'
output_excel_name='result.xlsx'
sheet_names = ["Export"]   #注意sheet_names是列表，有几个sheet就列几个


if os.path.exists(workpath + output_excel_name):
    os.remove(workpath + output_excel_name)

# 将excel文件名称放入列表
xlsx_names = [x for x in os.listdir(workpath) if x.endswith(".xlsx")]
print(xlsx_names)
writer = pd.ExcelWriter(workpath+output_excel_name,engine='openpyxl')

num = 1
for sheet_name in sheet_names:
    df = None
    for xlsx_name in xlsx_names:
        _df = pd.read_excel(workpath+xlsx_name, sheet_name=sheet_name)
        if df is None:
            df = _df
        else:
            df = pd.concat([df, _df], ignore_index=True)
    # 下面的保存文件处填写writer，结果会不断地新增sheet，避免循环时被覆盖
    df.to_excel(excel_writer=writer, sheet_name=sheet_name, encoding="utf-8", index=False)
    print(sheet_name + "表保存成功！共%d个表，这是第%d个。" % (len(sheet_names),num))
    num += 1
writer.save()
writer.close()