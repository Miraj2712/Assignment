s= input("Enter a string:")
digit_count=0

for c in s:
  if c.isdigit():
    digit_count+=1
print(f"Number of digits in the given string:{digit_count}")