
from pickle import FALSE


def get_words() -> list:
    with open('words.txt') as file:
        words = file.read().split()
    return remove_words_with_duplicate_letters(words)

def remove_words_with_duplicate_letters(words: list) -> list:
    new_words = []
    for w in words:
        if len(list(set([c for c in w]))) == 5:
            new_words.append(w)
    return new_words

def contains(word: str, *letter_list: tuple) -> bool:
    for l in letter_list:
        if l not in word:
            return False
    return True


def check_format(cmd_list) -> bool:
    if len(cmd_list) != 5:
        return False
    
    for l in cmd_list:
        if type(l) != str or (len(l) == 2 and l[0] not in ('!', '?')) or not ord(l[-1]) in range(97, 123):
            return False
        
    return True

def my_filter(words: list, rule: str) -> list:
    ind = int(rule[0])

    if len(rule) == 2:
        return list(filter(lambda word : word[ind] == rule[1], words))
    
    if rule[1] == '!':
        return list(filter(lambda word : rule[2] not in word, words))
    
    # rule[1] == '?'
    return list(filter(lambda word : rule[2] in word and word[ind] != rule[2], words))

def solve() -> None:
    words = get_words()
    rules = []
    found = False

    while not found:
        while True:
            cmd_list = input("-->").split()

            if check_format(cmd_list):
                break

        for i, r in enumerate(cmd_list):
            rules.append(str(i)+r)

        for r in rules:
            words = my_filter(words, r)
        
        #print(rules)

        for w in words:
            print(w)

        print(f"Best word: '{calculate(words)}'")
        
        if input(":"):
            found = True


def calculate(words: list) -> str:
    letter_freq = {}
    #words = get_words()

    for ac in range(97, 123):
        letter_freq[chr(ac)] = 0

    for w in words:
        for c in w:
            letter_freq[c] += 1

    for p in letter_freq:
        print(f"{p}: {letter_freq[p]}")

    best_word = ""
    best_score = 0
    for w in words:
        score = 0
        for c in w:
            score += letter_freq[c]
        
        if score > best_score:
            best_word = w
            best_score = score
    
    print(f"{best_word} : {best_score}")

    return best_word


def main() -> None:
    while True:
        x = input("mode: ")

        if x == 's':
            solve()
            break

        elif x == 'c':
            calculate(get_words())
            break
    
    

if __name__ == '__main__':
    main()
