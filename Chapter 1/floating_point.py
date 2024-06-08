import math
def round_to_d_significant_figures(num, d):
    if num == 0:
        return 0
    
    decimal_places = d - int(math.floor(math.log10(abs(num)))) - 1
    
    return round(num, decimal_places)

# Example usage
number = 12345.6789
rounded_number = round_to_d_significant_figures(number, 3)
print("Rounded number:", rounded_number)
