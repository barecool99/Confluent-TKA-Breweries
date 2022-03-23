# Confluent-TKA-Breweries

# Set-up

  1. Create a file called 'config.ini' witin repo folder.
  2. Paste the following boilerplate config code

    [default]
    bootstrap.servers=pkc-l6wr6.europe-west2.gcp.confluent.cloud:9092
    security.protocol=SASL_SSL
    sasl.mechanisms=PLAIN
    sasl.username=<API KEY>
    sasl.password=<API SECRET>

    [consumer]
    group.id=grp_PythonBreweries
    session.timeout.ms = 60000
    connections.max.idle.ms = 540000

    [producer]
    batch.size = 25
    linger.ms = 5


    # 'auto.offset.reset=earliest' to start reading from the beginning of
    # the topic if no committed offsets exist.
    auto.offset.reset=earliest
    
  3. Initialise the virtual environment - 
      > python -m venv venv
      > venv/Scripts/activate
      > pip install -r requirements.txt

  4. Run the consumer 'consumer_Breweries.py'
  5. Run the producer 'producer_Breweries.py'
  6. Producer console should now be displaying the producer sending the data to the confluent topic.
  7. Consumer console should now be displaying it receiving the messages from the topic.


# Assignment Questions:

***Experiment with multiple partitions in your topics. How do the number of partitions affect your producer and
consumer applications?***

  Producers allocate messages to partitions in a round robin fashion (each message is sent to the next partition in turn). 
  This will in turn balance out the amount of messages sent to each partition and ensure that no single partition is 
  overloaded.
  
  Consumers only read messages from their assigned partitions. If there were 6 partitions and 2 consumers, the partitions
  would be evenly split between the two consumers to read the messages from as efficiently as possible. However, if there
  was 4 partitions and 5 consumers, there would be 1 consumer that would be idling until one of the already assigned consumers
  stops reading messages due to being stopped.


***Experiment with the Kafka producer config settings, specifically acks, batch.size and linger.ms. How do these affect
throughput, latency and durability?***

  'linger.ms' groups together messages that are being held due to high load. This helps reduce the overall load by as
  messages are being sent grouped together rather than as individual requests. Therefore, this improves the overall
  throughput of the system however, it comes at a cost of adding latency to messages being sent out which can be set
  within the config.

  'acks' is a configuration option to determine when the producer can mark a message being sent as successful. The 
  default option (0) does not require the producer to have an acknowledgement returned to mark a message sent as succesful.
  When 'acks' is set to '1', the producer must await for an acknowledgement to be returned from a topic to mark the 
  message as being succesfully sent. Finally, option 'all' requires the producer to receive an acknowledgement from all
  topics the message has been sent to to return an acknowledgement before marking the message as a success. Using either
  options '1' or 'all' will impact the durability of the system by ensuring that the producer must receive an acknowledgement 
  and therefore cannot mark a message as success before verifying it has been delivered.

  'batch.size' groups together individual messages into grouped messages reducing the number of individual requests being 
  made to the topic/kafka server. This may negatively impact the rate at which messages are sent if the batch size is 
  too small. It may also impact the latency if the batch size is too large as a message may be queued for some time
  until the batch is large enough to be sent off based on the configuration value.


***Experiment with the Kafka consumer config settings, how do multiple consumers work together?***

  Depending on the # of partitions on the given topic, the consumers will automatically split the partitions that they
  will read the messages from between them. ==> 1 topic has 10 partitions, 2 consumers will split the partitions evenly
  reading meassages from 5 partitions respectively. 


***In your consumer application output the message metadata to the console (partition, offset, etc)***

  Example console output:
    Consumed event from topic tpc-race-data | value = {"season": "1958", "round": "7", "Races": 
    [{"season": "1958", "round": "7", "url": "http://en.wikipedia.org/wiki/1958_British_Grand_Prix", "raceName": 
    "British Grand Prix", "Circuit": {"circuitId": "silverstone", "url": "http://en.wikipedia.org/wiki/Silverstone_Circuit", 
    "circuitName": "Silverstone Circuit", "Location": {"lat": "52.0786", "long": "-1.01694", "locality": "Silverstone", 
    "country": "UK"}}, "date": "1958-07-19"}]}zn
    **Message Metadata >> Offset: 2048 | Partition: 0


***Install and connect the Confluent Cloud CLI to your cluster***
 
 Main commands to connect to CC:
 
    > confluent login

    > confluent environment use env-00666

    > confluent kafka cluster use lkc-388g5j


***Create additional ksqlDB streams and tables***
Issues occured when trying to create the ksqlDB streams/tables. No data was being streamed to either process.

***Use a managed Connector to sink your messages to an external system***
Was not implemented this time.
