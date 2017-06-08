# CompanyMaster
Sample AWS ElasticSearch (5.3) project. Contains CloudFormation template sample, Index Creation Python ES API, Logstash config


## How to use this code
1. Use the CloudFormation template to create an ElasticSearch Cluster on AWS. Make sure you add your AWS Account ID in the appropriate places. Then add your public IP to the list of IP addresses from where you will access the ES and Kibana cluster
2. Create the index by running create_index.py file. Ensure that you use the appropriate endpoint that is given out from CloudFormation Output. Index creation helps in helping you nail down data types for indexed items.
3. Install logstash on your local machine. Upload datafiles using logstash and the config given in config/company_logstash.conf.

syntax is 
logstash -f <appropriate folder structure>/config/company_logstash.conf

Data will then be uploaded to ES using logstash.
You may want to configure Kibana using KibanaVisualizations.json in the config folder for various graphs.


** Enjoy **


