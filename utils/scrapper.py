import requests

from bs4 import BeautifulSoup as bs
from requests import RequestException
from termcolor import colored
from urllib.parse import urlparse
from utils.magenoir import Spell


global main_page    # The URL's domain


def get_html(page_url):
    """
    Extracts the HTML code from a URL page, if possible.

    :param page_url:  the page's url.

    :return: the page's html or none if error.
    """
    html = None

    try:
        request = requests.get(page_url, timeout=5)

        if request.status_code == 200:
            html = bs(request.content, "html.parser")

    except RequestException as ex:
        print(colored(f"Request's exception:\n\t{ex}", 'red'))

    return html


def get_spells_urls(database_url):
    """
    Extracts the spells' URLs from the database page.

    :param database_url: the database's page URL.
    :return: a list of spells' URLs.
    """
    # Define the database's URL domain
    main_page = "https://www." + urlparse(database_url).netloc

    # Make a request to the database's URL and get the HTML content
    html = get_html(database_url)

    spells_urls = []

    for element in ['vegetal', 'fire', 'water', 'air', 'mineral', 'arcane']:
        for item in html.find_all('div', class_=f'Portfolio-box card {element}'):
            for i in item.find_all('a'):
                spells_urls.append(main_page + "/" + i['href'])

    return spells_urls


def get_spells_info(spells_urls):
    """
    Extracts the spells' data from the spells' URLs.

    :param spells_urls: a list of spells' URLs.
    :return: a list of spells' data.
    """
    spells_info = []

    for spell_url in spells_urls:
        spells_info.append(get_data(spell_url))

    return spells_info


def get_data(spell_url):
    """
    Extracts the data from a spell's page.

    :param spell_url: the spell's URL.
    :return: an instance of the class SPELL.
    """
    # Create an instance of the class SPELL
    spell = Spell()

    # Make a request to the spell's URL and get the HTML content
    html = get_html(spell_url)

    # Extract the spell's name
    name = html.find('td', class_='row-title', text='Name : ')
    if name:
        spell.name = name.find_next_sibling('td').text.strip()

    # Extract the spell's element
    element = html.find('td', class_='row-title', text='Element : ')
    if element:
        spell.element = element.find_next_sibling('td').text.strip()

    # Extract the spell's type
    stype = html.find('td', class_='row-title', text='Type : ')
    if stype:
        spell.type = stype.find_next_sibling('td').text.strip()

    # Extract the spell's mana cost
    manas = html.find('td', class_='row-title', text='Mana cost : ')
    if manas:
        manas_count = manas.find_next_sibling('td').find_all('li')

        # Extract each mana type and its quantity
        for item in manas_count:
            m_quantity = item.find('span').text.strip()
            element = item.find('img', class_='font-pictogram')
            m_type = element['alt'].replace('-icon', '').capitalize()

            spell.manas[m_type] = int(m_quantity)

    # Extract the spell's components
    components = html.find('td', class_='row-title', text='Components needed : ')
    if components:
        components_counts = components.find_next_sibling('td').text.strip()

        # This page has the string 'None' if the spell has no components
        if components_counts != 'None':
            # Extract each component type and its quantity
            for item in components_counts.split('\n'):
                c_quantity = item.split(' ')[0].strip()
                c_type = item.split(' ')[1].strip().capitalize()

                spell.components[c_type] = int(c_quantity)

    # Extract the spell's effect (card description)
    effect = html.find('td', class_='row-title', text='Effect : ')
    if effect:
        text = effect.find_next_sibling('td').text.strip()
        text = text.replace('\t', '').replace('\n\n', '\n')
        spell.effect = "\"" + text + "\""

    return spell
