.. _Organisation:

Organisations
#############
TODO Description

Properties
==========
This section is to describe the metadata fields for the **Organisations**.

Local identifier
----
:Description: Unique code identifiying the Organisation in the OSG (if any, otherwise "stateless identifier")
:Type: string 
:Use: 
:Representation: XML element ``localIdentifier``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Identifier
----
:Description: Persistent identifiers for the organization
:Type: string
:Use: recommended, (1..*)
:Representation: XML element ``identifier``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Identifier scheme
^^^^^^^^
:Description: 
:Type: string
:Use: mandatory
:Representation: XML element ``identifierScheme``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Identifier value
^^^^^^^^
:Description: 
:Type: string
:Use: mandatory
:Representation: XML element ``identifierValue``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Name
----
:Description: 
:Type: string
:Use: mandatory, (1)
:Representation: XML element ``name``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Short name
----
:Description: 
:Type: string
:Use: optional, (1..*)
:Representation: XML element ``shortName``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Other names
----
:Description: 
:Type: string
:Use: optional, (1..*)
:Representation: XML element ``otherNames``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Website
----
:Description: 
:Type: string
:Use: mandatory, (1)
:Representation: XML element ``website``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Country
----
:Description: 
:Type: string
:Use: mandatory, (1)
:Representation: XML element ``country``
 
.. code-block:: xml
   :linenos:

    <tag>...</tag>



Relationships
=============
- isBeneficiaryOfProject (to Project)