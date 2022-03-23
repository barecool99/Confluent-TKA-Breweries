import json
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from token import EXACT_TOKEN_TYPES
from confluent_kafka import Producer
from datetime import datetime

from brewery import getAllBreweries


if __name__ == '__main__':
    '''
        Config parser from:
        https://developer.confluent.io/get-started/python/#build-producer
    '''
    # Parse the command line.
    parser = ArgumentParser()
    parser.add_argument('config_file', type=FileType('r'))
    args = parser.parse_args()

    # Parse the configuration.
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    config_parser = ConfigParser()
    config_parser.read_file(args.config_file)
    config = dict(config_parser['default'])

    # Create Producer instance
    producer = Producer(config)
    topic = "tpc_breweries"
    
    while True:
        breweries = getAllBreweries()

        for brewery in breweries:
            brewery = json.dumps(brewery).replace('null', '""')
            json.loads(brewery)

            brewData = brewery
            print (f'\nMessage sent @ {datetime.now()} | Message: \n {str(brewData)}')
            producer.produce(topic, value = brewData)

        producer.poll(10000)
        producer.flush()

        print ('\n\nAll Data Sent From API\n\nEnding Producer...')
        break