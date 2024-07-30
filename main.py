import os
import logging
from dotenv import load_dotenv
from bot.bot import bot

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        if TOKEN is None:
            logger.error("DISCORD_TOKEN is not set. Please check your .env file.")
        else:
            logger.info(f"DISCORD_TOKEN is set: {TOKEN[:4]}...")  # Print first 4 characters for security
            bot.run(TOKEN)
    except Exception as e:
        logger.error(f"Error starting the bot: {e}")
