T = int(input())

for case in range(1, T+1):
    S = input().strip()
    
    cards = {'S': set(), 'D': set(), 'H': set(), 'C': set()}
    
    error = False
    
    for i in range(0, len(S), 3):
        suit = S[i]  
        number = S[i+1:i+3]  
        
        if number in cards[suit]:
            error = True
            break
        else:
            cards[suit].add(number)
    
    output = f"#{case} "
    
    if error:
        output += "ERROR"
    else:
        output += f"{13 - len(cards['S'])} {13 - len(cards['D'])} {13 - len(cards['H'])} {13 - len(cards['C'])}"
    
    print(output)
