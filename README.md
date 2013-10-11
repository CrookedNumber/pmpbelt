pmpbelt - a utility belt for hypermedia APIs
=======

pmpbelt is a python SDK for working with the [PMP](http://docs.pmp.io). 

## Requirements

Requests for python is required. 

    pip install requests
    

uritemplate is also required

    pip install uritemplate
    
And OAuth2 client is also required. A mature, OAuth2 conformant client like [rauth](https://github.com/litl/rauth) is recommended. For simplicity, we've included `simple_auth`, a very simple client.

You will need PMP credentials and a working knowledge of the PMP. Read the [Getting Started](https://github.com/publicmediaplatform/pmpdocs/wiki#getting-started) guide. You will need user/pw to generate `client_id` and `client_secret` before you can begin. 



## Sample Usage

First, do your imports, create an auth object, and pull the PMP home document


    import pmpbelt
    from simple_auth import AuthClient

    client_id = "< REDACTED >"
    client_secret = "< REDACTED >"
    
    # PMP sandbox URL
    my_uri = "https://api-sandbox.pmp.io"   
    
    # build an auth object
    my_auth = AuthClient( my_uri, client_id, client_secret)

    # perform a GET on the PMP API
    home_doc = pmpbelt.get(my_uri, my_auth)


You've saved the home document as a pmpbelt object. Let's see what else we have in there:

    print home_doc.urns
    
Prints out your URNs and Query Titles in key/value pairs:
    
    [{u'urn:pmp:query:users': u'Query for users'},
    {u'urn:pmp:query:groups': u'Query for groups'},
    {u'urn:pmp:hreftpl:profiles': u'Access profiles'},
    {u'urn:pmp:hreftpl:schemas': u'Access schemas'},
    {u'urn:pmp:hreftpl:docs': u'Access documents'},
    {u'urn:pmp:query:docs': u'Query for documents'},
    {u'urn:pmp:query:guids': u'Generate guids'},
    {u'urn:pmp:query:files': u'Upload media files'}]
    
You can also access all links available in a document.

    home_doc.links            # all link relations
    home_doc.items            # item links, if available
    home_doc.querylinks       # query links
    home_doc.editlinks        # edit links, if available
    home_doc.navlinks         # navigation links
    
Choose a URN to query and set some corresponding parameters.  
    
    # Query for documents
    urn = 'urn:pmp:query:docs' 
    
    # all documents tagged 'samplecontent', filtered by profile 'story'
    params = {'tag': 'samplecontent', 'profile': 'story'}
    


    
    
    
    
