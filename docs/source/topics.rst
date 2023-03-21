.. _Topic:

Topics
######
This section is to describe the metadata fields for the research **Topic** entity.


Properties
==========
This section is to describe the metadata fields for the Topics.


Local identifier		
----
:Description: Unique code identifiying the **Topic** in the SKG (if any, otherwise "stateless identifier").
:Type: String
:Use: mandatory, (1)
 
.. code-block:: json
   :linenos:

    "local_id": "123_local_id"


Identifiers			
----
:Description: Alternative identifiers.
:Type: list
:Use: optional, (1..*)

Identifier scheme
^^^^^^^^^^^
:Description: The scheme for the external identifier.
:Type: String
:Use: mandatory (1)

Identifier value
^^^^^^^^^
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


Provenance
----
:Description: 
:Type: Wrapper element
:Use: 
 
Provenance type
^^^^^^^^^
:Description: 
:Type: 
:Use: 
 
Trust
^^^^^^^^^
:Description: 
:Type: 
:Use: 
 
.. code-block:: json
   :linenos:

    "provenance": {
        "type": "OpenAIRE",
        "trust": 0.9
        }



Relationships
=============
TODO