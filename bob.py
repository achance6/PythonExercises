def response(hey_bob: str) -> str:
    """Determines what bob will say in response to a given phrase"""
    hey_bob = hey_bob.rstrip()
    is_shout = hey_bob.isupper()
    is_question = hey_bob.endswith('?')
    is_empty = hey_bob.isspace() or (len(hey_bob) == 0)

    if is_empty:
        return 'Fine. Be that way!'
    if is_shout and is_question:
        return "Calm down, I know what I'm doing!"
    if is_question: 
        return 'Sure.'
    if is_shout:
        return 'Whoa, chill out!'
    return 'Whatever.'
    
print(response("Tom-ay-to, tom-aaaah-to."))