import pyautogui
import time

msg = input("Enter the message: ")
n = input("How many times?: ")
delay = int(input("Enter the delay: "))

print("Straing the program!")

time.sleep(1)

while(delay != 0):
	print("T minus " + str(delay) + " seconds")
	time.sleep(1)
	delay = delay - 1

print("Spamming!!")

for i in range(0,int(n)):
	pyautogui.typewrite(msg + "\n")

print("Done!")
print("Developed by Chathusha Mendis")