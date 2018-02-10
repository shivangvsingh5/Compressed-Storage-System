import swiftclient
import boto3
import gzip
import gzip
import shutil

# Creating the connection to S3

class storageCompressor():
    #    s3connection
    def __init__(self):
        '''
        Initializes the connection to S3 and Openstack

        '''
        self.swift_conn = swiftclient.client.Connection(authurl='Yoururl',
                                                        user='Yourame', key='Yourname', tenant_name='Yourname',
                                                        auth_version='Yourversion',
                                                        os_options={'tenant_id': 'YourID',
                                                                    'region_name': ''}
                                                        )

        self.s3_client = boto3.client('s3', aws_access_key_id='YourAWSAccessKey',
                                      aws_secret_access_key='YourSecretKey',
                                      region_name='YourRegionName'
                                      )
        if self.swift_conn and self.s3_client:
            print "Connection Successfully Validated for Openstack and AWS Public Cloud"
        else:
            print "Connection Failed"

    def createbucket(self, bucket_name):
        swift_created_bucket = self.swift_conn.put_container(bucket_name)
        s3_created_bucket = self.s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
            'LocationConstraint': 'us-west-1'})

        # Returning Success (0) if buckets are successfully created else returning 1

        if swift_created_bucket and s3_created_bucket:
            return 0
        else:
            return 1

    def compressAndPut(self, bucket_name, object_name):
        response_s3 = self.s3_client.put_object(Body=open(object_name, 'rb'), Bucket=bucket_name, Key=object_name)
        with open(object_name, 'rb') as f_in, gzip.open(object_name + '.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        file_post = open(object_name + '.gz', 'rb')

        response_swift = self.swift_conn.put_object(bucket_name, object_name, file_post)

    def retrieveObject(self, bucket_name, object_name):
        response = self.s3_client.get_object(Bucket=bucket_name, Key=object_name)
        with open(object_name, 'w') as f:
            chunk = response['Body'].read(1024 * 8)
            while chunk:
                f.write(chunk)
                chunk = response['Body'].read(1024 * 8)
        print "Downloaded the file" + object_name + "from public Cloud"


if __name__ == "__main__":

    while True:
        print("\n\
        #Cross-ObjectCompressedStorage#\n\n\tInitializeConnection(I)\n\tCreateBucket(C)\n\tCompressAndPut(P)\n\tRetrieveObject(R)\n\tQuit(Q)")

        choice = raw_input(">>> ").lower().rstrip()
        if choice == "i":
            sc = storageCompressor()

        elif choice == "c":
            bucketname = raw_input('Enter Bucket Name:').lower().rstrip()

            if sc.createbucket(bucketname):
                print "Successfully Created Replicated buckets on prem and on AWS"

        elif choice == "p":
            bucketname = raw_input('Enter Bucket Name:').lower().rstrip()
            object_name = raw_input('Enter object Name:').lower().rstrip()

            sc.compressAndPut(bucketname, object_name)

            print "Successfully Compressed and saved on prem and Replicated to AWS cloud"

        elif choice == "r":
            bucketname = raw_input('Enter Bucket Name:').lower().rstrip()
            object_name = raw_input('Enter object Name:').lower().rstrip()
            sc.retrieveObject(bucketname, object_name)



        elif choice == "q":
            break
        else:
            print("Invalid choice, please choose again\n")
