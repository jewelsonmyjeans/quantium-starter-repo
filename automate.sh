#!/bin/bash
source venv/bin/activate
pytest testing.py
TEST_EXIT_CODE=$?
deactivate
exit TEST_EXIT_CODE
