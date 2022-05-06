import sys
import csv
import re
from twilio.rest import Client
import smtplib

assid = 'AC5a68c81973bf7c5d51669bcca1e7595e'
atoken ='ddb10f4974848519b698bdd6daeb2c1d'

email = "nuassabu3@gmail.com"
password ="abunuass3"


def add(i):
    with open ("data.csv","a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(i)
        
#add(["ken","m","0988 ","as@gmail.com"])
#add(["olu","m","1238 ","ols@gmail.com"])


def view():
    data = []
    with open ("data.csv") as f:
        read = csv.reader(f)
        for row in read:
            data.append(row)
    return data

def remove (i):
    def save(j):
        with open("data.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(j)
    newlist = []
    telephone = i
    
    with open("data.csv", "r") as f:
        read = csv.reader(f)
        for row in read:
            newlist.append(row)
            for element in row:
                if element == telephone:
                    newlist.remove(row)
    save(newlist)
#remove('0988')
#view()



def update(i):
    def update_newlist(j):
        with open("data.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(j)
    newlist = []
    telephone = i[0]
    
    with open("data.csv") as f:
        read = csv.reader(f)
        for row in read:
            newlist.append(row)
            for element in row:
                if element == telephone:
                    name = i[1]
                    gender = i[2]
                    telephone = i[3]
                    email = i[4]
                    data = [name, gender, telephone, email]
                    index = newlist.index(row)     
                    newlist[index] = data
    update_newlist(newlist)
#sample = ["9876","kene","m","9876","pasckene@gmail.com"]
#update(sample)

def search(i):
    data = []
    telephone = i
    with open("data.csv", "r") as f:
            read = csv.reader(f)
            for row in read:
                for element in row:
                    if element == telephone:
                        data.append(row)
    return data
#search("1234")
          
    
def makecall(i):
            dat = []
            telephone = i
            with open("data.csv") as f:
                read = csv.reader(f)
                for row in read:
                    dat.append(row)
                    for element in row:
                      
                        if element == telephone:
                            pass
                            #newlist.remove(row)
def tocall(i):
    client = Client(assid, atoken)
    call = client.calls.create(
    twiml = '<Response><Say>hello</Say></Response>',
    to= f'{i}',
    from_ = '+19133793936'
    )
    print (call.sid)
def tosende(i):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(email, password )
            connection.sendmail(
            from_addr = email,
            to_addrs = f"{i}",
            msg=f"subject: Monday Quote  \n\n {quote}" )
        