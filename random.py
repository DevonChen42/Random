print("Computer will begin to shut down in...")
count = 11
import time
while True:
	count = count - 1
	print (count)
	time.sleep(1)
	if count < 1: break
print ("Computer will now shutdown")
