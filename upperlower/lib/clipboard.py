import pyperclip


def set_text(text: str) -> None:
    pyperclip.copy(text)


def get_text() -> str:
    return pyperclip.paste()


def clear_text() -> None:
    set_text("")
