import os
import shutil

# Дополнительно:
# Создайте приложение, проверяющее текст на недопустимые слова.
# Если недопустимое слово найдено, оно должно быть заменено на набор символов *.
# По итогам работы приложения необходимо показать статистику действий.

original_text = "text.txt"
word_for_replace = (input("Enter word for replace: ")).lower()
count = 0

with open(original_text, "r") as text:
    text = text.read()

text = text.split(" ")
text_2 = []

for line in text:
    if word_for_replace in line.lower():
        text_2.append(line.lower().replace(word_for_replace, len(word_for_replace)*"*"))
        count += 1
    else:
        text_2.append(line)

text_2 = " ".join(text_2)

with open(original_text, "w") as text:
    text.write(text_2)

with open(original_text, "r") as text:
    text = text.read()

print(text)
print("Number of replacements made:", count)

# Удалить все файлы в директории:
# импортируем модуль os и модуль shutil
# shutil содержит набор функций высокого уровня для обработки файлов, групп файлов, и папок.
# В частности, доступные здесь функции позволяют копировать, перемещать и удалять файлы и папки.
# Часто используется вместе с модулем os.

del_dir = input("Input pass to dir: ")
for files in os.listdir(del_dir):
    path = os.path.join(del_dir, files)
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)

#Код работает, но скажу честно не доконца разобрался с данным модулем, еще уделю ему внимание.
