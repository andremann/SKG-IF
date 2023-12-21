.. _Topic:

Topics
######
A :ref:`Topic <Topic>` entity describes the scientific disciplines, the subjects and the keywords potentially relevant for a :ref:`Research product <Research product>`.


This section describes the metadata fields for a :ref:`Topic <Topic>`.


``local_identifier``		
----
*String* (mandatory): Unique code identifiying the :ref:`Topic <Topic>` in the SKG (if any, otherwise "stateless identifier").
 
.. code-block:: json
   :linenos:

    "local_identifier": "topic_1"


``identifiers``
----
*List* (optional):  A list objects representing of external identifiers for the entity. Each object is structured as follows.

* ``scheme`` *String* (mandatory): The scheme for the external identifier.
* ``value`` *String* (mandatory): The external identifier.

 
.. code-block:: json
   :linenos:

    "identifiers": [
        {
            "scheme": "Computer Science Ontology",
            "value": "https://cso.kmi.open.ac.uk/topics/semantic_web"
        },
        {
            "scheme": "dbpedia",
            "value": "https://dbpedia.org/page/Semantic_Web"
        }
    ]

``name``
----
*String* (mandatory): The display name of the :ref:`Topic <Topic>`.

.. code-block:: json
   :linenos:

    "name": "Semantic Web"