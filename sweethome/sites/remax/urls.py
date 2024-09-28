from collections import namedtuple
from typing import Dict
from urllib.parse import urlencode, urlunparse

domain = "www.remax.com.ar"

Components = namedtuple(
    typename="Components",
    field_names=["scheme", "netloc", "url", "path", "query", "fragment"],
)


def unparse(path: str, query: Dict[str, str] = None) -> str:
    return urlunparse(
        Components(
            scheme="https",
            netloc=domain,
            query=urlencode(query) if query else "",
            path=path,
            url="",
            fragment="",
        )
    )


home = unparse(path="")

login = unparse(path="/iniciar-sesion")

signup = unparse(path="/registro")

departments_all = unparse(
    path="/listings/rent",
    query={
        "page": "0",
        "pageSize": "24",
        "sort": "-createdAt",
        "in:operationId": "2",
        "in:eStageId": "0,1,2,3,4",
        "in:typeId": "1,2,3,4,5,6,7,8",
        "filterCount": "1",
        "viewMode": "listViewMode",
    },
)
