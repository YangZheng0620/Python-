import pyperclip

text = pyperclip.paste()

# 将字符串以\n为分隔符，分割成列表
lines = text.split('\n')        

# 在列表的每个元素前加上'* '
for i in range(len(lines)):
	lines[i] = '* ' + lines[i]      

# 将列表合成一个字符串
text = '\n'.join(lines)           
 
pyperclip.copy(text)
print(pyperclip.paste())