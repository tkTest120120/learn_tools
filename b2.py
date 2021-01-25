# doc ghi file exel
import openpyxl


def get_value_excel(filename, cellname):
    wb = openpyxl.load_workbook(filename)
    Sheet1 = wb["Trang_tính1"]
    wb.close()
    return Sheet1[cellname].value

def update_value_excel(filename, cellname, value):
    wb = openpyxl.load_workbook(filename)
    Sheet1 = wb["Trang_tính1"]
    Sheet1[cellname].value = value
    wb.close()
    wb.save(filename)
    print("update sucessfully")

# demo1 ( get data cell ) Lấy dữ liệu từ file
# filename = 'test.xlsx'
# cellname = 'D1'
# data_cell = get_value_excel(filename, cellname)
# print(f'data_cell ( {cellname} ) = ', data_cell)

 # demo2 ( update data cell ) Cập nhật dữ liệu trong file
# filename = 'test.xlsx'
# cellname = 'D1'
# new_value='ok men'
# update_value_excel(filename, cellname, new_value)


# demo3
# F7 => F17
# G7 =>G17

col_name_acc = "D"
col_name_pass = "E"
filename = 'test.xlsx'

for i_row in range(2, 11):
    cell_name_acc = "%s%s" % (col_name_acc, i_row)
    cell_name_pass = "%s%s" % (col_name_pass, i_row)

    account = get_value_excel(filename, cell_name_acc)
    password = get_value_excel(filename, cell_name_pass)
    print('current username = ', account)
    print('current password = ', password)
    account = update_value_excel(filename , cell_name_acc , f"xem {i_row}")
    password = update_value_excel(filename , cell_name_pass , f"xem {i_row}")

    # hamLogin(account,password)
    input('pause')
