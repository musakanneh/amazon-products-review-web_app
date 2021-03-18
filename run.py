#!/usr/bin/env python
import logging
from app import app as application

logger = logging.getLogger("app")


def main(port=5000, debug=True):
    """Runs the server in development

    Args:
        port(int): port number to access the app in the browser
        debug(Bool): sets the debug mode to true, for development

    """
    logger.info(
        "Staring App at Port: {} with Debug Option: {}".format(port, debug))
    application.run(port=port, debug=debug)


if __name__ == '__main__':
    main()
