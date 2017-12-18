#!/usr/bin/python


import math
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []
    dataLength = []

    ### your code goes here
    tenPercent = (len(predictions) // 10)
    for index, v in enumerate(predictions):
        k = math.pow(v-net_worths[index], 2)
        dataLength.append(k)
        cleaned_data.append((ages[index], net_worths[index], k))

    for i in range(tenPercent):
        index = dataLength.index(max(dataLength))
        del cleaned_data[index]
        dataLength.remove(max(dataLength))

    return cleaned_data

