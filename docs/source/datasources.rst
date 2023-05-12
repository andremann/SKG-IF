.. _Data source:

Data sources
############
A **Data source** is a service where published material (metadata and files) are stored, preserved, and made discoverable and accessible; a data source is described by the `EOSC Profile for data sources <https://wiki.eoscfuture.eu/display/PUBLIC/D.+v4.00+EOSC+Data+Source+Profile>`_.

Example:
`Episciences <https://episciences.org>`_  is an overlay platform supporting the management of open-access journals on top of the Open Access repository HAL.fr. In this context, episciences.org is a publishing venue (journal, open access, open peer review), while HAL is a data source. Articles published via episciences.org will be therefore linked to the respective journal (publishing venue) and the data source HAL. 
However, HAL is also a publishing venue for researchers that are directly uploading their products; a publishing venue with peer-review and some support for metadata curation. In this case, research products will be linked to HAL as a publishing venue and as a data source. 

.. note::
    Each :ref:`Research product <Research product>` must be associated with its publishing venue and its data source.


Properties
==========
This section is to describe the metadata fields for the Data sources.


Local identifier		
----
:Description: Unique code identifiying the Data source in the SKG (if any, otherwise "stateless identifier").
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "local_identifier": "123"


Identifiers			
----
:Description: Identifier for the entity outside of the SKG (e.g., PID). 
:Type: List
:Use: Optional, (0..1)

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


Name		
----
:Description: Name of the data source.
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "name": "Zenodo"


Submission policy URL	
----
:Description: EOSC Data Source Profile This policy provides a comprehensive framework for the contribution of research products. Criteria for submitting content to the repository as well as product preparation guidelines can be stated. Concepts for quality assurance may be provided.
:Type: URL
:Use: Recommended (0..1)
 
.. code-block:: json
   :linenos:

    "submission_policy_url": "https://..."


Preservation policy URL	
----
:Description: EOSC Data Source Profile This policy provides a comprehensive framework for the long-term preservation of the research products. Principles aims and responsibilities must be clarified. An important aspect is the description of preservation concepts to ensure the technical and conceptual utility of the content	
:Type: URL
:Use: Recommended (0..1)
 
.. code-block:: json
   :linenos:

    "preservation_policy_url": "https://..."


Version control	
----
:Description: EOSC Data Source Profile If data versioning is supported: the data source explicitly allows the deposition of different versions of the same object
:Type: Boolean
:Use: Optional (0..1)
 
.. code-block:: json
   :linenos:

    "version_control": true


Persistent Identity Systems	
----
:Description: EOSC Data Source Profile The persistent identifier systems that are used by the Data Source to identify the ProductType it supports.
:Type: List
:Use: Recommended (0..1)


Persistent Identity Product Type
^^^^^^^^^^^^^^
:Description: 	EOSC Data Source Profile Specify the ProductType to which the persistent identifier is referring to.
:Type: Vocabulary: `Research Product Type <https://wiki.eoscfuture.eu/display/PUBLIC/D.+v4.00+EOSC+Data+Source+Profile#D.v4.00EOSCDataSourceProfile-ResearchProductType>`_
:Use: Mandatory (1)


Persistent Identity Product Type Scheme	
^^^^^^^^^^^^^^^^
:Description: EOSC Data Source Profile Specify the list of persistent identifier schemes used to refer to ProductTypes
:Type: List of terms following the vocabulary: `Persistent Identity Scheme <https://wiki.eoscfuture.eu/display/PUBLIC/D.+v4.00+EOSC+Data+Source+Profile#D.v4.00EOSCDataSourceProfile-PersistentIdentityScheme>`_
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "persistent_identity_systems": [
        {
            "product_type": "Research Literature",
            "pid_scheme": ["DOI", "Handle"]
        }
    ]


Jurisdiction	
----
:Description: EOSC Data Source Profile The property defines the jurisdiction of the users of the data source, based on the vocabulary for this property	
:Type: Vocabulary: `Jurisdiction <https://wiki.eoscfuture.eu/display/PUBLIC/D.+v4.00+EOSC+Data+Source+Profile#D.v4.00EOSCDataSourceProfile-Jurisdiction>`_ 
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "jurisdiction": "National"


Data Source Classification	
----
:Description: EOSC Data Source Profile The specific type of the data source based on the vocabulary defined for this property.
:Type: Vocabulary: `Data Source Classification <https://wiki.eoscfuture.eu/display/PUBLIC/D.+v4.00+EOSC+Data+Source+Profile#D.v4.00EOSCDataSourceProfile-DataSourceClassification>`_
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "data_source_classification": "Journal Archive"


Research Product Types	
----
:Description: The types of OpenAIRE entities managed by the data source, based on the vocabulary for this property	
:Type: List of vocabulary terms: `Research Product Type <https://wiki.eoscfuture.eu/display/PUBLIC/D.+v4.00+EOSC+Data+Source+Profile#D.v4.00EOSCDataSourceProfile-ResearchProductType>`_
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "research_product_type": []


Thematic	
----
:Description: EOSC Data Source Profile Boolean value specifying if the data source is dedicated to a given discipline or is instead discipline agnostic	
:Type: Boolean
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "thematic": False


Research Product Licensing	
----
:Description: EOSC Data Source Profile Licenses under which the research products contained within the data sources can be made available. Repositories can allow a license to be defined for each research product, while for scientific databases the database is typically provided under a single license.	
:Type: List
:Use: Recommended, (0..1)
 

Research Product License Name		
^^^^^^^
:Description: 
:Type: String
:Use: Mandatory (1)
 

Research Product License URL
^^^^^^^^^
:Description: 
:Type: URL
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "research_product_license": [
        {
            "name": "..."
            "url": "https://..."
        }
    ]


Research Product Access Policy		
----
:Description: 
:Type: List of terms following vocabulary: `COAR Access Rights 1.0 <https://vocabularies.coar-repositories.org/access_rights/>`_
:Use: Recommended (0..1)
 
.. code-block:: json
   :linenos:

    "research_product_access_policy": ["open access"]


Research Product Metadata Licensing	
----
:Description: "EOSC Data Source Profile Metadata Policy for information describing items in the repository: Access and re-use of metadata"
:Type: List
:Use: Recommended (0..1)


Research Product Metadata License Name		
^^^^^^^^^^^^
:Description: 
:Type: String
:Use: Mandatory (1)


Research Product Metadata License URL
^^^^^^^^^^^^^^^^^^
:Description: 
:Type: URL
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "research_product_metadata_license": [
        {
            "name": "..."
            "url": "https://..."
        }
    ]


Research Product Metadata Access Policy		
----
:Description: 
:Type: List of terms following vocabulary: `COAR Access Rights 1.0 <https://vocabularies.coar-repositories.org/access_rights/>`_
:Use: Recommended (0..1)
 
.. code-block:: json
   :linenos:

    "research_product_metadata_access_policy": ["open access"]


