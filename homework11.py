import re
with open("text1.txt", "w", encoding="utf-8") as text1_file:
    text1_file.write("""To be, or not to be, that is the question, 
    Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, 
    Or to take arms against a sea of troubles""")
with open("text1.txt", "r", encoding="utf-8") as text1_file:
    result = text1_file.read()
    print(result)


with open("text1.txt", "r", encoding="utf-8") as text1_file:
    text_from_file = text1_file.read()
    seven_letter_word_search = re.findall(r"[A-Za-zА-Яа-яёЁЇїІіЄєґҐ']{7,}", text_from_file)
with open("text2.txt", "w", encoding="utf-8") as text2_file:
    text2_file.write(" ".join(seven_letter_word_search))
with open("text2.txt", "r", encoding="utf-8") as text2_file:
    result2 = text2_file.read()
    print(result2)


with open("text1.txt", "r", encoding="utf-8") as text1_file:
    text_from_file = text1_file.read()
    number_of_words_in_text = len(text_from_file.split())
    print(f"Number of words in the text: {number_of_words_in_text}")


def forbidden_word_search_change(text_list, forbidden_word, forbidden_word_count = 0):
    for i in range(len(text_list)):
        if text_list[i].lower() == forbidden_word.lower():
            text_list[i] = "*" * len(forbidden_word)
            forbidden_word_count += 1
    print(f"Forbidden word found and changed {forbidden_word_count} times")


with open("text1.txt", "r+", encoding="utf-8") as text1_file:
    text_from_file = text1_file.read()
    text_list = text_from_file.split()
    forbidden_word = input("Enter forbidden word: ")
    forbidden_word_search_change(text_list, forbidden_word, forbidden_word_count=0)
with open("text1.txt", "w", encoding="utf-8") as text1_file:
    text1_file.write(" ".join(text_list))
with open("text1.txt", "r", encoding="utf-8") as text1_file:
    result3 = text1_file.read()
    print(result3)











