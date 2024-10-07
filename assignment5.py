def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = sum(1 for character in string if character in vowels)
    return count


String = input("Enter a string :")
vowel_count = count_vowels(String)
print(f"The number of vowels in the string is:{vowel_count}")