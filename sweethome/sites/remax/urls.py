import urllib.parse
from typing import Dict, NamedTuple
from urllib.parse import urlencode, urlunparse

domain = "www.remax.com.ar"
netloc = domain  # TODO map to port 80 or 443

last_page_index = 0


class UrlComponents(NamedTuple):
    scheme: str
    netloc: str
    url: str
    params: str
    query: str
    fragment: str


def unparse(url: str = None, query: Dict[str, str] = None) -> str:
    return urlunparse(
        UrlComponents(
            scheme="https",
            netloc=netloc,
            url=url,
            params="",
            query=urlencode(query) if query else "",
            fragment="",
        )
    )


def get_department_page(page_index: int) -> str:
    assert page_index >= 0
    return unparse(
        url="/listings/rent",
        query={
            "page": str(page_index),
            "pageSize": "24",
            "sort": "-createdAt",
            "in:operationId": "2",
            "in:eStageId": "0,1,2,3,4",
            "in:typeId": "1,2,3,4,5,6,7,8",
            "filterCount": "1",
            "viewMode": "listViewMode",
        },
    )


def next_page_url(url: str) -> str:
    """
    Returns url string with page argument increased by 1

    Args:
        url (str): the url string

    Returns:
        str: url string with page argument increased by 1
    """
    parsed_url = urllib.parse.urlparse(url)
    query_dict = urllib.parse.parse_qs(parsed_url.query)
    current_page = int(query_dict["page"][0])
    query_dict["page"] = [str(current_page + 1)]
    new_query_string = urllib.parse.urlencode(query_dict, doseq=True)
    new_url = urllib.parse.urlunparse(
        components=UrlComponents(
            scheme=parsed_url.scheme,
            netloc=parsed_url.netloc,
            url=parsed_url.path,
            params=parsed_url.params,
            query=new_query_string,
            fragment=parsed_url.fragment,
        )
    )
    return new_url


def next_department() -> str:
    global last_page_index
    url = get_department_page(page_index=last_page_index + 1)
    last_page_index += 1
    return url


home = unparse(url="")

login = unparse(url="iniciar-sesion")

signup = unparse(url="/registro")

departments_all = get_department_page(page_index=0)
