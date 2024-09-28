from typing import Dict, NamedTuple
from urllib.parse import urlencode, urlunparse

domain = "www.remax.com.ar"
netloc = domain  # TODO map to port 80 or 443


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


home = unparse(url="")

login = unparse(url="iniciar-sesion")

signup = unparse(url="/registro")

departments_all = get_department_page(page_index=0)
