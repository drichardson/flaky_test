#!/usr/bin/env bash

set -euo pipefail

PYTEST_FLAKY="uv run pytest -m flaky"

$PYTEST_FLAKY ||
	$PYTEST_FLAKY --lf ||
	$PYTEST_FLAKY --lf
