def check_run_triplet(cards):
    for i in range(8):
        if cards[i] > 0 and cards[i+1] > 0 and cards[i+2] > 0:
            return True
        if cards[i] >= 3:
            return True
    return False

T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player1_cards = [0] * 10
    player2_cards = [0] * 10
    winner = 0
    
    for i in range(12):
        if i % 2 == 0:
            player1_cards[cards[i]] += 1
            if check_run_triplet(player1_cards):
                winner = 1
                break
        else:
            player2_cards[cards[i]] += 1
            if check_run_triplet(player2_cards):
                winner = 2
                break

    print(f"#{tc} {winner}")
