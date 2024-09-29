"""
This module provides utility functions for working with web pages in the
SweetHome project.

It includes functions for generating file names based on page URLs, saving HTML
content, and other page-related operations. These utilities are designed to
support web scraping and data extraction tasks within the SweetHome application.
"""

import os
import re

from sweethome.logging import logger
from sweethome.types import Page

from . import copy


def get_file_name(page: Page) -> str:
    """
    Generate a file name based on the last part of the page URL.

    This function takes a Page object, extracts the full path and converts it to
    lowercase, and replaces all non-alphanumeric characters with underscores to
    create a valid file name.

    Args:
        page (Page): The Page object containing the URL to process.

    Returns:
        str: A string representing the generated file name.

    Example:
        If the page URL is "https://example.com/Some-Page/123",
        the function will return "some_page_123".
    """
    full_path = page.url.lower()
    # replace all non-alphanumeric characters with an underscore
    file_name = re.sub(r"\W", "_", full_path)
    return file_name


def save_html(page: Page = None, overwrite: bool = False) -> str:
    """
    Saves the html source code into a .html file.

    Args:
        page (Page, optional): The page object to generate the file name.
        overwrite (bool, optional): If True, the file will be overwritten if it
        exists. Defaults to False.

    Returns:
        str: The path to the saved file.

    Raises:
        FileExistsError: If the file already exists and overwrite is False.
        ValueError: If the page name is not one word.
    """
    # create data folder if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
    file_name = get_file_name(page)
    html = copy.html(page)
    # assert page is one word
    if not len(file_name.split()) == 1:
        raise ValueError("Page name must be one word.")
    # TODO add a random number at the end of the file name
    # check if the file already exists
    file_path = f"data/{file_name}.html"
    if os.path.exists(file_path):
        if not overwrite:
            raise FileExistsError(f"The file {file_path} already exists.")
        else:
            logger.warning(f"The file {file_path} already exists, overwriting...")
    # save the html source code into the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html)
    logger.info(f"Saved {file_path}")
    return file_path
