index=(12,22,55,66,88,98,4624,33)
count_even =0
count_odd =0
for x in index:
    if x %2==0:
        count_even+=1
    else:
        count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)


count_even=0
count_odd =0  
count_prime=0
while index<20:
    if index%2==0:
        count_even+=1
    elif index%3==0:
        count_odd+=1
    elif count_prime%2!=0:
        count_prime+=1
    else:
        print("none of intergers")
print("total number even number",count_even)
print("total number odd number",count_odd)
print("total number prime number",count_prime)