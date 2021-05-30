import traceback
from functools import wraps
from typing import Union

import requests

from lib.logging import logger
from lib.util import jsondumps, jsonloads


class HttpResult:
    '''Http Result'''

    def __init__(self, *args, **kwargs):
        # 'if response := ~' is not working
        if (response := kwargs.get('response')) is not None:
            self.status_code = response.status_code
            self.body = jsonloads(response.text)
            self.headers = response.headers
            self.cookies = response.cookies
            self.reason = response.reason
        else:
            self.status_code = int(kwargs.get('status_code', 0))
            self.body = kwargs.get('body', {})
            self.reason = kwargs.get('reason')
            self.headers = {}
            self.cookies = {}

    def json(self, shrink_body=False):
        return {
            'statusCode': self.status_code,
            'body': self.body if not shrink_body else _shrink(self.body),
            'headers': dict(self.headers),
            'cookies': dict(self.cookies),
            'reason': self.reason,
        }


def log_and_catch(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        (url, headers, method, queries, body, params, shrink_logging_body,) = map(
            kwargs.get,
            [
                'url',
                'headers',
                'method',
                'queries',
                'body',
                'params',
                'shrink_logging_body',
            ],
            [None, None, {}, None, {}, None, {}, True, False],
        )

        logger.info(
            {
                'headers': headers,
                'method': method,
                'queries': queries,
                'params': params,
                'body': _shrink(body) if shrink_logging_body else body,
            }
        )
        try:
            response = func(*args, **kwargs)
        except Exception as e:
            logger.error(
                {
                    'headers': headers,
                    'method': method,
                    'queries': queries,
                    'body': body,
                    'errorMessage': str(e),
                    'trackback': traceback.format_exc(),
                }
            )
            raise e

        logger.info(response.json(shrink_logging_body))

        return response

    return wrapper


@log_and_catch
def request(
    url: str,
    headers: dict,
    method: str,
    queries: dict = None,
    body: Union[list, dict, str] = None,
    timeout_in_second: int = 60,
    encoding: str = 'utf-8',
    shrink_logging_body: bool = False,
) -> HttpResult:
    response = getattr(requests, method.lower())(
        url,
        headers=headers,
        params=queries,
        timeout=timeout_in_second,
        data=body if isinstance(body, str) else jsondumps(body),
    )
    response.encoding = encoding

    return HttpResult(response=response)


def _shrink(target: Union[list, dict], max_size=200):
    ret = jsondumps(target)

    return ret[:max_size] if ret and len(ret) > max_size else target
