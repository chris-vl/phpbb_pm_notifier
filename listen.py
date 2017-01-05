#!/usr/bin/env python


from bs4 import BeautifulSoup
from gi.repository import Notify, GdkPixbuf
import login 
import time 




def have_pm(soup_res):
    count = len(soup_res.findAll('dl', {'class' : 'icon pm_unread'}))
    return count


def extract_pms(soup_res):
    for i in soup.find_all('dl', {'class' : 'icon pm_unread'}):
        username = i.select_one("a.username").getText()
        subject = i.select_one("a.topictitle").getText()
        pm_notify(username,subject)
        time.sleep(60)


def pm_notify(user,subject):
	Notify.init("Forum pm notify")
	summary = "New Message from %s" %user
	body = "Subject: %s" %subject
	notification = Notify.Notification.new(
	    summary,
	    body, # Optional
	)

	image = GdkPixbuf.Pixbuf.new_from_file("msg.png")
	notification.set_icon_from_pixbuf(image)
	notification.set_image_from_pixbuf(image)

	notification.show()




while True:
    response = login.login()
    soup = BeautifulSoup(response, "lxml") 
    if have_pm(soup) > 0:
    	extract_pms(soup)
    	time.sleep(3600)

