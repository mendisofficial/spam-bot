import pyautogui
import time

msg = input("Enter the message: ")
n = int(input("How many times?: "))
count_down = int(input("set a countdown in seconds: "))
delay = int(input("Enter the delay: "))

print("Straing the program!")

time.sleep(1)

# Use a for loop instead of a while loop for the countdown
for _ in range(count_down,0,-1):
    print(f"starting in {_} second(s)")
    time.sleep(1)
    

  



print("Spamming!!")

for i in range(n):
    pyautogui.typewrite(msg+"\n")
    time.sleep(delay)
    
    

print("Done!")
print("Developed by Chathusha Mendis, forked by chamodhk")
