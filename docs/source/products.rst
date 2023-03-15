Research products
####

TODO add Description

Literature
====
:Description: Intended for reading by humans (article, thesis, peer-review, blog posts, books, reports, patents, etc.)


Research data
====
:Description: Self-contained, persistently identified digital assets intended for processing (e.g. files containing: tables, metadata collections, dumps; persistent dynamic queries to scientific databases)


Research Software
====
:Description: (definition from RDA WG) Research Software includes source code files, algorithms, scripts, computational workflows and executables that were created during the research process or for a research purpose. Note that software components (e.g., operating systems, libraries, dependencies, packages, scripts, etc.) that are used for research but were not created during or with a clear research intent should be considered software in research and not Research Software. This differentiation may vary between disciplines. The minimal requirement for achieving computational reproducibility is that all the computational components (Research Software, software used in research, documentation and hardware) used during the research are identified, described, and made accessible to the extent that is possible.


Others
====
:Description: any digital asset, uniquely identified, whose nature does not fall in the first three types




Properties
====
This section is to describe the metadata fields for the Research Products



Local Identifier
----
:Description: Unique code identifiying the Produc in the SKG (if any, otherwise "stateless identifier")
:Type: String
:Use: mandatory (1)
:Representation: XML element ``localIdentifier``
:Example: 

.. code-block:: xml
   :linenos:

    <localIdentifier>50|doi_dedup___::80f29c8c8ba18c46c88a285b7e739dc3</localIdentifier>


Identifiers
----
:Description: Identifier for the resource outside of the SKG. 
:Type: Wrapper element
:Use: optional (0,.. n)
:Representation: XML element ``identifiers``

identifier
^^^^^^^^^^^

:Description: The external identifier 
:Type: string
:Use: mandatory (1)
:Representation: XML element ``identifier``


identifierValue
^^^^^^^^^

:Description: The scheme for the external identifier
:Type: string
:Use: mandatory (1)
:Representation: XML attribute ``IdentifierScheme``

:Example:

.. code-block:: xml
   :linenos:

    <identifiers>
        <identifier identifierScheme="doi">10....</identifier>
    </identifiers>

Title
----
:Description: The title of the research product
:Type: string
:Use: mandatory, possibly multiple (1..*)
:Representation: XML element ``title`` as a multilingual string

titleType
^^^^^^^^

:Description: The type of the title (main, subtitle)
:Type: string
:Use: mandatory, (1)
:Representation: XML attribute ``titleType`` 


titleLanguage
^^^^^^^^^^

:Description: The language of the title of the research product
:Type: string
:Use: mandatory, (1)
:Representation: XML attribute ``titleLanguage`` 


languageCode
^^^^^^^^^^
:Description: The code of the language of the title of the research product
:Type: string
:Use: mandatory, (1)
:Representation: XML attribute ``languageCode`` 


:Example:

.. code-block:: xml
   :linenos:

    <title titleType="main", titleLanguage="en" languageCode="ISO-2">On the.... </title>
       

Abstract
----
:Description: A description for the research product 
:Type: string
:Use: required, possibly multiple (0..*)
:Representation: XML element ``abstract`` 

abstractLanguage
^^^^^^^^^^^^^^
:Description: The language of the abstract of the research product
:Type: string
:Use: mandatory, (1)
:Representation: XML attribute ``abstractLanguage`` 


languageCode
^^^^^^^^^^^
:Description: The code of the language of the abstract of the research product
:Type: string
:Use: mandatory, (1)
:Representation: XML attribute ``languageCode`` 

.. code-block:: xml
   :linenos:

    <abstract abstractLanguage="en" languageCode="ISO-2">This dataset ...</abstract>


Dates
---
:Description: Relevant dates for the research product
:Type: wrapper element 
:Use: mandatory, possibly more than one (1..*)
:Representation: XML element ``dates``

Date
^^^^^^^^^^^^^
:Description: The relevant date for the research product 
:Type: string 
:Use: mandatory (1)
:Representation: XML element ``date``


Date Type
"""""""""""""
:Description: The type of the date (e.g. publishing, embargo...)
:Type: string
:Use: mandatory (1)
:Representation: XML attribute ``dateType


Date Format
"""""""""""""
:Description: The format of the relevant date 
:Type: string 
:Use: mandatory (1)
:Representation: XML attribute ``dateFormat``


:Example:

.. code-block:: xml
   :linenos:

    <dates>
        <date dateType="embargo" dateFormat="yyyy-MM-dd">2022-12-03</date> 
    </dates>


ResourceType
-----
:Description: The type of the research product. One among (literatur, researcData, researchSoftware, Other)
:Type: string
:Use: mandatory
:Representation: XML element ``resourceType``

ResourceTypeDescription
^^^^^^^^^^^^^^^
:Description: Free text describing the resource (i.e. journal-article, workflow, collection ....)
:Type: string 
:Use: required 
:Representation: XML attribute ``resourceTypeDescription``


:Example:

.. code-block:: xml
   :linenos:

    <resourceType resourceTypeGeneral="monograph">literature</resourceType>


Relationships
============

hasDeclaredAffiliation
----------------------

:Description: It is the affiliation of one of the people creating the research result. Reference to a pair <author, organization>, i.e. organization to which the author was affiliated when generating this product. For this relation the author is an entity in the SKG
:Source: research product 
:Target: (author, organization)


:Example:

.. code-block:: xml
   :linenos:

    <relation semantics="hasDeclaredAffiliation">
        <source type="researchProduct">resultId</source>
        <targets>
            <target type="author">authorId</target>
            <target type="organization">organizationId</target>
        </targets>
    </relation>


hasAuthorAffiliatedWith 
---------------------------
:Description: It is a relation between the result and the organization. We do not know who is the author involved
:Source: research product 
:Target: organization 
:Example:

.. code-block:: xml
   :linenos:

    <relation semantics="hasAuthorAffiliatedWith">
        <source type="researchProduct">resultId</source>
        <targets>
            <target type="organization">organizationId</target>
        </targets>
    </relation>

publishedIn
--------------

:Description: The research product publishing venue 
:Source: research product
:Target: venue 
:Example:

.. code-block:: xml
   :linenos:

    <relation semantics="publishedIn">
        <source type="researchProduct">resultId</source>
        <targets>
            <target type="venue">venueId</target>
        </targets>
    </relation>

fundedBy 
-------------

:Description: the funds thanks to which the product has been made
:Source: research product 
:Target: project, organization (funder) 
:Example:


.. code-block:: xml
   :linenos:

    <relation semantics="fundedBy">
        <source type="researchProduct">resultId</source>
        <targets>
            <target type="project">projectId</target>
            <target type="organization">organizationId</target> 
        </targets>
    </relation>



hasSubject
-----------

:Description: The topic this research product is related to 
:Source: research product 
:Target: Topic 
:Example:


.. code-block:: xml
   :linenos:

    <relation semantics="hasSubject">
        <source type="researchProduct">resultId</source>
        <targets>
            <target type="project">topicId</target>
        </targets>
    </relation>


relatedWithProduct 
-------------------

:Description: other product the research product is related with 
:Source: research product 
:Target: research product
:Note: the semantics should be one among a set of predifined values. Possible "imposed" semantics: DataCite semantics or Scholix semantics set
:Example:


.. code-block:: xml
   :linenos:

    <relation semantics="IsSupplementedBy">
        <source type="researchProduct">resultId</source>
        <targets>
            <target type="researchProduct">resultId</target>
        </targets>
    </relation>
