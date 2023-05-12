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
:Description: Identifier for the entity outside of the SKG (e.g., ORCiD ID). 
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
:Description: The given name of a **Person**.
:Type: String 
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "given_name": "John"


Family name
-------------
:Description: The family name of a **Person**.
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


Affiliations
------
:Description: A list of all the affiliations of a **Person**.
:Type: List
:Use: Optional (0..1)

Organisation
^^^^^^^^^
:Description: 
:Type: String
:Use: Mandatory (1)

Start date
^^^^^^^^^
:Description: 
:Type: 
:Use: Recommended (1)

End date
^^^^^^^^^
:Description: 
:Type: 
:Use: Optional (1)

.. code-block:: json
   :linenos:

    "affiliations": [
        {
            "organisation": "org2",
            start_date: "2015",
            end_date: "2017"
        },
        {
            "organisation": "org3",
            start_date: "2017",
            end_date: "2019"
        }
    ]


Contribution to venues
------
:Description: A list of all the contributions of a **Person** gives to a :ref:`Venue`.
:Type: List
:Use: Optional (0..1)

Venue
^^^^^^^^^
:Description: The id of a :ref:`Venue`.
:Type: 
:Use: Mandatory (1)

Roles
^^^^^^^^^
:Description: 
:Type: List of Strings representing the roles for the venue.
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

   "venues": [
        {
            "venue": "venue_3",
            "roles": ["editor"]
        }
   ]