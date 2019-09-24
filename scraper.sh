#!/bin/bash
# Use the Python file url_algo.py to create a file called
# data_file_list.txt which will store the URLs of the files
# that contain publicly available MTA turnstile data.  This
# script will then invoke wget to retrieve each MTA file
# that corresponds with the URL in the Python outfile data_file_list.txt

python3 url_algo.py;

FILENAME="data_file_list.txt"

while read line; do
    wget $line
#    n = $((n+1))
done < "$FILENAME"

echo "Process complete!"

exit
