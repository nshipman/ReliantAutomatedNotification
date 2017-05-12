# The following script will access an email template, take command line prompted input from the users 
# and fill in the information. 
# This current version is specially tailored for conference bridge notifications to employees.   
# Version: 1.0
# Company: Reliant Solutions 
# Author: Norman Shipman 

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
  
# Reads the email template located in the same directory as this script. 
# The .txt file is stored in the variable template. 

with open("phone_bridge.txt") as file: 

	template = file.read() 

fromaddr = "internal.email.address@gmail.com"
toaddr = raw_input('Enter employee\'s address: ')

msg = MIMEMultipart() 
msg['From'] = "Reliant Internal Notification" 
msg['To'] = toaddr 
msg['Subject'] = "[Automated System Do Not Reply] Conference Bridge Assignment"

# Input data for the conference bridge template. 
employee_name = raw_input('Enter Employee\'s name: ') 
bridge_number = raw_input('Enter employee\'s conference bridge: ')
guest_pin = raw_input('Enter employee\'s guest pin: ')
host_pin = raw_input('Enter employee\'s host pin: ')

# The body variable stores the formatted template information which will be presented in the main body of the email. 

body = template.format(employee_name = employee_name, bridge_number = bridge_number, guest_pin = guest_pin, host_pin = host_pin)
contents = body 
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587) 
server.starttls()
server.login(fromaddr, "Password For Account") 
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print("Conference Bridge infromation has been sent successfully")
server.quit()
