import re

# 1. Дан текстовый файл. Необходимо создать новый файл, в который требуется переписать из
# исходного файла все слова, состоящие не менее чем из семи букв.

try:
    with open("initial_text.txt", "r") as text_1:
        with open("received_text.txt", "w") as text_2:
            for row in text_1:
                words = re.split(r'[\s@#$%^&*()+=\]\[{}\\|`~.,?!:;"\'-]', row)
                for word in words:
                    if len(word) >= 7:
                        text_2.write(word+"\n")
except Exception as error:
    print(error)

# 2. Дан текстовый файл. Подсчитать количество слов в нём.

COUNT = 0
try:
    with open("initial_text.txt", "r") as text_1:
        for row in text_1:
            words = re.split(r'[\s@#$%^&*()+=\]\[{}\\|`~.,?!:;"\'-]', row)
            for word in words:
                if len(word) > 0:
                    COUNT += 1
    print("Number of words in a file:", COUNT)
except Exception as error:
    print(error)
