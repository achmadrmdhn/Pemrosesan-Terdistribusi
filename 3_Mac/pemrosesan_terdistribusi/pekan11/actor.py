import ray
@ray.remote
class Counter:
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1
    def get(self):
        return self.value
counter = Counter.remote()
counter.increment.remote()
print(ray.get(counter.get.remote()))