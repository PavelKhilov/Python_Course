values = [1, 32, 54, 'srthwe']

tranformation = lambda x: x
transformation_values = list(map(tranformation, values))

if values == transformation_values:
    print('ok')
else:
    print('fail')