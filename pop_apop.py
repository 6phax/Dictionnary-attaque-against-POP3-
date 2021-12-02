import hashlib


texte = '<1896.697170952@dbc.mtview.ca.us>'  # the hidden password is "tanstaaf"

with open('rockyou.txt', 'rb') as file:
	passwords = file.readlines()
   
print('processing ....\n')
for i in passwords:
		try:
			
			i = str(i, 'UTF-8').replace('\n','')
			tmp = texte + i
			utf = tmp.encode('UTF-8')
			
			hashe = hashlib.md5(utf)
			hexa = hashe.hexdigest()
			if hexa == "c4c9334bac560ecc979e58001b3e22fb":    # the md5 hash of <process-ID.clock@hostname>password ;  
				print ('password ==> {}'.format(i))
				break
		except :
				print('pass')
