import smtplib, ssl, random
from ss_toolkit import *
# Create a secure SSL context
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
# Create an array of participants
participants = PeopleParser().get_list()
# Randomize the list order
random.shuffle(participants)
# copy the list to make a two-array structure. This prevents the program from running out of indices to pick for the case where one person remains.
remaining = participants.copy()
log = SelectionDatabase("files/log.csv")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    cp = ConfigParser()
    server.login(cp.get_username(), cp.get_password())
    for index, person in enumerate(participants):
        # Person to be sent email to
        recipient_name = person[0]
        recipient_email = person[1]
        # picking a person to be the recipient
        picked = random.choice(remaining)
        # checks to make sure the gifted individual is the giver
        if picked[0] == recipient_name:
            while picked[0] == recipient_name:
                picked = random.choice(remaining)

        remaining.remove(picked)
        log.add(recipient_name, picked[0]) # logging it
        # The message:
        message = f"""Subject: Your Secret Santa Assignment

        Dear {recipient_name},
        
        And now, the moment you've been probably waiting for. Your secret recipient is:
        {picked[0]}
        
        With love and best regards,
        Your friends
        """

        # sends
        server.sendmail(cp.get_username(), recipient_email, message)

