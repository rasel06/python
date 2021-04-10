# import os
# arr = os.listdir("/etc")
# f = open("myfile.txt", "w+")
# f.write("\n".join(arr))

import os
import smtplib
import ssl

file_list = "\n".join(os.listdir("/etc"))

port = 2525  # For SSL
smtp_server = "smtp.mailtrap.io"
sender = "rasel.course@gmail.com"  # Enter your address
receiver = "rasel06@gmail.com"  # Enter receiver address
message = """\
Subject: Hi there

This Files are found in 'etc' directory.
"""+file_list


with smtplib.SMTP(smtp_server, port) as server:
    server.login("1d985fa0a1b0bb", "7b70d246629ab1")
    server.sendmail(sender, receiver, message)

print("Mail Sent Successfully")
