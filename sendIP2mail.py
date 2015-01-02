
import ipgetter
import smtplib


def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

# gets my external IP
myip = ipgetter.myip()

f = open('myip.dat','r+')
fileip = f.read()

# sends the IP to my e-mail address
if myip != None and myip != fileip:
    f.write(myip) # python will convert \n to os.linesep
    f.close()
    sendemail(from_addr    = 'from@gmail.com', 
              to_addr_list = ['to@gmail.com'],
              cc_addr_list = ['cc@gmail.com'], 
              subject      = 'IP change notification', 
              message      = myip, 
              login        = 'from', 
              password     = 'password')
else:
    f.close()
    


