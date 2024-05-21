from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GBGB
	Price 0
	
	**🪙 Basic** 
	Daily  Upload  limit 20GB
	Price $1 per Month
	
	**⚡ Standard**
	Daily Upload limit 50GB
	Price $2 per Month
	
	**💎 Pro**
	Daily Upload limit 100GB
	Price $3 per Month
	
	
	Message @Maltexade to make payment"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Admin",url = "https://t.me/maltexade")], 
        			[InlineKeyboardButton("Pay In Naira",url = "https://t.me/maltexade"),
        			InlineKeyboardButton("Pay In Dollar",url = "https://t.me/maltexade")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**🪙 Basic** 
	Daily  Upload  limit 20GB
	Price $1 per Month
	
	**⚡ Standard**
	Daily Upload limit 50GB
	Price $2 per Month
	
	**💎 Pro**
	Daily Upload limit 100GB
	Price $3 per Month
	
	
	Message @Maltexade to make payment"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Admin",url = "https://t.me/maltexade")], 
        			[InlineKeyboardButton("Pay In Naira",url = "https://t.me/maltexade"),
        			InlineKeyboardButton("Pay In Dollar",url = "https://t.me/maltexade")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
