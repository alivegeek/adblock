import urllib2
import admin
import shutil

def getAdmin():
    if not admin.isUserAdmin():
        admin.runAsAdmin()

def getHosts(user_choices):

