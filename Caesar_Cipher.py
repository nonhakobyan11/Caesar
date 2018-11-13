k = input("Input the key - ")
t = input("Input the text - ")

def kodavorum(k,t):
	x = ''
	for i in t:
		if ord(i)>=ord('a') and ord(i)<=ord('z'):
			if ord(i)+k > ord('z'):
				x = x + chr((ord(i)+k)-26)
			else:
				x = x + chr(ord(i)+k)
		elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
			if ord(i)+k>ord('Z'):
				x = x+chr((ord(i)+k)-26)
			else:
				x = x+chr(ord(i)+k)
		else:
			x = x + i
	return x


    

def vercanum(k,t):
	x = ''
	for i in t:
		if ord(i)>=ord('a') and ord(i)<=ord('z'):
			if ord(i)-k < ord('a'):
				x = x + chr((ord(i)-k)+26)
			else:
				x = x + chr(ord(i)-k)
		elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
			if ord(i)-k<ord('A'):
				x = x + chr((ord(i)-k)+26)
			else:
				x = x + chr(ord(i)-k)
		else:
			x = x + i
	return x



#print ("Deciphered text is - ", vercanum(int(k),t))
print ("Ciphered text is - ",kodavorum(int(k),t))
