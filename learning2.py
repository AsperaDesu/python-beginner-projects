def palindrome(nums):
    print(f"original number {nums}")
    if nums[::-1] == nums:
        text = "Yes. given number is palindrome number"
        return text
    else:
        text ="No. given number is not a palindrome number"
        return text

print(f"{palindrome(input('Enter a number : '))}")
print("")
