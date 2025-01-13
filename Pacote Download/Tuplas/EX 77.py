words = ('Arara', 'Utero', 'Celta', 'Sonic', 'Palmeiras')

vowels = 'AEIOUaeiou'  # Lista genérica de vogais
for word in words:
    print(f"The word '{word}' has the vowels: ", end="")
    for letter in word:
        if letter in vowels:
            print(letter, end=" ")
    print()  # Quebra de linha após cada palavra
