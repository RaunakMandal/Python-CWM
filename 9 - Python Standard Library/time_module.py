import time
print(time.time())  # Time elapsed After JAN 1st 1970


def send_emails():
    for i in range(500000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)
