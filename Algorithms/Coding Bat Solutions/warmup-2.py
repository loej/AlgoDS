# 1. string_times
def string_times(str, n):
  result = ""
  for i in range(n):
    result  =  result + str
  return result 

#2. front_times

def front_times(str, n):
  front3 = str[:3]
  return front3*n

#3. string_bits

def string_bits(str):
  result = ""
  for index in range(len(str)):
    if index % 2 ==0:
      result += str[index]
  return result

#4. string _splosion

def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result += str[:i+1]
  return result
