.. _Venue:

Venue
######
A :ref:`Venue <Venue>` is an entity that models a publishing “gateway” used by :ref:`Person <Person>` to make their :ref:`Research products <Research product>` available to others.

:Example: `Episciences <https://episciences.org>`_  is an overlay platform supporting the management of open-access journals on top of the Open Access repository `HAL <https://hal.science>`_. In this context, episciences.org is a publishing :ref:`Venue <Venue>` (journal, open access, open peer review), while HAL is a :ref:`Data source <Data source>`. Articles published via episciences.org will be therefore linked to the respective journal (publishing :ref:`Venue <Venue>`) and the data source HAL. 
    However, HAL is also a publishing :ref:`Venue <Venue>` for researchers that are directly uploading their :ref:`Research product <Research product>`. More specifically, a publishing :ref:`Venue <Venue>` with peer-review and some support for metadata curation. In this case, a :ref:`Research product <Research product>` will be linked to HAL both as a publishing :ref:`Venue <Venue>` and as a :ref:`Data source <Data source>`. 

.. note::
    Each :ref:`Research product <Research product>` must be associated with its publishing :ref:`Venue <Venue>` and its :ref:`Data source <Data source>`. 


This section is to describe the metadata fields for the :ref:`Venue <Venue>`.


``local_identifier``		
----
*String* (mandatory): Unique code identifiying the :ref:`Venue <Venue>` in the SKG (if any, otherwise "stateless identifier").
 
.. code-block:: json
   :linenos:

    "local_identifier": "123_local_id"


``identifiers``
----
*List* (recommended): A list of objects representing external identifiers for the entity. Each object is structured as follows.

* ``scheme`` *String* (mandatory): The scheme for the external identifier. It can be one of the following

    * ``issn``
    * ``eissn``
    * ``lissn``
    * ``isbn``
    * ``opendoar``
    * ``re3data.org``
    * ``fairsharing``
    * ``doi``
    * ``handle``

* ``value`` *String* (mandatory): The external identifier.

.. code-block:: json
   :linenos:

    "identifiers": [
        {
            "scheme": "issn"
            "value": "0302-9743"
        },
        {
            "scheme": "isbn"
            "value": "978-3-031-25049-1"
        }
    ]


``entity_type``
----
*String* (mandatory): Field stating what kind of entity is being serialised. Needed for parsing purposes; fixed to ``venue``.

.. code-block:: json
   :linenos:

    "entity_type": "venue"
    

``name`` 
----
 *String* (optional): The name of the :ref:`Venue <Venue>`.

.. code-block:: json
   :linenos:

    "name": "Lecture Notes in Computer Science"


``acronym`` 
----
 *String* (optional): Acronym used by a :ref:`Venue <Venue>`.

.. code-block:: json
   :linenos:

    "acronym": "JASIST"


``type``
----
*String* (optional): The type of the :ref:`Venue <Venue>`. The String follows the vocabulary below

.. tabularcolumns:: p{0.132\linewidth}p{0.198\linewidth}p{0.330\linewidth}
.. csv-table:: Controlled vocabulary for different types of venue and its mapping towards OpenCitations
   :name: tables-csv-example
   :header: "SKG-IF", "OpenCitations"
   :class: longtable
   :align: center

   "``repository``", "Repository, Scientific database"
   "``journal``", "Journal issue, Journal volume, Journal"
   "``conference``", "Proceedings series, Proceedings"
   "``book``", "Book, Book part, Book section, Book series, Book set, Edited book, Reference book, Monograph"
   "``other``", "Report series, Standard series, Archival document"
   "``unknown``", ""

.. code-block:: json
   :linenos:

    "type": "repository"


``publisher``
----
*String* (optional): The name of the publisher (for journals, books, conferences).

.. code-block:: json
   :linenos:

    "publisher": "Springer Nature"


``series``
----
*String* (optional): The name of the conference or book series.

.. code-block:: json
   :linenos:

    "series": "Lecture Notes in Computer Science (LNCS)"


``is_full_oa``
----
*Boolean* (optional): True if the :ref:`Venue <Venue>` contains only open access products (to the best of knowledge, at the time of expert).
 
.. code-block:: json
   :linenos:

    "is_currently_full_oa": true


``creation_date``
----
*String* (optional): The date of creation of the :ref:`Venue <Venue>` expressed as `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_.
 
.. code-block:: json
   :linenos:

    "creation_date": "2019-09-13"


``contributions``
------
*List* (optional) : A list of all the :ref:`Person` that contributed to the :ref:`Venue <Venue>`. Each element of the list is structured as follows:

* ``person`` *String* (mandatory): The id of a :ref:`Person`.
* ``roles`` *List* (mandatory): The roles of the :ref:`Person` contributing to the :ref:`Venue <Venue>`.

.. code-block:: json
   :linenos:

   "contributions": [
        {
            "person": "person_3",
            "roles": ["editor"]
        }
   ]