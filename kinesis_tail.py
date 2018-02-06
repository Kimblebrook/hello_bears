import boto3
import time
import snowplow_analytics_sdk.event_transformer
import pprint

my_stream_name = 'lambda-test'

kinesis_client = boto3.client('kinesis', region_name='eu-west-1')

response = kinesis_client.describe_stream(StreamName=my_stream_name)

my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']

shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
                                                   ShardId=my_shard_id,
                                                   ShardIteratorType='LATEST')

my_shard_iterator = shard_iterator['ShardIterator']

record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
                                             Limit=2)

while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(
        ShardIterator=record_response['NextShardIterator'], Limit=2)

    if record_response['Records']:
        # print(record_response['Records'][0]['Data'])
        pprint.pprint(snowplow_analytics_sdk.event_transformer.transform(
            record_response['Records'][0]['Data'].decode()))

    # wait for 5 seconds
    time.sleep(5)
