#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            div_result = dividend / divisor
        except ZeroDivisionError:
            print("Division by 0")
            div_result = 0
        except (TypeError, ValueError):
            print("wrong type")
            div_result = 0
        except IndexError:
            print("out of range")
        finally:
            result.append(div_result)
    return result
