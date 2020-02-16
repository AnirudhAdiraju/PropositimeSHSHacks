import time

class Timer:
    def __init__(self, seconds):
        self.seconds = seconds

    def timer(self):
        start = time.time()
        while (time.time()-start < self.seconds):
            continue
        return "Time is up!"

# Tester
timer1 = Timer(5)

print("Start")
timer1.timer()
print("End")