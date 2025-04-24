def luas_lingkaran(radius) :
	luas = 3, 14 * radius * radius
	return luas	

r = int(input('masukkan jari-jari: '))
L = luas_lingkaran(r)

print(f'Luas lingkaran adalah {L}')