fru = ['apples', 'bananas', 'tofu', 'cats', 'hearts', 'tea']
fr_massage = ''
for i in range(len(fru) - 1):
  fr_massage += fru[i] + ', '
print(fr_massage + 'and ' + fru[-1])
