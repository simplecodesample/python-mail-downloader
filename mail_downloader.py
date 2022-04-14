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
