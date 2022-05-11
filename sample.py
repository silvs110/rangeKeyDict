from RangeKeyDict import RangeKeyDict


range_dict = RangeKeyDict()
range_dict[(0, 10)] = 5
range_dict[(-5, -1)] = 1
range_dict[(11, 13)] = 0
print(range_dict) # {(0, 10): 5, (-5, 0): 1, (10, 13): 0}
print(range_dict[0]) # 5
print(range_dict[12]) # 0
print(range_dict[-5,-1]) # 1
range_dict[(0,10)] = 100
print(range_dict[0]) # 100
range_dict[-5,-1] = 35
print(range_dict[-3]) #35