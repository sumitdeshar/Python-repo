from pathlib import Path 

path = Path(r'chapter_10\exception\alice.txt')
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"Sorry, the file {path} does not exist.")
# else: 
#     # Count the approximate number of words in the file: 
#     words = contents.split() 
#     num_words = len(words) 
#     print(f"The file {path} has about {num_words} words.")
    
def count_word(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry,the file{path} does not exist.")
    else:
        words = contents.split()
        num_of_words = len(words)
        print(f"The file {path} has about {num_of_words} words.")
count_word(path)