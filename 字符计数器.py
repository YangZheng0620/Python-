import pprint

message = input('请输入自定义字符，将自动为你计数:\n')
count = {}

for character in message:
	count.setdefault(character,0)
	count[character] = count[character] + 1

pprint.pprint(count)