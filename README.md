pmpbelt - a utility belt for hypermedia APIs
=======

pmpbelt is a python SDK for working with the [PMP](http://docs.pmp.io). It uses and is heavily influenced by Requests. 

## Requirements

Requests for python is required. 

    pip install requests
    

[uritemplate](https://pypi.python.org/pypi/uritemplate) is also required for URI Templating.

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

    # perform a GET on the PMP API. BAM!
    home_doc = pmpbelt.get(my_uri, my_auth)


You've saved the home document as a pmpbelt object. Let's see what else we have in there:

    print home_doc.urns
    
Prints out your URNs and Query Titles in key/value pairs (POW!):
    
    [{u'urn:pmp:query:users': u'Query for users'},
    {u'urn:pmp:query:groups': u'Query for groups'},
    {u'urn:pmp:hreftpl:profiles': u'Access profiles'},
    {u'urn:pmp:hreftpl:schemas': u'Access schemas'},
    {u'urn:pmp:hreftpl:docs': u'Access documents'},
    {u'urn:pmp:query:docs': u'Query for documents'},
    {u'urn:pmp:query:guids': u'Generate guids'},
    {u'urn:pmp:query:files': u'Upload media files'}]
    
( You can also access all links available in a document. SMACK! )

    home_doc.links            # all link relations
    home_doc.items            # item links, if available
    home_doc.querylinks       # query links
    home_doc.editlinks        # edit links, if available
    home_doc.navlinks         # navigation links
    
Let's choose the query for Query for Documents. Let's set its URN in a variable and see the options for that URN:
    
    urn = 'urn:pmp:query:docs' 

    print home_doc.options(urn)
    
We see all query options for the given URN:
    
    {u'author': u'https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Retrieval',
     u'collection': u'https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Retrieval',
     u'distributor': u'https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Retrieval',
     u'distributorgroup': u'https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Retrieval',
     u'enddate': u'https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Retrieval',
     u'has': u'https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Retrieval',
     u'language': u'https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Retrieval',
     u'limit': u'https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Retrieval',
     u'offset': u'https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Retrieval',
     u'profile': u'https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Retrieval',
     u'searchsort': u'https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Retrieval',
     u'startdate': u'https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Retrieval',
     u'tag': u'https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Retrieval',
     u'text': u'https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Retrieval'}
    
The links correspond to human readable documentation.

Choose a few options and save them in a dict.

    # all documents tagged 'samplecontent', filtered by profile 'story'
    params = {'tag': 'samplecontent', 'profile': 'story'}
    


    
    
    
    
