from os import getenv
from dotenv import load_dotenv

#Remove ADD_HERE and add your variable there

#Dont edit anything if you dont know

#Necessary Variables 
API_ID = int(getenv("API_ID", ADD_HERE)) #In Integer dont add quotes
API_HASH = getenv("API_HASH", "ADD_HERE")
BOT_TOKEN = getenv("BOT_TOKEN", "ADD_HERE") #Put your bot token here
CHANNEL = getenv("CHANNEL", "ADD_HERE") #Your public channel username without @ for force subscription.
MONGO = getenv("MONGO", "ADD_HERE") #Put mongo db url here
#Optional Variables
OWNER_ID = int(getenv("OWNER_ID", "ADD_HERE")) #Put Owner Id
FSUB = bool(getenv("FSUB", False)) #Set this True if you want to enable force subscription from users else set to False.
