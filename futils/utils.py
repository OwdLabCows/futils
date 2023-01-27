import logging
import sys
# typing
from typing import Union


class Utils():

    def __init__(self, logger: Union[logging.Logger, None] = None):
        if logger is None:
            self.logger = logging.getLogger(__name__)
            terminal = logging.StreamHandler(sys.stdout)
            msgfmt = "%(asctime)s in %(funcName)s(%(filename)s)"
            dtfmt = "%Y-%m-%d %I:%M:%S %p"
            fmt = logging.Formatter(msgfmt, dtfmt)
            terminal.setFormatter(fmt)
            self.logger.addHandler(terminal)
        else:
            self.logger = logger
