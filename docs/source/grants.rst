.. _Grant:

Grants
########
The entity :ref:`Grant <Grant>` it to describe funding awarded to an individual or an organization 
by a funding body. These bodies, both public and private, can be funders, foundations, governments, agencies or institutions. 


Properties
==========


Local identifier
----
:Description: Unique code identifiying the :ref:`Grant <Grant>` in the SKG (if any, otherwise "stateless identifier").
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "local_identifier": "the_id"


Identifiers			
----
:Description: Identifier for the entity outside of the SKG (e.g., PID). 
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


Title
----
:Description: Title of the grant.
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "title": "the title"


Abstract
----
:Description: Abstract of the grant.
:Type: String
:Use: Recommended (1)
 
.. code-block:: json
   :linenos:

    "abstract": "..."


Acronym
----
:Description: Grant acronym.
:Type: String
:Use: Optional (1)
 
.. code-block:: json
   :linenos:

    "acronym": "GraspOS"


Funder
------
:Description: Grant funder.
:Type: String
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "funder": ""


Funding stream
------
:Description: Grant funding stream.
:Type: String
:Use: Optional (0..1)

.. code-block:: json
   :linenos:

    "funding_stream": ""


Currency
------
:Description: Currency of the funded amount.
:Type: String
:Use: Optional (0..1), Mandatory if funded amount is given
.. code-block:: json
   :linenos:

    "currency": ""


Funded amount
------
:Description: Amount funded for the grant.
:Type: Number
:Use: Optional (0..1)

 
.. code-block:: json
   :linenos:

    "funded_amount": 1.000.000


Keywords
----
:Description: Grant keywords.
:Type: List
:Use: Optional (0..1)
 
.. code-block:: json
   :linenos:

    "keywords": ["key1", "key2", "key3", "key4", "key5"]


Start date
----
:Description: The date the grand started 
:Type: String (ISO 8601 date string)
:Use: Recommended (0..1)

.. code-block:: json
   :linenos:

    "start_date": "2019-09-13"


End date
----
:Description: The date the grant finishes
:Type: String (ISO 8601 date string)
:Use: Recommended, (0..1)
 
.. code-block:: json
   :linenos:

    "start_date": "2022-12-03"


Website
----
:Description: Grant website.
:Type: URL
:Use: Recommended (0..1)
 
.. code-block:: json
   :linenos:

    "website": "https://..."


Beneficiaries
----
:Description: A list of the :ref:`Organisation` funded by the :ref:`Grant <Grant>`.
:Type: List
:Use: Recommended (0..1)
 
.. code-block:: json
   :linenos:

    "beneficiaries": ["org_2", "org_5"]


Contributors
----
:Description: A list of the :ref:`Person` contributing to the :ref:`Grant <Grant>`.
:Type: List
:Use: Recommended (0..1)
 
 Person
 ^^^^^^^^^^^
:Description: The identifier of the :ref:`Person` who is the principal investigator  
:Type: 
:Use: 

 Organisation
 ^^^^^^^^^^^
:Description: The identifier of the :ref:`Organization` the principal investigator declares as affiliation for the :ref:`Grant <Grant>`
:Type: 
:Use: 

 Roles
 ^^^^^^^^^^^
:Description: A list of the roles that the :ref:`Person` has in the :ref:`Grant <Grant>`.
:Type: List of roles.
:Use: Recommended (1)

.. code-block:: json
   :linenos:

    "contributors": [
        {
            "person": "person_2",
            "organisation": "org_3",
            "roles": ["principal investigator"]
        }
    ]