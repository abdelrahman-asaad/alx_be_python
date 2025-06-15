def safe_divide(numerator, denominator):
    try :
        print(float(numerator)/float(denominator))
    except ZeroDivisionError as e:
        print(e)
    except ValueError :
        print(f"please Enter Number")


safe_divide(10,2)
safe_divide(10,0)
#safe_divide(ten,5)        