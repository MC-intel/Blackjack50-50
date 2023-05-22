def calculate_score(self, hand):
        score = 0
        has_ace = False

        for card in hand:
            value = card[0]

            if value.isdigit():
                score += int(value)
            elif value in ['J', 'Q', 'K']:
                score += 10
            elif value == 'A':
                has_ace = True
                score += 1

        if has_ace and score + 10 <= 21:
            score += 10

        return score
