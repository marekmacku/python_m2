def validate_ingredients(ingredients: str) -> str:
    # Lazy (function-local) import breaks the circular dependency:
    # by the time this runs, light_spellbook's module body has finished
    # executing, so the name is safely resolvable from sys.modules.
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    haystack = ingredients.lower()
    keyword = "VALID" if any(a in haystack for a in allowed) else "INVALID"
    return f"{ingredients} - {keyword}"
