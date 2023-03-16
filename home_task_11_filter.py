inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

is_palindrome = list(filter(lambda inputdata: inputdata.lower() == inputdata.lower()[::-1], inputdata))

print(is_palindrome)
