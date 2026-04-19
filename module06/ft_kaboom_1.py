print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

from alchemy.grimoire.dark_spellbook import dark_spell_record  # noqa: E402

# Never reached: the import above raises ImportError (circular) first.
result = dark_spell_record("Necromancy", "bats and frogs")
print(f"Testing record dark spell: {result}")
