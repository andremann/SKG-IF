.. _Topic:

Topics
######
A :ref:`Topic <Topic>` entity describes the scientific disciplines, the subjects and the keywords potentially relevant for a :ref:`Research product <Research product>`.


Properties
==========
This section describes the metadata fields for a :ref:`Topic <Topic>`.


Local identifier		
----
:Description: Unique code identifiying the :ref:`Topic <Topic>` in the SKG (if any, otherwise "stateless identifier").
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "local_identifier": "topic_1"


Identifiers			
----
:Description: Identifier for the entity outside of the SKG (e.g., PID, pURL). 
:Type: List
:Use: Optional, (0..1)

Scheme
^^^^^^^^^^^
:Description: The scheme for the external identifier.
:Type: String
:Use: Mandatory (1)

Value
^^^^^^^^^
:Description: The external identifier.
:Type: String
:Use: Mandatory (1)

 
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

Name
----
:Description: The display name of the :ref:`Topic <Topic>`.
:Type: String
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "name": "Semantic Web"