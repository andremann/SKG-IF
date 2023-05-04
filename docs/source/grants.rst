.. _Grant:

Grants
########
This section is to describe the metadata fields for the **Grant** entity.

Properties
==========
This section is to describe the metadata fields for the **Grant**.

Local identifier
----
:Description: Unique code identifiying the **Grant** in the SKG (if any, otherwise "stateless identifier").
:Type: 
:Use: 
 
.. code-block:: json
   :linenos:

    "local_identifier": "the_id"


Identifiers			
----
:Description: Alternative identifiers.
:Type: List
:Use: Optional, (1..*)

Identifier scheme
^^^^^^^^^^^
:Description: The scheme for the external identifier.
:Type: String
:Use: Mandatory (1)

Identifier value
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


Title
----
:Description: Title of the grant.
:Type: String
:Use: Mandatory, (1)
 
.. code-block:: json
   :linenos:

    "title": "the title"


Abstract
----
:Description: Abstract of the grant.
:Type: String
:Use: Recommended, (1)
 
.. code-block:: json
   :linenos:

    "abstract": "..."


Acronym
----
:Description: Grant acronym.
:Type: String
:Use: Optional, (1)
 
.. code-block:: json
   :linenos:

    "acronym": "GraspOS"


Funding
----
:Description: Grant funding information.
:Type: 
:Use: 

Funder
^^^^^^
:Description: Grant funder.
:Type: 
:Use: 

Funding stream
^^^^^^
:Description: Grant funding stream.
:Type: 
:Use: 

Currency
^^^^^^
:Description: Currency of the funded amount.
:Type: 
:Use: 

Funded amount
^^^^^^
:Description: Amount funded for the grant.
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
:Description: Grant keywords.
:Type: 
:Use: 
 
.. code-block:: json
   :linenos:

    "keywords": ["key1", "key2", "key3", "key4", "key5"]


Start date
----
:Description: 
:Type: Date
:Use: Recommended, (0..1)
 
Date value
^^^^^^^^^^^^^
:Description: The relevant date for the research product.
:Type: String 
:Use: Mandatory (1)

Date type
"""""""""""""
:Description: The type of the date (e.g. publishing, embargo...).
:Type: String
:Use: Mandatory (1)

Date format
"""""""""""""
:Description: The format of the relevant date.
:Type: String 
:Use: Mandatory (1)

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
:Use: Recommended, (0..1)
 
Date value
^^^^^^^^^^^^^
:Description: The relevant date for the research product.
:Type: String 
:Use: Mandatory (1)

Date type
"""""""""""""
:Description: The type of the date (e.g. publishing, embargo...).
:Type: String
:Use: Mandatory (1)

Date format
"""""""""""""
:Description: The format of the relevant date.
:Type: String 
:Use: Mandatory (1)

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
:Description: Grant website.
:Type: URL
:Use: Recommended, (0..1)
 
.. code-block:: json
   :linenos:

    "website": "https://..."



Relationships
=============
- toResearchProduct
- to organization
- hasSubject (to Topic)