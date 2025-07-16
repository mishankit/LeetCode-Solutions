def sort_stack(stack):
    if not stack:
        return 
    top = stack.pop()
    sort_stack(stack)
    
    insert_in_stack(stack, top)
    
def insert_in_stack(stack, element):
    if not stack or stack[-1] >= element:
        stack.append(element)
        return 
    temp = stack.pop()
    insert_in_stack(stack, element)
    stack.append(temp)
        
    
s = [3,2,1]
sort_stack(s)
print(s)
