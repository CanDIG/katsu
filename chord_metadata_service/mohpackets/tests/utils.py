# List of invalid values that do not match regex ^[A-Za-z0-9\-\._]{1,64}$
INVALID_ID_LIST = [
    "this_is_a_string_that_is_definitely_longer_than_64_characters_123456789",  # More than 64 characters
    None,  # None value
    True,  # Boolean value
    "",  # Empty string
    " ",  # Single space
    "    ",  # Multiple spaces
    "id_with_|*?",  # Special characters
    "id with space",
]