.. _Project:

Projects
########
This section is to describe the metadata fields for the **Project** entity.

Properties
==========
This section is to describe the metadata fields for the **Projects**.

Local identifier
----
:Description: Unique code identifiying the **Project** in the OSG (if any, otherwise "stateless identifier").
:Type: 
:Use: 
 
.. code-block:: json
   :linenos:

    "local_identifier": "the_id"


Identifiers			
----
:Description: Alternative identifiers.
:Type: list
:Use: optional, (1..*)

Identifier scheme
^^^^^^^^^^^
:Description: The scheme for the external identifier.
:Type: String
:Use: mandatory (1)

Identifier value
^^^^^^^^^
:Description: The external identifier.
:Type: String
:Use: mandatory (1)

 
.. code-block:: json
   :linenos:

    "identifiers": [
        {
            "scheme": "https://..."
            "value": "the_id"
        }
    ]


Title
----
:Description: Title of the project.
:Type: String
:Use: mandatory, (1)
 
.. code-block:: json
   :linenos:

    "title": "the title"


Abstract
----
:Description: Abstract of the project.
:Type: String
:Use: recommended, (1)
 
.. code-block:: json
   :linenos:

    "abstract": "..."


Acronym
----
:Description: Project acronym.
:Type: String
:Use: optional, (1)
 
.. code-block:: json
   :linenos:

    "acronym": "GraspOS"


Funding
----
:Description: Project funding information.
:Type: 
:Use: 

Funder
^^^^^^
:Description: Project funder.
:Type: 
:Use: 

Funding stream
^^^^^^
:Description: Project funding stream.
:Type: 
:Use: 

Currency
^^^^^^
:Description: Currency of the funded amount.
:Type: 
:Use: 

Funded amount
^^^^^^
:Description: Amount funded for the project.
:Type: 
:Use: 

 
.. code-block:: json
   :linenos:

    "funding": {
        "funder": "",
        "funding_stream": "",
        "currency": "",
        "funded_amount": ""
        }

    }


Keywords
----
:Description: Project keywords.
:Type: 
:Use: 
 
.. code-block:: json
   :linenos:

    "keywords": ["key1", "key2", "key3", "key4", "key5"]


Start date
----
:Description: 
:Type: Date
:Use: recommended, (0..1)
 
Date value
^^^^^^^^^^^^^
:Description: The relevant date for the research product.
:Type: String 
:Use: mandatory (1)

Date type
"""""""""""""
:Description: The type of the date (e.g. publishing, embargo...).
:Type: String
:Use: mandatory (1)

Date format
"""""""""""""
:Description: The format of the relevant date.
:Type: String 
:Use: mandatory (1)

.. code-block:: json
   :linenos:

    "start_date": [
        {
            "date_value": "2022-12-03",
            "date_type": "embargo",
            "date_format": "yyyy-MM-dd",
        }
    ]


End date
----
:Description: 
:Type: Date
:Use: recommended, (0..1)
 
Date value
^^^^^^^^^^^^^
:Description: The relevant date for the research product.
:Type: String 
:Use: mandatory (1)

Date type
"""""""""""""
:Description: The type of the date (e.g. publishing, embargo...).
:Type: String
:Use: mandatory (1)

Date format
"""""""""""""
:Description: The format of the relevant date.
:Type: String 
:Use: mandatory (1)

.. code-block:: json
   :linenos:

    "end_date": [
        {
            "date_value": "2022-12-03",
            "date_type": "embargo",
            "date_format": "yyyy-MM-dd",
        }
    ]


Website
----
:Description: Project website.
:Type: URL
:Use: recommended, (0..1)
 
.. code-block:: json
   :linenos:

    "website": "https://..."



Relationships
=============
- toResearchProduct
- to organization
- hasSubject (to Topic)