def Calculate(num_1, num_2, operation):
    result = None
    try:
        if operation == 'add':
            result = num_1 + num_2
        elif operation == 'subtract':
            result = num_1 - num_2
        elif operation == 'multiply':
            result = num_1 * num_2
        elif operation == 'divide':
            result = num_1 / num_2
    except:
        result = None
    return result