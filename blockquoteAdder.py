#! python3

import pyperclip
#Store text from clipboard
text = pyperclip.paste()

#Seperate lines and add >
lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = '> ' + lines[i]

#Rejoin the modified lines
text = '\n'.join(lines)

#Copy new text in the clipboard
pyperclip.copy(text)