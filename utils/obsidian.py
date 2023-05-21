import os

from utils.progressbar import ProgressBar


def create_vault(path):
    """
    Create a new Obsidian vault at the given path.

    :param path: the path to the new vault.
    """
    if not os.path.exists(path):
        os.makedirs(path)

    return path


def add_spells(spells, path):
    """
    Add a set of spells to the vault.

    :param spells: the list of spells to add.
    :param path: the path to the vault.
    """
    progress = ProgressBar(len(spells))

    for spell in spells:
        add_spell(spell, path)
        progress.update(1, spell.name)


def add_spell(spell, vault_path):
    """
    Add a spell to the vault.

    :param spell: the spell to add.
    :param vault_path: the path to the vault.
    """
    note_name = spell.name + '.md'
    note_path = os.path.join(vault_path, note_name)

    with open(note_path, 'w') as f:
        # Obsidian note metadata
        f.write('---\n')
        f.write('element:\t' + spell.element + '\n')
        f.write('type:\t\t' + spell.type + '\n')
        f.write("manas:\t\t" + str(spell.manas) + '\n')
        f.write('components:\t' + str(spell.components) + '\n')
        f.write('---\n')

        # Obsidian note content
        f.write('\n' + spell.effect.strip('\"') + '\n\n')

        f.close()
