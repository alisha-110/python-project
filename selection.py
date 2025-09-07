def selectionsort(Lst):
    n=len(Lst)
    for i in range(n):
        least=i
        for k in range(i+1,n):
            if Lst[k] < Lst[least]:
                least=k
        if least != i:
             swap(Lst,least,i)
             print(f"Pass{i+1}:{Lst}")
def swap(A,x,y):
    tmp=A[x]
    A[x]=A[y]
    A[y]=tmp
print("===SELECTION SORT===")
num=int(input("Enter the number of element:"))

Lst=[]
for i in range(num):
    element=int(input(f"Enter Element{i+1}:"))
    Lst.append(element)
print(f"\nOriginal List:{Lst}\n")
selectionsort(Lst)
print(f"\n sorted list:{Lst}")
        
