input_string = "aabbbcccc"
# initializing two pointers
i = 0
j = i + 1 
count = 1
ans = ""
# checking if pointer two is less than len of input_string
while(j < len(input_string)):
    # counting char
    if (input_string[i] == input_string[j]):
        count += 1 
    else:
        # Appending count if a char and the next char is not same 
        ans += input_string[i] + str(count)
        # reinitialising count 
        count = 1
    # incrementing since we use while loop 
    i = i + 1
    j = j + 1
# for end case
ans += input_string[i] + str(count)
print(ans)