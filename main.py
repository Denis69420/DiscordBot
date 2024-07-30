import os
import logging
from dotenv import load_dotenv
from bot.bot import bot

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except Exception as e:
        logging.error(f"Error starting the bot: {e}")
