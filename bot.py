import discord
from google import genai

DISCORD_TOKEN = "DISCORD_TOKEN"
GEMINI_API_KEY = "API_KEY"

ai = genai.Client(api_key=GEMINI_API_KEY)

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

    try:
        response = ai.models.generate_content(
            model="gemini-2.5-flash",
            contents=message.content
        )

        await message.channel.send(response.text)

    except Exception as e:
        print(e)
        await message.channel.send("AI lỗi")

bot.run(DISCORD_TOKEN)
