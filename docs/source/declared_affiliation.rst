Authorship
####################

It is to model the contribution of a researcher in the creation of the research result. 
Each declared affiliation will have one link to the researcher contributing to the creation of the research result, and one link to the reserch result.
One link can also be made to refer to the organization the researcher related to the declared affiliation entity, declared to be affiliated to when contributing to create the research result.  

Properties
==========

Local Identifier
----
:Description: Unique code identifiying the DeclaredAffiliation in the SKG (if any, otherwise "stateless identifier")
:Type: String
:Use: mandatory (1)
:Representation: XML element ``localIdentifier``
:Example: 

.. code-block:: xml
   :linenos:

    <localIdentifier>20|....</localIdentifier>


Role
----
:Description: Specific role of the researcher 
:Type: String (possibility: values from CRediT taxonomy)
:Use: Mandatory (1)
:Representation: XML element ``role``


:Example:

.. code-block:: xml
   :linenos:

    <role>43ebbd94-98b4-42f1-866b-c930cef228ca</role>
    
Rank
----
:Description: The rank of the author 
:Type: Integer
:Use: Optiona, (0..1)
:Representation: XML element ``rank`` 

:Example:

.. code-block:: xml
   :linenos:

    <rank>1</rank>
       




Relationships
============

relatedProduct
----------------------

:Description: It is the product related to this declared affiliation
:Use: Mandatory (1)
:Source: declaredAffiliation 
:Target: research product 


:Example:

.. code-block:: xml
   :linenos:

    <relation semantics="relatedProduct">
        <source type="declaredAffiliation">declaredAffiliationId</source>
        <target type=researchProduct>resultId</target>
    </relation>


relatedAuthor 
---------------------------
:Description: It is the researcher related to this declaredAffiliation entity
:Use: Mandatory (1)
:Source: declared affiliation 
:Target: research result 
:Example:

.. code-block:: xml
   :linenos:

    <relation semantics="relatedAuthor">
        <source type="declaredAffiliation">declaredAffiliationId</source>
        <target type="researchProduct">resultId</target>
    </relation>

relatedAuthorAffiliation
--------------
:Description: The affiliation of the researched related to the declaredAffiliation entity
:Use: Optional (0..*)
:Source: declaredAffiliation 
:Target: Organization
:Example:

.. code-block:: xml
   :linenos:

    <relation semantics="relatedAuthorAffiliation">
        <source type="declaredAffiliation">declaredAffiliationId</source>
        <target type="organization">organizationId</target>
    </relation>

