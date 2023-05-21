import os

from utils import scrapper
from utils import obsidian

# Scrape Mage Noir's public database for all the spells
database = 'https://magenoir.com/collection.html'

spells_urls = scrapper.get_spells_urls(database)

print(f"Found {len(spells_urls)} spells in the database. Downloading...")

spells = scrapper.get_spells_info(spells_urls)

for spell in spells:
    print(spell)

# Save the spells in an Obsidian vault
actual_path = os.path.dirname(os.path.abspath(__file__))
vault_name = 'Mage Noir'

vault = obsidian.create_vault(os.path.join(actual_path, vault_name))
print(f"Created a new vault at '{vault_name}/'. Adding spells...")

obsidian.add_spells(spells, vault)
print(f"\tAdded {len(spells)} spells to {vault_name}'s vault.")
