import urllib2
import admin
import shutil
global hostlines
hostlines = []
global dedupedHostLines
dedupedHostLines = []


def getAdmin():
    if not admin.isUserAdmin():
        admin.runAsAdmin()
urlList = ["http://adaway.org/hosts.txt", "http://someonewhocares.org/hosts/hosts", "http://winhelp2002.mvps.org/hosts.txt", "http://www.malwaredomainlist.com/hostslist/hosts.txt"]
# def getHosts(user_choices):
#     if user_choices[0] == True:
#         getDataFromServers(urlList[1])

def getHosts(booleanResultsFromMain):
    list(booleanResultsFromMain)
    print booleanResultsFromMain
    for x in booleanResultsFromMain:
        if booleanResultsFromMain[x]== True:
            opener = urllib2.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0'), ]
            response = opener.open(urlList[x])
            hostdata = response.read()
            # return hostdata
        print x
        return hostdata
    return hostdata

def getHosts2(booleanList):
    hostlines = []
    boolList2 = []
    for each in booleanList:
        boolList2.append(str(each))

    for i in range(len(boolList2)):
        if boolList2[i] is "True":
            opener = urllib2.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0'), ]
            response = opener.open(urlList[i])
            hostdata = response.read()
            hostlines.append(hostdata.splitlines())
    return hostlines

    # for each in hostdata:
    #     line = each.splitlines()
    #     hostlines.append(line)

def dedupeHosts(hostlines):
    dedupedList = []
    for each in hostlines:
        for i in each:
            if i not in dedupedList:
                dedupedList.append(i)
    return dedupedList

global hostsPath
hostsPath = "C:\\Windows\\System32\\drivers\\etc\\"

def backupHostsFile():
    shutil.copy(hostsPath + "hosts",hostsPath + "hosts.bak")

def writeHosts(hostsToWrite):
    lines = hostsToWrite

    f = open(hostsPath + "hosts", "w")
    for each in lines:
        f.write(str(each) + "\n")
    f.close



Test = [True,True]
if __name__ == '__main__':
    getAdmin()
    testBoolean = [False,False,False,True]
    a = getHosts2(testBoolean)
    b = dedupeHosts(a)
    writeHosts(b)
