message = "Hemlo"  # global


def greet(name):
    message = "a"  # local


def send_mail(name):
    global message  # changing value here
    message = "b"  # do


greet("Hallo")
print(message)
