# li = [i for i in range(1, 101) if i%10==3 or i%10==6 or i%10==9 or ((i//10)%3==0 and i//10 != 0)]
li = [i for i in range(1, 101) if i%10 in [3,6,9] or ((i//10)%3==0 and i//10 != 0)]
print(li)