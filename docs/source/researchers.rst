.. _Researcher:

Researcher
############

TODO definition

Properties 
===========

Local Identifier
---------------
:Description: Unique code identifiying the Researcher in the SKG (if any, otherwise "stateless identifier")	
:Type: String
:Use: mandatory (1)
:Representation: XML element ``localIdentifier``
:Example: 

.. code-block:: xml
   :linenos:

    <localIdentifier>authorIdentifier</localIdentifier>

Identifiers
------------
:Description: External identifiers for the researcher 
:Type: Wrapping element 
:Use: Required (0..*)
:Representation: XML element ``identifiers``

Identifier 
^^^^^^^^^^^^
:Description: The value for the external identifier
:Type: String 
:Use: Mandatory (1)
:Representation: Xml element ``identifier``

Identifier Scheme
^^^^^^^^^^^^^^^^^^
:Description: The scheme for the identifier
:Type: String
:Use: Mandatory (1) (possible values ORCID, Viaf, create a controlled vocabulary?)
:Representation: XML attribute ``identifierScheme``

:Example:

.. code-block:: xml
   :linenos:

    <identifiers>
        <identifier identifierScheme="doi">10....</identifier>
    </identifiers>


Given name
---------
:Description: The given name of a person
:Type: String 
:Use: Required (1)
:Representation: XML element ``givenName``
:Example:

.. code-block:: xml
   :linenos:

    <giveName>John</giveName>


Family name
-------------
:Description: The family name of a person
:Type: String
:Use: Mandatory (1)
:Representation: XML element ``familyName``

.. code-block:: xml
   :linenos:

    <familyName>Doe</familyName>

Agent
------
:Description: The name of an agent which produced the (for example UNICEF)
:Type: String
:Use: Optional (0..1) 
:Representation: XML element ``agent``

.. code-block:: xml
   :linenos:

    <familyName>UNICEF</familyName>



Relationships
================

isAffiliatedWith
------------------
:Description: the affiliation of the researcher 
:Use: Optional (0..*)
:Source: researcher id 
:Target: affiliation 
:Example:


.. code-block:: xml
   :linenos:

    <relation semantics="isAffiliatedWith">
        <source type="researcher">researcherId</source>
        <target type="affiliation">affiliationId</target>
    </relation>


hasCollaboratedToProject
-----------------------
:Description: the projects the researcher has collaborated to
:Use: Optional(0..*)
:Source: researcher 
:Target: Project
:Example: 

.. code-block:: xml
   :linenos:

    <relation semantics="hasCollaboratedToProject">
        <source type="researcher">researcherId</source>
        <target type="project">projectId</target>
    </relation>