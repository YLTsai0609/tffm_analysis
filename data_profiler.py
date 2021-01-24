'''
support 

input record-base, user, item?
profling 

1. number of record / users (mean, groupby count)
2. count unique users and unique items
3. count unseen users between two dataset
4. count unseen items between two dataset

'''
import numpy as np
from nptyping import NDArray


def summary_x(input_data: NDArray):
    print('Data Shape : ', input_data.shape)
    print('Non Zero Ratio : ', np.mean(input_data != 0))
