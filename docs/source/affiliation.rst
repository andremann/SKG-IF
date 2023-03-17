Affiliation
####################

It is to model the affiliation of a researcher during their working life time. 

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

