This bot uses the discordpy API: documentation can be found at https://discordpy.readthedocs.io/en/stable/

This bot uses python 3.9.0 and postgresql 15.1

For ease of use, I recommend using VSCode to deploy the bot; it allows for ease of access to edit the configuration file and deployment via its built-in terminal.  You are free to use any terminal you can run python on, however.

There are several critical pieces of information that will assist you in deploying this bot to your own discord server with the specifications you desire.

After inviting the bot to your server and setting their privileges as administrator/moderator, you'll want to get some ID's; specifically the ID's of the moderation team, and the ID of the VIP role for your server if you plan on having the VIP role features of the bot enabled. If you just want to use the user-facing features, (dice rolls, tarot cards, chat curses), simply add the bot token to the config.yml file and run the bot by typing python bot.py in the terminal of your choice.

To get these ID's, you will need to enable developer mode on discord.  Don't worry though, it's actually not very hard.  There's a good guide for enabling developer mode and getting user/role ID's <a href="https://www.guidingtech.com/how-to-find-a-discord-user-id/">here</a>, but if you're looking for a quick and dirty rundown...

Launch discord > Click gear icon on bottom left > under app settings, click advanced > first option of advanced is enable developer mode; click it to enable.

Now that developer mode is enabled, you can right click on users to copy their IDs, as well as role ID's.

Copy down the user ID's for the moderation team, and paste them into the ADMIN field of the config.yml file. Do the same with the role ID into the VIP_ROLE field if you're enabling it.

Your bot's token will go into the token field in the config.yml

By default ENABLE_KICKING and ENABLE_VIP are set to False.  If you wish to use these features, change them to True.  You're free to change the values for TASK_LOOP, TASKS_INACTIVE_TIMER, VIP_MESSAGES, and VIP_TIMER.

Some default values are provided for the database configuration. (TODO: Add information on setting up postgresql because i don't remember how to do that for this project)