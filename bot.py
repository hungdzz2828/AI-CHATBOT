import discord
from google import genai

# ===== TOKEN =====
DISCORD_TOKEN = "MTQ4MTUzNDI2Mzg3NzY5NzU2Ng.GdyqkT.7QVXEXOKXEK7vfxSGn2nyzIXWcmmjcCMGri_pM"
GEMINI_API_KEY = "AIzaSyDLqVnTQskYV-tsC07CMuVWPgfqYh6IT0E"

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

    # bỏ qua tin nhắn của bot
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
        await message.channel.send("⚠ Lỗi AI")
        print(e)


bot.run(DISCORD_TOKEN)
