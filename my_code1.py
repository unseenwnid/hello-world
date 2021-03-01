import time
import datetime

#获取今天的日期
today = datetime.date.today()
#获取当前的时间
time = time.strftime('%H:%M:%S',time.localtime(time.time()))
d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '9:00', '%Y-%m-%d%H:%M')
d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '18:00', '%Y-%m-%d%H:%M')

#现在的时间
n_time = datetime.datetime.now()

print("Hello World")
print(d_time)

if n_time > d_time and n_time < d_time1:
    print("Hi,nice to meet you!")


print(f"The date is: {today}")
print(f"The time is: {time}")
    

