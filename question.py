class Example:
    
    def __init__(self,value=10):
        print("Initializing object",value)

obj=Example()
Example.__init__(obj,5)

obj.value