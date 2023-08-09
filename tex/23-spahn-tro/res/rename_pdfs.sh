#!/usr/bin/bash

find . -name '*.pdf' -type f -exec sh -c '
for f; do
    file_name=${f%-eps-converted-to.pdf}
    new_file_name=${file_name}.pdf
    echo $new_file_name
    mv $f $new_file_name
done' sh {} +

