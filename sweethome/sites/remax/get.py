"""
This module contains functions to get data from the REMAX website.
"""

from typing import List, NamedTuple

from sweethome.logging import Logger
from sweethome.types import Page

logger = Logger(__name__)

departments_items_xpath = "xpath=/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content/div/div/app-list/div[2]/div[1]/qr-card-property"


class DepartmentItem(NamedTuple):
    title: str
    price: str
    location: str
    url: str


def get_sep_lines(department_index: int) -> str:
    return (
        f"----------------------------------------\n"
        f"----------------------------------------\n"
        f"   Department: {department_index}\n"
        f"----------------------------------------\n"
    )


def get_departments_all(page: Page = None) -> List[DepartmentItem]:
    """
    Get the departments from the departments all page.

    This function scrapes department information from the REMAX website.
    It extracts text content for each department listing, processes it,
    and logs debug information about the structure of the listings.

    Args:
        page (Page, optional): The Page object representing the web page to
        scrape.

    Returns:
        List[DepartmentItem]: A list of DepartmentItem objects containing
        the scraped department information. Currently returns an empty list.

    Note:
        TODO populate the departments_list.
        This function currently only logs debug information and does not
        populate the departments_list. Further implementation is needed
        to extract and return actual department data.
    """
    departments_list: List[DepartmentItem] = []

    departments_items = page.locator(departments_items_xpath).all()

    line_counts = {}

    for department_index, department in enumerate(departments_items):
        # TODO populate the departments_list here
        #
        # title = department.locator("css=h2").inner_text()
        # price = department.locator("css=div").inner_text()
        # location = department.locator("css=div").inner_text()
        # url = department.locator("css=a").get_attribute("href")
        # departments_list.append(DepartmentItem(title, price, location, url))
        logger.debug(get_sep_lines(department_index))
        publication_text = department.inner_text()
        # split the text into lines
        publication_lines = publication_text.splitlines()
        # remove trailing whitespace
        publication_lines = [line.strip() for line in publication_lines]
        # filter out empty lines
        publication_lines = [line for line in publication_lines if line]
        pulbication_lines_count = len(publication_lines)
        # join the lines into a single string
        # debug will split the lines into multiple lines and print each line
        # because there is a wrapper in sweethome.logging.Logger
        logger.debug("\n".join(publication_lines))
        logger.debug(f"---- publication_lines_count: {pulbication_lines_count}")
        logger.debug(f"---- ")
        line_counts[pulbication_lines_count] = (
            line_counts.get(pulbication_lines_count, 0) + 1
        )

    for count, times in line_counts.items():
        logger.debug(f"---- line_counts count {count} times: {times}")

    return departments_list
