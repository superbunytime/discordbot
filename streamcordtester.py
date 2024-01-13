import discord, aiohttp, asyncio, sys, time
from discord.ext import commands, tasks
import text_coloring as text_channels
import datetime
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


intents = discord.Intents.all()
client = discord.Client(intents = intents)

@client.event
async def on_message(message):

    msg = message.content

    if message.author.id == 375805687529209857 or message.author.name == "Streamcord":
        # print(f'the condition that triggered this code to run was...')
        # print(f'message.author.id: {message.author.id == 375805687529209857} message.author.name is Streamcord: {message.author.name == "Streamcord"}')
        # figured out which conditions evaulate true, commenting long print statement out
        # but preserving it for reference
        print(msg)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get('https://github.com/superbunytime')

        # dynamically getting the link is the next step. i think i know an easy way to do this
        # i may need to rework this using discordjs in order to put it into an electron app


with open("token", "r+") as keyfile:
    key = keyfile.read()
    client.run(key)