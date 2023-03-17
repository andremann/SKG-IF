Projects
########
TODO Description

Properties
==========
This section is to describe the metadata fields for the **Projects**.

Local identifier
----
:Description: Unique code identifiying the **Project** in the OSG (if any, otherwise "stateless identifier")
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
:Description: 
:Type: String
:Use: mandatory, (1)
:Representation: XML element ``identifierScheme``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Identifier value
^^^^^^^^
:Description: 
:Type: String
:Use: mandatory, (1)
:Representation: XML element ``identifierValue``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Title
----
:Description: 
:Type: String
:Use: mandatory, (1)
:Representation: XML element ``title``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Abstract
----
:Description: 
:Type: String
:Use: recommended, (1)
:Representation: XML element ``abstract``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Acronym
----
:Description: 
:Type: String
:Use: optional, (1)
:Representation: XML element ``acronym``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Funding
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``funding``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Money granted
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``moneyGranted``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Currency
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``currency``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Funded amount
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``fundedAmount``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Keywords
----
:Description: 
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
:Type: 
:Use: 
:Representation: XML element ``startDate``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

End date
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``endDate``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Website
----
:Description: 
:Type: 
:Use: 
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