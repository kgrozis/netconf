#!/bin/bash
set -e

echo "Starting netconf.py"
exec python "netconf.py" $ENV
