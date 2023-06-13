Capstone project proposal

1. What goal will your website be designed to achieve?

My capstone project will give discord servers automatic moderation features, as well as user-facing commands proven in a test environment to drive up community engagement.

2. What kind of users will visit your site? In other words, what is the demographic of
your users?

Anyone who uses discord's messaging platform will find utility in my bot; server owners, moderation teams, and end users.

3. What data do you plan on using? You may have not picked your actual API yet,
which is fine, just outline what kind of data you would like it to contain.

The bot runs on discordpy; its documentation can be found here: https://discordpy.readthedocs.io/en/stable/

4. In brief, outline your approach to creating your project (knowing that you may not
know everything in advance and that these details might change later). Answer
questions like the ones below, but feel free to add more information:

a. What does your database schema look like?

The database schema is currently slated to contain two tables; users, and have_not_onboarded.  Its intended purposes are for moderation only.

b. What kinds of issues might you run into with your API?

Unclear documentation (likely a skill issue on my end, to be honest.)

c. Is there any sensitive information you need to secure?

User/server IDs, authorization tokens, user messages, private server channels.

d. What functionality will your app include?

Automatic kicking for users that fail to complete onboarding; a large number of malicious bots tend to join servers solely to harvest user profiles or send malicious/phishing DM's.  Members that fail to complete onboarding, and therefore do not gain access to server channels, are usually not malicious bots, but joining a server and then never actually participating is something that server owners are seeking to cut down on.

With the addition of some for-fun commands like a dice command, and random tarot card drawings for users, the bot ensures that people who are willing to participate in the community stay engaged.

e. What will the user flow look like?

The beautiful thing about the bot's user flow is its ease of access and hands-off moderation.  Users just enter slash commands for whatever user-facing feature they want to use, and moderation doesn't have to lift a finger to kick members who don't do their onboarding.

f. What features make your site more than CRUD? Do you have any stretch
goals?

Stretch goals are any fun user-facing command people would like to see me add, within reason, as well as a privileged role automoderation.

The privileged role assignment would function similarly to the kicking automod function; users that meet a specific criteria as determined by server owners (say, sends 10+ messages within a 7 day sliding window) will be granted a privileged role that gains them access to exclusive channels on the server.

This is something that could be put in place for metrics as simple as active user, and as complex as users who support the server financially through sites like patreon.  (That last part would rely on external API calls.)