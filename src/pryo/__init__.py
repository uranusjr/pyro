"""Project-level Python virtual environment management tool.
"""

__version__ = "0.1.0"


def main():
    from .cmds import dispatch

    return dispatch(None)
