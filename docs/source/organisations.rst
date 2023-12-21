.. _Organisation:

Organisations
#############
The entity :ref:`Organisation <Organisation>` represents academic institutions, research centers, funders, or any other institutions taking part to the research process.


This section is to describe the metadata fields for the :ref:`Organisation <Organisation>`.


``local_identifier``
----
*String* (mandatory): Unique code identifiying the :ref:`Organisation <Organisation>` in the SKG (if any, otherwise "stateless identifier").
 
.. code-block:: json
   :linenos:

    "local_identifier": "the_id"


``identifiers``
----
*List* (recommended):  A list of objects representing external identifiers for the entity. Each object is structured as follows.

* ``scheme`` *String* (mandatory): The scheme for the external identifier (e.g., ROR, ISNI).
* ``value`` *String* (mandatory): The external identifier.

 
.. code-block:: json
   :linenos:

    "identifiers": [
        {
            "scheme": "ROR"
            "value": "05kacka20"
        }
    ]


``name``
----
*String* (mandatory): The name of the :ref:`Organisation <Organisation>`.
 
.. code-block:: json
   :linenos:

    "name": "Institute of Information Science and Technologies"


``short_name``
----
*String* (optional): The short name/acronym for the :ref:`Organisation <Organisation>`.
 
.. code-block:: json
   :linenos:

    "short_name": "CNR-ISTI"


``other_names``
----
*List* (optional): A list of other names, maybe in different languages, identifiying the :ref:`Organisation <Organisation>`.
 
.. code-block:: json
   :linenos:

    "other_names": ["ISTI", "ISTI-CNR"]


``website``
----
*String* (mandatory): The website URL for the :ref:`Organisation <Organisation>`.
 
.. code-block:: json
   :linenos:

    "website": "http://www.isti.cnr.it"


``country``
----
*String* (mandatory): The country code of the :ref:`Organisation <Organisation>` expressed as `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_.
 
.. code-block:: json
   :linenos:

    "country": "DE"


``type``
----
*String* (recommended): The type of the :ref:`Organisation <Organisation>`. One from the following values:
    
    * ``archive``
    * ``company``
    * ``education``
    * ``facility``
    * ``government``
    * ``healthcare``
    * ``nonprofit``
    * ``funder``
    * ``other``

.. code-block:: json
   :linenos:

    "type": "education"