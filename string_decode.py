input_string = "a2b3c4"
answer = ""
# to get odd indices
for i in range(0, len(input_string),2):
    # multiplying even indices with odd indices 
    answer += (input_string[i] * int(input_string[i+1]))
print(answer)
    
    
