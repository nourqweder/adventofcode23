def calculate_scratchcards(file_name):
    cards = []
    with open(file_name, 'r') as f:
        cards = [line for line in f]

    card_counts = [1] * len(cards)
    for i in range(len(cards)):
        _, numbers = cards[i].split('Card')
        _, numbers = numbers.split(': ')
        winning_numbers, your_numbers = numbers.split(' | ')
        winning_numbers = set(map(int, winning_numbers.split()))
        your_numbers = set(map(int, your_numbers.split()))
        matches = winning_numbers & your_numbers
        for j in range(1, len(matches) + 1):
            if i + j < len(cards):
                card_counts[i + j] += card_counts[i]

    return sum(card_counts)

print(calculate_scratchcards('input.txt'))  # It should print the total number of scratchcards