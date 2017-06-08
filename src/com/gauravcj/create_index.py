'''
Created on May 30, 2017

@author: jagavkar
'''

import boto3
from elasticsearch import Elasticsearch



def createIndex():
    #client = boto3.client('es')
    #print ("domain names"+ str(client.list_domain_names()))
    es = Elasticsearch([{'host':'search-companymaster2-33sqnlirsg4v62qtaqsvjahyzu.ap-south-1.es.amazonaws.com', 'port':443,'use_ssl':True}],verify_certs = False)
    #mov_index = es.indices.get(index="movies",feature="_settings,_mappings")
    #print(mov_index)
    
    #Delete the index
    #es.indices.delete(index="companies")
    
    #Create the index
    companymapping = """{
                            "settings" : {
                                "number_of_shards" : 4
                            },
                            "mappings" : {
                                "company" : {
                                    "properties" : {
                                        "CIN" : {   "type" : "text" 
                                                },
                                        "DATE_OF_REGISTRATION" : {   
                                                    "type" : "date" ,
                                                    "format": "yyyy-MM-dd HH:mm:ss||dd-MM-yyyy||epoch_millis"
                                                    
                                                },
                                        "COMPANY_STATUS" : {    "type" : "text" ,
                                                                "fields" : {
                                                                  "keyword" : {
                                                                    "type" : "keyword",
                                                                    "ignore_above" : 256,
                                                                    "index" : true
                                                                  }
                                                                }
                                                },
                                        "COMPANY_CLASS" : {    "type" : "text" ,
                                                                "fields" : {
                                                                  "keyword" : {
                                                                    "type" : "keyword",
                                                                    "ignore_above" : 256,
                                                                    "index" : true
                                                                  }
                                                                }
                                                },
                                        "COMPANY_CATEGORY" : {    "type" : "text" ,
                                                                "fields" : {
                                                                  "keyword" : {
                                                                    "type" : "keyword",
                                                                    "ignore_above" : 256,
                                                                    "index" : true
                                                                  }
                                                                }
                                                },
                                        "AUTHORIZED_CAPITAL" : {    "type" : "long" 
                                                },
                                        "PAIDUP_CAPITAL" : {    "type" : "long" 
                                                },
                                        "REGISTERED_STATE" : {    "type" : "text" ,
                                                                "fields" : {
                                                                  "keyword" : {
                                                                    "type" : "keyword",
                                                                    "ignore_above" : 256,
                                                                    "index" : true
                                                                  }
                                                                }
                                                },
                                        "REGISTRAR_OF_COMPANIES" : {    "type" : "text" ,
                                                                "fields" : {
                                                                  "keyword" : {
                                                                    "type" : "keyword",
                                                                    "ignore_above" : 256,
                                                                    "index" : true
                                                                  }
                                                                }
                                                },
                                        "PRINCIPAL_BUSINESS_ACTIVITY" : {    "type" : "text" ,
                                                                "fields" : {
                                                                  "keyword" : {
                                                                    "type" : "keyword",
                                                                    "ignore_above" : 256,
                                                                    "index" : true
                                                                  }
                                                                }
                                                },
                                        "REGISTERED_OFFICE_ADDRESS" : {    "type" : "text" 
                                                },
                                        "SUB_CATEGORY" : {    "type" : "text" ,
                                                                "fields" : {
                                                                  "keyword" : {
                                                                    "type" : "keyword",
                                                                    "ignore_above" : 256,
                                                                    "index" : true
                                                                  }
                                                                }
                                                }                            
                                    }
                                }
                            }
                        }"""
    
    
    es.indices.create(index="companies", body=companymapping)

if __name__ == '__main__':
    createIndex()    
    print("done!")
    pass