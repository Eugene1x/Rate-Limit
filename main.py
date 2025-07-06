import requests
import time
from collections import deque
import tkinter as tk
from tkinter import Label, Button

class RateLimit:
    def __init__(self, maxRequest, slidingWindow):
        self.slidingWindow = slidingWindow
        self. maxRequest = maxRequest
        self.request = deque()

    
    def allowRequest(self):
        currentTime = time.time()

        while self.request and currentTime - self.request[0] >= self.slidingWindow:
            self.request.popleft()

        if len(self.request) < self.maxRequest:
            self.request.append(currentTime)
            return True
        return False



Limit = RateLimit(maxRequest=5, slidingWindow=10)

root = tk.Tk()
root.title("Eugene Rate Limit")
root.geometry("300x400")

statusLabel = Label(root, text="Click here to make a request", font=("Arial",14))
statusLabel.pack(pady=20)


requestCount = 0

def makeRequest():
    global requestCount
    if Limit.allowRequest():
        requestCount += 1
        statusLabel.config(text=f"Request {requestCount} Allowed", fg="green")
    else:
        statusLabel.config(text=f"Request not allowed", fg="red")


requestButton = Button(root, text="Make Request", command=makeRequest, font=("Arial", 12))
requestButton.pack(pady=20)

root.mainloop()

