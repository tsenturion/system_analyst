def capitalize(text):
    if text == "":
        return ""
    if text is None:
        return None
    first_char = text[0].upper()
    rest_subsring = text[1:]
    return first_char + rest_subsring

"""def capitalize(text: str): str:
    first_char, *rest_chars = text
    rest_subsring = "".join(rest_chars)
    return first_char.upper() + rest_subsring"""