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


Alternative identifiers
----
:Description: Identifier for the resource outside of the SKG. 
:Type: List
:Use: Optional (0..n)

Identifier scheme
^^^^^^^^^
:Description: The scheme for the external identifier.
:Type: String
:Use: Mandatory (1)

Itentifier value
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
:Description: The titles of a research product (multiple for multilinguism).
:Type: List
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "title": ["The computer science ontology: a large-scale taxonomy of research areas"]
       

Abstracts
--------
:Description: The abstracts of a research product (multiple for multilinguism).
:Type: List
:Use: Recommended (1)

.. code-block:: json
   :linenos:

    "abstracts": ["Ontologies of research areas are important tools for characterising, exploring, and analysing the research landscape..."]


Dates
-----
:Description: Relevant dates for the research product.
:Type: List
:Use: Mandatory, possibly more than one (1..*)

Date value
^^^^^^^^^^^^^
:Description: The relevant date for the research product.
:Type: String (ISO 8601 date string)
:Use: Mandatory (1)

Date type
"""""""""""""
:Description: The type of the date (e.g. publishing, embargo...).
:Type: String
:Use: Mandatory (1)

Date format
"""""""""""""
:Description: The format of the relevant date.
:Type: String 
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "dates": [
        {
            "date_value": "2022-12-03",
            "date_type": "embargo",
            "date_format": "yyyy-MM-dd",
        }
    ]


Product type
-----
:Description: The type of the research product. 
:Type: String, one among `literature`, `research data`, `research software`, `other``}.
:Use: Mandatory, (1)

.. code-block:: json
   :linenos:

    "product_type": "literature"


Product type description
-----
:Description: Free text describing the product.
:Type: String, e.g., `journal-article`, `workflow`, `collection`, etc.
:Use: Required 

.. code-block:: json
   :linenos:

    "product_type_description": "journal-article"


Issue
----
:Description: 
:Type: String
:Use: 

.. code-block:: json
   :linenos:

    "issue": "42"


Volume
----
:Description: 
:Type: 
:Use: 

.. code-block:: json
   :linenos:

    "volume": "IX"


Start page
----
:Description: 
:Type: Integer
:Use: Optional, (0..1)

.. code-block:: json
   :linenos:

    "start_page": "3"


End page
----
:Description: 
:Type: Integer
:Use: Optional, (0..1)

.. code-block:: json
   :linenos:

    "end_page": "13"


Edition
----
:Description: 
:Type: 
:Use: 

.. code-block:: json
   :linenos:

    "edition": ""


Relationships
============

hasContribution
---------------------
:Description: It models the contribution of the research result. It can also reference to the :ref:`Organisation <Organisation>`(s) to which the :ref:`Person <Person>` was affiliated when generating this product. For this relation the :ref:`Person <Person>` is an entity in the SKG.
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
:Description: It is a relation between the result and the :ref:`Organisation <Organisation>`. We do not know who is the :ref:`Person <Person>` involved (affiliated to the :ref:`Organisation <Organisation>`).
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
:Description: The research product publishing venue 
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
:Description: the funds thanks to which the product has been made
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
:Description: The topic this research product is related to 
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
:Description: other product the research product is related with 
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
