import ray
import time

ray.init(include_dashboard=False)

@ray.remote
def square(x):
    time.sleep(2)
    return x * x

futures = [square.remote(i) for i in range(10)]
results = ray.get(futures)
print(results)