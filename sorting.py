#defining the function that takes one argument
def sorting(taken_list):
#assigning  a variable to an empty dictinary using the keyword "dict"
    created_dict=dict()
#assigning variables to empty lists 
    even_list=[]
    odd_list=[]
    char_list=[]
#The conditional logic using The isinstance() function that checks if the object (first argument) is an instance or subclass of classinfo class (second argument).


    if not isinstance(taken_list,list):
#outputting  a message "Invalid input"  when the condtion is not satisfied
        print("Invalid input")
    if not taken_list:
        created_dict["odds"] = odd_list
        created_dict["evens"] = even_list
        created_dict["chars"] = char_list
        print(created_dict)
    for x in taken_list:
        if isinstance(x,int):
            if x % 2 == 0:
                even_list.append(x)
            else:
                odd_list.append(x)
        elif isinstance(x,str):
            char_list.append(x)
#sorting the items inside the lists(values) of the keys 
    created_dict["evens"] = sorted(even_list)
    created_dict["odds"] = sorted(odd_list)
    created_dict["chars"] = sorted(char_list)
#outputting the dictionary that has been created    
    print(created_dict)

print(sorting([1,2,4,6, 3, 5, 'a', 'b']))