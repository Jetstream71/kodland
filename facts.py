meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ": "Шутка",
            "ЩИЩ": "Одобрение или восторг",
            "КРИПОВЫЙ": "Страшный, пугающий",
            "АГРИТЬСЯ": "Злиться"
            }
word = input("Введите непонятное слово (большими буквами!): ").upper()

if word in meme_dict.keys():
    # Что делать, если слово нашлось
    print(meme_dict[word])
else:
    # Что делать, если слово не нашлось
    print("Слово не найдено")
