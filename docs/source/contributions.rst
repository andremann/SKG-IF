.. _Contribution:

Contributions
####################

It is to model the contribution of a :ref:`Person <Person>` in the creation of the :ref:`Research product <Research product>`. 
Each **Contribution** will have one link to the :ref:`Person <Person>` contributing to the creation of the :ref:`Research product <Research product>`, and one link to the :ref:`Research product <Research product>`.
One link can also be made to refer to the :ref:`Organisation <Organisation>` the :ref:`Person <Person>` related to the Contribution entity, declared to be affiliated to when contributing to create the :ref:`Research product <Research product>`.  

Properties
==========

Local Identifier
----
:Description: Unique code identifiying the Contribution in the SKG (if any, otherwise "stateless identifier")
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "local_id": "the_id"


Roles
----
:Description: Specific role of a :ref:`Person <Person>` for the **Contribution**
:Type: List of values from CRediT taxonomy
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "roles": ["writing-original-draft", "supervision"]
    

Rank
----
:Description: The rank of the person (as an author) 
:Type: Integer
:Use: Recommended (0..1)

.. code-block:: json
   :linenos:

    "rank": 1
       

Relationships
============

related_person 
---------------------------
:Description: It is the :ref:`Person <Person>` related to this contribution entity
:Use: Mandatory (1)
:Source: Contribution
:Target: :ref:`Person <Person>`

.. code-block:: json
   :linenos:

   {
   
   }


related_product
----------------------
:Description: It is the product related to this contribution
:Use: Optional (0..1)
:Source type: Contribution
:Target type: :ref:`Research product <Research product>`

.. code-block:: json
   :linenos:

    {

    }


related_venue
----------------------
:Description: 
:Use: Optional (0..1)
:Source type: Contribution
:Target type: Venue

.. code-block:: json
   :linenos:

    {

    }


related_grant
--------------
:Description: The affiliation of the :ref:`Person <Person>` related to the contribution entity
:Use: Optional (0..1)
:Source: Contribution  
:Target: :ref:`Organization <Organization>`

.. code-block:: json
   :linenos:

    {
    
    }


related_person_affiliation
--------------
:Description: The affiliation of the :ref:`Person <Person>` related to the contribution entity
:Use: Optional (0..*)
:Source: Contribution  
:Target: :ref:`Organization <Organization>`

.. code-block:: json
   :linenos:

    {
    
    }
