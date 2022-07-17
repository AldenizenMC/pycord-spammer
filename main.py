# Libraries
import sys
import discord
from colorama import Fore
from time import sleep
import os

# Constants and Variables
BANNER = Fore.RED + """\n
                ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
                ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
                ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
                ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
                ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
                ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
"""

# Helper commands
def cls():
    os.system("cls")

class Spammer: 
    client = discord.Client()

    channel_id:int = 0
    channel:discord.TextChannel = None
    message_content = "@everyone"
    message_amount = 50
    delay = 100 # in miliseconds

def main():
    print(BANNER)
    token = input("[>] Token: ")
    print("[i] Logging in...")
    try:
        Spammer.client.run(token)
    except discord.errors.LoginFailure:
        print("[!] Invalid token.")
        print("[i] Terminal will now be closed in 3 seconds due to a pycord error that can't be handled.")
        sleep(3)
        sys.exit()
    except RuntimeError:
        pass

async def logged_in_options():
    print(BANNER)
    print(" " * 16 + Fore.RED + f"[i] Logged in as {Spammer.client.user.name}#{Spammer.client.user.discriminator}")
    print("")
    print(" " * 16 + Fore.RED + "1. Channel ID          : " + Fore.YELLOW + str(Spammer.channel_id))
    if not Spammer.channel_id == 000000000000000000 and not Spammer.channel == None:
        print(" " * 19 + Fore.RED + "Channel Name        : " + Fore.YELLOW + "#" + str(Spammer.channel.name))
    print(" " * 16 + Fore.RED + "2. Message Content     : " + Fore.YELLOW + "\"" + str(Spammer.message_content) + "\"")
    if Spammer.message_amount == 0:
        print(" " * 16 + Fore.RED + "3. Message Amount      : " + Fore.YELLOW + "Infinite")
    else:
        print(" " * 16 + Fore.RED + "3. Message Amount      : " + Fore.YELLOW + str(Spammer.message_amount))
    print(" " * 16 + Fore.RED + "4. Delay per Message   : " + Fore.YELLOW + str(Spammer.delay) + "ms")
    print(" " * 16 + Fore.RED + "99. Execute\n")
    option = input("[>] Option: ")

    if option == "":
        cls()
        print("[!] Select an option.")
        await logged_in_options()
    elif option == "1":
        channel_id = input("[>] Channel ID: ")
        if channel_id.isnumeric():
            channel = Spammer.client.get_channel(int(channel_id))
        else:
            cls()
            print("[!] Channel ID is either blank or not a number.")
            await logged_in_options()
        
        if channel == None:
            cls()
            print("[!] Channel not found.")
            await logged_in_options()
        elif not channel.type == discord.ChannelType.text:
            cls()
            print(f"[!] Channel is a \"{channel.type} channel\" and not a text channel.")
            await logged_in_options()
        else:
            Spammer.channel_id = int(channel_id)
            Spammer.channel = channel
            cls()
            await logged_in_options()
    elif option == "2":
        print("[i] Spaces is not supported (yet).")
        content = input("[>] Message Content: ")
        if content == "":
            cls()
            print("[!] Message content cannot be blank.")
            await logged_in_options()
        else:
            Spammer.message_content = content
            cls()
            await logged_in_options()
    elif option == "3":
        print("[i] Type 0 for infinite")
        amount = input("[>] Message amount: ")
        if not amount.isnumeric():
            cls()
            print("[!] Amount is either blank or not a number.")
            await logged_in_options()
        else:
            Spammer.message_amount = int(amount)
            cls()
            await logged_in_options()
    elif option == "4":
        delay = input("[>] Delay (ms): ")
        if not delay.isnumeric():
            cls()
            print("[!] Delay is either blank or not a number.")
            await logged_in_options()
        else:
            Spammer.delay = int(delay)
            cls()
            await logged_in_options()
    elif option == "99":
        confirm = input(f"[>] Are you sure you want to spam #{Spammer.channel.name} (Y/n) ")
        if confirm.lower() == "y" or confirm == "":
            cls()
            await spam()
        else:
            cls()
            await logged_in_options()
    else:
        cls()
        print("[!] Invalid option.")
        await logged_in_options()

async def spam():
    print(BANNER)
    print(" " * 16 + Fore.RED + f"[i] Logged in as {Spammer.client.user.name}#{Spammer.client.user.name}")
    print(" " * 16 + Fore.RED + f"[i] Currently spamming #{Spammer.channel.name}")
    print(" " * 16 + Fore.RED + f"[i] Press CTRL + C to force stop spam.\n\n")
    if Spammer.message_amount == 0:
        i = 0
        try:
            while True:
                i += 1
                print(f"[i] Message sent: {i}", end="\r")
                await Spammer.channel.send(content=Spammer.message_content)
                sleep(Spammer.delay/1000)
        except KeyboardInterrupt:
            cls()
            print(f"[i] Finished with messages sent: {i}")
            await logged_in_options()
    else:
        try:
            i = 1
            for i in range(Spammer.message_amount):
                i += 1
                print(f"[i] Message sent: {i}/{Spammer.message_amount}", end="\r")
                await Spammer.channel.send(content=Spammer.message_content)
                sleep(Spammer.delay/1000)
            cls()
            print(f"[i] Finished with messages sent: {i}/{Spammer.message_amount}")
            await logged_in_options()
        except KeyboardInterrupt:
            cls()
            print(f"[i] Finished with messages sent: {i}/{Spammer.message_amount}")
            await logged_in_options()

@Spammer.client.event
async def on_ready():
    cls()
    await logged_in_options()


if __name__ == '__main__':
    main()