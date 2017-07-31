import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host = "smtp.gmail.com"
port = 587
username = "sxsw2016bchang@gmail.com"
password = "11478542"
from_email = username
to_list = ["b.b.briann@gmail.com"]
try:
	email_conn = smtplib.SMTP(host, port)
	email_conn.ehlo()
	email_conn.starttls()
	email_conn.login(username, password)
	# email_conn.sendmail(from_email, to_list, "Hello there this is python test2.")
	# typically set to alternative - tells system this is a html message
	the_msg = MIMEMultipart("alternative")
	the_msg['Subject'] = "Hello there!"
	the_msg["From"] = from_email
	# the_msg["To"] = to_list
	plain_txt = "Testing the message"
	html_txt = """\
	<html lang="en">
	<head>
		<title></title>
		<meta charset="UTF-8">
	</head>
	<body>
		Testing this email <b>message</b> Made by <a href="http://google.com">LINKS WHAT WHAT WHAT</a>
	</body>
	</html>
	"""
	part_1 = MIMEText(plain_txt, 'plain')
	part_2 = MIMEText(html_txt, "html")
	the_msg.attach(part_1)
	the_msg.attach(part_2)
	# print(the_msg.as_string())
	email_conn.sendmail(from_email, to_list, the_msg.as_string())
	email_conn.quit()
except smtplib.SMTPException:
	print("error sending message")