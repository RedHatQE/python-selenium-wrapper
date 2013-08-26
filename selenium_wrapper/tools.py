from . import SE
from contextlib import contextmanager

@contextmanager
def restore_url(url=None):
    '''restore SE.current_url or given url'''
    if url is None:
        url = SE.current_url
    try:
        yield
    finally:
        if SE.current_url != url:
            SE.get(url)

@contextmanager
def current_url(url):
    '''navigate given url and restore original url upon return'''
    with restore_url():
        SE.get(url)
        yield
