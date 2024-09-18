import xlwt
import xlrd
wb=xlwt.Workbook()
#C:\Users\Kangyl\Desktop>
# (行，列)
sh=wb.add_sheet("电影")
wt=sh.write(0,0,"名字")
# wt=sh.write(0,1,"票房")
# wt=sh.write(1,0,"复仇者联盟")
# wt=sh.write(2,0,"奇异博士")
# wt=sh.write(1,1,200)
# wt=sh.write(2,1,201)

# wt=sh.write(0,0,"复仇者联盟")
# wt=sh.write(0,0,"复仇者联盟")
wb.save('C:\\Users\\Kangyl\\Desktop\\电影列表.xls')
