def second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort()
    return unique_numbers[-2]


nums = list(map(int, input(f"Enter Numbers:").split()))
result = second_largest(nums)
print(f"The second largest number is: {result}")