sen = 'this is a string with spaces'
splits = []
pos = -1
last_pos = -1
while ' ' in sen[pos + 1:]:
pos = sen. index(' ', pos + 1)
splits. append(sen[last_pos + 1 pos])