import asyncio
from telethon import TelegramClient
from telethon.errors import FloodWaitError
from openrouter import OpenRouter
from telethon import utils

api_id = 
api_hash = ""

telegram = TelegramClient("telegram", api_id, api_hash)

OPENROUTER_KEY = ""

output = []
lock = asyncio.Lock()

# limit concurrent tasks
semaphore = asyncio.Semaphore(5)

client = OpenRouter(api_key=OPENROUTER_KEY)

mcount = 0
async def process_dialog(dialog):
    global mcount
    async with semaphore:
        try:
            message_zero = await telegram.get_messages(
                dialog,
                min_id = dialog.dialog.read_inbox_max_id,
                reverse=True,
                limit = None,
            )
            for i in message_zero:
                if i.text and len(i.text) >= 30:
                    text = """Ты — фильтр новостей Minecraft Telegram-каналов.

        Твоя задача: определить, является ли сообщение интересной новостью.

        Ответ должен содержать ТОЛЬКО одно слово:
        ДА
        или
        НЕТ

        Любой другой текст запрещён.

        Отвечай НЕТ, если сообщение:
        - является анонсом стрима, видео или трансляции;
        - связано с личной жизнью;
        - поздравляет с днём рождения;
        - является рекламой, оффтопом или обычным общением;
        - не связано напрямую с Minecraft.

        Отвечай ДА, если сообщение:
        - содержит важные события;
        - рассказывает о драмах, конфликтах или расследованиях;
        - сообщает о достижениях игроков;
        - содержит значимые новости сообщества;
        - связано с крупными Minecraft-проектами, серверами, турнирами или игроками.

        Если есть сомнения — отвечай ДА.

        Сообщение: \n""" + i.text

                    # run blocking OpenRouter call in thread
                    response = await asyncio.to_thread(
                        lambda: client.chat.send(
                            model="deepseek/deepseek-v4-flash",
                            messages=[
                                {
                                    "role": "user",
                                    "content": text
                                }
                            ],
                        )
                    )
                   
                    if response.choices[0].message.content.lower() == "да":
                        entity = await telegram.get_entity(dialog)
                        olink = f"https://t.me/{entity.username}/{i.id}"
                        output.append(olink + "\n" + i.text + "\n" + "-------" + "\n")
                    mcount += 1;
                
                    async with lock:
                        entity = await telegram.get_entity(dialog)
                        print(
                            f'Message: https://t.me/{entity.username}/{i.id} \n'
                            f'Output: "{response.choices[0].message.content}"\n'
                        )
                    await telegram.send_read_acknowledge(dialog, max_id=message_zero[-1].id)
                
        except FloodWaitError as e:
            print(f"Flood wait: sleeping {e.seconds}s")
            await asyncio.sleep(e.seconds)

        except Exception as e:
            print(f"Error: {e}")

async def main():
    tasks = []

    async for dialog in telegram.iter_dialogs():
        if (
            dialog.is_channel
            and dialog.archived
            and dialog.unread_count != 0
        ):
            tasks.append(asyncio.create_task(process_dialog(dialog)))

    await asyncio.gather(*tasks)
    
    with open('output.txt', 'w', encoding='utf-8') as file:
                        file.writelines(output)


with telegram:
    telegram.loop.run_until_complete(main())
