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
:Use: mandatory (1)
:Representation: XML element ``localIdentifier``
 

.. code-block:: xml
   :linenos:

    <localIdentifier>20|....</localIdentifier>


Role
----
:Description: Specific role of the :ref:`Person <Person>` in the organization
:Type: String (possibility: values from CRediT taxonomy)
:Use: Mandatory (1)
:Representation: XML element ``role``


.. code-block:: xml
   :linenos:

    <role>43ebbd94-98b4-42f1-866b-c930cef228ca</role>
    
Start Date
----
:Description: The date when the :ref:`Person <Person>` started to be affiliated with the organization
:Type: String
:Use: Required, (1)
:Representation: XML element ``startDate`` 

.. code-block:: xml
   :linenos:

    <startDate>2019-01-01</startDate>
       

End Date
----
:Description: The date when the :ref:`Person <Person>` was no more affiliated with the organization
:Type: String
:Use: Required, (1)
:Representation: XML element ``endDate`` 

.. code-block:: xml
   :linenos:

    <endDate>2019-01-01</endDate>


Relationships
============

relatedPerson
----------------------

:Description: It is the Person to whom this affiliation is related
:Use: Mandatory (1)
:Source: affiliation 
:Target: person

.. code-block:: xml
   :linenos:

    <relation semantics="relatedPerson">
        <source type="affiliation">affiliation_id</source>
        <target type=person>person_id</target>
    </relation>


relatedOrganization
----------------------

:Description: It is the organization to which this affiliation is related
:Use: Mandatory (1)
:Source: affiliation 
:Target: organization

.. code-block:: xml
   :linenos:

    <relation semantics="relatedOrganization">
        <source type="affiliation">affiliationId</source>
        <target type=organization>organizationId</target>
    </relation>
