import re


with open('row.txt', 'r', encoding='utf-8') as f:
    read_data = f.read()
    # we could obviously find each and every match
    # in the file by iterating over each line in the
    # file. I won't do it just for the sake of convinence 
    # and the fact that it was't explicitly said in the Lab

#Task1
pattern = re.compile(r'ab*')
print(pattern.fullmatch(read_data))

#Task2
pattern = re.compile(r'ab{2,3}')
print(pattern.match(read_data))

#Task3
pattern = re.compile(r'[a-z]+_[a-z]+')
print(pattern.findall(read_data))

# Task4
pattern = re.compile(r'[A-Z]+[a-z]+')
print(pattern.findall(read_data))

#Task5
pattern = re.compile(r'a.*b')
print(pattern.match(read_data))

#Task6
pattern = r'[ ,.]'
print(re.sub(pattern, ":", read_data))

#Task7
pattern = re.split(r'_', read_data)
new_string = ''.join([pattern[0].lower()] + [word.capitalize() for word in pattern[1:]])
print(pattern)
print(new_string)

#Task8

new_string = re.split(r'[A-Z]', read_data)
print(new_string)


#Task9
new_string = re.sub(r'([A-Z].)', r' \1', read_data)
print(new_string)

#Task10
text = "wqertyuWuwgebwkeUwjkehbdeHwejkhwk"
new_text = re.sub(r'(.)([A-Z])', lambda match: match.group(1) + '_' + match.group(2).lower() , text)
print(new_text)