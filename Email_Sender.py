import smtplib

from tkinter import *
from email.mime.text import MIMEText
from envs import password


sender = "enter sender email" #email of the sender


def sendEmail():
    
    subject = subjectEntry.get()
    body = bodyText.get("1.0", END)

    recipients = recipientEntry.get().split(",") #get recipients from the entry field, split by commas
    recipients = [email.strip() for email in recipients] #clean up spaces around email addresses

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)

            for recipient in recipients:
                #create a message for each recipient in the list
                message = MIMEText(body)
                message['Subject'] = subject
                message['From'] = sender
                message['To'] = recipient

                smtp_server.sendmail(sender, recipient, message.as_string())

        statusLabel.config(text="Message sent to all recipients!", fg="green")
    except Exception as e:
        statusLabel.config(text=f"Something went wrong: {e}", fg="red")


#create the user interface
root = Tk()
root.title("Email Sender")
root.geometry("700x400")


Label(root, text="Email subject:").grid(row=0, column=0, padx=10, pady=5)
subjectEntry= Entry(root, width=50)
subjectEntry.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Body: ").grid(row=1, column=0, padx=10, pady=5)
bodyText= Text(root, width=50, height=10)
bodyText.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Sender: ").grid(row=2, column=0, padx=10, pady=5)
senderLabel= Label(root, text=sender)
senderLabel.grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Recipients (separate by a comma): ").grid(row=3, column=0, padx=10, pady=5)
recipientEntry = Entry(root, width=50)
recipientEntry.grid(row=3, column=1, padx=10, pady=5)

sendButton = Button(root, text="Send Email", command=sendEmail)
sendButton.grid(row=4, column=1, padx=10, pady=10)
sendButton.config(bg='lightgreen') 
statusLabel = Label(root, text="", fg="black")
statusLabel.grid(row=5, column=1, padx=10, pady=5)

root.mainloop()
