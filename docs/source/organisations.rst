.. _Organisation:

Organisations
#############
TODO Description

Properties
==========
This section is to describe the metadata fields for the **Organisations**.

Local identifier
----
:Description: Unique code identifiying the Organisation in the SKG (if any, otherwise "stateless identifier")
:Type: string 
:Use: 
 
.. code-block:: json
   :linenos:

    "local_identifier": "the_id"


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


Name
----
:Description: 
:Type: string
:Use: mandatory, (1)
 
.. code-block:: json
   :linenos:

    "name": "the name"


Short name
----
:Description: 
:Type: string
:Use: optional, (1..*)
 
.. code-block:: json
   :linenos:

    "short_name": "the short name"


Other names
----
:Description: 
:Type: List of strings
:Use: optional, (1..*)
 
.. code-block:: json
   :linenos:

    "other_names": ["foo", "bar"]


Website
----
:Description: 
:Type: URL
:Use: mandatory, (1)
 
.. code-block:: json
   :linenos:

    "website": "https://..."


Country
----
:Description: 
:Type: String (follow ISO??)
:Use: mandatory, (1)
 
.. code-block:: json
   :linenos:

    "country": "Italy"



Relationships
=============
- isBeneficiaryOfProject (to Project)