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
:Type: String 
:Use: 
 
.. code-block:: json
   :linenos:

    "local_identifier": "the_id"


Identifiers			
----
:Description: Alternative identifiers.
:Type: List
:Use: Optional, (1..*)

Identifier scheme
^^^^^^^^^^^
:Description: The scheme for the external identifier.
:Type: String
:Use: Mandatory (1)

Identifier value
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


Name
----
:Description: 
:Type: String
:Use: Mandatory, (1)
 
.. code-block:: json
   :linenos:

    "name": "the name"


Short name
----
:Description: 
:Type: String
:Use: Optional, (1..*)
 
.. code-block:: json
   :linenos:

    "short_name": "the short name"


Other names
----
:Description: 
:Type: List of strings
:Use: Optional, (1..*)
 
.. code-block:: json
   :linenos:

    "other_names": ["foo", "bar"]


Website
----
:Description: 
:Type: URL
:Use: Mandatory, (1)
 
.. code-block:: json
   :linenos:

    "website": "https://..."


Country
----
:Description: 
:Type: String (follow ISO??)
:Use: Mandatory, (1)
 
.. code-block:: json
   :linenos:

    "country": "Italy"



Relationships
=============
- isBeneficiaryOfGrant (to Grant)