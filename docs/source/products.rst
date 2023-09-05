.. _Research product:

Research products
####################

This entity models :ref:`Research product`, which may be of four types, as follows.

:Literature: Intended for reading by humans (article, thesis, peer-review, blog posts, books, reports, patents, etc.)
:Research data: Self-contained, persistently identified digital assets intended for processing (e.g. files containing: tables, metadata collections, dumps; persistent dynamic queries to scientific databases)
:Research software: (definition from RDA WG) Research Software includes source code files, algorithms, scripts, computational workflows and executables that were created during the research process or for a research purpose. Note that software components (e.g., operating systems, libraries, dependencies, packages, scripts, etc.) that are used for research but were not created during or with a clear research intent should be considered software in research and not Research Software. This differentiation may vary between disciplines. The minimal requirement for achieving computational reproducibility is that all the computational components (Research Software, software used in research, documentation and hardware) used during the research are identified, described, and made accessible to the extent that is possible.
:Other products: any digital asset, uniquely identified, whose nature does not fall in the first three types



Properties
====

This section describes the metadata fields for the :ref:`Research product`.


Local identifier
----
:Description: Unique code identifiying the :ref:`Research product <Research product>` in the SKG (if any, otherwise "stateless identifier")
:Type: String
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "local_identifier": "product_1"


Identifiers
----
:Description: A list of external identifiers for the entity. 
:Type: List
:Use: Optional (0..1)

Scheme
^^^^^^^^^
:Description: The scheme for the external identifier (e.g., doi, handle, purl, pubmed, etc.).
:Type: String
:Use: Mandatory (1)

Value
^^^^^^^^^^^
:Description: The external identifier.
:Type: String
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "identifiers": [
        {
            "scheme": "doi"
            "value": "10.1103/PhysRevE.80.056103"
        }
    ]
    

Titles
----
:Description: The titles of a :ref:`Research product <Research product>` (multiple for multilinguism).
:Type: List
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "titles": ["The computer science ontology: a large-scale taxonomy of research areas"]


Abstracts
--------
:Description: The abstracts of a :ref:`Research product <Research product>` (multiple for multilinguism).
:Type: List
:Use: Recommended (0..1)

.. code-block:: json
   :linenos:

    "abstracts": ["Ontologies of research areas are important tools for characterising, exploring, and analysing the research landscape..."]


Product type
-----
:Description: The type of the :ref:`Research product <Research product>`. 
:Type: String, one among 

    * literature
    * research data
    * research software
    * other

:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "product_type": "literature"


Topics
--------------------
:Description: A list of :ref:`Topic` covered by the :ref:`Research product <Research product>`.
:Type: List
:Use: Recommended (0..1)

Topic identifier
^^^^^^^^^
:Description: The identifier of a :ref:`Topic <Topic>` relevant for the :ref:`Research product <Research product>`.
:Type: String
:Use: Mandatory (1)

Provenance
^^^^^^^^^
:Description: A list of provenance information tracking the origin of the relation between a :ref:`Topic` and a :ref:`Research product <Research product>`.
:Type: List
:Use: Recommended (0..1)
 
Type
""""""""""""
:Description: A string tracking the provenance of the topic relation.
:Type: String
:Use: Mandatory (1)
 
Trust
""""""""""""
:Description: A numeric value associated to the trust given to the relation to a :ref:`Topic`
:Type: Number
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "topics": [
        {
            "topic": "topic_1",
            "provenance": [
                {
                    "type": "OpenAIRE mining",
                    "trust": 0.7
                }
            ]
        },
        {
            "topic": "topic_2",
            "provenance": [
                {
                    "type": "OpenAlex",
                    "trust": 0.9
                }
            ]
        }
    ]


Contributions
--------------------
:Description: A list of objects that describe a :ref:`Person <Person>`, his/her role, rank and declared affiliations to :ref:`Organisations <Organisation>` when working to a :ref:`Research product <Research product>`.
:Type: List
:Use: Mandatory (1)

Person
^^^^^^^^^^^^^^^^
:Description: The identifier of a :ref:`Person <Person>` contributing to the :ref:`Research product <Research product>`.
:Type: String
:Use: Mandatory (1)

Declared affiliations
^^^^^^^^^^^^^^^^
:Description: A list of :ref:`Organisations <Organisation>` identifiers that reflect the declared affiliations of a :ref:`Person <Person>` for the :ref:`Research product <Research product>`.
:Type: List
:Use: Recommended (0..1)

Roles
^^^^^^^^^^^^^^^^
:Description: The specific role that a :ref:`Person <Person>` had in the :ref:`Research product <Research product>`.
:Type: List of values from `CRediT taxonomy <https://credit.niso.org>`_
:Use: Recommended (0..1)

Rank
^^^^^^^^^^^^^^^^
:Description: The rank of the :ref:`Person <Person>` in the author list of a :ref:`Product <Product>`.
:Type: Integer
:Use: Recommended (0..1)

.. code-block:: json
   :linenos:

    "contributions": [
        {
            "person": "person_123",
            "declared_affiliations": ["org_1", "org_3"],
            "rank": 1,
            "roles": ["writing-original-draft", "conceptualization"]
        }
    ]


Manifestations
--------------------
:Description:  A list of manifestations for the same :ref:`Research product <Research product>` (e.g., a preprint, a postprint, etc.)
:Type: List
:Use: Mandatory (1)

Product local type 
^^^^^^^^^^^^^^^^
:Description: The type of the manifestation. 
:Type: String
:Use: Mandatory (1)

Product local type schema
^^^^^^^^^^^^^^^^
:Description: The schema of the manifestation type. 
:Type: String
:Use: Mandatory (1)

Dates
^^^^^^^^^^^^^^^^
:Description: Relevant dates for the :ref:`Research product <Research product>`.
:Type: List
:Use: Mandatory (1)

Value
"""""""""""""
:Description: The relevant date for the :ref:`Research product <Research product>`.
:Type: String (`ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ date string)
:Use: Mandatory (1)

Type
"""""""""""""
:Description: The type of the date (e.g., publishing, embargo, preprint, ...).
:Type: String
:Use: Mandatory (1)

Peer review
^^^^^^^^^^^^^^^^
:Description: Whether the :ref:`Research product <Research product>` has undergone a peer review process.
:Type: String, one of the following

    * peer-reviewed
    * not peer-reviewed
    * single-blind
    * double-blind
    * open peer review

:Use: Mandatory (1)

Metadata curation
^^^^^^^^^^^^^^^^
:Description: Whether the :ref:`Research product <Research product>` has undergone a metadata curation process.
:Type: String, one of the following 

    * yes
    * no
    * unavailable

:Use: Mandatory (1)

URL
^^^^^^^^^^^^^^^^
:Description: An URL for the manifestation.
:Type: URL
:Use: Mandatory (1)

PID
^^^^^^^^^^^^^^^^
:Description: the pid for the specific manifestation.
:Type: String
:Use: Recommended (0..1)

Access right
^^^^^^^^^^^^^^^^
:Description: The access right for the specific materialisation.
:Type: String, one of the following 

    * open
    * closed
    * embargo
    * restricted
    * unavailable

:Use: Mandatory (1)

Licence
^^^^^^^^^^^^^^^^
:Description: Licence specific to the manifestation.
:Type: String
:Use: Recommended (0..1)

Licence schema
^^^^^^^^^^^^^^^^
:Description: Schema of the licence.
:Type: String
:Use: Recommended (0..1)

Bibliographic information
^^^^^^^^^^^^^^^^
:Description: An object containing bibliographic information about a :ref:`Research product <Research product>` of literature type.
:Type: Object
:Use: Mandatory (1)

Issue
"""""""""""""
:Description: Issue number.
:Type: String
:Use: Optional (0..1)

Start page
"""""""""""""
:Description: The starting page.
:Type: String
:Use: Optional (0..1)

End page
"""""""""""""
:Description: The ending date.
:Type: String
:Use: Optional (0..1)

Volume
"""""""""""""
:Description: Volume number (for journals, books, conferences).
:Type: String
:Use: Optional (0..1)

Edition
"""""""""""""
:Description: The edition (for journals and books).
:Type: String
:Use: Optional (0..1)

Number
"""""""""""""
:Description: Journal number.
:Type: String
:Use: Optional (0..1)

Publisher
"""""""""""""
:Description: The name of the publisher (for journals, books, conferences).
:Type: String
:Use: Optional (0..1)

Series
"""""""""""""
:Description: The name of the conference and book series.
:Type: String
:Use: Optional (0..1)

Venue
""""""""""""
:Description: A :ref:`Venue <Venue>` identifier for the manifestation.
:Type: String
:Use: Mandatory (1)

Hosting data source
""""""""""""
:Description: A :ref:`Data source <Data source>` identifier for the manifestation.`
:Type: String
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "manifestations": [
        {
            "product_local_type": "",
            "product_local_type_schema": "",
            "dates": {
                "value": "2012-03-21",
                "type": "preprint"
            }
            "peer-review": "open",
            "metadata curation": "yes",
            "access rights": "",
            "license": "",
            "license_schema": "",
            "url": "https://link.springer.com/chapter/...",
            "pid": "https://doi.org/10.1007/...",
            "biblio": {
                "issue": "1",
                "start_page": "640",
                "end_page": "645",
                "volume": "13833",
                "edition": "",
                "number": "",
                "publisher": "Springer International Publishing",
                "series": "Lecture Notes in Computer Science"
            }
            "venue": "venue_7",
            "hosting_data_source": "datasource_4",
        }
    ]


Relevant organisations
--------------------
:Description: A list of relevant :ref:`Organisation <Organisation>` identifiers associated with the :ref:`Research product <Research product>` (In case the individual affiliations of the :ref:`Person <Person>` are not available).
:Type: List
:Use: Recommended (0..1)

.. code-block:: json
   :linenos:

    "relevant_organisations": ["org_1", "org5"]

 
Funding
--------------------
:Description: A list of relevant :ref:`Grant <Grant>` identifiers associated with the :ref:`Research product <Research product>`.
:Type: List
:Use: Recommended (0..1)

.. code-block:: json
   :linenos:

    "funding": ["grant_1", "grant_2"]
    

Related products
--------------------
:Description: A list objects representing related :ref:`Research product` and the semantics of such relationships.
:Type: List
:Use: Recommended (0..1)

Relation Type
^^^^^^^^^^^^^^^^
:Description: A list of :ref:`Research product` identifiers supplementing the present one.
:Type: String; one of the following selection of `DataCite relationTypes <https://schema.datacite.org/meta/kernel-4.4/doc/DataCite-MetadataKernel_v4.4.pdf>`_ 

    * cites
    * is_supplemented_by
    * is_documented_by
    * is_new_version_of
    * is_part_of

:Use: Mandatory (1)

Product list
^^^^^^^^^^^^^^^^
:Description: A list of :ref:`Research product` identifiers describing the present one.
:Type: List
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "related_products": [
        {
            "relation_type": "cites", 
            "products": ["product_2", "product_3", "product_4"]
        },
        {
            "relation_type": "is_supplemented_by",
            "products": ["product_7", "product_8", "product_9"],
        },
        {
            "relation_type": "is_documented_by",
            "products": ["product_10", "product_13"],
        },
        {
            "relation_type": "is_new_version_of",
            "products": ["product_5"],
        },
        {
            "relation_type": "is_part_of",
            "products": ["product_11"],
        }
    ]


        





    