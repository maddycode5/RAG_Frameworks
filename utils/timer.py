import time

class Timer:

    def __enter__(self):
        self.start =time.time()
    
    def __exit__(self, *args):
        print(f"Execution Time : {time.time() - self.start:.2f} seconds")
        