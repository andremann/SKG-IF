.. _Person:

Persons
#######

The :ref:`Person <Person>` entity represents an individual who is involved in the creation, publication, and dissemination of :ref:`Research products <Research product>`. 
A :ref:`Person <Person>` can be an author, a reviewer, an editor, a publisher, a researcher, or any other stakeholder involved in the scholarly communication process. 


Properties 
==========
This section describes the metadata fields for the :ref:`Person <Person>`.


Local identifier
----------------
:Description: Unique code identifiying the :ref:`Person <Person>` in the SKG (if any, otherwise "stateless identifier").
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "local_identifier": "the_id"


Identifiers
-----------
:Description: Identifier for the entity outside of the SKG (e.g., ORCID). 
:Type: List
:Use: Recommended (1)

Scheme
^^^^^^
:Description: The scheme for the external identifier.
:Type: String
:Use: Mandatory (1)

Value
^^^^^
:Description: The external identifier.
:Type: String
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "identifiers": [
        {
            "scheme": "orcid"
            "value": "000-0002-5193-7851"
        }
    ]


Given name
----------
:Description: The given name of a :ref:`Person <Person>`.
:Type: String 
:Use: Mandatory (1), unless an agent is specified

.. code-block:: json
   :linenos:

    "given_name": "John"


Family name
-----------
:Description: The family name of a :ref:`Person <Person>`.
:Type: String
:Use: Mandatory (1), unless an agent is specified.


.. code-block:: json
   :linenos:

    "family_name": "Doe"


Agent
-----
:Description: The name of an agent (e.g., a collactive name or a legal entity).
:Type: String
:Use: Optional (0..1), unless given name and family name are not present.

.. code-block:: json
   :linenos:

    "agent": "Data curation team"


Affiliations
------------
:Description: A list of all the affiliations of a :ref:`Person <Person>` (*à la* ORCID).
:Type: List
:Use: Optional (0..1)

Organisation
^^^^^^^^^^^^
:Description: The identifier of the :ref:`Organisation <Organisation>` a :ref:`Person <Person>` is affiliated with. 
:Type: String
:Use: Mandatory (1)

Start date
^^^^^^^^^^
:Description: The start date of the affiliation with the :ref:`Organisation <Organisation>`.
:Type: String (`ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ date string)
:Use: Recommended (1)

End date
^^^^^^^^
:Description: The end day (if any) of the affiliation with the :ref:`Organisation <Organisation>`.
:Type: String (`ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ date string)
:Use: Optional (1)

.. code-block:: json
   :linenos:

    "affiliations": [
        {
            "organisation": "org2",
            "start_date": "2015-01-01",
            "end_date": "2017-01-01"
        },
        {
            "organisation": "org3",
            "start_date": "2017-01-01",
            "end_date": "2019-01-01"
        }
    ]