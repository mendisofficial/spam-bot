import pyautogui
import time

msg = input("Enter the message: ")
n = int(input("How many times?: "))
count_down = int(input("set a countdown in seconds: ")
delay = int(input("Enter the delay: "))

print("Straing the program!")

time.sleep(1)

# Use a for loop instead of a while loop for the countdown
for _ in range(count_down):
	print(f"Starting in {count_down} second(s))
 	count_down -= 1
  	time.sleep(1)
  



print("Spamming!!")

for _ in range(0):
	pyautogui.typewrite(msg + "\n","interval=delay)

print("Done!")
print("Developed by Chathusha Mendis, forked by chamodhk")
