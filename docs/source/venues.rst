.. _Venue:

Venues
######
A **Venue** is an entity that models a publishing “gateway” used by :ref:`Researcher <Researcher>` to make their :ref:`Research product <Research product>` available to others.

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
:Use: mandatory, (1)
 
.. code-block:: json
   :linenos:

    "local_id": "123_local_id"


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


Name
----
:Description: The name of the venue.
:Type: string
:Use: mandatory, (1)
:Representation: XML element ``name``
 
.. code-block:: json
   :linenos:

    "name": "the name"


Venue type
----
:Description: The type of the venue.
:Type: vocabulary (see below)
:Use: mandatory, (1)
:Representation: XML element ``venueType``
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

    "venue_type", "Repository"


Peer review
----
:Description: the type of peer-review in charge at a venue.
:Type: Vocabulary {single-blind, double-blind, open, none}
:Use: mandatory, (1)
 
.. code-block:: json
   :linenos:

    "peer_review": "open"


Metadata curation
----
:Description: The type of metadata curation taking place at a venue.
:Type: Boolean
:Use: mandatory, (1)
 
.. code-block:: json
   :linenos:

    "metadata_curation": true


ISSN
----
:Description: The ISSNs used by a venue.
:Type: String
:Use: optional, (0..*)
 
.. code-block:: json
   :linenos:

    "issn": "xxxx-yyyy"


eISSN
----
:Description: Eletronic ISSN used by a venue.
:Type: String
:Use: optional, (0..*)
 
.. code-block:: json
   :linenos:

    "eissn": "xxxx-yyyy"


Linked ISSN
----
:Description: The `ISSN-L <https://en.wikipedia.org/wiki/International_Standard_Serial_Number#Linking_ISSN>`_ identifying this venue. 
:Type: String
:Use: optional, (0..1)
 
.. code-block:: json
   :linenos:

    "lissn": "xxxx-yyyy"


Acronym
----
:Description: Acronym used by a venue.
:Type: String
:Use: recommended, (0..1)
 
.. code-block:: json
   :linenos:

    "acronym": "ABC"


Conference place
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``place``
 
.. code-block:: json
   :linenos:

    "place": "NYC"


Conference dates
----
:Description: 
:Type: date period
:Use: 
:Representation: XML element ``dates``
 
Start date
^^^^^^^^^^^^^
:Description: 
:Type: String 
:Use: mandatory (1)

End date
^^^^^^^^^^^^^
:Description: 
:Type: String 
:Use: mandatory (1)

Date format
"""""""""""""
:Description: The format of the relevant date.
:Type: String 
:Use: mandatory (1)

.. code-block:: json
   :linenos:

    "dates": [
        {
            "start_date": "2022-12-03",
            "end_date": "2022-12-06",
            "date_format": "yyyy-MM-dd",
        }
    ]

    



Relationships
=============
TODO