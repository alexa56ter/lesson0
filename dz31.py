calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(str):
      t = []
      t.append(int((len(str))))
      t.append(str.upper())
      t.append(str.lower())
      h = tuple(t)
      print(h)
      count_calls()
      return(h)

def is_contains(string, list_to_search):
      string = string.lower()
      list_to_search = [i.lower() for i in list_to_search]
      if list_to_search.count(string):
            print(True)
      else:
            print(False)
      count_calls()






#print(string_info('Capybara'))
#print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)