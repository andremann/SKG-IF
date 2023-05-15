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
            "scheme": ""
            "value": ""
        }
    ]


Provenance
----
:Description: 
:Type: List
:Use: Recommended (0..1)
 
Type
^^^^^^^^^
:Description: 
:Type: String
:Use: Mandatory (1)
 
Trust
^^^^^^^^^
:Description: 
:Type: Number
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "provenance": [
        {
            "type": "OpenAIRE",
            "trust": 0.9
        }
    ]