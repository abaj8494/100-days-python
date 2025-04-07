p = ['k', 'a', 'y', 'a', 'k']
n = ['n', 'o', 't']
def list_palindrome(l):
    for i in range(len(l)//2):
        if l[i] != l[-1-i]:
            return False
    return True

list_palindrome(n)
