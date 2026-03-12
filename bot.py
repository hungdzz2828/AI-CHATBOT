import discord
import os
from google import genai

TOKEN = os.getenv("TOKEN")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

ai = genai.Client(api_key=GEMINI_KEY)

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

        try:
            response = ai.models.generate_content(
                model="gemini-2.0-flash",
                contents=question
            )

            await message.channel.send(response.text)

        except Exception as e:
            print(e)
            await message.channel.send("AI lỗi.")

bot.run(TOKEN)
