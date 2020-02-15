import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


# Banking System
# Purpose: Allow players to track, buy and sell loot.
# 1. Accounts
#   a. Total assets
#       - Wealth in coin
#       - Items possessed
#   b. Deposit
#   c. Withdraw
#   d. See personal assets
#       - List of deposits
#       - List of withdraws
#       - List of purchases
#   e. Audit other player's assets
#       - Obscure item names
#       - Obscure player names
# 2. Buying and Selling
#   a. Cost
#   b. Subject of purchase
#   c. Availability
#       - Purchaser
#       - Purchasee

@bot.command()
async def deposit(ctx, amount):
    await ctx.channel.send("You deposited " + str(amount))
    if os.path.exists("./deposit-log.txt"):
        with open("./deposit-log.txt", 'a') as fob:
            fob.writelines("\n\"" + str(ctx.author) + "\" deposited " + str(amount))
    else:
        with open("./deposit-log.txt", 'w') as fob:
            fob.writelines(str(ctx.author) + " deposited " + str(amount))

@bot.command()
async def withdraw(ctx, amount):
    return

bot.run('[YOUR TOKEN HERE]')