"""Функия, которая делает текст большим"""


def upper_text(text):
    return text.upper()


"""Функция, которая делает первые буквы слов заглавными"""


def title_word(text):
    return text.title()


user_text = input()

print(upper_text(user_text))
print(title_word(user_text))
