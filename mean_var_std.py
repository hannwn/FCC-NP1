import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    # list.sort()
    list_np = np.reshape(np.array(list),(3,3))

    mean_ax1 = list_np.mean(axis = 0).tolist()
    mean_ax2 = list_np.mean(axis = 1).tolist()
    mean_flat = list_np.mean().tolist()

    var_ax1 = list_np.var(axis = 0).tolist()
    var_ax2 = list_np.var(axis = 1).tolist()
    var_flat = list_np.var().tolist()

    std_ax1 = list_np.std(axis = 0).tolist()
    std_ax2 = list_np.std(axis = 1).tolist()
    std_flat = list_np.std().tolist()

    max_ax1 = list_np.max(axis = 0).tolist()
    max_ax2 = list_np.max(axis = 1).tolist()
    max_flat = list_np.max().tolist()

    min_ax1 = list_np.min(axis = 0).tolist()
    min_ax2 = list_np.min(axis = 1).tolist()
    min_flat = list_np.min().tolist()

    sum_ax1 = list_np.sum(axis = 0).tolist()
    sum_ax2 = list_np.sum(axis = 1).tolist()
    sum_flat = list_np.sum().tolist()

    calculations = {
        'mean' : [mean_ax1, mean_ax2, mean_flat],
        'variance' : [var_ax1, var_ax2, var_flat],
        'standard deviation' : [std_ax1, std_ax2, std_flat],
        'max' : [max_ax1, max_ax2, max_flat],
        'min' : [min_ax1, min_ax2, min_flat],
        'sum' : [sum_ax1, sum_ax2, sum_flat]
    }

    return calculations
