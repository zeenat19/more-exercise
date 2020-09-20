def function(list1,list2):
    i=0
    list3=[]
    while i<len(list1):
        a=list1[i]list2[i]
        list3.append(a)
        if list1[i]==list2:
            print(list3[i])
        i=i+1
list1=[1,5,10,16,20,3]
list2=[1,2,10,13,16]
function(list1,list2)

