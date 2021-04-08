


myp = 'soyroroelreno'
passw = 'KHYqOB-4Q_AUoAXoECAIQAQ&biw' + myp + 'KHYqOB-4Q_AUoAXoECAIQAQ&biw'
print(passw)
res = len(passw) - 54
letter = []
rest = 27 + res
for i in passw:
	letter.append(i)
if len(letter) >= 54:
	print(letter[:27])
	print(letter[27:rest])
	restl = letter[27:rest]
else:
	print('No pass')
print(restl)
