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
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Identifiers
----
:Description: Alternative identifiers
:Type: Wrapper element
:Use: recommended, (0..*)
:Representation: XML element ``identifiers``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Identifier scheme
^^^^^^^^
:Description: The scheme for the external identifier.
:Type: String
:Use: mandatory, (1)
:Representation: XML element ``identifierScheme``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Identifier value
^^^^^^^^
:Description: The scheme for the external identifier.
:Type: String
:Use: mandatory, (1)
:Representation: XML element ``identifierValue``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Title
----
:Description: Title of the project.
:Type: String
:Use: mandatory, (1)
:Representation: XML element ``title``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Abstract
----
:Description: Abstract of the project.
:Type: String
:Use: recommended, (1)
:Representation: XML element ``abstract``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Acronym
----
:Description: Project acronym.
:Type: String
:Use: optional, (1)
:Representation: XML element ``acronym``
 
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

Funding stream
^^^^^^
:Description: Project funding stream.
:Type: 
:Use: 
:Representation: XML element ``fundingStram``

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

 
.. code-block:: xml
   :linenos:

    <tag>...</tag>



Keywords
----
:Description: Project keywords.
:Type: 
:Use: 
:Representation: XML element ``keywords``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Start date
----
:Description: 
:Type: Date
:Use: recommended, (0..1)
:Representation: XML element ``startDate``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


End date
----
:Description: 
:Type: Date
:Use: recommended, (0..1)
:Representation: XML element ``endDate``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Website
----
:Description: Project website.
:Type: URL
:Use: recommended, (0..1)
:Representation: XML element ``website``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>



Relationships
=============
- toResearchProduct
- to organization
- hasSubject (to Topic)