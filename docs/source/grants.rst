.. _Grant:

Grants
########
The entity :ref:`Grant <Grant>` describes funding awarded to a :ref:`Person <Person>` or an :ref:`Organisation <Organisation>` 
by a funding body. These bodies, both public and private, can be funders, foundations, governments, agencies or institutions. 



``local_identifier``
----
*String* (mandatory): Unique code identifiying the :ref:`Grant <Grant>` at the funder.
 
.. code-block:: json
   :linenos:

    "local_identifier": "101095129"


``identifiers``
----
*List* (optional):  A list of objects representing external identifiers for the entity. Each object is structured as follows.

* ``scheme`` *String* (mandatory): The scheme for the external identifier (e.g., DOI).
* ``value`` *String* (mandatory): The external identifier.

.. code-block:: json
   :linenos:

    "identifiers": [
        {
            "scheme": "doi"
            "value": "10.3030/101095129"
        }
    ]


``title``
----
*String* (mandatory): Title of the :ref:`Grant <Grant>`.
 
.. code-block:: json
   :linenos:

    "title": "GraspOS: next Generation Research Assessment to Promote Open Science"


``abstract``
----
*String* (recommended): The abstract or a description of the :ref:`Grant <Grant>`.
 
.. code-block:: json
   :linenos:

    "abstract": "GraspOS aims to build and operate a data infrastructure to support the policy reforms and pave the way towards a responsible research assessment system that embeds OS practices and accelerates its adoption in Europe. GraspOS will focus on extending the EOSC ecosystem with tools and services that will facilitate monitoring the use and uptake of various types of research services and outputs (publications, datasets, software) and will catalyse the implementation of policy-level rewards to foster OS practices. These tools and services will build upon multiple sources of metric data (e.g. OpenCitations, Scholexplorer) including capabilities offered by the EOSC Core, that will be federated in the context of the project, and will take into consideration both contemporary guidelines for Responsible Research Assessment (RRA), like those provided by initiatives like DORA and the Leiden Manifesto, and the suggestions from a diversity of relevant stakeholders. GraspOS will also incorporate piloting activities to co-design, showcase, validate, and evaluate GraspOS’s key results considering domain-specific aspects and different levels of OS-aware RRA, such as the researcher (individual/group), institution, and national level."


``acronym``
----
*String* (optional): The acronym of the :ref:`Grant <Grant>`.
 
.. code-block:: json
   :linenos:

    "acronym": "GraspOS"


``funder``
------
*String* (mandatory): The name of the body funding the :ref:`Grant <Grant>`.

.. code-block:: json
   :linenos:

    "funder": "EC"


``funding_stream``
------
*String* (optional): The funding stream of the :ref:`Grant <Grant>`.

.. code-block:: json
   :linenos:

    "funding_stream": "Horizon Europe"


``currency``
------
*String* (mandatory, if ``funded_amount`` is provided): Currency of the funded amount, following `ISO 4217 <https://en.wikipedia.org/wiki/ISO_4217>`_.

.. code-block:: 
    json
   :linenos:

    "currency": "EUR"


``funded_amount``
------
*Numeric* (optional): Amount funded for the :ref:`Grant <Grant>`.

 
.. code-block:: json
   :linenos:

    "funded_amount": 2.985.441


``keywords``
----
*List* (optional): A list of keywords for the :ref:`Grant <Grant>`.
 
.. code-block:: json
   :linenos:

    "keywords": ["Open science", "mutual learning", "open research"]


``start_date``
----
*String* (recommended): The date the :ref:`Grant <Grant>` started expressed as `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_.

.. code-block:: json
   :linenos:

    "start_date": "2019-09-13"


``end_date``
----
*String* (recommended): The date the :ref:`Grant <Grant>` finished expressed as `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_.
 
.. code-block:: json
   :linenos:

    "end_date": "2022-12-03"


``website``
----
*String* (recommended): An URL poiting to the website of the funded project.
 
.. code-block:: json
   :linenos:

    "website": "https://graspos.eu"


``beneficiaries``
----
*List* (recommended): A list of the :ref:`Organisation` identifiers funded by the :ref:`Grant <Grant>`.
 
.. code-block:: json
   :linenos:

    "beneficiaries": ["org_2", "org_5"]


``contributors``
----
*List* (recommended): A list of the :ref:`Person` contributing to the :ref:`Grant <Grant>`.
 
* ``person``: The identifier of the :ref:`Person` who is the principal investigator  
* ``organisation``: The identifier of the :ref:`Organisation <Organisation>` the principal investigator has declared as affiliation for the :ref:`Grant <Grant>`.
* ``poles`` *List* (recommended): A list of the roles that the :ref:`Person` has in the :ref:`Grant <Grant>`.

.. code-block:: json
   :linenos:

    "contributors": [
        {
            "person": "person_2",
            "organisation": "org_3",
            "roles": ["principal investigator"]
        }
    ]