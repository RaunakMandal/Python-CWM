import sys
print(sys.argv)

if(len(sys.argv) == 1):
    print("USAGE: python3 cmdline.py <data>")
else:
    data = sys.argv[1]
    print("data:", data)
