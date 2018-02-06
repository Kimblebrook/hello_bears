## Setting up the Snowplow applications

Snowplow configuration files are stored in `snowplow_config`.

Stream collector:

`java -jar snowplow-stream-collector-0.12.0.jar --config application.conf`

Stream enrich:

`java -jar snowplow-stream-enrich-0.13.0.jar --config enrich.conf --resolver file:iglu_resolver.json`

S3 loader:

`java -jar snowplow-s3-loader-0.6.0.jar --config s3_loader.conf`

Upload schemas to S3:

`./igluctl static s3cp schema_repository sb-user-bucket --region eu-west-1`

## Overall architecture

Taking input from [here](https://discourse.snowplowanalytics.com/t/how-to-setup-a-lambda-architecture-for-snowplow).

`stream collector` -> `kinesis raw stream` -> `kinesis enrich` -> `kinesis good stream`   -> `s3 enriched`
                                                               -> `kinesis bad stream`    -> `s3 bad`
                                           -> `s3 raw`

## Ideas for what to do next

~- Get self-describing events working~
- Write data to S3
- Try out Athena
- Replace Kinesis with Kafka so that we can try out KSQL
- Implement an iOS app for testing purposes


## Iglu Repository

http://sb-user-bucket.s3-website-eu-west-1.amazonaws.com
