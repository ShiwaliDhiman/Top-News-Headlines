import requests
from bs4 import *
import smtplib
from email.message import EmailMessage
import datetime,os
td=datetime.date.today()
pemail=os.environ.get("User_Email")
p_password=os.environ.get("User_Password")


print("Connecting to source....Please wait!!!!")
page=requests.get("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

print("-----------------------------------------------------------------------------------")
print(">>>>>>>>>>>>>>>>TODAY'S TOP NEWS HEADLINES<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("---------------------------------------------------------------------------------")
print(td.strftime("%d-%b-%y"))
print("------------------------------------------------------------------------------------")
soup=BeautifulSoup(page.content,"html.parser")
containers=soup.find_all("h3")

filename="Latest_News_Headlines.txt"
f=open(filename,'w',encoding='utf-8')
f.write(td.strftime("%d-%b-%y")+"\n")
f.write("         --------------------------------------------------------"+"\n")
f.write("           TODAY'S TOP NEWS HEADLINES                "+"\n")
f.write("          --------------------------------------------------------             "+"\n")
i=1
for container in containers:
    print(str(i)+">>"+container.get_text())
    f.write(str(i)+"."+container.get_text()+"\n")
    i+=1
f.close()

print("*********************************************")
print("adding these headlines to your mail...")
user_email_id=input("Enter your Email in which you want your news headlines????")
msg=EmailMessage()
msg["Subject"]="Today's Top News Headlines"
msg["From"]=pemail
msg["To"]=user_email_id
msg.set_content("Here is the attached document to see the news headlines")
with open(filename,"rb") as f:
    file_name=f.name
    file_data=f.read()

msg.add_attachment(file_data, maintype="document",subtype="txt",filename=file_name)

server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login(pemail,p_password)
server.send_message(msg)
server.quit()
print("successfully added to you email id_______:):):)")







