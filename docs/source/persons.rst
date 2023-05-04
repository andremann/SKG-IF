.. _Person:

Persons
############

This section is to describe the metadata fields for the **Person** entity.

Properties 
===========


Local identifier
----
:Description: Unique code identifiying the **Person** in the SKG (if any, otherwise "stateless identifier").
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "local_identifier": "the_id"


Identifiers
----
:Description: Identifier for the resource outside of the SKG. 
:Type: List
:Use: Recommended (1)

Scheme
^^^^^^^^^
:Description: The scheme for the external identifier.
:Type: String
:Use: Mandatory (1)

Value
^^^^^^^^^^^
:Description: The external identifier.
:Type: String
:Use: Mandatory (1)

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
:Description: The given name of a person.
:Type: String 
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "given_name": "John"


Family name
-------------
:Description: The family name of a person.
:Type: String
:Use: Mandatory (1)


.. code-block:: json
   :linenos:

    "family_name": "Doe"


Agent
------
:Description: The name of an agent (e.g., a collactive name or a legal entity).
:Type: String
:Use: Optional (0..1)

.. code-block:: json
   :linenos:

    "agent": "UNICEF"



Relationships
================

is_affiliated_with
------------------
:Description: 
:Use: Optional (0..*)
:Source type: Person
:Target type: Affiliation 

.. code-block:: json
   :linenos:

    {
    "semantics"="is_affiliated_with"
    "source" = "person_id",
    "target" = "affiliation_id"
    }


has_contribution
-----------------------
:Description: 
:Use: Optional(0..*)
:Source type: Person 
:Target type: Contribution
 
.. code-block:: json
   :linenos:

    {
    "semantics"="has_contribution"
    "source" = "person_id",
    "target" = "contribution_id"
    }