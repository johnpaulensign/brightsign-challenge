# Usage
```bash
usage: queryip.py [-h] [-k KEY] [-o OUTPUT] [-c] [-j] [-q] ip

Query IPStack for an IP address

positional arguments:
  ip                    IP address to query

options:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     API key for IPStack or use IPSTACK_KEY environment variable
  -o OUTPUT, --output OUTPUT
                        Output filename
  -c, --csv             Output in CSV format
  -j, --json            Output in JSON format
  -q, --quiet           Suppress output
```

# Docker
## Build
`docker build --build-arg IPSTACK_KEY=<API_KEY> --build-arg IP=<IP> Dockerfile`

## Run
`docker run <image>`

### Output
```bash
$ docker run 823f
37.75394058227539,-122.39080047607422
```