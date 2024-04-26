# This is a sample Python script.
import socket
import sys
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(status):#######
    sender = 'ENSBOT@bracbank.com'
    receivers = ['nahid.hasan32081@bracbank.com']
    # receivers = ['nahid.hasan32081@bracbank.com']
    cc_recipients = ['nahid.hasan32081@bracbank.com']  # Add CC recipients here
    subject = 'Election Commission Status'

    curr_time = time.strftime("%H:%M:%S", time.localtime())

    message = f"""
    Currently Election Commission (EC) is {status}
    Current time is {curr_time}
    """

    try:
        msg = MIMEMultipart()  # Create a MIME message

        msg['From'] = sender
        msg['To'] = ', '.join(receivers)
        msg['Cc'] = ', '.join(cc_recipients)  # Set CC recipients
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        smtpObj = smtplib.SMTP("IP", port)
        smtpObj.sendmail(sender, receivers + cc_recipients, msg.as_string())  # Send the MIME message
        smtpObj.quit()
        print("Successfully sent email")
    except smtplib.SMTPException as e:
        print("Error: unable to send email:", str(e))

def telnet_check(host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout in seconds
        s.settimeout(10)
        # Attempt to connect to the host and port
        s.connect((host, port))
        # Close the connection
        s.close()
        return True  # Connection successful

    except socket.error as e:
        print(f"Unable to connect to {host} on port {port}: {e}")
        return False  # Connection failed


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Replace these values with the appropriate host and port
    host = "IP"
    port = port # Change the port number if needed
    while True:
        for i in range(3):
            print("checking ", i)
            result = telnet_check(host, port)
        if result:
            print(f"Telnet to {host}:{port} is OK")
            # time.sleep(60)  ##for now it is 1min
            # print("slept for 5mins")
            send_mail("UP")
            sys.exit(0)
        else:
            print(f"Telnet to {host}:{port} failed")
            send_mail("DOWN")
            sys.exit(0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
