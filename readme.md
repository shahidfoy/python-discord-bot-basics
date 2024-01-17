# Tutorial steps
- 1. setup
- 2. events
- 3. commands
- 4. cogs 
- 5. tasks
- 6. mod cog
- 7. admin cog
- 8. poll cog
- 9. hosting your bot on heroku

## Installing discory.py library
Before we can make any bots, we first have to install the discord.py library. Here's how to do that:

### On Windows:

Open up your Command Prompt (go the Windows Search Bar and type in "cmd")

Type in this command: 

```bash
py -3 -m pip install -U discord.py[voice]
```

if that doesn't work, try 
```bash
pip install -U discord.py[voice]
```

### On Mac:

Open up your Terminal

Type in 
```bash
python3 -m pip install -U "discord.py[voice]"
```

Note: discord.py is only supported by Python 3.5.3 or higher. If you have a lower version, go download a newer version at the Python Homepage.

## Discord developer setup
discord developer portal: https://discord.com/developers/applications \
create `New Application` \
after applicaiton is created go to `Bot` tab and `Reset Token`
