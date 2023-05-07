def binarysearch(arr,low,high,x):
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarysearch(arr,low,mid-1,x)
        else:
            return binarysearch(arr,mid+1,high,x)
    else:
        return -1
array=[]
num=int(input("Enter the size of array:"))
for n in range(num):
    numbers=int(input("Enter the list of elements:"))
    array.append(numbers)
x=int(input("Enter number to search in list"))
result=binarysearch(array,0,len(array)-1,x)
if result!=-1:
    print("Element is present at index",str(result))
else:
    print("Element is not present in array")
