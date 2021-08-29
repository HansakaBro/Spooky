from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	alpha2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("WhatsApp Group", url="https://chat.whatsapp.com/FOALYW6PMitLo9jntxEGqi")],
                [InlineKeyboardButton("Youtube Channel", url="https://youtube.com/channel/UC6ZgCl_f6YPxAsrzWhApPow")],
		 ])
	help_image = "https://telegra.ph/file/778e59fcf123197692cb0.jpg"
	await message.reply_photo(help_image,  caption="**Spooky Help** \n\n`ENG HELP...`\n**• Just Send your Youtube video url** \n**• And i will give Method list to select your choice**\n\n`SI HELP...`\n**• කොපි කරගත් Youtube ලින්කුව එවන්න.**\n**• එවිට ලැබෙන ලැයිස්තුවෙන් අවශ්‍ය ප්‍රමාණය හා මාදිලිය තෝරාදෙන්න.**\n\n\n**•This bot is fully free.**\n__• Don't pay anyone for Bots like this.__",reply_markup=alpha2)
