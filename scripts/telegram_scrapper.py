from telethon import TelegramClient
import csv
import os
import json
import asyncio
import logging
import demoji
from dotenv import load_dotenv
from database import DbConn


log_dir = os.path.join(os.getcwd(), 'logs')

if not os.path.exists(log_dir):
    os.mkdir(log_dir)

log_file_info = os.path.join(log_dir, 'Info.log')
log_file_error = os.path.join(log_dir, 'Error.log')

formatter = logging.Formatter('%(asctime)s - %(levelname)s :: %(message)s',
                              datefmt='%Y-%m-%d %H:%M')

info_handler = logging.FileHandler(log_file_info)
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

error_handler = logging.FileHandler(log_file_error)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(info_handler)
logger.addHandler(error_handler)
logger.addHandler(console_handler)


def remove_emoji(text):
    try:
        no_emoji = demoji.replace(text, repl = "")
    except:
        no_emoji = text

    return no_emoji

# Load environment variables once
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
# phone = os.getenv('phone')

CACHE_FILE = 'data/scraped_message_id.json'

dbConn = DbConn()

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as file:
            return json.load(file)  
    return {}  


def save_cache(data):
    with open(CACHE_FILE, 'w') as file:  
        json.dump(data, file)


# Function to scrape data from a single channel
async def scrape_channel(client, channel_username, writer, media_dir, cache):
    try:
        entity = await client.get_entity(channel_username)
        channel_title = entity.title  # Extract the channel's title

        async for message in client.iter_messages(entity, limit=10000):
            
            try:
                if message.id in cache[channel_username]:
                    continue
            except:
                logger.info(f"Scraping new Channel {channel_username}")
                cache[channel_username] = []

            media_path = None
            if message.media:
                # Create a unique filename for the photo
                filename = f"{channel_username}_{message.id}.{message.media.document.mime_type.split('/')[-1]}" if hasattr(message.media, 'document') else f"{channel_username}_{message.id}.jpg"
                media_path = os.path.join(media_dir, filename)
                # Download the media to the specified directory if it's a photo
                await client.download_media(message.media, media_path)
                logger.info(f"Downloaded media for message ID {message.id}.")
            
            # Write the channel title along with other data
            writer.writerow([channel_title, channel_username, message.id, remove_emoji(message.message), message.date, media_path])
            logger.info(f"saved message ID {message.id} from {channel_username} to csv format.")
            dbConn.insert_data(channel_title, channel_username, message.id, remove_emoji(message.message), message.date, media_path)
            logger.info(f"saved message ID {message.id} from {channel_username} to database.")
            logger.info(f"Processed message ID {message.id} from {channel_username}.")
            
            cache[channel_username].append(message.id)


            save_cache(cache)
    except Exception as e:
        logger.error(f"Error while scraping {channel_username}: {e}")            

# Initialize the client once
client = TelegramClient('scraping_session', api_id, api_hash)

async def main():
    await client.start()
    
    # Create a directory for media files
    media_dir = 'data/photos'
    os.makedirs(media_dir, exist_ok=True)

    # Open the CSV file and prepare the writer
    with open('data/telegram_data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        cache = load_cache()

        if os.stat('data/telegram_data.csv').st_size==0:
            writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])  # Include channel title in the header
        
        # List of channels to scrape
        channels = [
            '@DoctorsET',
            '@CheMed123',
            '@lobelia4cosmetics' ,
            '@yetenaweg',
            '@EAHCI',

        ]

        tasks = [scrape_channel(client, channel, writer, media_dir, cache) for channel in channels]

        await asyncio.gather(*tasks)

        logger.info("Scraping completed.")
        print("Scraping completed.")        
        
        # # Iterate over channels and scrape data into the single CSV file
        # for channel in channels:
        #     await scrape_channel(client, channel, writer, media_dir, cache)
        #     print(f"Scraped data from {channel}")

        

with client:
    client.loop.run_until_complete(main())
