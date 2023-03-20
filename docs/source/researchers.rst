.. _Researcher:

Researcher
############

This section is to describe the metadata fields for the **Researcher** entity.

Properties 
===========

Local Identifier
---------------
:Description: Unique code identifiying the Researcher in the SKG (if any, otherwise "stateless identifier")	
:Type: String
:Use: mandatory (1)
:Representation: XML element ``localIdentifier``
 

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
 
.. code-block:: xml
   :linenos:

    <relation semantics="hasCollaboratedToProject">
        <source type="researcher">researcherId</source>
        <target type="project">projectId</target>
    </relation>