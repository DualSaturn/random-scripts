import csv

def convert_word(word):
    converted_word = ''
    list_of_elements_used = []
    double_letter_found = False

    for i in range(len(word)):
        if double_letter_found:
            double_letter_found = False
            continue
        for b in elements_and_symbols:
            if word[i:i + 2] == b[0].lower():
                converted_word = converted_word + b[0]
                list_of_elements_used.append(b[1].lower())
                double_letter_found = True
                break
        if double_letter_found:
            continue
        for b in elements_and_symbols:
            if word[i] == b[0].lower():
                converted_word = converted_word + b[0]
                list_of_elements_used.append(b[1].lower())
                break
    return '{} ({})'.format(converted_word, ', '.join(list_of_elements_used))
    
if __name__ == '__main__':
	csv_file = 'ptdata2.csv'
	elements_and_symbols = []
	with open(csv_file, 'r') as e_data:
	    reader = csv.reader(e_data)
	    for row in reader:
	        elements_and_symbols.append((row[1].strip(), row[2].strip()))

	print('Enter word to convert:')
	word_input = input()
	print(convert_word(word_input))

