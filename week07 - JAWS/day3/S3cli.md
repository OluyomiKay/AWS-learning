## Using AWS S3 from CLI

* https://docs.aws.amazon.com/cli/latest/reference/s3
* https://docs.aws.amazon.com/cli/latest/reference/s3api/

### Create S3 bucket:
```
aws s3 mb <target> [--options]

Example: create a simple bucket
aws s3 mb s3://bucket-name

Example: create a bucket name, using the current date timestamp
bucket_name=test_$(date "+%Y-%m-%d_%H-%M-%S")
aws s3 mb s3://$bucket_name
```

### Create a public facing S3 bucket:
```
aws s3api create-bucket --acl "public-read-write" --bucket $bucket_name

```

### List a bucket information:
```
aws s3 ls <bucket name>

```

### List Existing S3 Buckets:
```
aws s3 ls

```

### Synchronize Objects with S3 Bucket:
```
aws s3 sync <source> <destination> [--Options]

Example:
aws s3 sync . s3://mompopbakerycafe 					[sync current folder with bucket]
aws s3 sync . s3://mompopbakerycafe --acl public-read 	[sync current folder with bucket with public read]

```

### Copy Objects to S3 Bucket:
```
aws s3 cp <source> <destination> [--options]

Example:
aws s3 cp <filename> s3://bucket			[single file]
aws s3 cp . s3://bucket 					[copy all in current folder]
```

### Remove Objects from Bucket:
```
aws s3 rm <target> [--options]

Example:
aws s3 rm s3://bucket/filename          	[single file]
aws s3 rm s3://bucket --recursive			[delete all files in the bucket]
```

### Moving Objects between Buckets:
```
aws s3 mv <source> <destination>

Example:
aws s3 mv s3://bucket1 s3://bucket2

```

### Delete a Bucket
```
aws s3 rb <target> [--options]

Example:
aws s3 rb s3://bucket    		[delete an empty bucket]

aws s3 rb s3://bucket --force 	[delete all files and bucket]
```

### Host Static Website on S3:
```
aws s3 website s3://bucket --index-document index.html

```

### Automate Web Hosting using a script:
```
#!/bin/bash

#bucket=$1

echo -n "Enter bucket name: "
read bucket

aws s3 mb s3://$bucket

aws s3 website s3://$bucket/ --index-document index.html

aws s3 sync . s3://$bucket --acl public-read

aws s3 ls

#curl http://$bucket.s3-website.ap-southeast-2.amazonaws.com

start http://$bucket.s3-website-ap-southeast-2.amazonaws.com


```


### Clean S3 Environment using a script:
```
#!/bin/bash

echo -n "Bucket name: "
read bucket
#bucket=$1

aws s3 rm s3://$bucket --recursive  #deletes the contents of the bucket (empty)

aws s3 rb s3://$bucket #deletes the bucket itself

aws s3 ls


```