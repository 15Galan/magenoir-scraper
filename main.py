from utils import scrapper

# Scrape Mage Noir's public database for all the spells
database = 'https://magenoir.com/collection.html'

spells_urls = scrapper.get_spells_urls(database)

print(f"Found {len(spells_urls)} spells in the database. Downloading...")

spells = scrapper.get_spells_info(spells_urls)

for spell in spells:
    print(spell)

# Save the spells in an Obsidian vault
