import imaplib



# Log in credentials for the email account
EMAIL = "email@email.com"
PASSWORD = "password"

# Mail folder (inbox, sent and etc.)
mail_box="Inbox"

# Link/IP for the imap server
mail_server=""

# Connect and login to mail server
imap = imaplib.IMAP4_SSL(mail_server)   # Connect
imap.login(EMAIL,PASSWORD)              # Login

# Set the mail folder
imap.select(mail_box)

# Email filtering
_, mail_index = imap.search(None,"ALL")



# Loop all the mails in mail_box
for index in mail_index[0].split():
    _, mail_data = imap.fetch(index,"(RFC822)")
    email = email.message_from_bytes(mail_data[0][1])

    # Print the subject of each mail
    print(mail.get("Subject"))



# Close and log out from server
imap.close()
imap.logout()
