def print_operation_table(operation,num_rows,num_colums):
    for i in range(1,num_rows):
        k = ""
        for j in range(1,num_colums):
            k = k + operation(i,j) + " "
        print(k)
 print_operation_table((lambda x,y: str(x*y)),7,7)