from pprint import pprint


def match_encoding(encoding_list, current_encoding, lookup_loc):
	i, j = lookup_loc
	if (encoding_list[i][j] == current_encoding):
		encoding_list[i][j] = None # mark as matched
		match_encoding(encoding_list, current_encoding, (i, j + 1)) if j + 1 < len(encoding_list[j]) else None
		match_encoding(encoding_list, current_encoding, (i, j - 1)) if j - 1 > -1 else None
		match_encoding(encoding_list, current_encoding, (i+1, j)) if i + 1 < len(encoding_list) else None
		match_encoding(encoding_list, current_encoding, (i-1, j)) if i - 1 > -1 else None

		return encoding_list
	# if no match return the modified encoding list
	return encoding_list

def getCountries(encoding_list):
	country_count = 0
	for i in range(len(encoding_list)):
		row = encoding_list[i]
		for j in range(len(row)):
			if row[j] is None:
				continue
			else: # country has not been matched yet
				country_count += 1
				current_encoding = row[j]

				# ternary if's are for checking agains border overflow
				match_encoding(encoding_list, current_encoding, (i, j + 1)) if j + 1 < len(encoding_list[j]) else None
				match_encoding(encoding_list, current_encoding, (i, j - 1)) if j - 1 > -1 else None
				match_encoding(encoding_list, current_encoding, (i+1, j)) if i + 1 < len(encoding_list) else None
				match_encoding(encoding_list, current_encoding, (i-1, j)) if i - 1 > -1 else None

				row[j] = None # after checks mark element as None

			pprint(encoding_list)	
			print("\n\n")

			
	return country_count


if __name__ == "__main__":
	encodings = [[5, 4, 4],   	 
	 [4, 3, 4],    
	 [3, 2, 4],
	 [2, 2, 2],
	 [3, 3, 4],
	 [1, 4, 4],
	 [4, 1, 1],
	]

	country_count = getCountries(encodings)
	print(country_count)