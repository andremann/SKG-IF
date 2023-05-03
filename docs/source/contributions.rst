.. _Contribution:

Contribution
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
:Use: mandatory (1)
:Representation: XML element ``localIdentifier``
 
.. code-block:: xml
   :linenos:

    <localIdentifier>20|....</localIdentifier>


Role
----
:Description: Specific role of the researcher 
:Type: String (possibility: values from CRediT taxonomy)
:Use: Mandatory (1)
:Representation: XML element ``role``

.. code-block:: xml
   :linenos:

    <role>43ebbd94-98b4-42f1-866b-c930cef228ca</role>
    

Rank
----
:Description: The rank of the author 
:Type: Integer
:Use: Optional (0..1)
:Representation: XML element ``rank`` 

.. code-block:: xml
   :linenos:

    <rank>1</rank>
       

Relationships
============

relatedProduct
----------------------
:Description: It is the product related to this contribution
:Use: Mandatory (1)
:Source: **Contribution** 
:Target: :ref:`Research product <Research product>`

.. code-block:: xml
   :linenos:

    <relation semantics="relatedProduct">
        <source type="contribution">contributionId</source>
        <target type=researchProduct>resultId</target>
    </relation>


relatedAuthor 
---------------------------
:Description: It is the researcher related to this contribution entity
:Use: Mandatory (1)
:Source: **Contribution** 
:Target: :ref:`Researcher <Researcher>`

.. code-block:: xml
   :linenos:

    <relation semantics="relatedAuthor">
        <source type="contribution">contributionId</source>
        <target type="researcher">researcherId</target>
    </relation>


relatedAuthorAffiliation
--------------
:Description: The affiliation of the researched related to the contribution entity
:Use: Optional (0..*)
:Source: **Contribution**  
:Target: :ref:`Organization <Organization>`

.. code-block:: xml
   :linenos:

    <relation semantics="relatedAuthorAffiliation">
        <source type="contribution">contributionId</source>
        <target type="organization">organizationId</target>
    </relation>
