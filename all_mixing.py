#Mixing
list1=[1,2,3,"shubham"]
tuple1="aglawe",4,5,6
set1={7,8,9,"x"}
dict1={"y":"z",10:11}

l=[*list1,*tuple1,*set1,{**dict1}]
print(f"In List:{l}")
t=*list1,*tuple1,*set1,{**dict1}
print(f"In Tuple:{t}")
s={*list1,*tuple1,*set1,*dict1}
print(f"In Set:{s}")
d={**dict1}
print(f"In Dictionary:{d}")
