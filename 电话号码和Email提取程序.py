import pyperclip,re

phoneRegex = re.compile(r'1[35678]\d{9}')

emailRegex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]{2,}\.[com,cn,net]{2,4}')

text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
	matches.append(groups)

for groups in emailRegex.findall(text):
	matches.append(groups)

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to the clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')
