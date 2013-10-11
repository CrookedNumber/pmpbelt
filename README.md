pmpbelt - a utility belt for hypermedia APIs
=======

pmpbelt is a python SDK for working with the [PMP](http://docs.pmp.io). 

## Requirements

Requests for python is required. 

    pip install requests
    

uritemplate is also required

    pip install uritemplate
    
And OAuth2 client is also required. A mature, OAuth2 conformant client like rauth is recommended. For simplicity, we've included `simple_auth`, a very simple client.

You will need PMP credentials and a working knowledge of the PMP. Read the [Getting Started](https://github.com/publicmediaplatform/pmpdocs/wiki#getting-started) guide. You will need user/pw to generate `client_id` and `client_secret` before you can begin. 



## Sample Usage

First, do your imports, create an auth object, and pull the PMP home document


    import pmpbelt
    from simple_auth import AuthClient
    
    # just for pretty-printing
    from pprint import pprint
    
    
    client_id = "< REDACTED >"
    client_secret = "< REDACTED >"
    
    # PMP sandbox URL
    my_uri = "https://api-sandbox.pmp.io"   
    
    # build an auth object
    my_auth = AuthClient( my_uri, client_id, client_secret)

    # perform a GET on the PMP API
    home_doc = pmpbelt.get(my_uri, my_auth)


You've saved the home document as a pmpbelt object. Let's see what else we have in there:

    my_doc.urns
    
    
    
    
