import pyqrcode

text = ""

print('================================================')
print('What type of QRCode would you like to create?')
print('1. Text')
print('2. Phone Number')
print('3. Email')
print('4. URL')
print('5. Send SMS')
print('6. Geo location')
print('7. Wifi Connection')
print('================================================')

QRtype = raw_input(":> ")

if QRtype == "1": 
    text = raw_input("Please, enter the text: ")
elif QRtype == "2":
    data = raw_input("Please, enter the phone number: ")
    text = "tel:" + data
elif QRtype == "3":
    data = raw_input("Please, enter the email: ")
    text = "mailto:" + data
elif QRtype == "4":
    data = raw_input("Please, enter the URL: ")
    if data.startswith("https://") or data.startswith("http://"):
        text = data
    else:
        text = "http://" + data + "/"
elif QRtype == "5":
    number = raw_input("Please, enter the number of the person: ")
    message = raw_input("Now, enter the message you want to send (in case you don't want an specific message press enter without a message): ")
    if message != "" or message != " ":
        text = "sms:" + number + "?body=" + message
    else:
        text = "sms:" + number
elif QRtype == "6":
    latitude = raw_input("Please, enter the latitude: ")
    longitude = raw_input("Please, enter the longitude: ")
    altitude = raw_input("Please, enter the altitude (in meters): ")
    text = "geo:" + latitude + "," + longitude + "," + altitude
elif QRtype == "7":
    ssid = raw_input("Please, enter the SSID: ")
    passwordType = raw_input("Please, enter the password encryption (NONE, WPA/WPA2, WEP): ")
    password = raw_input("Please, enter the password: ")
    if passwordType == "NONE":
        text = "WIFI:S:" + ssid + ";T:nopass;P:" + password + ";;"
    elif passwordType == "WPA/WPA2":
        text = "WIFI:S:" + ssid + ";T:WPA;P:" + password + ";;"
    elif passwordType == "WEP":
        text = "WIFI:S:" + ssid + ";T:WEP;P:" + password + ";;"

url = pyqrcode.create(text)
url.svg('Output.svg',scale = 8)
print(url.terminal(quiet_zone = 1))