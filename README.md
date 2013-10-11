pmpbelt - a utility belt for hypermedia APIs
=======

pmpbelt is a python SDK for working with the [PMP](http://docs.pmp.io). It uses and is heavily influenced by [Requests](http://docs.python-requests.org/en/latest/). And [Batman](http://en.wikipedia.org/wiki/Batman_(TV_series\)).

## Requirements

Requests for python is required. 

    pip install requests
    

[uritemplate](https://pypi.python.org/pypi/uritemplate) is also required for URI Templating.

    pip install uritemplate
    
An OAuth2 client is also required. A mature, OAuth2 conformant client like [rauth](https://github.com/litl/rauth) is recommended. For simplicity, we've included `simple_auth`, a very simple client.

You will need PMP credentials and a working knowledge of the PMP. Read the [Getting Started](https://github.com/publicmediaplatform/pmpdocs/wiki#getting-started) guide. You will need user/pw to generate `client_id` and `client_secret` before you can begin. 



## Sample Usage

First, do your imports, create an auth object, and retrieve the PMP home document (**BAM!**)


    import pmpbelt
    from simple_auth import AuthClient

    client_id = "< REDACTED >"
    client_secret = "< REDACTED >"
    
    # PMP sandbox URL
    my_uri = "https://api-sandbox.pmp.io"   
    
    # build an auth object
    my_auth = AuthClient( my_uri, client_id, client_secret)

    # perform a GET on the PMP API. 
    home_doc = pmpbelt.get(my_uri, my_auth)


You've retrieved the home document as a [Collection.doc+JSON](https://github.com/publicmediaplatform/pmpdocs/wiki/Content-Types,-Profiles-and-Schemas) object. Let's see what else we have in there:

    print home_doc.urns
    
Prints out your URNs and Query Titles in key/value pairs (**POW!**):
    
    [{u'urn:pmp:query:users': u'Query for users'},
    {u'urn:pmp:query:groups': u'Query for groups'},
    {u'urn:pmp:hreftpl:profiles': u'Access profiles'},
    {u'urn:pmp:hreftpl:schemas': u'Access schemas'},
    {u'urn:pmp:hreftpl:docs': u'Access documents'},
    {u'urn:pmp:query:docs': u'Query for documents'},
    {u'urn:pmp:query:guids': u'Generate guids'},
    {u'urn:pmp:query:files': u'Upload media files'}]
    
( You can also access all links available in a document. **SMACK!** )

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

We also need to grab the URI template for our URN. We do that with the `.template` method:

    new_uri = my_doc.template(urn)
    
Print `new_uri` to see what the template looks like. You can see all our query options listed.

    https://api-sandbox.pmp.io/docs{?limit,offset,tag,collection,text,searchsort,has,author,distributor,distributorgroup,startdate,enddate,profile,language}


Choose a few options and save them in a dict.

    # all documents tagged 'samplecontent', filtered by profile 'story'
    params = {'tag': 'samplecontent', 'profile': 'story'}
    
Finally, let's call `pmpbelt.get` again to query for 'story' documents tagged 'samplecontent'. This time, we pass our params into the method call. (**KAPLOOEY!!**)

    new_doc = pmpbelt.get(new_uri, my_auth, params)

## Contributions
This project is open and seeking contributors who are working directly with the PMP. Fork and send a pull request.

That's all for now. Tune in next time. Same Bat time. Same Bat channel.

    
    
    
    
