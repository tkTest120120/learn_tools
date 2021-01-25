from os import listdir
from os.path import isfile, join
import os
import playsound
mypath = r"D:\testcode\youtube\nhac" + "\\"
ds = listdir(mypath)
td = {}
dem = 0
ds_ten = [i.split(".mp3") for i in ds]
# for i in ds:
#     # print("Đang phát bài :  " + i)
#     # td[dem] = i
#     # dem += 1

    # os.rename(mypath + i, mypath + "file_" + str(dem) + ".mp3")
#     # with open('test.txt' , 'a+' , encoding="utf-8") as file:
#     #     file.write(i)
#     #     file.close()
#     # pass
#     os.system(mypath + i)
#     # playsound.playsound(mypath + "/" + i)
# print(td)
for i in ds:
    os.system(mypath + i)