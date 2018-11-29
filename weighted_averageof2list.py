weights = [0.5, 0.8, 0.7, 0.8, 1.0]
values = [10, 20, 10, 10, 30]
average = sum([weight[i] * values[i] for i in range(len(weight))])/sum(values)
zip_average = sum ([x * y for x,y in zip(weights,values)]) / sum(values)
print (average, zip_average)  # 0.825 0.825

  