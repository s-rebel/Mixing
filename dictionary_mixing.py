#Mixing
dict1={1:2,3:4,"shubham":"aglawe"}
dict2={"X":"Y",5:6,7:8}
d={**dict1,**dict2}
print(d)


#Output:{1: 2, 3: 4, 'shubham': 'aglawe', 'X': 'Y', 5: 6, 7: 8}