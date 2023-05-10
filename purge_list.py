def purge():
    print("does nothing yet")


# alright so what i'm doing is running some timed function in bot.py to add items to the purge list that i'll define here, then run another timed function two minutes after that last timed function to print out the purge list, which by then, should be populated.

# i can confirm that it's populated with the right people by running it in the populated discord server, and as long as it prints the right list, i can test the kick function in the test server, then deploy it for production.

# i see no reason that this shouldn't work; can even define the timer function in this file.

# so for when i get the database working, what happens if someone rejoins and fails to complete the onboarding again? i should set a column for number of times kicked, and have it incremented with each kick.