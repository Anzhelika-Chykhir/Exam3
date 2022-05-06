# Напишите функцию, которая проверяет: является ли слово палиндромом
def is_palindrome(s):
    rev = s[::-1]

    if (s == rev):
        return True
    else:
        return False


print(is_palindrome("olo"))
