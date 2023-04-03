import inspect
signature = inspect.signature(print_operation_table)
for i in signature.parameters.values():
    print(i,':',i.kind.description)