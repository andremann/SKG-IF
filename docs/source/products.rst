.. _Research product:

Research products
####

This entity models **Research products**, which may be of four types, as follows.

:Literature: Intended for reading by humans (article, thesis, peer-review, blog posts, books, reports, patents, etc.)
:Research data: Self-contained, persistently identified digital assets intended for processing (e.g. files containing: tables, metadata collections, dumps; persistent dynamic queries to scientific databases)
:Research software: (definition from RDA WG) Research Software includes source code files, algorithms, scripts, computational workflows and executables that were created during the research process or for a research purpose. Note that software components (e.g., operating systems, libraries, dependencies, packages, scripts, etc.) that are used for research but were not created during or with a clear research intent should be considered software in research and not Research Software. This differentiation may vary between disciplines. The minimal requirement for achieving computational reproducibility is that all the computational components (Research Software, software used in research, documentation and hardware) used during the research are identified, described, and made accessible to the extent that is possible.
:Other products: any digital asset, uniquely identified, whose nature does not fall in the first three types



Properties
====
This section is to describe the metadata fields for the **Research Products**.


Local identifier
----
:Description: Unique code identifiying the **Research product** in the SKG (if any, otherwise "stateless identifier")
:Type: String
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "localIdentifier": "product_1"


Identifiers
----
:Description: Identifier for the entity outside of the SKG. 
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
:Description: The type of the research product. 
:Type: String, one among `literature`, `research data`, `research software`, `other``}.
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "product_type": "literature"


Topics
--------------------
:Description: A list of :ref:`Topic <Topic>` identifiers covered by the **Research product**.
:Type: List
:Use: Recommended (0..1)

.. code-block:: json
   :linenos:

    "topics": ["topic_1", "topic_2"]


Contributions
--------------------
:Description: A list of objects that describe a :ref:`Person <Person>`, his/her role, rank and declared affiliations to :ref:`Organisation <Organisation>` when working to a **Research product**.
:Type: List
:Use: Mandatory (1)

Person
^^^^^^^^^^^^^^^^
:Description: The identifier of a :ref:`Person <Person>` contributing to the **Research product**.
:Type: String
:Use: Mandatory (1)

Declared affiliations
^^^^^^^^^^^^^^^^
:Description: A list of :ref:`Organisation <Organisation>` identifiers that reflect the declared affiliations of a :ref:`Person <Person>` for the **research product**.
:Type: List
:Use: Recommended (0..1)

Roles
^^^^^^^^^^^^^^^^
:Description: The specific role that a :ref:`Person <Person>` had in the **Research product**.
:Type: List of values from CRediT taxonomy
:Use: Recommended (0..1)

Rank
^^^^^^^^^^^^^^^^
:Description: The rank of the :ref:`Person <Person>` in the author list of a :ref:`Product <Product>`.
:Type: Integer
:Use: Recommended (0..1)

.. code-block:: json
   :linenos:

    "contributions": [
        {"person": "person_123",
        "declared_affiliations": ["org_1", "org_3"],
        "rank": 1,
        "roles": ["writing-original-draft", "conceptualization"]
        }
    ]


Manifestations
--------------------
:Description:  A list of manifestations for the same **Research product** (e.g., a preprint, a postprint, etc.)
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
:Description: Relevant dates for the **research product**.
:Type: List
:Use: Mandatory (1)

Value
"""""""""""""
:Description: The relevant date for the **research product**.
:Type: String (ISO 8601 date string)
:Use: Mandatory (1)

Type
"""""""""""""
:Description: The type of the date (e.g. publishing, embargo, ...).
:Type: String
:Use: Mandatory (1)

Peer review
^^^^^^^^^^^^^^^^
:Description: Whether the **Research product** has undergone a peer review process.
:Type: String, one of the following (single-blind, open, double-blind, unavailable)
:Use: Mandatory (1)

Metadata curation
^^^^^^^^^^^^^^^^
:Description: Whether the **Research product** has undergone a metadata curation process.
:Type: String, one of the following (yes, no, unavailable)
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
:Type: String, one of the following (open, closed, embargo, restricted, unavailable).
:Use: Mandatory (1)

Licence
^^^^^^^^^^^^^^^^
:Description: 
:Type: String
:Use: Recommended (0..1)

Licence schema
^^^^^^^^^^^^^^^^
:Description: 
:Type: String
:Use: Recommended (0..1)

Bibliographic information
^^^^^^^^^^^^^^^^
:Description: An object containing bibliographic information about a **Research product**.
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
:Description: Volume number.
:Type: String
:Use: Optional (0..1)

Edition
"""""""""""""
:Description: The edition.
:Type: String
:Use: Optional (0..1)

Number
"""""""""""""
:Description: 
:Type: String
:Use: Optional (0..1)

Publisher
"""""""""""""
:Description: The name of the publisher.
:Type: String
:Use: Optional (0..1)

Series
"""""""""""""
:Description: The name of the book series.
:Type: String
:Use: Optional (0..1)

Venue
""""""""""""
:Description: A :ref:`Venue <Venue>` identifiers for the manifestation.
:Type: String
:Use: Mandatory (1)

Hosting data source
""""""""""""
:Description: A :ref:`Data source <Data source>` identifiers for the manifestation.`
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
            "url": "",
            "pid": "",
            "biblio_info": {
                "issue": "",
                "start_page": "",
                "end_page": "",
                "volume": "",
                "edition": "",
                "number": "",
                "publisher": "",
                "series": ""
            }
            "venue": "venue_7",
            "hosting_data_source": "datasource_4",
        }
    ]


Relevant organisations
--------------------
:Description: A list of relevant :ref:`Organisation <Organisation>` identifiers associated with the **Research product** (without passing from a :ref:`Person <Person>`)
:Type: List
:Use: Recommended (0..1)

.. code-block:: json
   :linenos:

    "relevant_organisations": ["org_1", "org5"]

 
Funding
--------------------
:Description: A list of relevant :ref:`Grant <Grant>` identifiers associated with the **Research product**.
:Type: List
:Use: Recommended (0..1)

.. code-block:: json
   :linenos:

    "funding": ["grant_1", "grant_2"]
    

TODO: need to extend Product-to-Product relationship (a selection from DataCite).

Citations
--------------------
:Description: A list of **Research product** identifiers cited.
:Type: List
:Use: Recommended (0..1)

.. code-block:: json
   :linenos:

    "cites": ["product_2", "product_3", "product_4"]












