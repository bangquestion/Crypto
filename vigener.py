import collections
import re
import numpy as np
from itertools import cycle
from functools import reduce

chars_i_want = set('абвгдежзийклмнопрстуфхцчшщъыьэюя')
ALPHA = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
BETA = 'оеаин'
document_text = open('9.txt', 'r')
document_text2 = open('text2.txt', 'r')

text_string2 = document_text2.read().lower()
text_string = document_text.read().lower()
string_with_symbols_from_set = ''.join(c for c in text_string if c in chars_i_want)
text_two = ''.join(c for c in text_string2 if c in chars_i_want)
#[line[i::n] for i in range(0, len(line), n)]

def Letter_Frequency(string):
	letter_frequency = collections.Counter(string).most_common
	return letter_frequency

def Letter_Freq_List(string):
	letter_frequency = collections.Counter(string)
	letter_frequency_list = [(i, letter_frequency[i]) for i in letter_frequency]
	return letter_frequency_list

def getKey(item):
	return item[1]

def Letter_Freq_List_Sorted(string):
	letter_frequency = collections.Counter(string)
	letter_frequency_list = [(i, letter_frequency[i]) for i in letter_frequency]
	sorted_list = sorted(letter_frequency_list, key=getKey, reverse=True)
	return sorted_list

sorted_freq_list = Letter_Freq_List_Sorted(string_with_symbols_from_set)
ind = ALPHA.index(sorted_freq_list[0][0])

def My_Function(string):
	sorted_freq_list = Letter_Freq_List_Sorted(string)
	most_frequency_letter = ALPHA.index(sorted_freq_list[0][0])
	k = (most_frequency_letter - 14) % 32
	result = ''
	for l in string:
		try:
			i = (ALPHA.index(l) - k) % 32
			result += ALPHA[i]
		except ValueError:
			result += l
	return result

def FindKey(string):
	sorted_freq_list = Letter_Freq_List_Sorted(string)
	most_frequency_letter = ALPHA.index(sorted_freq_list[0][0])
	k = (most_frequency_letter - 14) % 32
	result = ''
	result += ALPHA[k]
	return result

def CoinsidenceIndex(string1):
	index = 0
	list_of_frequences = Letter_Freq_List(string1)
	for i in range(len(list_of_frequences)):
		val = list_of_frequences[i][1]
		sum_val = val*(val - 1)
		index += sum_val
	coinsidence_index = index / (len(string1)*(len(string1) - 1))
	return coinsidence_index

def split_string(line, n):
	return [line[i::n] for i in range(0, n)]

def unsplit_string(our_list):
	line = ''
	for i in range(len(our_list[-1])):
		for j in range(len(our_list)):
			list_element = our_list[j]
			line += list_element[i]
	return line
	

def index_result(line, n):
	summa = 0
	list_of_strings = split_string(line, n)
	for i in range(len(list_of_strings)):
		list_element = list_of_strings[i]
		index_elemet = CoinsidenceIndex(list_element)
		summa += index_elemet
	return summa/n

#for i in range(1,30):
	#print('Index for {number} is {index}.'.format(number = i, index = index_result(string_with_symbols_from_set, i)))


list_of_10_strings = split_string(string_with_symbols_from_set, 12)
list_of_10_strings = [My_Function(x) for x in list_of_10_strings]
#for i in range(len(list_of_10_strings)):
	#print('Frequency for {number} string is {index}.'.format(number = i+1, index = Letter_Freq_List_Sorted(list_of_10_strings[i])))

def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    pairs = zip(plaintext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) + ALPHA.index(y), pair)
        result += ALPHA[total % 32]

    return result.lower()


def decrypt(key, ciphertext):
    """Decrypt the string and return the plaintext"""
    pairs = zip(ciphertext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
        result += ALPHA[total % 32]

    return result

def show_result(plaintext, key):
    """Generate a resulting cipher with elements shown"""
    encrypted = encrypt(key, plaintext)
    decrypted = decrypt(key, encrypted)

    print(key)
    print(plaintext)
    print(encrypted)
    print(decrypted)