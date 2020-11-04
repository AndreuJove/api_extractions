"""

This document conforms a primary classification of the procedence of different domains.
This classification will be used to compare metrics between them. And show their strengths and weaknesses.


"""


# Primary classification of domains, can be change it in the future.
#There 5 groups.

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
CLASSIFICATION_DOMAINS = [
                            {'university': UNIVERSITY},
                            {'institucional': INSTITUTIONAL},
                            {'lifeScience': LIFESCIENCE},
                            {'collections': COLLECTIONS},
                            {'generic': GENERIC},
                            {'others': []},
                            {'total': []}
                        ]