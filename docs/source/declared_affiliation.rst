Authorship
####################

It is to model the contribution of a researcher in the creation of the research result. 
Each declared affiliation will have one link to the researcher contributing to the creation of the research result, and one link to the reserch result.
One link can also be made to refer to the organization the researcher related to the declared affiliation entity, declared to be affiliated to when contributing to create the research result.  

Properties
==========

Local Identifier
----
:Description: Unique code identifiying the Authorship in the SKG (if any, otherwise "stateless identifier")
:Type: String
:Use: mandatory (1)
:Representation: XML element ``localIdentifier``
:Example: 

.. code-block:: xml
   :linenos:

    <localIdentifier>20|....</localIdentifier>


Role
----
:Description: Specific role of the researcher in the organization
:Type: String (possibility: values from CRediT taxonomy)
:Use: Mandatory (1)
:Representation: XML element ``role``


:Example:

.. code-block:: xml
   :linenos:

    <role>43ebbd94-98b4-42f1-866b-c930cef228ca</role>
    
Start Date
----
:Description: The date when the researcher started to be affiliated with the organization
:Type: String
:Use: Required, (1)
:Representation: XML element ``startDate`` 

:Example:

.. code-block:: xml
   :linenos:

    <startDate>2019-01-01</startDate>
       

Start Date
----
:Description: The date when the researcher was no more affiliated with the organization
:Type: String
:Use: Required, (1)
:Representation: XML element ``endDate`` 

:Example:

.. code-block:: xml
   :linenos:

    <endDate>2019-01-01</endDate>


Relationships
============

relatedResearcher
----------------------

:Description: It is the researcher to whom this affiliation is related
:Use: Mandatory (1)
:Source: affiliation 
:Target: researcher


:Example:

.. code-block:: xml
   :linenos:

    <relation semantics="relatedResearcher">
        <source type="affiliation">affiliationId</source>
        <target type=researcher>researcherId</target>
    </relation>


relatedOrganization
----------------------

:Description: It is the organization to which this affiliation is related
:Use: Mandatory (1)
:Source: affiliation 
:Target: organization


:Example:

.. code-block:: xml
   :linenos:

    <relation semantics="relatedOrganization">
        <source type="affiliation">affiliationId</source>
        <target type=organization>organizationId</target>
    </relation>