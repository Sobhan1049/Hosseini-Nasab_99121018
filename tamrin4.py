import numpy as np
from sklearn.metrics import f1_score


# All students
N = 30

# Rejected
m = 8

# Accepted
p = N - m

# random guess for accepted
np.random.seed(30)
y_true = np.array([1] * m + [0] * p)
y_pred_random = np.random.choice([0, 1], size=N)


f1_random = f1_score(y_true, y_pred_random, pos_label=0)
print(f"F1 Score for random guess: {f1_random}")



# always pass for accepted
y_pred_always_pass = np.zeros(N)


f1_always_pass = f1_score(y_true, y_pred_always_pass, pos_label=0)
print(f"F1 Score for always pass: {f1_always_pass}")



print("*"*50)


# random guess for Rejected
np.random.seed(30)
y_true = np.array([1] * m + [0] * p)
y_pred_random = np.random.choice([0, 1], size=N)


f1_random = f1_score(y_true, y_pred_random, pos_label=1)
print(f"F1 Score for random guess: {f1_random}")



# always pass for rejected
y_pred_always_pass = np.zeros(N)


f1_always_pass = f1_score(y_true, y_pred_always_pass, pos_label=1)
print(f"F1 Score for always pass: {f1_always_pass}")