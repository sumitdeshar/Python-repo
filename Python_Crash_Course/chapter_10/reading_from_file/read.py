from pathlib import Path

path = Path(r'.\chapter_10\reading_from_file\pi.txt')
contents = path.read_text()
contents = contents.rstrip()
# print(contents)

#reading lines as it is
# lines = contents.splitlines() 
# # print(lines)  ['3.1415926535', '  8979323846', '  2643383279']
# for line in lines: 
#     print(line)

# 3.1415926535
#   8979323846
#   2643383279

#reading lines as it should be using strip function
# lines = contents.splitlines() 
# pi_string = '' 
# for line in lines:
#     line = line.rstrip()
#     pi_string += line.lstrip()
# print(pi_string) 
# print(len(pi_string))

#reading a bigger file
path = Path(r'.\chapter_10\reading_from_file\million_digit.txt')
contents = path.read_text()
contents = contents.rstrip()

#this is how a file is being read nowadays
# with open('pi_digits.txt', 'r') as file:
#         pi_digits = file.read().replace('\n', '')

pi_string = ''
for line in contents.splitlines():
    pi_string += line.strip()

    
print(f'{pi_string[:52]}')
print(type(pi_string))


