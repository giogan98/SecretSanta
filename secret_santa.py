import csv
import copy
import random
import smtplib
from itertools import chain
import config


def importEmailsFromCSV():
    emails = []
    with open('emails.csv', newline = '') as f:
        reader = csv.reader(f)
        emails = list(filter(None, chain(*reader)))
    return emails

def sendEmail(gift_sender, gift_receiver):
    message = """\
    Secret Santa più bello di sempre \n
    Ciao, l'essere fortunato a cui devi fare il regalo è: """ 
    #message += gift_receiver[0 : gift_receiver.find('@')]
    print(message)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(config.gmail_user, config.gmail_password)
        #server.sendmail(config.gmail_user, gift_sender, message)
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong...')

def startSecretSanta(emails):
    remaining_receivers = emails.copy()

    for ii in range (0, len(emails)):
        possible_receivers = remaining_receivers.copy()
        try:
            possible_receivers.remove(emails[ii])
        except:
            pass
        chosen = random.choice(possible_receivers)
        remaining_receivers.remove(chosen)
        sendEmail(emails[ii], chosen)        

if __name__ == '__main__':
    lista = importEmailsFromCSV()
    startSecretSanta(lista)