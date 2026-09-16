# capitalize string
# if input is multi-word, then return a list over all words
def f(text: str):
	array = []
	word = ""
	capitalized_text = text.upper();

	for char in range(len(capitalized_text)):
		if capitalized_text[char] == ' ': 
			array.append(word)
			word = ""
		elif char == len(capitalized_text) - 1:
			word += capitalized_text[char]
			array.append(word)
		else: word += capitalized_text[char]

	return array

words = f("hello world")
print(words)