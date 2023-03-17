.. _Research products:

Research products
####

TODO add Description

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
:Representation: XML element ``localIdentifier``

.. code-block:: xml
   :linenos:

    <localIdentifier>50|doi_dedup___::80f29c8c8ba18c46c88a285b7e739dc3</localIdentifier>


Alternative identifiers
----
:Description: Identifier for the resource outside of the SKG. 
:Type: Wrapper element
:Use: optional (0,.. n)
:Representation: XML element ``identifiers``

Identifier scheme
^^^^^^^^^
:Description: The scheme for the external identifier.
:Type: String
:Use: mandatory (1)
:Representation: XML attribute ``IdentifierScheme``

Itentifier value
^^^^^^^^^^^
:Description: The external identifier.
:Type: String
:Use: mandatory (1)
:Representation: XML element ``identifier``

.. code-block:: xml
   :linenos:

    <identifiers>
        <identifier identifierScheme="doi">10....</identifier>
    </identifiers>


Title
----
:Description: The title of the research product.
:Type: String
:Use: mandatory, possibly multiple (1..*)
:Representation: XML element ``title`` as a multilingual string

titleType
^^^^^^^^
:Description: The type of the title (main, subtitle).
:Type: String
:Use: mandatory, (1)
:Representation: XML attribute ``titleType`` 

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

.. code-block:: xml
   :linenos:

    <title titleType="main">On the.... </title>
       

Abstract
----
:Description: A description for the research product.
:Type: String
:Use: required, possibly multiple (0..*)
:Representation: XML element ``abstract`` 

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

.. code-block:: xml
   :linenos:

    <abstract>This dataset ...</abstract>


Dates
---
:Description: Relevant dates for the research product.
:Type: Wrapper element 
:Use: mandatory, possibly more than one (1..*)
:Representation: XML element ``dates``

Date
^^^^^^^^^^^^^
:Description: The relevant date for the research product.
:Type: String 
:Use: mandatory (1)
:Representation: XML element ``date``

Date Type
"""""""""""""
:Description: The type of the date (e.g. publishing, embargo...).
:Type: String
:Use: mandatory (1)
:Representation: XML attribute ``dateType

Date Format
"""""""""""""
:Description: The format of the relevant date.
:Type: String 
:Use: mandatory (1)
:Representation: XML attribute ``dateFormat``

.. code-block:: xml
   :linenos:

    <dates>
        <date dateType="embargo" dateFormat="yyyy-MM-dd">2022-12-03</date> 
    </dates>


Resource type
-----
:Description: The type of the research product. One among (literatur, researcData, researchSoftware, Other).
:Type: String
:Use: mandatory
:Representation: XML element ``resourceType``

Resource type description
^^^^^^^^^^^^^^^
:Description: Free text describing the resource (i.e. journal-article, workflow, collection ....).
:Type: String 
:Use: required 
:Representation: XML attribute ``resourceTypeDescription``

.. code-block:: xml
   :linenos:

    <resourceType resourceTypeGeneral="monograph">literature</resourceType>


Issue
----
:Description: 
:Type: String
:Use: 
:Representation: XML element ``issue``

.. code-block:: xml
   :linenos:

    <tag>...</tag>


Volume
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``volume``

.. code-block:: xml
   :linenos:

    <tag>...</tag>


Start page
----
:Description: 
:Type: Integer
:Use: optional, (0..1)
:Representation: XML element ``startPage``

.. code-block:: xml
   :linenos:

    <tag>...</tag>


End page
----
:Description: 
:Type: Integer
:Use: optional, (0..1)
:Representation: XML element ``endPage``

.. code-block:: xml
   :linenos:

    <tag>...</tag>


Edition
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``edition``

.. code-block:: xml
   :linenos:

    <tag>...</tag>


Relationships
============

hasAuthorship
---------------------
:Description: It models the authorship of the research result. It can also reference to the organization(s) to which the author was affiliated when generating this product. For this relation the author is an entity in the SKG
:Use: Optional (0..*)
:Source: research product 
:Target: authorship 

.. code-block:: xml
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

.. code-block:: xml
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

.. code-block:: xml
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

.. code-block:: xml
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

.. code-block:: xml
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

.. code-block:: xml
   :linenos:

    <relation semantics="IsSupplementedBy">
        <source type="researchProduct">resultId</source>
        <target type="researchProduct">resultId</target>
    </relation>
