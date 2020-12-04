"""

This document contains differents constants for the package

"""

# Primary classification of domains, can be change it in the future.
# There 5 groups.

#These domains referes to websites of Universtiies.
UNIVERSITY = [  'ncbi.nlm.nih.gov',
                'ebi.ac.uk',
                'broadinstitute.org',
                'csbio.sjtu.edu.cn',
                'dna.leeds.ac.uk'
            ]

INSTITUTIONAL = ['cbs.dtu.dk',
                'galaxy.pasteur.fr',
                'bioinformatics.psb.ugent.be',
                'zhanglab.ccmb.med.umich.edu',
                'jci-bioinfo.cn',
                'sanger.ac.uk',
                'protein.bio.unipd.it',
                'imgt.org',
                'genius.embnet.dkfz-heidelberg.de',
                'bioinformatics.psb.ugent.be',
                'ccb.jhu.edu',
                'tools.proteomecenter.org',
                'genome.sph.umich.edu'
                ]

LIFESCIENCE =  [
                'bioconductor.org',
                'emboss.open-bio.org'
                ]

COLLECTIONS = [
                'bioinformatics.org',
                'ms-utils.org',
                'web.expasy.org'
            ]

GENERIC = [
            'github.com',
            'cran.r-project.org',
            'doi.org',
            'imtech.res.in',
            'pypi.python.org',
            'sourceforge.net',
            'sites.google.com',
            'metacpan.org',
            'gitlab.com',
            'code.google.com',
            'bitbucket.org'
        ]

# Create list of dictionaries to save in json format:
CLASSIFICATION_DOMAINS = {
                            'university': UNIVERSITY,
                            'institucional': INSTITUTIONAL,
                            'lifeScience': LIFESCIENCE,
                            'collections': COLLECTIONS,
                            'generic': GENERIC,
                            'others': [],
                            'total': [],
                        }
                        

# Codes HTTP and the description
DICT_CODES_DESCRIPTION = {
    100 : "100 <br>Continue",
    101 : "101 <br>Switching Protocols",
    102 : "102 <br>Processing",
    200 : "200 <br>OK",
    201 : "201 <br>Created",
    202 : "202 <br>Accepted",
    203 : "203 <br>Non-authoritative Information",
    204 : "204 <br>No Content",
    205 : "205 <br>Reset Content",
    206 : "206 <br>Partial Content",
    207 : "207 <br>Multi-Status",
    208 : "208 <br>Already Reported",
    226 : "226 <br>IM Used",
    300 : "300 <br>Multiple Choices",
    301 : "301 <br>Moved Permanently",
    302 : "302 <br>Found",
    303 : "303 <br>See Other",
    304 : "304 <br>Not Modified",
    305 : "305 <br>Use Proxy",
    307 : "306 <br>Temporary Redirect",
    308 : "307 <br>Permanent Redirect",
    400 : "400 <br>Bad Request",
    401 : "400 <br>Unauthorized",
    402 : "402 <br>Payment Required",
    403 : "403 <br>Forbidden",
    404 : "404 <br>Not Found",
    405 : "405 <br>Method Not Allowed",
    406 : "406 <br>Not Acceptable",
    407 : "407 <br>Proxy Authentication Required",
    408 : "408 <br>Request Timeout",
    409 : "409 <br>Conflict",
    410 : "410 <br>Gone",
    411 : "411 <br>Length Required",
    412 : "412 <br>Precondition Failed",
    413 : "413 <br>Payload Too Large",
    414 : "414 <br>Request-URI Too Long",
    415 : "415 <br>Unsupported Media Type",
    416 : "416 <br>Requested Range Not Satisfiable",
    417 : "417 <br>Expectation Failed",
    418 : "418 <br>I'm a teapot",
    421 : "421 <br>Misdirected Request",
    422 : "422 <br>Unprocessable Entity",
    423 : "423 <br>Locked",
    424 : "424 <br>Failed Dependency",
    426 : "426 <br>Upgrade Required",
    428 : "428 <br>Precondition Required",
    429 : "429 <br>Too Many Requests",
    431 : "431 <br>Request Header Fields Too Large",
    444 : "444 <br>Connection Closed Without Response",
    451 : "451 <br>Unavailable For Legal Reasons",
    499 : "499 <br>Client Closed Request",
    500 : "500 <br>Internal Server Error",
    501 : "501 <br>Not Implemented",
    502 : "502 <br>Bad Gateway",
    503 : "503 <br>Service Unavailable",
    504 : "504 <br>Gateway Timeout",
    505 : "505 <br>HTTP Version Not Supported",
    506 : "506 <br>Variant Also Negotiates",
    507 : "507 <br>Insufficient Storage",
    508 : "508 <br>Loop Detected",
    510 : "510 <br>Not Extended",
    511 : "511 <br>Network Authentication Required",
    599 : "599 <br>Network Connect Timeout Error",
}
