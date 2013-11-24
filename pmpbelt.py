# -*- coding: utf-8 -*- 

"""
Module doc string here
"""
import requests
import uritemplate
from uuid import uuid4
from pprint import pprint


def get(uri, my_auth, params=None):
    """
    Performs a GET on the PMP
    Crates and returns a CollectionDoc object
    """
    if params:
        uri = uritemplate.expand(uri, params)

    collection_doc = CollectionDoc(uri, my_auth)

    # store full json as CollectionDoc document attribute
    document = collection_doc.get_document()
    
    collection_doc.parse_document(document)

    return collection_doc
    

def put():
    pass

def post(uri, my_auth):
    pass



def delete():
    pass

# create a new blank collection doc w/ GUID
def new(uri, my_auth):
    new_doc = CollectionDoc(uri, my_auth)
    new_doc.attributes["guid"] = str(uuid4())
    return new_doc
    
        

class CollectionDoc(object):
    """m
    Class doc string
    """
   
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

        # initialize as a blank document object
        
        
        self.attributes = {}

        # many convenient attributes as shortcuts for links
        self.links = {}
        self.querylinks = []
        self.itemlinks = [] # item links, not the expanded items
        self.navlinks = []
        self.editlinks = []
        self.urns = {} # why is this a dict?
        
        self.items = [] # expanded items array
        
        self.error = {}

        self.document = {"version": "1.0", "attributes": self.attributes, 
                        "links" : self.links, "items" : self.items } # full doc. unordered dic.
        
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
        return r.json()


    def parse_document(self, document):

        self.document = document # it will always return something or blank

        # all links
        try:
            self.links = self._extract_obj(self.document['links'])
        except:
            self.links = {}

        # query links (read-only)
        try:
            self.querylinks = self._extract_obj(self.document['links']['query'])
        except:
            self.querylinks = []

        # item links (only collection docs have, so handle)
        try:
            self.itemlinks = self._extract_obj(self.document['links']['item'])
        except:
            self.itemlinks = []

        # nav links (not every doc has nav, so handle)
        try:
            self.navlinks = self._extract_obj(self.document['links']['navigation'])
        except:
            self.navlinks = []

        # edit links
        try:
            self.editlinks = self._extract_obj(self.document['links']['edit'])
        except:
            self.editlinks = []

        # dictionary of urns / query titles
        try:
            self.urns = self._extract_query_types()
        except:
            self.urns = {}

        # attributes
        try:
            self.attributes = self._extract_obj(self.document['attributes'])
        except:
            self.attributes = {}

        # error
        try:
            self.error = self._extract_obj(self.document['error'])
        except:
            self.error = {}

        # items
        try:
            self.items = self._extract_obj(self.document['error'])
        except:
            self.items = []

        return None


    
    def _extract_obj(self, doc_key):
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
                links = doc_key
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

 
