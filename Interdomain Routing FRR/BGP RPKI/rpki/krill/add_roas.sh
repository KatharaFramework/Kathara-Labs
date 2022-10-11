#!/bin/bash -e
krillc roas update --ca $1 --add "193.201.0.0/16 => 1"
krillc roas update --ca $1 --add "193.204.0.0/16 => 4"

