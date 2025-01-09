def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  print(f"{num_words} words found in the document")
  chars = char_counter(text)
  char_list = create_list_from_dict(chars)
  print_report(char_list)
  
  


def create_list_from_dict(dict1):
  output = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))

  list = []
  for key in output:
    if key.isalpha():
      list.append({key: output[key]})
  return list

def print_report(lists):
  for item in lists:
    key = list(item.keys())[0];
    value = item[key]
    print(f"The '{key}' character was found {value} times")


def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)



def char_counter(text):
  
  dict = {}
  for char in text:
    if char.lower() not in dict:
      dict[char.lower()] = 1
    else:
      dict[char.lower()] += 1
  return dict


main()