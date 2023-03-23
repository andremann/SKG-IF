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
:Use: mandatory (1)

.. code-block:: json
   :linenos:

    "localIdentifier": "the_id"


Alternative identifiers
----
:Description: Identifier for the resource outside of the SKG. 
:Type: List
:Use: optional (0..n)

Identifier scheme
^^^^^^^^^
:Description: The scheme for the external identifier.
:Type: String
:Use: mandatory (1)

Itentifier value
^^^^^^^^^^^
:Description: The external identifier.
:Type: String
:Use: mandatory (1)

.. code-block:: json
   :linenos:

    "identifiers": [
        {
            "scheme": "https://..."
            "value": "the_id"
        }
    ]
    


Title
----
:Description: The title of the research product.
:Type: String
:Use: mandatory, possibly multiple (1..*)

.. titleType
.. ^^^^^^^^
.. :Description: The type of the title (main, subtitle).
.. :Type: String
.. :Use: mandatory, (1)

.. titleLanguage
.. ^^^^^^^^^^

.. :Description: The language of the title of the research product
.. :Type: string
.. :Use: mandatory, (1)
.. :Representation: XML attribute ``titleLanguage`` 


.. languageCode
.. ^^^^^^^^^^
.. :Description: The code of the language of the title of the research product
.. :Type: string
.. :Use: mandatory, (1)
.. :Representation: XML attribute ``languageCode`` 

.. code-block:: json
   :linenos:

    "title": "title"
       

Abstract
--------
:Description: A description for the research product.
:Type: String
:Use: required, possibly multiple (0..*) 

.. abstractLanguage
.. ^^^^^^^^^^^^^^
.. :Description: The language of the abstract of the research product
.. :Type: string
.. :Use: mandatory, (1)
.. :Representation: XML attribute ``abstractLanguage`` 


.. languageCode
.. ^^^^^^^^^^^
.. :Description: The code of the language of the abstract of the research product
.. :Type: string
.. :Use: mandatory, (1)
.. :Representation: XML attribute ``languageCode`` 

.. code-block:: json
   :linenos:

    "abstract": "..."


Dates
-----
:Description: Relevant dates for the research product.
:Type: List
:Use: mandatory, possibly more than one (1..*)

Date value
^^^^^^^^^^^^^
:Description: The relevant date for the research product.
:Type: String 
:Use: mandatory (1)

Date type
"""""""""""""
:Description: The type of the date (e.g. publishing, embargo...).
:Type: String
:Use: mandatory (1)

Date format
"""""""""""""
:Description: The format of the relevant date.
:Type: String 
:Use: mandatory (1)

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
:Description: The type of the research product. One among {literature, researcData, researchSoftware, Other}.
:Type: String
:Use: mandatory

.. code-block:: json
   :linenos:

    "product_type": "literature"


Product type description
-----
:Description: Free text describing the product (i.e., journal-article, workflow, collection, etc.).
:Type: String 
:Use: required 

.. code-block:: json
   :linenos:

    "product_type_descritpion": "journal-article"


Issue
----
:Description: 
:Type: String
:Use: 

.. code-block:: json
   :linenos:

    "issue": ""


Volume
----
:Description: 
:Type: 
:Use: 

.. code-block:: json
   :linenos:

    "volume": ""


Start page
----
:Description: 
:Type: Integer
:Use: optional, (0..1)

.. code-block:: json
   :linenos:

    "start_page": ""


End page
----
:Description: 
:Type: Integer
:Use: optional, (0..1)

.. code-block:: json
   :linenos:

    "end_page": ""


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

hasAuthorship
---------------------
:Description: It models the authorship of the research result. It can also reference to the organization(s) to which the author was affiliated when generating this product. For this relation the author is an entity in the SKG
:Use: Optional (0..*)
:Source: research product 
:Target: authorship 

.. code-block:: json
   :linenos:

    <relation semantics="hasAuthorship">
        <source type="researchProduct">resultId</source>
        <target type="authorship">authorshipId</target>
    </relation>


hasAuthorAffiliatedWith 
---------------------------
:Description: It is a relation between the result and the organization. We do not know who is the researcher involved (affiliated to the organization)
:Use: Optional (0..*)
:Source: research product 
:Target: organization 

.. code-block:: json
   :linenos:

    <relation semantics="hasAuthorAffiliatedWith">
        <source type="researchProduct">resultId</source>
        <target type="organization">organizationId</target>
    </relation>

publishedIn
--------------
:Description: The research product publishing venue 
:Use: Optional (0..*)
:Source: research product
:Target: venue 

.. code-block:: json
   :linenos:

    <relation semantics="publishedIn">
        <source type="researchProduct">resultId</source>
        <target type="venue">venueId</target>
    </relation>

fundedBy 
-------------
:Description: the funds thanks to which the product has been made
:Use: Optional (0..*)
:Source: research product 
:Target: project

.. code-block:: json
   :linenos:

    <relation semantics="fundedBy">
        <source type="researchProduct">resultId</source>
            <target type="project">projectId</target>
    </relation>



hasSubject
-----------
:Description: The topic this research product is related to 
:Use: Optional (0..*)
:Source: research product 
:Target: Topic 

.. code-block:: json
   :linenos:

    <relation semantics="hasSubject">
        <source type="researchProduct">resultId</source>
        <target type="project">topicId</target>
    </relation>


relatedWithProduct 
-------------------
:Description: other product the research product is related with 
:Use: Optional (0..*)
:Source: research product 
:Target: research product
:Note: the semantics should be one among a set of predifined values. Possible "imposed" semantics: DataCite semantics or Scholix semantics set

.. code-block:: json
   :linenos:

    <relation semantics="IsSupplementedBy">
        <source type="researchProduct">resultId</source>
        <target type="researchProduct">resultId</target>
    </relation>
