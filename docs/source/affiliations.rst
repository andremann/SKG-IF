.. _ Affiliation:

Affiliation
####################

An **Affiliation** entity models the affiliation(s) of a :ref:`Person <Person>` to research :ref:`Organisation <Organisation>` during his/her working life time.

Properties
==========

Local Identifier
----
:Description: Unique code identifiying the DeclaredAffiliation in the SKG (if any, otherwise "stateless identifier")
:Type: String
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "local_id": "the_id"


Role
----
:Description: Specific role of the :ref:`Person <Person>` in the organization
:Type: String (possibility: values from CRediT taxonomy)
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "role": "researcher"

    
Start Date
----
:Description: The date when the :ref:`Person <Person>` started to be affiliated with the organization
:Type: String
:Use: Required, (1)

.. code-block:: json
   :linenos:

    "name": ""
       

End Date
----
:Description: The date when the :ref:`Person <Person>` was no more affiliated with the organization
:Type: String
:Use: Required, (1)

.. code-block:: json
   :linenos:

    "name": ""


Relationships
============

relatedPerson
----------------------

:Description: It is the Person to whom this affiliation is related
:Use: Mandatory (1)
:Source: affiliation 
:Target: person

.. code-block:: json
   :linenos:

    "name": ""


relatedOrganization
----------------------

:Description: It is the organization to which this affiliation is related
:Use: Mandatory (1)
:Source: affiliation 
:Target: organization

.. code-block:: json
   :linenos:

    "name": ""
