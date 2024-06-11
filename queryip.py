#!/usr/bin/python3

import argparse
import os
import sys
import requests

# Parse command line arguments
parser = argparse.ArgumentParser(description='Query IPStack for an IP address')
parser.add_argument('ip', help='IP address to query')
parser.add_argument('-k', '--key', help='API key for IPStack or use IPSTACK_KEY environment variable')
parser.add_argument('-o', '--output', help='Output filename')
parser.add_argument('-c', '--csv', action='store_true', help='Output in CSV format')
parser.add_argument('-j', '--json', action='store_true', help='Output in JSON format')
parser.add_argument('-q', '--quiet', action='store_true', help='Suppress output')

args = parser.parse_args()

# Check for API key from args or environment variable
if args.key:
    key = args.key
else:
    key = os.environ.get('IPSTACK_KEY')

if not key:
    print('Error: No API key specified')
    sys.exit(1)

url = 'http://api.ipstack.com/' + args.ip + '?access_key=' + key

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if 'error'  in data:
        print('Error:', data['error']['info'])
        sys.exit(1)

    # set default output to latitude and longitude
    output = str(data['latitude']) + "," + str(data['longitude'])
    ext = 'txt'
    if(args.json):
        output = str(data)
        ext = 'json'
    elif(args.csv):
        output = 'IP,Country,Region,City,Latitude,Longitude\n' + data['ip'] + "," + data['country_name'] + "," + data['region_name'] + "," + data['city'] + "," + str(data['latitude']) + "," + str(data['longitude'])
        ext = 'csv'

    # write output to file if specified
    if(args.output):
        with open(args.output + '.' + ext, 'w') as f:
            f.write(output)
    if not args.quiet:
        print(output)
else:
    print('Error:', response.status_code)

