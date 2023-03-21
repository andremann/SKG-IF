.. _Researcher:

Researcher
############

This section is to describe the metadata fields for the **Researcher** entity.

Properties 
===========


Local identifier
----
:Description: Unique code identifiying the **Project** in the OSG (if any, otherwise "stateless identifier").
:Type: 
:Use: 
 
.. code-block:: json
   :linenos:

    "local_identifier": "the_id"


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


Given name
---------
:Description: The given name of a person
:Type: String 
:Use: Required (1)

.. code-block:: json
   :linenos:

    "given_name": "Andrea"


Family name
-------------
:Description: The family name of a person
:Type: String
:Use: Mandatory (1)


.. code-block:: json
   :linenos:

    "family_name": "Mannocci"


Agent
------
:Description: The name of an agent (e.g., a collactive name or a legal entity) that authored the product.
:Type: String
:Use: Optional (0..1) 

.. code-block:: json
   :linenos:

    "agent": "UNICEF"



Relationships
================

isAffiliatedWith
------------------
:Description: the affiliation of the researcher 
:Use: Optional (0..*)
:Source: researcher id 
:Target: affiliation 

.. code-block:: json
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
 
.. code-block:: json
   :linenos:

    <relation semantics="hasCollaboratedToProject">
        <source type="researcher">researcherId</source>
        <target type="project">projectId</target>
    </relation>