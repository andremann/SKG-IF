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
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "local_identifier": "the_id"


Identifiers			
----
:Description: Identifier for the entity outside of the SKG (e.g., ROR ID, ISNI). 
:Type: List
:Use: Recommended (1)

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


Name
----
:Description: 
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "name": "the name"


Short name
----
:Description: 
:Type: String
:Use: Optional (0..1)
 
.. code-block:: json
   :linenos:

    "short_name": "the short name"


Other names
----
:Description: 
:Type: List
:Use: Optional (1..*)
 
.. code-block:: json
   :linenos:

    "other_names": ["foo", "bar"]


Website
----
:Description: 
:Type: URL
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "website": "https://..."


Country code
----
:Description: 
:Type: String (follow ISO 3166-1 alpha-2)
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "country": "IT"


Organisation type
----
:Description: 
:Type: String, one of the following [Archive, Company, Education, Facility, Government, Healthcare, Nonprofit, Funder, Other]
:Use: Recommended (1)
 
.. code-block:: json
   :linenos:

    "type": "Education"


Relationships
=============
- isBeneficiaryOfGrant (to Grant)