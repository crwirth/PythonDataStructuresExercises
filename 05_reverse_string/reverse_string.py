def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    str = ""
    for i in phrase:
        str = i + str
    return str


reverse_string('awesome')
reverse_string('sauce')