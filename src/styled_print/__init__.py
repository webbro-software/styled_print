from .core import styled_print

__all__ = ['styled_print']

def __call__(*args, **kwargs):
    return styled_print(*args, **kwargs)