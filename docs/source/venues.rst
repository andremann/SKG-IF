.. _Venue:

Venues
######
A **Venue** is an entity that models a publishing “gateway” used by :ref:`Person <Person>` to make their :ref:`Research product <Research product>` available to others.

Example:
`Episciences <https://episciences.org>`_  is an overlay platform supporting the management of open-access journals on top of the Open Access repository HAL.fr. In this context, episciences.org is a publishing venue (journal, open access, open peer review), while HAL is a data source. Articles published via episciences.org will be therefore linked to the respective journal (publishing venue) and the data source HAL. 
However, HAL is also a publishing venue for researchers that are directly uploading their products; a publishing venue with peer-review and some support for metadata curation. In this case, research products will be linked to HAL as a publishing venue and as a data source. 

.. note::
    Each :ref:`Research product <Research product>` must be associated with its publishing **Venue** and its :ref:`Data source <Data source>`. 


Properties
==========
This section is to describe the metadata fields for the Venues.


Local identifier		
----
:Description: Unique code identifiying the **Venue** in the SKG (if any, otherwise "stateless identifier").
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "local_identifier": "123_local_id"


Identifiers			
----
:Description: Alternative identifiers. Allowed schemes are ISSN, EISSN, LISSN, ISBN, OpenDOAR ID, re3data.org ID, etc.
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
:Description: The name of the venue.
:Type: String
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "name": "the name"


Acronym
----
:Description: Acronym used by a venue.
:Type: String
:Use: Recommended (0..1)
 
.. code-block:: json
   :linenos:

    "acronym": "IJDL"


Type
----
:Description: The type of the venue.
:Type: String following the vocabulary below
:Use: Mandatory (1)

.. tabularcolumns:: p{0.132\linewidth}p{0.198\linewidth}p{0.330\linewidth}
.. csv-table:: Controlled vocabulary for different types of venue and its mapping towards OpenCitations
   :name: tables-csv-example
   :header: "SKG-IF", "OpenCitations"
   :class: longtable
   :align: center

   "Repository", "Repository, Scientific database"
   "Journal", "Journal issue, Journal volume, Journal"
   "Conference", "Proceedings series, Proceedings"
   "Book", "Book, Book part, Book section, Book series, Book set, Edited book, Reference book, Monograph"
   "Other", "Report series, Standard series, Archival document"
   "Unknown", ""

.. code-block:: json
   :linenos:

    "type", "Repository"


Is currently full open access
----
:Description: 
:Type: Boolean
:Use: Mandatory (1)
 
.. code-block:: json
   :linenos:

    "is_currently_full_oa": True


Creation date
----
:Description: 
:Type: String ()
:Use: Recommended (1)
 
.. code-block:: json
   :linenos:

    "creation date": "2019-09-13"


Relationships
=============
TODO