try:
    text = input("Enter your text: ")

    text = text.capitalize()
    start_index = 0
    new_text = str()
    for i in range(len(text) - 2):
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            text_slice = text[start_index:i+2]
            letter_to_change = text[i + 2]
            letter_to_change = letter_to_change.upper()
            new_text += text_slice + letter_to_change
            start_index = i + 3
    new_text += text[start_index:]
    print(new_text)
    digit_count = 0
    exclamation_count = 0
    punctuation_marks = ".,!?:;()-\""
    punctuation_count = 0
    for i in range(len(new_text)):
        if new_text[i].isdigit():
            digit_count += 1
        if new_text[i] == "!":
            exclamation_count += 1
        mark_search = new_text[i]
        if punctuation_marks.find(new_text[i]) != -1:
            punctuation_count += 1
    print(f'Digits: {digit_count}')
    print(f'Punctuation marks: {punctuation_count}')
    print(f'Exclamation point: {exclamation_count}')
except Exception as e:
    print(e)




