#cheating with this one to see what the sols want:
import string
import random
length = 8
password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
print(password)
