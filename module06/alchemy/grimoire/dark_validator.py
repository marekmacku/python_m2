from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    haystack = ingredients.lower()
    keyword = "VALID" if any(a in haystack for a in allowed) else "INVALID"
    return f"{ingredients} - {keyword}"
