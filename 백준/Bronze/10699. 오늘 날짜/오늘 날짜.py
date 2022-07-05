from datetime import datetime
y = str(datetime.today().year)
m = str(datetime.today().month)
d = str(datetime.today().day)
yyyy=y.zfill(4)
mm=m.zfill(2)
dd=d.zfill(2)
print(yyyy,"-",mm,"-",dd,sep="")