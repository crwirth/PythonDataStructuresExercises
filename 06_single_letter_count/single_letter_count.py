def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """

    counter = word.lower().count(letter.lower())
    return str(counter)

single_letter_count('Hello World', 'h')
single_letter_count("Hello World", 'l')

