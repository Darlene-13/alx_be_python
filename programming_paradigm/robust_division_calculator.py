def safe_divide(numerator, denominator):
    """
    Safely perform division with proper error handling.
    
    Args:
        numerator: The dividend (can be string or numeric)
        denominator: The divisor (can be string or numeric)
    
    Returns:
        String with either the result or an error message
    """
    try:
        # Convert arguments to floats
        num = float(numerator)
        den = float(denominator)
        
        # Perform division
        result = num / den
        return f"The result of the division is {result}"
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."