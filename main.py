from multiprocessing import context
from sqlite3 import Timestamp
from time import sleep
from turtle import st
from unittest import skip
import discord
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import pytz
import time



discordClient = discord.Client()

@discordClient.event
async def on_ready():
    print('selam baba {0.user}'.format(discordClient))



def get_img(URL):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')

    images = soup.findAll('img')
    a = []
    for image in images:
        a.append(image['src'])
    for mig in a:
        if "cache" in mig:
            return mig





@discordClient.event
async def on_message(message):
    if message.author == discordClient.user:
        return


    # if message.content.startswith('!week'):
    #     strings = datetime.now().timestamp()
    #     strings = str(strings)
    #     strings = strings.split('.')[0]

    #     await message.channel.send(strings)
    #     await message.channel.send(int(strings)+604800)

    if message.content.startswith('!help'):
        embed=discord.Embed(title=f"HELP", color=0x36f410)
        embed.add_field(name="KEYWORD", value="!ctf - get all ctftime ctf event", inline=True)
        embed.set_footer(text="auther: fatkz & query")
        await message.channel.send(embed=embed)


    if message.content.startswith('!auther'):
        embed=discord.Embed(title=f"AUTHER", color=0x36f410)
        embed.add_field(name="NAME", value="FATKZ", inline=True)
        embed.add_field(name="NAME", value="QUERY", inline=True)
        embed.set_footer(text="auther: fatkz & query")
        await message.channel.send(embed=embed)


    if message.content.startswith('!ctf'):
        headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
                }
        response = requests.get("https://ctftime.org/api/v1/events/", headers=headers)
        jdata = response.json()




        number = 0
        try:
            for i in range(len(jdata)):
                ctf_name = jdata[i]['title']
                ctf_date = jdata[i]['format']
                ctf_link = jdata[i]['url']
                ctf_url = jdata[i]['ctftime_url']
                ctf_time = str(jdata[i]['start'])
                ctf_link = str(ctf_link)+"favicon.ico"
                ctf_users = jdata[i]['participants']
                ctf_time = ctf_time[0:10]

                a = get_img(ctf_url)
                print(a)
                embed=discord.Embed(title=f"{ctf_name}", url=f"{ctf_url}", color=0x36f410)
                embed.set_thumbnail(url=f"{a}")
                embed.add_field(name="TIME", value=f"{ctf_time}", inline=True)
                embed.add_field(name="TYPE", value=f"{ctf_date}", inline=True)
                embed.add_field(name="PARTICIPANTS", value=f"{ctf_users}", inline=True)
                embed.set_footer(text="auther: fatkz & query")
                await message.channel.send(embed=embed)
                i += 1
        except:
            await message.channel.send('Error')





discordClient.run('')


