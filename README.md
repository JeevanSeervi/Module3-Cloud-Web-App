# Module 3 - Cloud Web Application

## Overview

This project was completed as part of Module 3 of my cloud internship.

The goal was to deploy a simple web application on AWS and understand basic cloud services, storage, networking, IAM, monitoring, environment variables, and application logging.

## Technologies Used

- Python
- Flask
- AWS EC2
- AWS S3
- AWS CloudWatch
- Nginx
- GitHub
- Linux

## AWS Services Used

### Amazon EC2
Used EC2 to create and run the Linux server hosting the Flask web application.

### Amazon S3
Created an S3 bucket and uploaded the application file to demonstrate cloud object storage.

### IAM
Used an IAM user and permissions to access AWS services securely.

### CloudWatch
Checked EC2 monitoring metrics such as CPU utilization.

### Service Quotas
Checked the EC2 On-Demand Standard instance quota and its current utilization.

## Application Deployment

The application was built using Python and Flask.

Deployment flow:

```text
Flask Application
       ↓
   AWS EC2
       ↓
     Nginx
       ↓
Live Web Application