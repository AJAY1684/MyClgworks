import pandas as pd
import xlrd
import matplotlib.pyplot as plt
import xlwt

loc = ("C:\\Users\\Sompalli\\Desktop\\cropsdata\\CropsDataFile.xlsx")
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

for i in range(sheet.nrows):
    print(sheet.cell_value(i,0)+"--"+sheet.cell_value(i,1)+"--",sheet.cell_value(i,2),"--"+sheet.cell_value(i,3)+"---"+sheet.cell_value(i,4)+"---",sheet.cell_value(i,5),"---",sheet.cell_value(i,6))


x=list()
y = list()
print("enter any crop you want to know")
crop_name = input()

p=0
for j in range(1997,2011):
    x.append(j)
    for i in range(sheet.nrows):
        if(sheet.cell_value(i,2) == j):
            if(sheet.cell_value(i,4) == crop_name):
                p = p + sheet.cell_value(i,6)
    y.append(p)
    p=0 

plt.bar(x,y)
plt.title('CROP PRODUCTION FROM 1997 TO 2010')
plt.xlabel('DATE')
plt.ylabel('Production')
plt.show()
