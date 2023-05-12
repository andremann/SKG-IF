.. _Topic:

Topics
######
This section is to describe the metadata fields for the research **Topic** entity.


Properties
==========
This section is to describe the metadata fields for a **Topic**.


Local identifier		
----
:Description: Unique code identifiying the **Topic** in the SKG (if any, otherwise "stateless identifier").
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
            "scheme": "https://..."
            "value": "the_id"
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



Relationships
=============
TODO