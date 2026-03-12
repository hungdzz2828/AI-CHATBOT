import discord
import os
import google.generativeai as genai

TOKEN = os.getenv("TOKEN")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!ai"):

        question = message.content[3:].strip()

        if question == "":
            await message.channel.send("Bạn phải hỏi gì đó sau !ai")
            return

        try:
            response = model.generate_content(question)
            await message.channel.send(response.text)

        except Exception as e:
            await message.channel.send("AI đang lỗi tạm thời.")

bot.run(TOKEN)
