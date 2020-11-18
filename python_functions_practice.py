def return_10():
    return 10


def add(x, y):  
    return (x + y)

add(1, 2)


def subtract(x, y):
    return (x - y)

subtract(10, 5)

def multiply(x, y):
    return (x * y)

multiply(4, 2)


def divide(x, y):
    return (x / y)

divide(10, 2)

def length_of_string(x):
    return (len(x))

length_of_string('A string of length 21')

def join_string(x, y):  
    return (x + y)

join_string('Mary had a little lamb,', 'its fleece was white as snow')


def add_string_as_number(string_1, string_2):
    return(int(string_1) + int(string_2))

add_string_as_number('1', '2')    


months = {1 : 'January', 2: 'February', 3: 'March', 4: 'April', 9: 'September'}

def number_to_full_month_name(month_number):
    return (months[month_number])

number_to_full_month_name(1)

number_to_full_month_name(3)

number_to_full_month_name(9)


short_months = {1 : 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 9: 'Sep', 10: 'Oct'}

def number_to_short_month_name(month_number):
    return (short_months[month_number])

number_to_short_month_name(1)
number_to_short_month_name(4)
number_to_short_month_name(10)



#Given the length of a side of a cube calculate the volume
def test_volume_of_cube(self):
    return (self ** 3)

def reverse_string(string_to_reverse)
    return (string_to_reverse [::-1])

reverse_string('hello')