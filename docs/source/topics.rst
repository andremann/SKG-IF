Topics
######
TODO Description


Properties
==========
This section is to describe the metadata fields for the Topics.


Local identifier
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``localIdentifier``
:Example: 
.. code-block:: json
   :linenos:

    {id : '1234'}

Identifiers			
----
:Description: Alternative identifiers
:Type: Wrapper element
:Use: optional, (1..*)
:Representation: XML element ``identifiers``

Identifier scheme
^^^^^^^^^^^
:Description: The scheme for the external identifier
:Type: String
:Use: mandatory (1)
:Representation: XML element ``identifierScheme``

Identifier value
^^^^^^^^^
:Description: The external identifier 
:Type: String
:Use: mandatory (1)
:Representation: XML attribute ``identifierValue``

:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Provenance
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``provenance``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Provenance type
^^^^^^^^^
:Description: 
:Type: 
:Use: 
:Representation: XML element ``provenanceType``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Trust
^^^^^^^^^
:Description: 
:Type: 
:Use: 
:Representation: XML element ``trust``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>



Relationships
=============
TODO