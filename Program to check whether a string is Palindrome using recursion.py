def palindrome(text):
    if len(text)<=1:
        return True
    if text[0]==text[-1]:
        return palindrome(text[1:-1])
    else:
        return False
word="Madam"
if palindrome(word):
    print(word,"is a palindrome")
else:
    print(word,"is not a palindrome")