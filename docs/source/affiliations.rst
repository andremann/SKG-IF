.. _ Affiliation:

Affiliations
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

    
Start Date
----
:Description: The date when the :ref:`Person <Person>` started to be affiliated with the :ref:`Organisation <Organisation>`.
:Type: String (ISO 8601 date string)
:Use: Recommended (1)

.. code-block:: json
   :linenos:

    "start_date": "2019-09-13"
       

End Date
----
:Description: The date when the :ref:`Person <Person>` was no more affiliated with the :ref:`Organisation <Organisation>`.
:Type: String (ISO 8601 date string)
:Use: Recommended (1)

.. code-block:: json
   :linenos:

    "end_date": "2022-12-03"


Relationships
============

related_person
----------------------

:Description: It is the :ref:`Person <Person>` to whom this affiliation is related
:Use: Mandatory (1)
:Source type: Affiliation
:Target type: :ref:`Person <Person>`

.. code-block:: json
   :linenos:

    {
        "semantics"="related_person"
        "source" = "affiliation_id",
        "target" = "person_id"
    }


related_organisation
----------------------

:Description: It is the :ref:`Organisation <Organisation>` to which this affiliation is related
:Use: Mandatory (1)
:Source type: Affiliation
:Target type: :ref:`Organisation <Organisation>`

.. code-block:: json
   :linenos:

    {
        "semantics"="related_organisation"
        "source" = "affiliation_id",
        "target" = "organisation_id"
    }
