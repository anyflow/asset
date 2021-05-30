import json
from datetime import datetime
from decimal import Decimal
from typing import Union

import dateutil.parser
from inflection import camelize, underscore


class DecimalEncoder(json.JSONEncoder):
    """Class for jsondumps"""

    def default(self, o):
        if isinstance(o, Decimal):
            return float(o) if o % 1 > 0 else int(o)
        else:
            return super(DecimalEncoder, self).default(o)


def jsondumps(jsonable: Union[list, dict], indent=2, minimize=True):
    if not jsonable:
        return jsonable

    separators = (',', ':') if minimize else None

    try:
        return json.dumps(
            jsonable, separators=separators, indent=indent, cls=DecimalEncoder
        )
    except json.JSONDecodeError:
        return str(jsonable)


def jsonloads(jsonstr: str):
    try:
        return json.loads(jsonstr)
    except ValueError:
        return jsonstr


def timestamp() -> str:
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')


def utcstr(param) -> str:
    return param.strftime('%Y-%m-%dT%H:%M:%SZ')


def to_datetime(param) -> datetime:
    return dateutil.parser.parse(param)


def normalize_utcstr(param) -> str:
    return utcstr(to_datetime(param))


def snake_to_camel(input_str):
    return camelize(input_str, False)


def camel_to_snake(input_str):
    return underscore(input_str)
