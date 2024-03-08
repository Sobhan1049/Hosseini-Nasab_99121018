import numpy as np

np.random.seed(99121018)
random_vector = np.random.randint(0, 21, 10000)
counts = np.bincount(random_vector, minlength=21)

for i, count in enumerate(counts):
    print(f' تعداد تکرار {i}: {count}')
