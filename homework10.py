import re


home_phone_numbers = re.findall(r"\b\d{6,7}\b", "asdnjbvjb, 234578367, 685351, 7528440")
print(home_phone_numbers)


phone_numbers = re.findall(r"\b[+]?\d{10,12}\b", "+380956467463, 0673485673, ghjkdfb, 234567890104978")
print(phone_numbers)


email_search = re.findall(r"\b\w{8,16}@gmail\.com\b", "get_email@gmail.com, fghbjkm, 12345bjbkb@gmail.com")
print(email_search)


name_surname_search = re.findall(r"\b[a-zA-Z]{2,20}\b\s\b[a-zA-Z]{2,20}\b\s\b[a-zA-Z]{2,20}\b", "Ivan Ivanovich Ivanov, Ivan Ivanin, иыимрви, 1332тдтд")
print(name_surname_search)





