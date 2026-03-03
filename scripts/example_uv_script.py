#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(level="INFO", format="%(levelname)s %(message)s")
    logger.info("Example script executed via uv.")


if __name__ == "__main__":
    main()
