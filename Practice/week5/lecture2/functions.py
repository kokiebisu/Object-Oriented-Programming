def some_function():
    print("Something")


function_obj = some_function
print(function_obj)
print(function_obj.__name__)
print(function_obj.__class__)
print(type(function_obj))
function_obj()
