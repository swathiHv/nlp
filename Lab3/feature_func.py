import re
def feat_func1( x, y ):
    '''Identify if the word is the first word of the sentence'''
    if( x[0] == "*" and x[1] == "*" ):
        return 1
    return 0

def feat_func2( x, y ):
    '''Check for proper noun'''
    i = x[3] #Index
    if( x[2][i].isupper() ):
        return 1
    return 0

def feat_func3( x, y ):
    '''If Version'''
    i = x[3]
    w = x[2][i]
    if( re.match(r'[\d+\.?]+$',w) ):
        return 1
    return 0

def feat_func4( x, y ):
    '''Is model'''
    i = x[3]
    w = x[2][i]
    if( x[1] == "ORGANIZATION" or x[1] == "PERSON" or x[0] == "ORGANIZATION" or x[0] == "PERSON" ):
        return 1
    return 0

def feat_func5( x, y ):
    '''If money'''
    i = x[3]
    w = x[2][i]
    if( re.match( r'[\d+]',w ) ):
        return 1
    return 0
def feat_func6( x, y ):
    '''If organization'''
    i = x[3]
    w = x[2][i]
    if( w[0].isupper() and y == "ORGANIZATION" ):
        return 1
    return 0

def feat_func7( x, y ):
    '''If money (stupid feat func)'''
    i = x[3]
    w = x[2][i]
    if( re.match( r'[\d+]',w ) and y == "MONEY" ):
        return 1
    return 0
def feat_func8( x, y ):
    '''Specs'''
    i = x[3]
    w = x[2][i]
    if( re.search(r'[\d+]',w) and re.search(r'\.',w) and re.search(r'-',w) ):
        return 1
    return 0
def feat_func9( x, y ):
    '''Location'''
    if( y == "GPE" and x[2][x[3]][0].isupper() ):
        return 1
    return 0
def feat_func10( x, y ):
    ''' Operating System '''
    i = x[3]
    w = x[2][i]
    os = [ "windows", "android", "ios", "linux", "macintosh", "osx", "mac", "firefox", "ubuntu" ]
    if( w.lower() in os ):
        return 1
    return 0
