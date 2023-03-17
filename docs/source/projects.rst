Projects
########
TODO Description

Properties
==========
This section is to describe the metadata fields for the **Projects**.

Local identifier
----
:Description: Unique code identifiying the **Project** in the OSG (if any, otherwise "stateless identifier").
:Type: 
:Use: 
:Representation: XML element ``localIdentifier``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Identifiers
----
:Description: Alternative identifiers
:Type: Wrapper element
:Use: recommended, (0..*)
:Representation: XML element ``identifiers``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Identifier scheme
^^^^^^^^
:Description: The scheme for the external identifier.
:Type: String
:Use: mandatory, (1)
:Representation: XML element ``identifierScheme``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Identifier value
^^^^^^^^
:Description: The scheme for the external identifier.
:Type: String
:Use: mandatory, (1)
:Representation: XML element ``identifierValue``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Title
----
:Description: Title of the project.
:Type: String
:Use: mandatory, (1)
:Representation: XML element ``title``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Abstract
----
:Description: Abstract of the project.
:Type: String
:Use: recommended, (1)
:Representation: XML element ``abstract``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Acronym
----
:Description: Project acronym.
:Type: String
:Use: optional, (1)
:Representation: XML element ``acronym``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Funding
----
:Description: Project funding information.
:Type: 
:Use: 
:Representation: XML element ``funding``

Funder
^^^^^^
:Description: Project funder.
:Type: 
:Use: 
:Representation: XML element ``funder``

Funding scheme
^^^^^^
:Description: Project funding scheme.
:Type: 
:Use: 
:Representation: XML element ``fundingScheme``

Currency
^^^^^^
:Description: Currency of the funded amount.
:Type: 
:Use: 
:Representation: XML element ``currency``

Funded amount
^^^^^^
:Description: Amount funded for the project.
:Type: 
:Use: 
:Representation: XML element ``fundedAmount``

:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>



Keywords
----
:Description: Project keywords.
:Type: 
:Use: 
:Representation: XML element ``keywords``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Start date
----
:Description: 
:Type: Date
:Use: recommended, (0..1)
:Representation: XML element ``startDate``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


End date
----
:Description: 
:Type: Date
:Use: recommended, (0..1)
:Representation: XML element ``endDate``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Website
----
:Description: Project website.
:Type: URL
:Use: recommended, (0..1)
:Representation: XML element ``website``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>



Relationships
=============
- toResearchProduct
- to organization
- hasSubject (to Topic)