# write a binary search function
def binary_search(list, item):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# write a unit test to verify this binary_search function
binary_search([1, 2, 3, 4, 5], 5) == 

# write a function to create a new s3 bucket named 'gen-ai-demo-new-bucket'. Then upload a file named 'hello-world.txt' to the bucket. return True if the upload was successful
def create_s3_bucket(bucket_name):
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    s3.upload_file('hello-world.txt', bucket_name, 'hello-world.txt')
    return True

# invoke the create_s3_bucket with bucket name 'gen-ai-demo-new-bucket'
create_s3_bucket('gen-ai-demo-new-bucket')
