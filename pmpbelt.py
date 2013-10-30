# -*- coding: utf-8 -*- 

"""
Module doc string here
"""
import requests
import uritemplate
import json
from pprint import pprint



def get(uri, my_auth, params=None):
    """
    Performs a GET on the PMP
    Crates and returns a CollectionDoc object
    """
    if params:
        uri = uritemplate.expand(uri, params)
    
    return GetCollectionDoc(uri, my_auth)
    

def put():
    pass

def post():
    pass

def delete():
    pass

        

class CollectionDoc(object):
    """m
    Class doc string
    """
    
    #uri = ""
    #read_only_links = ""
    #read_links = ""
   
    
    def __init__(self, uri, authtoken):
        """
        Init doc string
        Creating the CollectionDoc
        Setting a bunch of attributes for links, 
        queries, navlinks, items, etc.
        """
        
        # ADDING A TRAILING SLASH BREAKS SHIT IN REQUESTS
        #if uri[-1] != "/":
        #   uri += "/"
        
        self.uri = uri

        self.authtoken = authtoken

class GetCollectionDoc(CollectionDoc):
    '''
    Doc string
    '''

    def __init__(self, uri, my_auth):

        # set attibutes from super class
        CollectionDoc.__init__(self, uri, my_auth)

        # Retrieve the document from the given URL.  
        # Document is never empty. It will throw exception if it is empty.
        self.document = self.get_document()
        
        # all links
        try:
            self.links = self._extract_links(self.document['links'])
        except:
            self.links = []

        # query links (read-only)
        try:
            self.querylinks = self._extract_links(self.document['links']['query'])
        except:
            self.querylinks = []

        # item links (only collection docs have, so handle)
        try:
            self.items = self._extract_links(self.document['links']['item'])
        except:
            self.items = []

        # nav links (not every doc has nav, so handle)
        try:
            self.navlinks = self._extract_links(self.document['links']['navigation'])
        except:
            self.navlinks = []


        # edit links
        try:
            self.editlinks = self._extract_links(self.document['links']['edit'])
        except:
            self.editlinks = []

        # dictionary of urns / query titles
        try:
            self.urns = self._extract_query_types()
        except:
            self.urns = {}
        
    def get_document(self):
        """
        Performs HTTP GET to retrieve from PMP API
        Args: 
        Returns: 
        Raises: 
        """
        #set our headers for requests
        headers = {'Authorization': 'Bearer ' + self.authtoken, 
                   'Content-Type': 'application/json'}
                
        r = requests.get(self.uri, headers=headers)
    
        document = r.json()
        return document 

    
    def _extract_links(self, doc_link_key):
        """
        Extracts the links object from document and returns variables to hold 
        all links, edit links, and query links.
        
        :doc_link_key: is the document key for a given link list
                example - self.document['links']['query']

        :Returns:  
        Raises : 
        """
        if (self.document):
            try:
                links = doc_link_key
                return links
                
            except KeyError:
                print 'KeyError : ' + str(e) 

                return False 
                pass 
            #    continue 
                

    def _extract_query_types(self):
        """
        Returns a list of dictionaries, each dict with k=v is URN=title
        Actually, we have to do the PHP way, in case URNs aren't unique
        Otherwise, a second occurrence of the same URN clobbers the value
        """
        
        urns = [ {link['rels'][0]: link['title']} for link in self.querylinks ]

        return urns
        

    def template(self, urn):
        """
        grabs uri from href-template for a given urn
        """

        for link in self.querylinks:
           if link['rels'][0] == urn:

                try: # do we have a link?
                    if link['href-template']:
                        uri = link['href-template']
                        return uri 
                    
                except Exception as e:
                    raise e


    def query_urn(self, urn):
        """
        Query by URN. Does a lookup of the href-template 
        Args : 
        Returns : 
        Raises :        
        """
        for link in self.querylinks:
           if link['rels'][0] == urn:
                
                #return our link options

                return link 


    def options(self, urn):
        query = self.query_urn(urn)

        try:
            if query['href-template'] and query['href-vars']:
                return query['href-vars']
        except KeyError as e:
            raise e

 
