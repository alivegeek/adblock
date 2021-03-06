from Tkinter import *
from getHosts import *
def mainWindow():
    ### Main GUI
    #Main Window
    root = Tk()
    root.minsize(width=620,height=200)
    root.wm_title("Ad Blocker v0.3 by NHolbrook")
    # photo = PhotoImage(file="./icon.ico")
    # root.tk.call('wm', 'icon', root._w, icon)

    ### Standard Menu Bar
    menubar = Menu(root)

    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=root.quit)
    filemenu.add_command(label="Run In Background On Startup", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=aboutWindow )
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)

    ### Top Frame - Begin Instructions Label
    labelframe_widget = LabelFrame(root, text="Instructions")
    label_widget = Label(labelframe_widget, justify=LEFT, text="This App blocks Ads, Malware Sites and other undesirable internet traffic using your hosts file. Some virus scanners including Windows Defender \n see modifying the Hosts file as a hijack attempt due to its ability to redirect traffic maliciously. \n \n Select the block lists you would like to use from the list below.")
    labelframe_widget.grid(column=1)
    label_widget.grid(column=1)



    choicesframe_widget = Frame(root)
    #List of hosts file sources for user to choose

    global listbox_entries

    # listbox_entries = ['1. The AdAway hosts file (adaway.org) - Blocks Ads, Updated Regularly"', '2. Dan Pollock - SomeonewhoCares.org (Blocks Ads, Shock Sites, HiJacks, Malware, Spyware, Tracking, etc.', '3. MVP Hosts File - http://winhelp2002.mvps.org/hosts.htm', '4. Malware Domain List at http://www.malwaredomainlist.com/, updated regularly.']

    listbox_entries = {'1. The AdAway hosts file (adaway.org) - Blocks Ads, Updated Regularly': 0, '2. Dan Pollock - SomeonewhoCares.org (Blocks Ads, Shock Sites, HiJacks, Malware, Spyware, Tracking, etc.': 0, '3. MVP Hosts File - http://winhelp2002.mvps.org/hosts.htm': 0, '4. Malware Domain List at http://www.malwaredomainlist.com/, updated regularly.': 0}
    checkbox_object = []
    # listbox_entries = {'ID1050': 0, 'ID1106': 0, 'ID1104': 0, 'ID1102': 0}
    for each_listbox_item in sorted(listbox_entries):
        listbox_entries[each_listbox_item] = BooleanVar()
        l = Checkbutton(root, text=each_listbox_item, variable=listbox_entries[each_listbox_item])
        l.grid(column=1, sticky=W)
        checkbox_object.append(l)


    def select_all():
        for each in checkbox_object:
            each.select()

    def deselect_all():
        for each in checkbox_object:
            each.deselect()
    def runTest():
        choices = []
        #
        # print listbox_entries["1. The AdAway hosts file (adaway.org) - Blocks Ads, Updated Regularly"].get()
        # print listbox_entries['2. Dan Pollock - SomeonewhoCares.org (Blocks Ads, Shock Sites, HiJacks, Malware, Spyware, Tracking, etc.'].get()
        # print listbox_entries['3. MVP Hosts File - http://winhelp2002.mvps.org/hosts.htm'].get()
        # print listbox_entries['4. Malware Domain List at http://www.malwaredomainlist.com/, updated regularly.'].get()

        choices.append(listbox_entries["1. The AdAway hosts file (adaway.org) - Blocks Ads, Updated Regularly"].get())
        choices.append(listbox_entries['2. Dan Pollock - SomeonewhoCares.org (Blocks Ads, Shock Sites, HiJacks, Malware, Spyware, Tracking, etc.'].get())
        choices.append(listbox_entries['3. MVP Hosts File - http://winhelp2002.mvps.org/hosts.htm'].get())
        choices.append(listbox_entries['4. Malware Domain List at http://www.malwaredomainlist.com/, updated regularly.'].get())
        # a = getHosts.getHosts(choices)
        # hosts = getHosts2(choices)
        # dedupeHosts(hosts)
        backupHostsFile()
        # print type(dedupedHosts)
        # writeHosts(dedupeHosts)
        writeHosts(dedupeHosts(getHosts2(choices)))


    cboxes = []
    box_values = {1:0, 2: 0, 3: 0, 4: 0}
    # create_cboxes()
    Button(root, text = 'Select All', command = select_all).grid(row=5,column=1,sticky=W)
    Button(root, text = 'Select None', command = deselect_all).grid(row=6,column=1, sticky=W)

    buttonsframe_widget = Frame(root)
    buttonsframe_widget.grid(row=10,column=0,columnspan=2,sticky=S)
    patch_button = Button(buttonsframe_widget, text="Patch")
    quit_button = Button(buttonsframe_widget, text="Quit", command=root.quit)
    patch_button.grid(row=0)
    quit_button.grid(row=0,column=1, )  
    test_button = Button(buttonsframe_widget, text="Test", command=runTest)
    test_button.grid()


    root.mainloop()

def aboutWindow():

    # create child window
    win = Toplevel()
    win.wm_title("About Ad Blocker")
    # display message
    title = "Ad Blocker v0.3 by NHolbrook "
    subtitle = "Ad blocking via Windows host file with options to update and auto update on boot"
    message = "This SOFTWARE PRODUCT is provided by THE PROVIDER \"as is\" and \"with all faults.\" THE PROVIDER makes no representations or warranties of any kind concerning the safety, suitability, lack of viruses, inaccuracies, typographical errors, or other harmful components of this SOFTWARE PRODUCT. There are inherent dangers in the use of any software, and you are solely responsible for determining whether this SOFTWARE PRODUCT is compatible with your equipment and other software installed on your equipment. You are also solely responsible for the protection of your equipment and backup of your data, and THE PROVIDER will not be liable for any damages you may suffer in connection with using, modifying, or distributing this SOFTWARE PRODUCT."
    Label(win, text=title, font=('helvetica', 14, 'bold')).pack()
    Label(win, text=subtitle,wraplength=400, font=('helvetica', 12)).pack()
    Label(win, text=message,wraplength=400, font=('helvetica', 6, 'italic')).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    Button(win, text='OK', command=win.destroy ).pack()


if __name__ == "__main__":
    getAdmin()
    mainWindow()
