"""Small utility functions used by fmuobs, parsers and/or writers"""

# Used in yaml file
CLASS_SHORTNAME = {
    "SUMMARY_OBSERVATION": "smry",
    "GENERAL_OBSERVATION": "general",
    "BLOCK_OBSERVATION": "rft",
    "HISTORY_OBSERVATION": "hist",
}


ERT_DATE_FORMAT = "%d/%m/%Y"


def lowercase_dictkeys(some_dict):
    """Convert all keys in a dictionary to lower-case"""
    return {key.lower(): value for key, value in some_dict.items()}


def uppercase_dictkeys(some_dict):
    """Convert all keys in a dictionary to upper-case"""
    return {key.upper(): value for key, value in some_dict.items()}
