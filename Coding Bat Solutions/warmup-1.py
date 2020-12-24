# Warmup-1

# 1. sleep_in
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


# 2. monkey_trouble
def monkey_trouble(a_smile, b_smile):
    # a Monkey => a_smile
    # b Monkey => b_smile
    if (not(a_smile) and not(b_smile)) or (a_smile and b_smile):
        return True
    else:
        return False

# 3. sum_double


def sum_double(a, b):
    if a != b:
        x = a+b
        # str(x)
        return x
    else:
        return 2*(a+b)


# 4. diff21
def diff21(n):
    if n > 21:
        return 2*abs(n-21)
    else:
        return abs(n-21)

# 5. parrot_trouble


def parrot_trouble(talking, hour):
    if ((hour < 7) or (hour > 20)) and talking == True:
        return True
    else:
        return False

# 6. makes10


def makes10(a, b):
    sum = a + b
    if (a == 10 or b == 10) or sum == 10:
        return True
    else:
        return False

# 7. near_hundred


def near_hundred(n):
    if (n >= 90 and n <= 110):
        return True
    elif n >= 190 and n <= 210:
        return True
    else:
        return False

# 8. pos_negative


def pos_neg(a, b, negative):
    if ((a < 0 and b > 0) or (a > 0 and b < 0)) and (negative == False):
        return True
    elif (negative == True) and (a < 0 and b < 0):
        return True
    else:
        return False
# 9. not_string

def not_string(str):
  if str[:3] == "not":
    return str
  else:
    return "not "+ str

# 10. missing_char

def missing_char(str, n):
  missing = str[:n]
  front = str[n+1:]  
  return missing + front

# 11. front_back

def front_back(str):
  if len(str) <= 1:
    return str
  # the last element is len(str)-1
  start = str[0] #inclusive
  end = len(str)-1
  # still need the middle 
  middle = str[1:end]
  return str[len(str)-1] + str[1:len(str)-1] + str[0]

# 12. front3

def front3(str):
  multiple = str[0:3]
  final = multiple*3
  return final
