try:
    text = input("Enter a string: ")
    letter_count = 0
    digit_count = 0
    for i in range(len(text)):
        if text[i].isalpha():
            letter_count += 1
        if text[i].isdigit():
            digit_count += 1
    result = f"{letter_count} letters and {digit_count} digits"
    print(result)
except Exception as e:
    print(e)
try:
    symbol_count = 0
    text2 = input("Enter a string: ")
    search_symbol = input("Enter a symbol: ")
    while len(search_symbol) > 1:
        print("Enter only one symbol!")
        search_symbol = input("Enter a symbol: ")
        continue
    for i in range(len(text2)):
        if text2[i] == search_symbol:
            symbol_count += 1
    if symbol_count == 0:
        print("Symbol is not found in the string")
    else:
        print(f"Symbol is found {symbol_count} times")
except Exception as e:
    print(e)
try:
    text3 = input("Enter your string: ")
    old_word = input("Enter word to search: ")
    new_word = input("Enter replacement word: ")
    text3 = text3.replace(old_word, new_word)
    print(text3)
except Exception as e:
    print(e)
try:
    text4 = input("Enter your text: ")
    print(text4[2])
    print(text4[-2])
    print(text4[:5])
    print(text4[:-2])
    print(text4[2::2])#все парные индексы- начиная с индекса 2, а не 1 как сказано в условии?
    print(text4[1::2])#непарные индексы - начиная с индекса 1, а не 2?
    print(text4[::-1])
    print(text4[::-2])
    print(len(text4))
except Exception as e:
    print(e)





