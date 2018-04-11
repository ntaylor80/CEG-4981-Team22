import time
import requests
import base64

with open("test.JPG", "rb") as imageFile:
    img_str = base64.b64encode(imageFile.read()).decode("utf-8")

# time.sleep(10)  # or do something more productive
services = list()
services.append(("/drone/available", dict()))
services.append(("/availability", {"lot": "1"}))
services.append(("/drone/update", {"image": img_str, "lot": "1"}, 0))
# time.sleep(10)  # or do something more productive

total_requests = 0
total_request_time = 0
total_max = 0
total_min = 100
iterations = 100
total_services = 0
for service in services:
    total_time = 0
    min = 100
    max = 0
    total_services += 1
    for i in range(iterations):
        start = time.time()
        foo = requests.post("http://127.0.0.1:5000" + service[0], json=service[1]).json()
        done = time.time()
        elapsed = done - start
        total_time += elapsed
        if elapsed < min:
            min = elapsed
        if elapsed > max:
            max = elapsed
    if min < total_min:
        total_min = min
    if total_max < max:
        total_max = max
    print("{} calls to {} took an average of {} ms with a maximum of {} and a minimum of {}".format(iterations,service[0],total_time/iterations,max,min))
    total_request_time += total_time

print("The average of all web server calls was {}ms with a maximum of {} and a minimum of {}".format(total_time/(iterations*total_services),total_max,total_min))