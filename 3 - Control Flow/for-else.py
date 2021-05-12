successful = False
for number in range(3):
    print("Attemt ", number + 1)
    if successful:
        print("Successful")
        break

else:  # after exiting loop this will be excuted
    print(f"Failed to determine after {number+1} attempts")
