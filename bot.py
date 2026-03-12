import discord
import os
from google import genai

# ===== ENV VARIABLES =====
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ===== AI CLIENT =====
client_ai = genai.Client(api_key=GEMINI_API_KEY)

# ===== DISCORD =====
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

    question = message.content

    try:
        response = client_ai.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        await message.channel.send(response.text)

    except Exception as e:
        print(e)
        await message.channel.send("⚠ AI lỗi")


bot.run(DISCORD_TOKEN)
