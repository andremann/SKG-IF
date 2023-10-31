.. _Venue:

Venues
######
A :ref:`Venue <Venue>` is an entity that models a publishing “gateway” used by :ref:`Person <Person>` to make their :ref:`Research products <Research product>` available to others.

:Example: `Episciences <https://episciences.org>`_  is an overlay platform supporting the management of open-access journals on top of the Open Access repository `HAL <https://hal.science>`_. In this context, episciences.org is a publishing :ref:`Venue <Venue>` (journal, open access, open peer review), while HAL is a :ref:`Data source <Data source>`. Articles published via episciences.org will be therefore linked to the respective journal (publishing :ref:`Venue <Venue>`) and the data source HAL. 
    However, HAL is also a publishing :ref:`Venue <Venue>` for researchers that are directly uploading their :ref:`Research product <Research product>`. More specifically, a publishing :ref:`Venue <Venue>` with peer-review and some support for metadata curation. In this case, a :ref:`Research product <Research product>` will be linked to HAL both as a publishing :ref:`Venue <Venue>` and as a :ref:`Data source <Data source>`. 

.. note::
    Each :ref:`Research product <Research product>` must be associated with its publishing :ref:`Venue <Venue>` and its :ref:`Data source <Data source>`. 


Properties
==========
This section is to describe the metadata fields for the :ref:`Venue <Venue>`.


Local identifier		
----
:Description: Unique code identifiying the :ref:`Venue <Venue>` in the SKG (if any, otherwise "stateless identifier").
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "local_identifier": "123_local_id"


Identifiers			
----
:Description: Identifier for the resource outside of the SKG.
:Type: List
:Use: Optional, (0..1)

Scheme
^^^^^^^^^^^
:Description: The scheme for the external identifier.
:Type: String one of the following

    * ISSN
    * EISSN
    * LISSN
    * ISBN
    * OpenDOAR
    * re3data.org
    * FAIRsharing
    * doi
    * handle

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
            "scheme": "issn"
            "value": "0302-9743"
        },
        {
            "scheme": "isbn"
            "value": "978-3-031-25049-1"
        }
    ]


Name
----
:Description: The name of the :ref:`Venue <Venue>`.
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "name": "Lecture Notes in Computer Science"


Acronym
----
:Description: Acronym used by a :ref:`Venue <Venue>`.
:Type: String
:Use: Recommended (0..1)
 
.. code-block:: json
   :linenos:

    "acronym": "IJDL"


Type
----
:Description: The type of the :ref:`Venue <Venue>`.
:Type: String following the vocabulary below
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

    "type": "repository"

.. tabularcolumns:: p{0.132\linewidth}p{0.198\linewidth}p{0.330\linewidth}
.. csv-table:: Controlled vocabulary for different types of venue and its mapping towards OpenCitations
   :name: tables-csv-example
   :header: "SKG-IF", "OpenCitations"
   :class: longtable
   :align: center

   "repository", "Repository, Scientific database"
   "journal", "Journal issue, Journal volume, Journal"
   "conference", "Proceedings series, Proceedings"
   "book", "Book, Book part, Book section, Book series, Book set, Edited book, Reference book, Monograph"
   "other", "Report series, Standard series, Archival document"
   "unknown", ""


Publisher
----
:Description: The name of the publisher (for journals, books, conferences).
:Type: String
:Use: Optional (0..1)

.. code-block:: json
   :linenos:

    "publisher": "Springer Nature"


Series
----
:Description: The name of the conference or book series.
:Type: String
:Use: Optional (0..1)

.. code-block:: json
   :linenos:

    "series": "Lecture Notes in Computer Science (LNCS)"


Is currently full open access
----
:Description: True if the :ref:`Venue <Venue>` contains only open access products 
:Type: Boolean
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "is_currently_full_oa": true


Creation date
----
:Description: The date of creation of the :ref:`Venue <Venue>`
:Type: String (`ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ date string)
:Use: Recommended (1)
 
.. code-block:: json
   :linenos:

    "creation_date": "2019-09-13"


Contributions
------
:Description: A list of all the :ref:`Person` that contributed to the :ref:`Venue <Venue>`.
:Type: List
:Use: Optional (0..1)

Person
^^^^^^^^^
:Description: The id of a :ref:`Person`.
:Type: String 
:Use: Mandatory (1)

Roles
^^^^^^^^^
:Description: The roles of the :ref:`Person` contributing to the :ref:`Venue <Venue>`.
:Type: List of strings 
:Use: Mandatory (1)

.. code-block:: json
   :linenos:

   "contributions": [
        {
            "person": "person_3",
            "roles": ["editor"]
        }
   ]