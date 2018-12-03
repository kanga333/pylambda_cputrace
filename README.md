# pylambda_cputrace

Lambda Layers to measure cpu in Python3 applications.


## How to use

### Create Lambda layers

```
make package S3_BACKET='backet_name' S3_PREFIX='prefix_name'
make deploy STACK_NAME='stack_name'
```

Note: `make package` uses the dokcer image of [pylambda-packer](https://hub.docker.com/r/kanga333/pylambda-packer/) for build. 
It is because some Python module requires build on AmazonLinux.

### Use with the Lambda function

Add `AWSLambda-Pyhon3-TraceUtil` to Layers of your Lambda function.
Import the package and add the decorator in the lambda function.

```python3
import json
from traceutil import cpu_trace
import time 

@cpu_trace
def lambda_handler(event, context):
    time.sleep(1)

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

```
