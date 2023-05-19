.. _Grant:

Grants
########
The entity :ref:`Grant <Grant>` describes funding awarded to a :ref:`Person <Person>` or an :ref:`Organisation <Organisation>` 
by a funding body. These bodies, both public and private, can be funders, foundations, governments, agencies or institutions. 


Properties
==========


Local identifier
----
:Description: Unique code identifiying the :ref:`Grant <Grant>` in the SKG (if any, otherwise "stateless identifier").
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "local_identifier": "the_id"


Identifiers			
----
:Description: Identifier for the entity outside of the SKG (e.g., PID). 
:Type: List
:Use: Recommended (1)

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
            "scheme": "cordis"
            "value": "101095129"
        }
    ]


Title
----
:Description: Title of the :ref:`Grant <Grant>`.
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "title": "GraspOS: next Generation Research Assessment to Promote Open Science"


Abstract
----
:Description: The abstract or a description of the :ref:`Grant <Grant>`.
:Type: String
:Use: Recommended (1)
 
.. code-block:: json
   :linenos:

    "abstract": "GraspOS aims to build and operate a data infrastructure to support the policy reforms and pave the way towards a responsible research assessment system that embeds OS practices and accelerates its adoption in Europe. GraspOS will focus on extending the EOSC ecosystem with tools and services that will facilitate monitoring the use and uptake of various types of research services and outputs (publications, datasets, software) and will catalyse the implementation of policy-level rewards to foster OS practices. These tools and services will build upon multiple sources of metric data (e.g. OpenCitations, Scholexplorer) including capabilities offered by the EOSC Core, that will be federated in the context of the project, and will take into consideration both contemporary guidelines for Responsible Research Assessment (RRA), like those provided by initiatives like DORA and the Leiden Manifesto, and the suggestions from a diversity of relevant stakeholders. GraspOS will also incorporate piloting activities to co-design, showcase, validate, and evaluate GraspOS’s key results considering domain-specific aspects and different levels of OS-aware RRA, such as the researcher (individual/group), institution, and national level."


Acronym
----
:Description: The acronym of the :ref:`Grant <Grant>`.
:Type: String
:Use: Optional (1)
 
.. code-block:: json
   :linenos:

    "acronym": "GraspOS"


Funder
------
:Description: The name of the body funding the :ref:`Grant <Grant>`.
:Type: String
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "funder": "EC"


Funding stream
------
:Description: The funding stream of the :ref:`Grant <Grant>`.
:Type: String
:Use: Optional (0..1)

.. code-block:: json
   :linenos:

    "funding_stream": "Horizon Europe"


Currency
------
:Description: Currency of the funded amount.
:Type: String (following `ISO 4217 <https://en.wikipedia.org/wiki/ISO_4217>`_ )
:Use: Optional (0..1), Mandatory if funded amount is given
.. code-block:: json
   :linenos:

    "currency": "EUR"


Funded amount
------
:Description: Amount funded for the :ref:`Grant <Grant>`.
:Type: Number
:Use: Optional (0..1)

 
.. code-block:: json
   :linenos:

    "funded_amount": 2.985.441


Keywords
----
:Description: A list of keywords for the :ref:`Grant <Grant>`.
:Type: List
:Use: Optional (0..1)
 
.. code-block:: json
   :linenos:

    "keywords": ["Open science", "mutual learning", "open research"]


Start date
----
:Description: The date the :ref:`Grant <Grant>` started.
:Type: String (`ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_  date string)
:Use: Recommended (0..1)

.. code-block:: json
   :linenos:

    "start_date": "2019-09-13"


End date
----
:Description: The date the :ref:`Grant <Grant>` finished.
:Type: String (`ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ date string)
:Use: Recommended, (0..1)
 
.. code-block:: json
   :linenos:

    "start_date": "2022-12-03"


Website
----
:Description: :ref:`Grant <Grant>` website.
:Type: URL
:Use: Recommended (0..1)
 
.. code-block:: json
   :linenos:

    "website": "https://graspos.eu"


Beneficiaries
----
:Description: A list of the :ref:`Organisation` identifiers funded by the :ref:`Grant <Grant>`.
:Type: List
:Use: Recommended (0..1)
 
.. code-block:: json
   :linenos:

    "beneficiaries": ["org_2", "org_5"]


Contributors
----
:Description: A list of the :ref:`Person` contributing to the :ref:`Grant <Grant>`.
:Type: List
:Use: Recommended (0..1)
 
 Person
 ^^^^^^^^^^^
:Description: The identifier of the :ref:`Person` who is the principal investigator  
:Type: 
:Use: 

 Organisation
 ^^^^^^^^^^^
:Description: The identifier of the :ref:`Organisation <Organisation>` the principal investigator has declared as affiliation for the :ref:`Grant <Grant>`.
:Type: 
:Use: 

 Roles
 ^^^^^^^^^^^
:Description: A list of the roles that the :ref:`Person` has in the :ref:`Grant <Grant>`.
:Type: List of roles.
:Use: Recommended (1)

.. code-block:: json
   :linenos:

    "contributors": [
        {
            "person": "person_2",
            "organisation": "org_3",
            "roles": ["principal investigator"]
        }
    ]