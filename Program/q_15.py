import time

wait_time = 1
max_retries = 5
attemtes = 0

while attemtes < max_retries:
       print("Attempt" , attemtes + 1 , "Wait Time " , wait_time)

       time.sleep(wait_time)
       wait_time *= 2
       attemtes += 1
