.. _Research product:

Research products
####

This entity models **Research products**, which may be of four types, as follows.

Literature
====
:Description: Intended for reading by humans (article, thesis, peer-review, blog posts, books, reports, patents, etc.)


Research data
====
:Description: Self-contained, persistently identified digital assets intended for processing (e.g. files containing: tables, metadata collections, dumps; persistent dynamic queries to scientific databases)


Research software
====
:Description: (definition from RDA WG) Research Software includes source code files, algorithms, scripts, computational workflows and executables that were created during the research process or for a research purpose. Note that software components (e.g., operating systems, libraries, dependencies, packages, scripts, etc.) that are used for research but were not created during or with a clear research intent should be considered software in research and not Research Software. This differentiation may vary between disciplines. The minimal requirement for achieving computational reproducibility is that all the computational components (Research Software, software used in research, documentation and hardware) used during the research are identified, described, and made accessible to the extent that is possible.


Other products
====
:Description: any digital asset, uniquely identified, whose nature does not fall in the first three types



Properties
====
This section is to describe the metadata fields for the Research Products


Local identifier
----
:Description: Unique code identifiying the Produc in the SKG (if any, otherwise "stateless identifier")
:Type: String
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "localIdentifier": "the_id"


Identifiers
----
:Description: Identifier for the entity outside of the SKG. 
:Type: List
:Use: Optional (0..1)

Scheme
^^^^^^^^^
:Description: The scheme for the external identifier.
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
            "scheme": "https://doi.org"
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

    "title": ["The computer science ontology: a large-scale taxonomy of research areas"]


Abstracts
--------
:Description: The abstracts of a :ref:`Research product <Research product>` (multiple for multilinguism).
:Type: List
:Use: Recommended (1)

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
:Description: A list of :ref:`Topic` covered by the **Research product**
:Type: List
:Use: Recommended (1)

.. code-block:: json
   :linenos:

    "topics": ["computer science", "semantic web"]

Contributions
--------------------
:Description:
:Type: List
:Use: Mandatory (1)

Person id
^^^^^^^^^^^^^^^^
:Description: 
:Type: String
:Use: Mandatory (1)

Organisation ids
^^^^^^^^^^^^^^^^
:Description: 
:Type: List
:Use: Recommended (1)

Roles
^^^^^^^^^^^^^^^^
:Description: Specific role of a :ref:`Person <Person>` for the **Contribution**
:Type: List of values from CRediT taxonomy
:Use: Recommended (1)

Rank
^^^^^^^^^^^^^^^^
:Description: The rank of the :ref:`Person <Person>` in the author list of a :ref:`Product <Product>`
:Type: Integer
:Use: Recommended (0..1)

.. code-block:: json
   :linenos:

    "contributions": [
        {"person_id": "the_id",
        "organisations": ["org1", "org2", "org3"],
        "rank": 1,
        "roles": ["writing-original-draft", "conceptualization"]
        }
    ]


Manifestations
--------------------
:Description: 
:Type: List
:Use: Mandatory (1)

Product local type 
^^^^^^^^^^^^^^^^
:Description: The type of the manifestation. 
:Type: String from a vocabulary
:Use: Mandatory (1)

Product local type schema
^^^^^^^^^^^^^^^^
:Description: The schema of the manifestation product type. 
:Type: String
:Use: Mandatory (1)

Dates
^^^^^^^^^^^^^^^^
:Description: Relevant dates for the research product.
:Type: List
:Use: Mandatory (1)

Value
"""""""""""""
:Description: The relevant date for the research product.
:Type: String (ISO 8601 date string)
:Use: Mandatory (1)

Type
"""""""""""""
:Description: The type of the date (e.g. publishing, embargo, ...).
:Type: String
:Use: Mandatory (1)

Peer review
^^^^^^^^^^^^^^^^
:Description: 
:Type: String, one of the following (single-blind, open, double-blind, unavailable)
:Use: Mandatory (1)

Metadata curation
^^^^^^^^^^^^^^^^
:Description: 
:Type: String, one of the following (yes, no, unavailable)
:Use: Mandatory (1)

URL
^^^^^^^^^^^^^^^^
:Description: 
:Type: URL
:Use: 

PID
^^^^^^^^^^^^^^^^
:Description: 
:Type: URL
:Use: Mandatory (1)

Access right
^^^^^^^^^^^^^^^^
:Description: 
:Type: String, one of the following (open, closed, embargo, restricted, unavailable).
:Use: Mandatory (1)

Licence
^^^^^^^^^^^^^^^^
:Description: 
:Type: String
:Use: Recommended (1)

Licence schema
^^^^^^^^^^^^^^^^
:Description: 
:Type: String
:Use: Recommended (1)

Bibliographic information
^^^^^^^^^^^^^^^^
:Description: 
:Type: Object
:Use: Mandatory (1)

Issue
"""""""""""""
:Description: 
:Type: 
:Use: 

Start page
"""""""""""""
:Description: 
:Type: 
:Use: 

End page
"""""""""""""
:Description: 
:Type: 
:Use: 

Volume
"""""""""""""
:Description: 
:Type: 
:Use: 

Edition
"""""""""""""
:Description: 
:Type: 
:Use: 

Number
"""""""""""""
:Description: 
:Type: 
:Use: 

Publisher
"""""""""""""
:Description: 
:Type: 
:Use: 

Series
"""""""""""""
:Description: 
:Type: 
:Use: 

Venue
""""""""""""
:Description: 
:Type: 
:Use: 

Hosting data source
""""""""""""
:Description: 
:Type: 
:Use: 

.. code-block:: json
   :linenos:

    "manifestations": [
        {
            "product_local_type": "",
            "product_local_type_schema": "",
            "dates": {
                "value": "",
                "type": ""
            }
            "peer-review": "",
            "metadata curation": "",
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
            "venue": "",
            "hosting_data_source": "",
        }
    ]


Relationships
============

hasContribution
---------------------
:Description: It models the contribution of the **research product**. It can also reference to the :ref:`Organisation <Organisation>`(s) to which the :ref:`Person <Person>` was affiliated when generating this product. For this relation the :ref:`Person <Person>` is an entity in the SKG.
:Use: Optional (0..*)
:Source: research product 
:Target: Contribution 

.. code-block:: json
   :linenos:

    "has_contribution": {
        "research_product": "product_id",
        "contribution": "contribution_id"
    }


hasPersonAffiliatedWith 
---------------------------
:Description: It is a relation between the **research product** and the :ref:`Organisation <Organisation>`. We do not know who is the :ref:`Person <Person>` involved (affiliated to the :ref:`Organisation <Organisation>`).
:Use: Optional (0..*)
:Source: research product 
:Target: :ref:`Organisation <Organisation>` 

.. code-block:: json
   :linenos:

    "has_person_affiliated_with": {
        "research_product": "product_id",
        "organisation": "organisation_id"
    }


is_published_in
--------------
:Description: The research **research product** publishing venue 
:Use: Optional (0..*)
:Source: research product
:Target: venue 

.. code-block:: json
   :linenos:

    "is_published_in": {
        "research_product": "product_id",
        "venue": "venue_id"
    }


is_funded_by 
-------------
:Description: the funds thanks to which the **research product** has been made
:Use: Optional (0..*)
:Source: research product 
:Target: grant

.. code-block:: json
   :linenos:

    "is_funded_by": {
         "research_product": "product_id",
         "grant": "grant_id"
    }


has_subject
-----------
:Description: The topic this **research product** is related to 
:Use: Optional (0..*)
:Source: research product 
:Target: Topic 

.. code-block:: json
   :linenos:

    "has_subject": {
        "research_product": "product_id",
         "subject": "subject_id"
    }


is_related_with_product
-------------------
:Description: other product the **research product** is related with 
:Use: Optional (0..*)
:Source: research product 
:Target: research product
:Note: the semantics should be one among a set of predifined values. Possible "imposed" semantics: DataCite semantics or Scholix semantics set

.. code-block:: json
   :linenos:

    "is_related_with_product": {
        "semantics": "IsSupplementTo"
        "research_product": "product_id",
         "research_product": "product_id",
    }
