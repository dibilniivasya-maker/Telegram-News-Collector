To actually run this thing you need three things:
1. A telegram api and hash. Those you can get under "Api Development Tools" on https://my.telegram.org
2. An OpenRouter account. Those are actually free over at https://openrouter.ai
If you want to use a free LLM (such as deepseek V4 flash (free) you will need to manualy change the "model" value to your preferred model (a good one is "deepseek/deepseek-v4-flash:free")

Once you have those, you will need to paste your telegram api, telegram hash and OpenRouter key into their respective values
The program runs in cmd 'cause I can't be FUCKED making an interface for that shit. Fuck you.


The way it works is rather simple:
1. Takes all of your archived channels
2. Pulls out all unread messages from those
3. Runs them through LLMs that determines if they're news worthy or not (each message is its own request)
4. If they are, it logs them in a text file "output.txt" alongside a link to them
5. At the end it reports how much money you spent and how many messages it went through
(The money counting IS a little bad at the moment, I may fix it in the future)
Any info about you specifically does not go to the LLM, if you're concerned about it

Right now the prompt is calibrated to my special needs. But the prompt is literally just letters so it's easy to replace it. Giant block of text. Won't miss ites

If you have any further questions text me over at @ElPhrog on telegram or laphroq on discord
