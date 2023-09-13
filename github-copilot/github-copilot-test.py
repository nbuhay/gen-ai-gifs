# write a binary search function
# that returns the index of the target
# if found, or -1 if not found
# https://en.wikipedia.org/wiki/Binary_search_algorithm
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# write a unit test to verify this binary_search function
def test_binary_search():
    arr = [1, 3, 5, 7, 9]
    target = 3
    assert binary_search(arr, target) == 1

# write a function to create a new s3 bucket with the name "gen-ai-demo-new-bucket". Then upload a file named 'hello-world.txt' to the bucket. Return True if the upload was successful.
def upload_file_to_s3():
    import boto3
    s3 = boto3.resource('s3')
    bucket_name = 'gen-ai-demo-new-bucket'
    bucket = s3.Bucket(bucket_name)
    bucket.upload_file('hello-world.txt', 'hello-world.txt')
    return True

# invoke the function
upload_file_to_s3()
