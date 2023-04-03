def counter(phrase:str) -> int:
    voewls = 'аиеёоуыэюя'
    num = 0
    for l in phrase:
        if l in voewls:
            num = num + 1
    return num

def parse_poem(poem: str) -> str:
    num_phrase = poem.lower().split()
    num_l = counter(poem[0])
    for p in num_phrase[1:]:
        if num_l != counter(p):
            return "Пам парам"
    return "Парам пам-пам"