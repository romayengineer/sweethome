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
    """
    departments_list: List[DepartmentItem] = []

    departments_items = page.locator(departments_items_xpath).all()

    for department_index, department in enumerate(departments_items):
        # title = department.locator("css=h2").inner_text()
        # price = department.locator("css=div").inner_text()
        # location = department.locator("css=div").inner_text()
        # url = department.locator("css=a").get_attribute("href")
        # departments_list.append(DepartmentItem(title, price, location, url))
        logger.debug(get_sep_lines(department_index))
        logger.debug(department.inner_text())
        continue

    return departments_list
