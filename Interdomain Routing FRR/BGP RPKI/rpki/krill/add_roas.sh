#!/bin/bash -e

krillc roas update --ca $1 --add "0.0.0.0/0 => 0" > /dev/null 2>&1
while [ $? -ne 0 ]
do
    sleep 1
    krillc roas update --ca $1 --add "0.0.0.0/0 => 0" > /dev/null 2>&1
done

krillc roas update --ca $1 --remove "0.0.0.0/0 => 0"

krillc roas update --ca $1 --add "193.201.0.0/16 => 1"
krillc roas update --ca $1 --add "193.202.0.0/16 => 2"
krillc roas update --ca $1 --add "193.203.0.0/16 => 3"
krillc roas update --ca $1 --add "193.204.0.0/16 => 4"
krillc roas update --ca $1 --add "193.205.0.0/16 => 5"
krillc roas update --ca $1 --add "193.206.0.0/16 => 6"
krillc roas update --ca $1 --add "193.0.0.0/16 => 3333"