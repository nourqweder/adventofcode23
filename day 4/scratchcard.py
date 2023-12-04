def calculate_points(file_name):
    total_points = 0
    with open(file_name, 'r') as f:
        for line in f:
            _, numbers = line.split('Card')
            _, numbers = numbers.split(': ')
            winning_numbers, your_numbers = numbers.split(' | ')
            winning_numbers = set(map(int, winning_numbers.split()))
            your_numbers = set(map(int, your_numbers.split()))
            matches = winning_numbers & your_numbers
            if matches:
                total_points += 2**(len(matches) - 1)
    return total_points

print(calculate_points('input.txt'))  # It should print the total points based on your file data
