#문자열 재정렬.py
data = input()

alphabet_list = []
number = 0
for i in sorted(data):
  if ord(i) < ord('A'):
    number += int(i)
  else:
    alphabet_list.append(i)

print(''.join(alphabet_list)+str(number))
