def division():
    try:
        x=5/0
        print(x)
    except ZeroDivisionError as e:
        print(e," is not possible")

division()
        
    
    
