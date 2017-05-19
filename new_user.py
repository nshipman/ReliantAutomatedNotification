import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# Reads the email template located in the same directory as this script. 
# The .txt file is stored in the variable template. 

with open("new_user.txt") as file:

        template = file.read()

fromaddr = 'internal.reliantsolutions@gmail.com'
toaddr = raw_input('Enter employee\'s address: ')
your_pwd = raw_input('Enter the password for YOUR internal mailing systen: ') 

msg = MIMEMultipart()
msg['From'] = "Reliant Internal Notification"
msg['To'] = toaddr
msg['Subject'] = "[Internal Notification]Reliant Solutions - New User Setup"

# Input data for the conference bridge template. 
employee_name = raw_input('Enter Employee\'s name: ')
user_name = raw_input('Enter employee\'s Username: ')
temp_pwd = raw_input('Enter employee\'s temp password for AD: ')
temp_pwd_2 = raw_input('Enter employee\'s temp password for their email: ') 
phone_number = raw_input('Enter employee\'s Intermedia phone number: ')
ext = raw_input('Enter employee\'s extension: ')
webfax_number = raw_input('Enter employee\'s Webfax Number: ') 
temp_pin = raw_input('Enter employee\'s temp password for their phone and webfax services (same pin): ')
# The body variable stores the formatted template information which will be presented in the main body of the email. 

body = template.format(employee_name = employee_name, user_name = user_name, temp_pwd = temp_pwd, temp_pwd_2 = temp_pwd_2, phone_number = phone_number, ext = ext, webfax_number = webfax_number, temp_pin = temp_pin )
contents = body
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, your_pwd)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print("New user infromation has been sent successfully")
server.quit()

