#!/usr/bin/bash

find . -name '*.eps' -type f -exec sh -c '
for f; do
    file_name=${f%.eps}
    new_file_name=${file_name}.pdf
    ps2pdf -DEPSCrop $f $new_file_name
done' sh {} +

