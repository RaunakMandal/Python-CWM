try:
    file = open("cleaningup.py")
except Exception as e:
    print(e)
finally:  # always executed if there is error or not
    file.close()
