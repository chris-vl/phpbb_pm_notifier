import cookielib 
import urllib2 
import mechanize 
import sys 
import config 
from BeautifulSoup import BeautifulSoup


def login():
	forum = config.forum_auth.get("forum_url")
	user = config.forum_auth.get("username")
	password = config.forum_auth.get("password")

    # Browser 
	br = mechanize.Browser() 

	# Enable cookie support for urllib2 
	cookiejar = cookielib.LWPCookieJar() 
	br.set_cookiejar( cookiejar ) 

	# Broser options 
	br.set_handle_equiv( True ) 
	br.set_handle_gzip( False ) 
	br.set_handle_redirect( True ) 
	br.set_handle_referer( True ) 
	br.set_handle_robots( False ) 
	br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 ) 

	br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ] 

	# authenticate 
	br.open(forum + "ucp.php?mode=login") 
	br.select_form(nr = 1)
	br[ "username" ] = user
	br[ "password" ] = password
	res = br.submit() 

	url = br.open(forum + "ucp.php?i=pm&folder=inbox") 
	return url.read()
