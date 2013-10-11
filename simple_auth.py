"""
Module docstring
"""

import requests
import time
from base64 import b64encode

class AuthClient(object):
    """
    Creates AuthClient
    Args
        auth_uri : URI of the authentication API, e.g.: http://auth.pmp.io/
        client_id : the client ID to use for authentication requests
        client_secret : the client secret to use for authentication requests
        
    Attributes
        AUTH_ENDPOINT : the URL to the token generation endpoint
        _auth_uri : 
        _client_id : client ID used for auth
        _client_secret : client secret used for auth
        _token_last_time : epoch time for issuance of current token
        _access_token
    Methods
        __init__ : inits object
        get_token : gets an access token
    """
    
    AUTH_ENDPOINT = 'auth/access_token'
    _access_token = ""
    token_last_time = ""
    
    def __init__(self, auth_uri, client_id, client_secret):
        """
        Inits AuthClient object with uri, clientID, client secret
        Raises
        """     
        # normalize to end uri with trailing /
        if auth_uri[-1] != "/":
            auth_uri += "/"
            
        self._auth_uri = auth_uri
        self._client_id = client_id
        self._client_secret = client_secret
        self.get_token()
        
    def get_token(self, refresh=False):
        """
        Gets a token for the given client ID and secret
            Args : (bool) refresh - whether to get a new token
            Returns : (string) token
            Raises : Exception
        """
        
        if 1:  # handle token expiration
            pass
        
        my_uri = self._auth_uri + self.AUTH_ENDPOINT
        
        client_string = self._client_id + ":" + self._client_secret
        
        my_hash = b64encode(client_string)
        
        refresh = refresh
        
        #set our headers for requests
        headers = {'Authorization': 'CLIENT_CREDENTIALS ' + my_hash}
        
        r = requests.get(my_uri, headers=headers)
        
        if r.status_code == 200:
            my_data = r.json()
            #self._access_token = my_data
            #self.token_last_time = int(time.time())
            self._access_token = my_data["access_token"]
            #return True
            return self._access_token #should check for empty dict?
            
    def revoke_token(self, my_token):
        """
        Revokes the current token
        """
        pass