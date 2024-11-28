"""Learning Outcome: Functions"""
def sum_of_squares(n: int):
    """
    Calculate the sum of the squares of all integers from 1 to n.

    Parameters:
    n (int): A non-negative integer up to which the squares will be summed.

    Returns:
    int: The sum of the squares of all integers from 1 to n.

    Raises:
    ValueError: If n is a negative integer.
    """
    pass

def evaluate_performance(grades: list, min_pass: int):
    """
    Evaluate the performance based on a list of grades and a minimum passing grade.

    Parameters:
    grades (list): A list of integers representing student grades.
    min_pass (int): The minimum average grade required to pass.

    Returns:
    str: "Pass" if the average grade is greater than or equal to min_pass, otherwise "Fail".
    """
    pass

def calculate_cumulative_performance(scores: dict):
    """
    Calculate the cumulative performance based on student scores.

    Parameters:
    scores (dict): A dictionary where keys are subject names and values are the corresponding scores.

    Returns:
    dict: A dictionary containing the average score and a list of subjects where the score is below average.
    """
    pass

def analyze_improvement(scores: list):
    """
    Analyze the improvement trend based on a list of scores.

    Parameters:
    scores (list): A list of integers representing scores over time.

    Returns:
    dict: A dictionary containing the trend of improvement ("positive", "negative", or "neutral") 
          and a boolean indicating whether there has been an improvement.
    """
    pass

def rank_students(students: list[tuple[str, int]]):
    """
    Rank students based on their scores.

    Parameters:
    students (list): A list of tuples where each tuple contains a student's name and their score.

    Returns:
    list: A sorted list of tuples in descending order based on scores.
    """
    pass

"""Learning Outcome: Basic Loops"""
def even_numbers(n: int):
    """
    Generate a list of even numbers from 1 to n.

    Parameters:
    n (int): The upper limit for generating even numbers.

    Returns:
    list: A list of even integers from 1 to n.
    """
    _list = [i for i in range(1,n+1) if i % 2 == 0]
    return _list

def odd_numbers(n: int):
    """
    Generate a list of odd numbers from 1 to n.

    Parameters:
    n (int): The upper limit for generating odd numbers.

    Returns:
    list: A list of odd integers from 1 to n.
    """
    _list = [i for i in range(1,n+1) if not i % 2 == 0]
    return _list
#print(odd_numbers(20))

def sum_multiples_of_num(num: int, length: int):
    """
    Calculate the sum of multiples of a given number up to a specified length.

    Parameters:
    num (int): The number whose multiples are to be summed.
    length (int): The upper limit for the range of multiples.

    Returns:
    int: The sum of multiples of num from 1 to length.
    """
    sum = 0
    for i in range(1,length + 1):
        if i % num ==0:
            sum += i
    return sum
#print(sum_multiples_of_num(3,10))

def skip_num(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, skipping a specific number.

    Parameters:
    n (int): The number to skip.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding n.
    """
    _list = []
    for i in range(1,length+1):
        if i == n:
            continue
        else:
            _list.append(i)
    return _list
#print(skip_num(5,10)) 

def break_test(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, stopping when a specific number is encountered.

    Parameters:
    n (int): The number at which to stop adding to the list.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding n and stopping before it.
    """
    _list = []
    for i in range(1,length+1):
        if i != n:
            _list.append(i)
        else:
            break
    return _list
#print(break_test(5,10))


def sum_numbers_until_zero(nums: list):
    """
    Calculate the sum of numbers in a list until a zero is encountered.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The sum of integers in the list up to (but not including) the first zero.
     [1, 2, 3, 0]
    """
    count = 0
    for num in nums:
        while num != 0:
            count += num
        break
    return count 
#print(sum_numbers_until_zero([1, 2, 3, 0]))

def count_positive_numbers(nums: list):
    """
    Count the number of positive integers in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The count of positive integers in the list.
    """
    count = 0
    for num in nums:
        if num > 0 :
            count += 1
    return count
#print(count_positive_numbers([-1, 2, 3, -4, 5]))
def sum_dictionary_values(dictionary: dict):
    """
    Calculate the sum of all values in a dictionary.

    Parameters:
    dictionary (dict): A dictionary with numeric values.

    Returns:
    int: The sum of all values in the dictionary.
    {'a': 1, 'b': 2, 'c': 3}
    """
    sum = 0
    for value in dictionary.values():
        sum+=value
    return sum
#print(sum_dictionary_values({'a': 1, 'b': 2, 'c': 3}))

def sum_unique_elements(elements: list):
    """
    Calculate the sum of unique elements in a list.

    Parameters:
    elements (list): A list of integers.

    Returns:
    int: The sum of unique integers in the list.
    """
    
    """_elements = sorted(elements)
    for element in _elements:
        count += element
        _elements.remove(element)
        if element in _elements:
            _elements.remove(element)
        else:
            continue
       
    return count"""
    count = 0 
    _set = set(elements)
    for num in _set:
        count+=num
    return count
#print(sum_unique_elements([1, 2, 2, 3]))

def skip_divisible_by_num(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, skipping those that are divisible by a specific number.

    Parameters:
    n (int): The number to skip multiples of.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding those divisible by n.
    3, 20
    """
    _list = [num for num in range(1,length+1) if not num % n ==0 ]
    return _list
#print(skip_divisible_by_num(3,20))

"""Learning Outcome: Processing Data"""

def square_numbers(nums: list):
    """
    Calculate the square of each number in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    list: A list containing the squares of the input integers.
    [1, 2, 3]
    """
    _list = [ num**2 for num in nums ]
    return _list
#print(square_numbers([1, 2, 3]))

def transform_string(input: str, transform: str):
    """
    Transform a string based on the specified transformation type.

    Parameters:
    input (str): The string to be transformed.
    transform (str): The type of transformation ('capitalize', 'upper', 'lower').

    Returns:
    str: The transformed string.

    Raises:
    ValueError: If the transformation type is unknown.
     text = 'hello, world'
        transform = ['Uppercase', 'Capitalize', 'Lowercase']
    """
    transformations = ['Uppercase', 'Capitalize', 'Lowercase']
    if transform.capitalize() not in transformations:
        raise ValueError
    else:
        if transform.capitalize() == transformations[0]:
            return input.upper()
        elif transform.capitalize() == transformations[1]:
            return input.capitalize()
        elif transform.capitalize() == transformations[2]:
            return input.lower()
    
#print(transform_string('hello, world!','capitalize'))
def sum_and_average(nums: list[int]):
    """
    Calculate the sum and average of a list of numbers.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    tuple: A tuple containing the sum and average of the numbers.
    """
    sum = 0
    
    _list = []
    for num in nums:
        sum+=num
    sum
    _list.append(sum)
    _list.append(sum/len(nums))
    return tuple(_list)
#print(sum_and_average([5, 15, 25]))   

def word_frequency_count(words: list[str]):
    """
    Count the frequency of each word in a list.

    Parameters:
    words (list[str]): A list of words.

    Returns:
    dict: A dictionary with words as keys and their frequencies as values.
    """
    count = 1
    _dict = {}
    for word in words:
        words.remove(word)
        if word in words:
            count +=1
            _dict[word] = count 
        else:
            count = count
            _dict[word]= count
    return _dict 
#print(word_frequency_count(['cat', 'dog', 'dog']))
def filter_even_numbers(nums: list[int]):
    """
    Filter out even numbers from a list.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    list: A list containing only the even integers from the input list.
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    _list = []
    for num in nums:
        if num % 2 == 0:
            _list.append(num)
    return _list 
#print(filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]))