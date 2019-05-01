#SMSLogAnalyzer v0.1
#mkysoft@gmail.com
import appuifw
import logs
import time
#fatura günüm
myftrdy = 23
bgn=time.localtime()
if bgn[2] <= myftrdy: 
    ayilk=bgn[1]-1
    ayson=bgn[1]
else:
    ayilk=bgn[1]
    ayson=bgn[1]+1
if ayilk==0:
    ayilk=12
if ayson==13:
    ayson=1    
smslgs = logs.sms(mode='out')
myht = 0
for line in smslgs:
    trh = time.localtime(line['time'])
    ay=trh[1]-1
    if (trh[1]==ayilk and trh[2]>myftrdy) or (trh[1]==ayson and trh[2]<=myftrdy):
        myht=myht+1
msg='SMS Sayısı: %d' % myht
appuifw.note(msg.decode('u8'), 'info')