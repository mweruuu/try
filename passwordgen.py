import random


def shuffle_list(string):
    mypassword = list(string)
    random.shuffle(mypassword)
    print("".join(mypassword))


num1 = str(random.randint(0, 9))
num2 = str(random.randint(0, 9))
uppercase1 = chr(random.randint(65, 90))
uppercase2 = chr(random.randint(65, 90))
lowercase1 = chr(random.randint(97, 122))
lowercase2 = chr(random.randint(97, 122))
punctuation1 = chr(random.randint(33, 47))
punctuation2 = chr(random.randint(33, 47))

password = (uppercase1 + uppercase2 + lowercase1 + lowercase2 + punctuation1 + punctuation2 + num1 + num2)
shuffle_list(password)

# print(password)
