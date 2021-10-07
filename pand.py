from json import loads
from json import dump

from jsonmerge import merge

# Store your json files here
# If all of them exist in directory, you can use os.listdir() instead
json_files = ['historical2000.json', 'historical2001.json', 'historical2002.json', 'historical2003.json', 'historical2004.json', 'historical2005.json', 'historical2006.json', 'historical2007.json', 'historical2008.json', 'historical2009.json', ]

with open('merged.json', 'w') as json_out:

    # Store updated results in this dict
    data = {}

    for file in json_files:
        with open(file, 'rb') as json_file:
            json_data = loads(json_file.read())

            # Update result dict with merged data
            data.update(merge(data, json_data))

    dump(data, json_out, indent=4)