# Written by Livia Salgueiro and Michael Franco
import pandas as pd
import datetime

numdays = 203 # Just setting the number of days we want to take back from
              # today we can increase it later, this is just so we can start
              # with a "small" data set

date_time_str = '2019-06-22 08:15:27.243860' # Penultimate date of the range
                                             # in the MTA website
date_time_obj = datetime.datetime.strptime(
                                           date_time_str,
                                           '%Y-%m-%d %H:%M:%S.%f'
                                          )

# Transforming it to a date_time obj
date_time_obj

# Creating a list of dates that starts on the penultimate date and
# goes back the numdays we've set (jumping 7 days each time)
date_list = [date_time_obj
             - datetime.timedelta(days=x) for x in range(0, numdays, 7)
            ]

date_list

# Transforming the dates into strings and putting in a list:
url_dates = []

for i in date_list:
    year = str(i.year).replace("20", "")
    day = str(i.day)
    if i.day < 10:
        day = "0" + day
    month = str(i.month)
    if i.month < 10:
        month = "0" + month
    date_str = year + month + day
    url_dates.append(date_str)

def complete_url_string(dates):
    '''
    Use loops to append YYMMDD date string to the MTA URL for the
    relevant dates for which we are interested in collecting data,
    and then append .txt onto the end of the strings.
    '''

    i = 0

    url_list = [] # This is the value to be returned,
                  # which can subsequently be output
                  # for use by scraper.sh to invoke
                  # wget in order to download files
                  # from MTA website.
    
    while(i < len(dates)):
        url_list.append('http://web.mta.info/developers/data/nyct/turnstile/turnstile_')
        url_list[i] =  url_list[i] + dates[i]

        i += 1

    i = 0
    while(i < len(dates)):
        url_list[i] = url_list[i] + '.txt \n'

        i = i + 1

    return url_list

file_list = list(complete_url_string(url_dates))

def displayFileList(files):
    '''
    Print the list of URLs in a format readable to shell script
    in standard output.
    '''
    i = 0
    
    while(i < len(files)):
        print(files[i], end = ' ')

        i += 1

def writeFilenamesToList(files):
    '''
    Write the list of URLs to a .txt file, which will then be read
    by the script scraper.sh
    '''
    outfile = open('data_file_list.txt', 'w')

    i = 0
    
    while(i < len(files)):
        outfile.write(files[i])

        i += 1

    outfile.close()

writeFilenamesToList(file_list)
