# capitalize string
# if input is multi-word, then return a list over all words
def f(text = str(input("skriv en tekst:\n"))):
	array = []
	word = ""
	text = text.upper()

	for i in range(len(text)):
		if text[i] == ' ': 
			array.append(word)
			word = ""
		elif i == len(text) - 1:
			word += text[i]
			array.append(word)
		else: 
			word += text[i]

	return array

words = f()
print(words)