.. _Person:

Persons
############

The :ref:`Person <Person>` entity represents an individual who is involved in the creation, publication, and dissemination of :ref:`Research products <Research product>`. 
A :ref:`Person <Person>` can be an author, a reviewer, an editor, a publisher, a researcher, or any other stakeholder involved in the scholarly communication process. 


This section describes the metadata fields for the :ref:`Person <Person>`.


``local_identifier``
----
*String* (mandatory): Unique code identifiying the :ref:`Person <Person>` in the SKG (if any, otherwise "stateless identifier").
 
.. code-block:: json
   :linenos:

    "local_identifier": "the_id"


``identifiers``
----
*List* (optional):  A list of objects representing external identifiers for the entity. Each object is structured as follows.

* ``scheme`` *String* (mandatory): The scheme for the external identifier (e.g., ORCID).
* ``value`` *String* (mandatory): The external identifier.

.. code-block:: json
   :linenos:

    "identifiers": [
        {
            "scheme": "orcid"
            "value": "000-0002-5193-7851"
        }
    ]


``given_name``
---------
*String* (mandatory, unless an ``agent`` or a ``fullname`` is indicated): The given name of a :ref:`Person <Person>`.

.. code-block:: json
   :linenos:

    "given_name": "John"


``family_name``
-------------
*String* (mandatory, unless an ``agent`` or a ``fullname`` is indicated): The family name of a :ref:`Person <Person>`.

.. code-block:: json
   :linenos:

    "family_name": "Doe"


``fullname``
---------
*String* (optional, unless ``given_name`` and ``family_name`` are not present, or an ``agent`` is not indicated): The string containing whatever concatenation of a :ref:`Person <Person>`'s name(s) and surnames(s).

.. code-block:: json
   :linenos:

    "fullname": "John M. Doe"


``agent``
------
*String* (optional, unless all name property are missing): The name of an agent (e.g., a collective name or a legal entity).

.. code-block:: json
   :linenos:

    "agent": "Data curation team"


``affiliations``
------
*List* (optional): A list of all the affiliations of a :ref:`Person <Person>` (*à la* ORCID). Each element of the list is structured as follows:

* ``organisation`` *String* (mandatory): The identifier of the :ref:`Organisation <Organisation>` a :ref:`Person <Person>` is affiliated with. 
* ``start_date`` *String* (recommended): The start date of the affiliation with the :ref:`Organisation <Organisation>`. It adheres to `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_.
* ``end_date`` *String* (optional): The end day (if any) of the affiliation with the :ref:`Organisation <Organisation>`. It adheres to `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_.

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