list = [1,2,3,2,1]

copy_list = list.copy()
copy_list.reverse()

if(list == copy_list):
    print("List is palindrom")
else:
    print("list is not palindrom")