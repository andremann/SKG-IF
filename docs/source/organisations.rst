.. _Organisation:

Organisations
#############
The entity :ref:`Organisation <Organisation>` represents academic institutions, research centers, funders, or any other institutions taking part to the research process.


Properties
==========

Local identifier
----
:Description: Unique code identifiying the :ref:`Organisation <Organisation>` in the SKG (if any, otherwise "stateless identifier")
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
            "scheme": "ROR"
            "value": "05kacka20"
        }
    ]


Name
----
:Description: The name of the :ref:`Organisation <Organisation>`
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "name": "Institute of Information Science and Technologies"


Short name
----
:Description: The short name/acronym for the :ref:`Organisation <Organisation>`
:Type: String
:Use: Optional (0..1)
 
.. code-block:: json
   :linenos:

    "short_name": "CNR-ISTI"


Other names
----
:Description: Other names, maybe in different languages, to identifie the :ref:`Organisation <Organisation>`
:Type: List
:Use: Optional (1..*)
 
.. code-block:: json
   :linenos:

    "other_names": ["ISTI", "ISTI-CNR"]


Website
----
:Description: The website URL for the :ref:`Organisation <Organisation>`
:Type: URL
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "website": "http://www.isti.cnr.it"


Country code
----
:Description: The country code of the :ref:`Organisation <Organisation>`
:Type: String (follow ISO 3166-1 alpha-2)
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "country": "IT"


Organisation type
----
:Description: The type of the :ref:`Organisation <Organisation>`
:Type: String, one of the following [Archive, Company, Education, Facility, Government, Healthcare, Nonprofit, Funder, Other]
:Use: Recommended (1)
 
.. code-block:: json
   :linenos:

    "type": "Education"