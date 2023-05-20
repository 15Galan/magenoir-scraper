from utils import scrapper

# Scrape Mage Noir's public database for all the spells
database = 'https://magenoir.com/collection/EN/fire/Flame.html'

print(scrapper.get_data(database))

# Save the spells in an Obsidian vault
