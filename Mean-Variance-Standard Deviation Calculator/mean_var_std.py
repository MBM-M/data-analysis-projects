import numpy as np

def calculate(list):
  if len(list) != 9:
    print("List must contain nine numbers.")
    return

  matrix = np.array(list).reshape(3,3)

  mean_flat = np.mean(matrix).tolist()
  mean_axis0 = np.mean(matrix, axis=0).tolist()
  mean_axis1 = np.mean(matrix, axis=1).tolist()
  mean = [mean_axis0, mean_axis1, mean_flat]

  var_flat = np.var(matrix).tolist()
  var_axis0 = np.var(matrix, axis=0).tolist()
  var_axis1 = np.var(matrix, axis=1).tolist()
  var = [var_axis0, var_axis1, var_flat]

  std_flat = np.std(matrix).tolist()
  std_axis0 = np.std(matrix, axis=0).tolist()
  std_axis1 = np.std(matrix, axis=1).tolist()
  std = [std_axis0, std_axis1, std_flat]

  max_flat = np.max(matrix).tolist()
  max_axis0 = np.max(matrix, axis=0).tolist()
  max_axis1 = np.max(matrix, axis=1).tolist()
  max = [max_axis0, max_axis1, max_flat]

  min_flat = np.min(matrix).tolist()
  min_axis0 = np.min(matrix, axis=0).tolist()
  min_axis1 = np.min(matrix, axis=1).tolist()
  min = [min_axis0, min_axis1, min_flat]

  sum_flat = np.sum(matrix).tolist()
  sum_axis0 = np.sum(matrix, axis=0).tolist()
  sum_axis1 = np.sum(matrix, axis=1).tolist()
  sum = [sum_axis0, sum_axis1, sum_flat]

  dict = {
    'mean': mean,
    'variance' : var,
    'standard deviation' : std,
    'max' : max,
    'min' : min,
    'sum' : sum
  }

  for key, value in dict.items():
    print(f"{key}: {value}")