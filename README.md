# How does this work?
The way it works is rather simple:
1. Takes all of your archived channels
2. Pulls out all unread messages from those
3. Runs them through LLMs that determines if they're news worthy or not (each message is its own request)
4. If they are, it logs them in a text file "output.txt" alongside a link to them
5. At the end should log how many messages it read, but I didn't test the accuracy. It's prolly wrong
### YES, it uses generative AI, but only as a filter

# How to run for the first time
## Firstly, you need to get some values
1. A telegram api and hash. Those you can get under "Api Development Tools" on https://my.telegram.org
2. Openrouter api key. To get one, you go to https://openrouter.ai and click on "Get API key"
### Once you have all these
You will need to open the code (I reccomend via Notepad++), and paste your api_id, api_hash and openrouter key into their respective values. All located in the very beginning of the file
## And then you need to install three things
1. Install python, if you didn't do that yet, from https://www.python.org/downloads/
2. Install Telethon. Instructions on how to do that on https://docs.telethon.dev/en/stable/basic/installation.html
3. Install Openrouter. Instructions on how to do that on https://openrouter.ai/docs/quickstart#using-the-client-sdks

# How to run in general
1. Download the .py file
2. Open CMD
3. Run `cd "route to the .py"`, for example `cd "C:\Users\user\Desktop"`, if you store it on your desktop
4. Run `py "Telegram News Collector.py"`
And it will begin immediately
## One detail
When you run it for the first time, it will prompt you to input your phone number and then input a code you got. That is so that Telethon can use your telegram account and see the channels you're subscribed to
It works on my pc, but lowk broke down on my laptop. Idk why. I may investigate in the future

# Customization and some details
Right now the prompt is calibrated to my special needs - that being russian minecraft content. In order to change it, you need to open the code and locate the big wall of text. That's the prompt, change it however you want

The default AI is deepseek v4 flash. To change it, you need to locate the `model=""` value. It is located in the block directly under the prompt. You will figure it out from there

The code may look videcoded, but that is because I couldn't figure out asycio, and as such had to use AI to add Asycio. Every other line (except comments) was written by my own two hands


### If you have any further questions text me over at @ElPhrog on telegram or laphroq on discord
