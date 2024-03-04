#!/usr/bin/bash

find . -name '*.pdf' -type f -exec sh -c '
for f; do
    rm $f
done' sh {} +

