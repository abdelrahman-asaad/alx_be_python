class Calculator:
    calculation_type = "Arithmetic Operations"  #class level attribute
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        cls.calculation_type =  a * b  #class level attribute
        print(f"Calculation type: {cls.calculation_type}")
        return a * b          #or return cls.calculation_type
    
#creating object
# Using the static method
#sum_result = Calculator.add(10, 5)
#print(f"The sum is: {sum_result}")

# Using the class method
#product_result = Calculator.multiply(10, 5)
#print(f"The product is: {product_result}")
    
    
