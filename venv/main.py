import string
import random

def randPassword():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits +string.punctuation
    size = 8
    return ''.join(random.choice(chars) for x in range(size,20))

num = 0
while num < 10:
    print(randPassword())
    num += 1