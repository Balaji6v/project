list1 = [4,2,-3,1,6]
sub_list = []
for i in range(len(list1)):
    for j in range(i + 1 , len(list1)+ 1):
        sub=list1[i:j]
        if sum(sub) == 0:
            sub_list.append(sub)
            print(sub_list)
        #0:0,0:1,0:2,0:3,0:4,0:5
