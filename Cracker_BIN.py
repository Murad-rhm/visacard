import random,os,sys,requests
Ba = 0
os.system("clear")
A = '\033[2;34m'
Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
B = '\033[2;36m'
Y = '\033[1;34m'
G = '0123456789'
TY = '123456789'
def me():
    os.system("lolcat logo.txt")
me()
print(Z+'='*58)
print(F+'  𝑺𝑯𝒐𝒘 𝒚𝒐𝒖𝒓 𝒔𝒌𝒊𝒍𝒍𝒔      ')
print('')
bw = input(Y+'(1) 𝘋𝒐 𝒚𝒐𝒖.𝒘𝒂𝒏𝒕 𝒕𝒐 𝘏𝘈𝘊𝘒 𝑩𝑰𝑵 𝘝𝘐𝘚𝘈   \n(2) 𝘉𝐈𝐍 𝐈𝐧𝐟𝐨 \n(3) 𝘋𝐨 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐦𝐚𝐤𝐞 𝐯𝐢𝐬𝐚𝐬    \n\n𝘊𝐡𝐨𝐨𝐬𝐞 𝐨𝐧𝐞  => ')
print(Z+'-'*58)
if bw == '1':
	os.system('clear')
	me()
	print(Z+'='*58)
	print(F+'  𝐖𝐇𝐀𝐓 𝐃𝐎 𝐘𝐎𝗨 𝐖𝐀𝐍𝐓?      ')
	print('')
	token = input(B+'𝘌𝐧𝐭𝐞𝐫 𝐲𝐨𝐮𝐫 𝘛𝘖𝘒𝘌𝘕  => ')
	ID = input(B+'𝘌𝐧𝐭𝐞𝐫 𝐲𝐨𝐮𝐫 𝐈𝘋  => ')
	
	while True:
		ml = '3'+str(''.join((random.choice(G) for i in range(5))))
		xc = '4'+str(''.join((random.choice(G) for i in range(5))))
		za = [ml,xc]
		v = (random.choice(za))
		api = f'https://lookup.binlist.net/{v}'
		reg = requests.get(api)
		response = reg.text
		if '"country"' in response:
		  	f = requests.get(api)
		  	res = f.json()
		  	z = res['country']['emoji']
		  	m = res['scheme']
		  	k = res['country']['name']
		  	g = res['country']['currency']
		  	u = v
		  	p = k +' '+z
		  	tlg = print(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=®
 HI ,
 
 NEW LIVE✅ BIN 
 
 FROM 😍𝐑𝐢𝐝𝐨𝐲😍
*---------------------------------------*
- 🏦BIN =>  {u}
- 🌏CoUnTrY =>  {p}
- 💳CaRd TyBe => {m}
- 💸The CuRrEnCy => {g}
*--------------------------------------                      ''')
		  	i = requests.post(tlg)
		  	print(F+'Available =>  '+v)
		  	print(k+' '+z)
		  	print(g)
		  	print(m)
		else:
			print(Z+'Not Available =>  '+v)
if bw == '2':
	print(Z+'='*58)
	tok = input(B+'𝘌𝐧𝐭𝐞𝐫 𝐘𝐨𝐮𝐫 𝘛𝘖𝘒𝘌𝘕  => ')
	id = input(B+'𝘌𝐧𝐭𝐞𝐫 𝐘𝐨𝐮𝐫 𝐈𝘋 => ')
	while True:
		v = input(F+'𝘌𝐧𝐭𝐞𝐫 𝐘𝐨𝐮𝐫 𝘉𝐈𝘕  =>  ')
		api = f'https://lookup.binlist.net/{v}'
		reg = requests.get(api)
		res = reg.json()
		z = res['country']['emoji']
		m = res['scheme']
		k = res['country']['name']
		g = res['country']['currency']
		print(B+k+z)
		print(B+m)
		print(B+g)
		u = v
		p = k +' '+z
		print('Done Send Your Bot ! ')
		print(Z+'='*58)
		tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=®
 HI ,
 
 NEW LIVE✅ BIN 
 
 FROM 🖤𝐑𝐢𝐝𝐨𝐲😍 
*--------git clone-------------------------------*
- 🏦BIN =>  {u}
- 🌏CoUnTrY =>  {p}
- 💳CaRd TyBe => {m}
- 💸The CuRrEnCy => {g}
*---------------------------------------*                      ''')
		i = requests.post(tlg)
if bw == '3':
	os.system('clear')
	print(F+'    𝑊𝐸𝐿𝐶𝑂𝑀𝐸   \n')
	me() 
	tok = input(Z1+'𝘌𝐧𝐭𝐞𝐫 𝐲𝐨𝐮𝐫 𝘛𝘖𝘒𝘌𝘕  => ')
	id = input(Z1+'𝘌𝐧𝐭𝐞𝐫 𝐘𝐨𝐮𝐫 𝐈𝘋  => ')
	os.system(f'rm -rf murad.txt')
	B = input(B+'(1) 𝑉𝐼𝑍𝐴 𝑅𝐚𝐧𝐝𝐨𝐦   \n(2) 𝑉𝐼𝑍𝐴 𝐹𝑅𝑂𝑀 𝐁𝐈𝐍   \n𝘊𝐡𝐨𝐨𝐬𝐞  => ')	
def bae():
	print(A+'='*58)
	if B == '2':
		ba = input('\033[1;31m'+'𝘠𝘖𝘜𝘙 𝘉𝘐𝘕 5 𝐨𝐫 6 ? => ')
		if ba == '6':
			bi = input(F+'𝘌𝐧𝐭𝐞𝐫 𝐘𝐨𝐮𝐫 𝘉𝐈𝐍  => ')
		if ba == '5':
			bi = input(F+'𝘌𝐧𝐭𝐞𝐫 𝐘𝐨𝐮𝐫 𝘉𝘐𝘕  => ')
	G = '0123456789'
	Z = ['2023','2024','2025','2026','2027','2028']
	Ba = 0
	while Ba < 20:
	   		if B == '1':
    				v = str(''.join((random.choice(G) for i in range(16))))
    				b = str(''.join((random.choice(TY) for i in range(2))))
    				a = str(''.join((random.choice(G) for i in range(3))))
    				p = str(random.choice(Z))
    				h = v+'|'+'0'+b+'|'+p+'|'+a
    				print(X+'𝘝𝘐𝘚𝘈 ==> '+'\033[2;36m'+h)
    				g = open('murad.txt', 'a')
    				g.write(h+ '\n')
    				tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={h} + \n''')
    				i = requests.post(tlg)
    				Ba = Ba + 1
	   		if B == '2':
	   			if ba == '5':
    					v = str(''.join((random.choice(G) for i in range(11))))
    					b = str(''.join((random.choice(TY) for i in range(2))))
    					a = str(''.join((random.choice(G) for i in range(3))))
    					p = str(random.choice(Z))
    					h = bi+v+'|'+'0'+b+'|'+p+'|'+a
    					print(X+'𝘝𝘐𝘚𝘈 ==> '+'\033[2;36m'+h)
    					g = open('murad.txt', 'a')
    					g.write(h+ '\n')
    					Ba = Ba + 1
    					tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={h} + \n''')
    					i = requests.post(tlg)
	   			if ba == '6':
	   				v = str(''.join((random.choice(G) for i in range(10))))
	   				b = str(''.join((random.choice(TY) for i in range(1))))
	   				a = str(''.join((random.choice(G) for i in range(3))))
	   				p = str(random.choice(Z))
	   				h = bi+v+'|'+'0'+b+'|'+p+'|'+a
	   				print(X+'𝘝𝘐𝘚𝘈 ==> '+'\033[2;36m'+h)
	   				g = open('murad.txt', 'a')
	   				g.write(h+ '\n')
	   				Ba = Ba + 1
	   				tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={h} + \n''')
	   				i = requests.post(tlg)
	   		

bae()  				
