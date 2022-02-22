string = "Welcome to Sirius, India team! "
# To Convert string to list 
string_list = list(string.split(" "))
# To find maximum in the list 
max_str = max(string_list, key=len)
# To print output in same line
print(max_str,end=" ")
# To Print length of maximum string
print(len(max_str))

