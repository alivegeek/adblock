import urllib2
from easygui import *
import admin
import shutil
#Dict that matches the descriptions from the main window to the actual URLS of th ehosts files - THIS MUST MATCH availableLists verbatim!
blocklistsDict = {"1. The AdAway hosts file (adaway.org) - Blocks Ads, Updated Regularly":"http://adaway.org/hosts.txt","2. Dan Pollock - SomeonewhoCares.org (Blocks Ads, Shock Sites, HiJacks, Malware, Spyware, Tracking, etc.":"http://someonewhocares.org/hosts/hosts","3. MVP Hosts File - http://winhelp2002.mvps.org/hosts.htm":"http://winhelp2002.mvps.org/hosts.txt","4. Malware Domain List at http://www.malwaredomainlist.com/, updated regularly.":"http://www.malwaredomainlist.com/hostslist/hosts.txt"}


#Gets admin privledges from Windows UAC
def getAdmin():
    if not admin.isUserAdmin():
        admin.runAsAdmin()


def main():
    blocklist = userSelect()
    urlsHosts = []
    for i in range(len(blocklist)):

        if blocklist[i] in blocklistsDict.keys():
            urlsHosts.append(blocklistsDict[blocklist[i]])
    dedupe(getHosts(urlsHosts))
    backupHostsFile()
# Menu prompts user to select what host files to add to their own
def userSelect():
    title = 'AdBlock with Hosts File v0.1 by NHolbrook'
    welcomeMsg = "This App blocks Ads, Malware and other undersirable internet traffic using your hosts file. Select the block lists you would like to use from the list below."
    availableLists = ["1. The AdAway hosts file (adaway.org) - Blocks Ads, Updated Regularly",
                      "2. Dan Pollock - SomeonewhoCares.org (Blocks Ads, Shock Sites, HiJacks, Malware, Spyware, Tracking, etc.",
                      "3. MVP Hosts File - http://winhelp2002.mvps.org/hosts.htm",
                      "4. Malware Domain List at http://www.malwaredomainlist.com/, updated regularly.",]

    chosenLists = multchoicebox(welcomeMsg,title=title, choices=availableLists )

    return chosenLists


#Downloads each of the hosts files chosen aboce and stores each line as an entry in a list
def getHosts(urlHosts):
    hostLines = []
    hostLinesFix = []
    def getEach(url):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0'), ]
        response = opener.open(url)
        hostdata = response.read()        # hostLines.append()        # a.striplines    # print dedupedList
        # print hostLines



        return hostdata


    for each in urlHosts:
        hostLines.append(getEach(each))
    for each in hostLines:
       a = each.splitlines()
       hostLinesFix.append(a)
    return hostLinesFix

#Removes any duplicate entries from the list
global dedupedList
dedupedList = []

def dedupe(list):
    for i in list:
        if i not in dedupedList:
            dedupedList.append(i)
    return dedupedList

#Backs up the systems existing host file
global hostsPath
hostsPath = "C:\\Windows\\System32\\drivers\\etc\\"

def backupHostsFile():
    shutil.copy(hostsPath + "hosts",hostsPath + "hosts.bak")

def writeHosts():
    f = open(hostsPath + "hosts", "w")
    for each in dedupedList:
        f.write(str(each) + "\n")

    f.close

if __name__ == '__main__':
    blocklist = userSelect()
    urlsHosts = []
    for i in range(len(blocklist)):

        if blocklist[i] in blocklistsDict.keys():
            urlsHosts.append(blocklistsDict[blocklist[i]])
    dedupe(getHosts(urlsHosts))
    backupHostsFile()
    writeHosts()






#Trash Code

