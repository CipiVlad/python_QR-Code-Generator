from segno import helpers

yes = 'yes'
no = 'no'

print('WiFi Name (SSID): ')
ssid = input()

print('WiFi Password: ')
password = input()

print('security Type (i.e. WPA, WPA2 ... :)')
security = input()

print(ssid + ', ' + password + ', ' + security)
print('Correct? Type: yes or no ')

question = input()

if question == yes:

	qrcode = helpers.make_wifi(ssid=ssid, password=password, security=security)
	qrcode.designator
	'3-M'
	qrcode.save(ssid + '.png', scale = 10,dark='darkred', light='yellow')


	print("Well done!")
	print('Get Your QR-Code inside of this directory.')

elif question == no:
	print('Try again!')
else: 
	print('Please run program again: choose yes or no.') 
