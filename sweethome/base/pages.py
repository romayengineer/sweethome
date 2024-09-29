"""
This module stores the pages html source code into .html files,
these files are stored into the data folder on the root directory.
"""

import os


def save_html(html: str, page: str, overwrite: bool = False) -> None:
    """
    Saves the html source code into a .html file.

    Args:
        html (str): The html source code to save.
        page (str): The name of the page.
        overwrite (bool, optional): If True, the file will be overwritten if it
        exists. Defaults to False.

    Raises:
        FileExistsError: If the file already exists and overwrite is False.
        ValueError: If the page name is not one word.
    """
    # create data folder if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
    # assert page is one word
    if not len(page.split()) == 1:
        raise ValueError("Page name must be one word.")
    # check if the file already exists
    file_path = f"data/{page}.html"
    if os.path.exists(file_path) and not overwrite:
        raise FileExistsError(f"The file {file_path} already exists.")
    # save the html source code into the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html)
