from pathlib import Path

path = Path(r'.\chapter_10\reading_from_file\string.txt')
contents = path.read_text()
contents = contents.rstrip()
# print(f'{contents}')

user_list = contents.splitlines()
user = user_list[4]
# print(f'{user}')

#python has a funtion lol
# my_string.find(' ')   
def finding_len(name):
    len = 0
    for index,letter in enumerate(name):
        if letter == ' ':
            len = index
            break
    # print(len)
    return len
finding_len(user)

def slicing_name(name,len):
    fname = name[:len]
    lname = name[len+1:]
    return fname,lname
    
def AFTL(lists):
    for list in lists:
        length = finding_len(list)
        first,last = slicing_name(list, length)
        print(f'Your first name is:{first}\nYOur last name is:{last}\n\n')
        
AFTL(user_list)