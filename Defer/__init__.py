__all__ = ['Defer']

from contextlib import contextmanager, ExitStack
@contextmanager
def Defer():
    with ExitStack() as stack:
        yield stack.callback
