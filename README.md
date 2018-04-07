# Cross-Object-Compressed-Storage-System

Cross-object storage is a storage architectural approach in which variety of objects are managed and saved in forms of objects, utilizing both on-premise and cloud resources. This storage technology allows huge retention for massive unstructured data present in today's world. This project aims at creating a cross-object storage system which uses **OpenStack** as its backbone and also leverages the services provided by **Amazon AWS S3** to create a robust, scalable and cheap storage system which is also prone to on-premise disasters.

The main functionalities of my Storage system include the following features - 

1. **COMPRESSION** - Compressing the object before being uploaded and put into OpenStack and further to AWS S3.
2. **BACKING UP** - Backing up data into 2 parts from OpenStack to AWS S3 for making storage extremely affordable.
3. **DISASTER RECOVERY** - Having a copy of the objects and a mechanism to get the object in any sudden case of disaster.
4. **REPLICATION** - Making multiple copies across both storage systems for getting copies of data and saving it at any cost. 
