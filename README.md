## Readme

### Purpose

This is an example application (using Flask and Bootstrap) for learning how to implement [Snowplow](https://github.com/snowplow/snowplow).

Here's current tracking thinking:

- Snowplow tracker
- Scala stream collector
- Stream Enrich -> writes to Kinesis in TV format
- AWS Lambda to translate TSV format to JSON using Python event transformer library
- Store to S3 in Parquet format (how?)
- Analyse using Amazon Athena

### Things I've learnt

`gevent` in the Python tracker is not compatible with Python 3. Use the code below to install a branch that has this updated.

> pip install git+git://github.com/generalassembly/snowplow-python-tracker.git@bugfix/python3-compatibility



