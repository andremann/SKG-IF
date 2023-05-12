.. _Person:

Persons
############

The **Person** entity is to represent as an individual who is involved in the creation, publication, and dissemination of academic research. 
A **Person** can be an author, a reviewer, an editor, a publisher, a researcher, or any other stakeholder in the scholarly 
communication process. 

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
:Description: The identifier of the **Organization** the **Person** is affiliated with. 
:Type: String
:Use: Mandatory (1)

Start date
^^^^^^^^^
:Description: The start date of the affiliation with the **Organization**.
:Type: String (ISO 8601 date string)
:Use: Recommended (1)

End date
^^^^^^^^^
:Description: The end day (if any) of the affiliation with the **Organization**.
:Type: String (ISO 8601 date string)
:Use: Optional (1)

.. code-block:: json
   :linenos:

    "affiliations": [
        {
            "organisation": "org2",
            start_date: "2015-01-01",
            end_date: "2017-01-01"
        },
        {
            "organisation": "org3",
            start_date: "2017-01-01",
            end_date: "2019-01-01"
        }
    ]