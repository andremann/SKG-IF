.. _Data source:

Data sources
############
A :ref:`Data source <Data source>` is a service where published material (metadata and files) are stored, preserved, and made discoverable and accessible. 
A data source is described by the `EOSC Profile for data sources <https://wiki.eoscfuture.eu/display/PUBLIC/D.+v4.00+EOSC+Data+Source+Profile>`_.

:Example: `Episciences <https://episciences.org>`_  is an overlay platform supporting the management of open-access journals on top of the Open Access repository `HAL <https://hal.science>`_. In this context, episciences.org is a publishing :ref:`Venue <Venue>` (journal, open access, open peer review), while HAL is a :ref:`Data source <Data source>`. Articles published via episciences.org will be therefore linked to the respective journal (publishing :ref:`Venue <Venue>`) and the data source HAL. 
    However, HAL is also a publishing :ref:`Venue <Venue>` for researchers that are directly uploading their :ref:`Research product <Research product>`. More specifically, a publishing :ref:`Venue <Venue>` with peer-review and some support for metadata curation. In this case, a :ref:`Research product <Research product>` will be linked to HAL both as a publishing :ref:`Venue <Venue>` and as a :ref:`Data source <Data source>`. 

.. note::
    Each :ref:`Research product <Research product>` must be associated with its publishing :ref:`Venue <Venue>` and its :ref:`Data source <Data source>`.


This section describes the metadata fields for a :ref:`Data source <Data source>`.


``local_identifier``		
----
*String* (mandatory): Unique code identifiying a :ref:`Data source <Data source>` in the SKG (if any, otherwise "stateless identifier").
 
.. code-block:: json
   :linenos:

    "local_identifier": "123"


``identifiers``
----
*List* (recommended):  A list of objects representing external identifiers for the entity. Each object is structured as follows.

* ``scheme`` *String* (mandatory): The scheme for the external identifier (e.g., a DOI).
* ``value`` *String* (mandatory): The external identifier.

.. code-block:: json
   :linenos:

    "identifiers": [
        {
            "scheme": "doi"
            "value": "https://doi.org/..."
        }
    ]


``name``
----
*String* (optional): Name of the :ref:`Data source <Data source>`.
 
.. code-block:: json
   :linenos:

    "name": "Zenodo"


``submission_policy_url``	
----
*String* (optional): This policy provides a comprehensive framework for the contribution of research products. Criteria for submitting content to the repository as well as product preparation guidelines can be stated. Concepts for quality assurance may be provided.
 
.. code-block:: json
   :linenos:

    "submission_policy_url": "https://..."


``preservation_policy_url``	
----
*String* (optional): This policy provides a comprehensive framework for the long-term preservation of the research products. Principles aims and responsibilities must be clarified. An important aspect is the description of preservation concepts to ensure the technical and conceptual utility of the content.
 
.. code-block:: json
   :linenos:

    "preservation_policy_url": "https://..."


``version_control``	
----
*Boolean* (optional): If data versioning is supported: the :ref:`Data source <Data source>` explicitly allows the deposition of different versions of the same object
 
.. code-block:: json
   :linenos:

    "version_control": True


``persistent_identity_systems``	
----
*List* (optional): The persistent identifier systems that are used by the :ref:`Data source <Data source>` to identify the ProductType it supports.


* ``product_type`` *String* (mandatory): The Product type to which the persistent identifier is referring to. Follows the EOSC vocabulary `Research Product Type <https://wiki.eoscfuture.eu/display/PUBLIC/D.+v4.00+EOSC+Data+Source+Profile#D.v4.00EOSCDataSourceProfile-ResearchProductType>`_.
* ``pid_schemes`` *List* (mandatory): the list of persistent identifier schemes used to refer to ProductTypes. Each elements must be drawn by the EOSC vocabulary `Persistent Identity Scheme <https://wiki.eoscfuture.eu/display/PUBLIC/D.+v4.00+EOSC+Data+Source+Profile#D.v4.00EOSCDataSourceProfile-PersistentIdentityScheme>`_.
 
.. code-block:: json
   :linenos:

    "persistent_identity_systems": [
        {
            "product_type": "Research Literature",
            "pid_schemes": ["DOI", "Handle"]
        }
    ]


``jurisdiction``	
----
*String* (optional): The property defines the jurisdiction of the users of the :ref:`Data source <Data source>`, based on the vocabulary `Jurisdiction <https://wiki.eoscfuture.eu/display/PUBLIC/D.+v4.00+EOSC+Data+Source+Profile#D.v4.00EOSCDataSourceProfile-Jurisdiction>`_.
 
.. code-block:: json
   :linenos:

    "jurisdiction": "National"


``data_source_classification``	
----
*String* (optional): The specific type of the :ref:`Data source <Data source>` based on the vocabulary `Data Source Classification <https://wiki.eoscfuture.eu/display/PUBLIC/D.+v4.00+EOSC+Data+Source+Profile#D.v4.00EOSCDataSourceProfile-DataSourceClassification>`_.
 
.. code-block:: json
   :linenos:

    "data_source_classification": "Journal Archive"


``research_product_type``	
----
*List* (optional): The types of OpenAIRE entities managed by the :ref:`Data source <Data source>`, based on the vocabulary `Research Product Type <https://wiki.eoscfuture.eu/display/PUBLIC/D.+v4.00+EOSC+Data+Source+Profile#D.v4.00EOSCDataSourceProfile-ResearchProductType>`_.
 
.. code-block:: json
   :linenos:

    "research_product_type": []


``thematic``	
----
*Boolean* (optional): Boolean value specifying if the :ref:`Data source <Data source>` is dedicated to a given discipline or is instead discipline agnostic.
 
.. code-block:: json
   :linenos:

    "thematic": False


``research_product_license``	
----
*List* (optional): Licenses under which the research products contained within the :ref:`Data source <Data source>` can be made available. Repositories can allow a license to be defined for each research product, while for scientific databases the database is typically provided under a single license. Each element in the list is structured as follows:
 
* ``Research Product License Name`` *String* (mandatory): 
* ``Research Product License URL`` *String* (mandatory): 
 
.. code-block:: json
   :linenos:

    "research_product_license": [
        {
            "name": "..."
            "url": "https://..."
        }
    ]


``research_product_access_policy``		
----
*List* (optional): List of terms following vocabulary: `COAR Access Rights 1.0 <https://vocabularies.coar-repositories.org/access_rights/>`_.
 
.. code-block:: json
   :linenos:

    "research_product_access_policy": ["open access"]


``research_product_metadata_license``	
----
*List* (optional): Metadata Policy for information describing items in the repository: Access and re-use of metadata. Each element has the following properties:

* ``name`` *String* (mandatory): 
* ``url`` *String* (mandatory): 
 
.. code-block:: json
   :linenos:

    "research_product_metadata_license": [
        {
            "name": "..."
            "url": "https://..."
        }
    ]


``research_product_metadata_access_policy``		
----
*List* (optional): List of terms following vocabulary: `COAR Access Rights 1.0 <https://vocabularies.coar-repositories.org/access_rights/>`_.
 
.. code-block:: json
   :linenos:

    "research_product_metadata_access_policy": ["open access"]


