from string import ascii_lowercase


def encripta(frase, rot=13):
    """Encripta o texto."""
    encriptado = ''
    for char in frase:
        char = char.lower()
        if char == ' ':
            encriptado += char
        elif char not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(char) + rot
            char = ascii_lowercase[pos % 26]
            encriptado += char
    return encriptado


def decripta(frase, rot=13):
    """Decripta o texto."""
    decriptado = ''
    for char in frase:
        char = char.lower()
        if char == ' ':
            decriptado += char
        elif char not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(char) - rot
            char = ascii_lowercase[pos % 26]
            decriptado += char
    return decriptado
