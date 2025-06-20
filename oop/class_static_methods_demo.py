class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: performs addition."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: performs multiplication and uses class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
