import time
from datetime import datetime

hosts_path = r"/private/etc/hosts" # host path
redirect = "120.0.0.1" # redirect server address

website_list = ["www.facebook.com", "facebook.com"] # the website to be blocked

# >>> from datetime import datetime
#>>> datetime.now()
# output --- datetime.datetime(2019, 11, 23, 7, 51, 58, 2519)
# check the date  

#compare the datetime
#datetime.now() < datetime(2019,11,23,7)
#False

while True:
    if datetime(datetime.now().year, datetime.now().month, datetime.now().day,8) < datetime.now() < datetime(datetime.now().year, datetime.now().month, datetime.now().day,16):
        print("working hours !!!")
    else:
        print("Fun hours !!!")
        
    time.sleep(5) # this will print 1 in every 5 seconds

    