# phpbb_pm_notifier
Get hourly desktop notifications about your messages in your favorite phpbb forum 


# Config

Edit the file **config.py** where forum_link add your forum link,where username your forum username and where pass your password

Sample **config.py**
```

forum_auth = {
        'forum_url': "https://theforumurl.com/",
        'username': "yourusername", 
        'password': "yourpassword" 
    }
```

# Listen 

When you have successfully edit the **config.py** and you have fill the corect login details and forum url are you ready to start 
listening about new pm on the specific forum,to start listening simple run **python listen.py**




