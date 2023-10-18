import threading
import time
class Hello(threading.Thread):             #inherit Thread module from threading
    def run(self):         # run() method is used to create thread
        for i in range(5):
            print("Hello")
            time.sleep(0.2)      #time taken between two threads to execute simultaneously

class Hi(threading.Thread):                    #creating another thread
    def run(self):
        for i in range(5):
            print("Hi")
            time.sleep(0.2)

h1 = Hello()
h2 = Hi()

h1.start()      #start() method is used to execute the thread
h2.start()