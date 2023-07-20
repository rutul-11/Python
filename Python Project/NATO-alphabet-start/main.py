import pandas

data = pandas.read_csv("/Users/rutulbhosale/Desktop/project/NATO-alphabet-start/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for(index,row) in data.iterrows()}
print(phonetic_dict)
def abc():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters" )
        abc()
    else:
        print(output_list)
        abc()

abc()
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
