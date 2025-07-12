def count_even_odd(numbers: list[int]) -> tuple[int, int]:
    try:
        if not isinstance(numbers, list):
            raise TypeError("Input must be a list")
        
        if not numbers:
            raise ValueError("List cannot be empty")
        
        even_count = 0
        odd_count = 0
        
        for i, num in enumerate(numbers):
            if not isinstance(num, int):
                raise TypeError(f"Element at index {i} is not an integer: {num}")
            
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        return even_count, odd_count
        
    except Exception as e:
        raise Exception(f"Error in count_even_odd: {e}")

def sum_of_digits(n: int) -> int:
    try:
        if not isinstance(n, int):
            raise TypeError(f"Input must be an integer, got {type(n).__name__}")
        
        n = abs(n)
        digit_sum = 0
        
        if n == 0:
            return 0
        
        while n > 0:
            digit_sum += n % 10
            n //= 10
        
        return digit_sum
        
    except Exception as e:
        raise Exception(f"Error in sum_of_digits: {e}")

def calculate_average(numbers: list[int]) -> float:
    try:
        if not isinstance(numbers, list):
            raise TypeError("Input must be a list")
        
        if not numbers:
            raise ValueError("List cannot be empty")
        
        for i, num in enumerate(numbers):
            if not isinstance(num, int):
                raise TypeError(f"Element at index {i} is not an integer: {num}")
        
        return sum(numbers) / len(numbers)
        
    except Exception as e:
        raise Exception(f"Error in calculate_average: {e}")

def find_min_max(numbers: list[int]) -> tuple[int, int]:
    try:
        if not isinstance(numbers, list):
            raise TypeError("Input must be a list")
        
        if not numbers:
            raise ValueError("List cannot be empty")
        
        for i, num in enumerate(numbers):
            if not isinstance(num, int):
                raise TypeError(f"Element at index {i} is not an integer: {num}")
        
        return min(numbers), max(numbers)
        
    except Exception as e:
        raise Exception(f"Error in find_min_max: {e}")
