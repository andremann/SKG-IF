Venues
######
A Venue is an entity that models a publishing “gateway” used by scientists to make their research products available to others.

Example:
`Episciences <https://episciences.org>`_  is an overlay platform supporting the management of open-access journals on top of the Open Access repository HAL.fr. In this context, episciences.org is a publishing venue (journal, open access, open peer review), while HAL is a data source. Articles published via episciences.org will be therefore linked to the respective journal (publishing venue) and the data source HAL. 
However, HAL is also a publishing venue for researchers that are directly uploading their products; a publishing venue with peer-review and some support for metadata curation. In this case, research products will be linked to HAL as a publishing venue and as a data source. 

.. note::
    Each Research product must be associated with its publishing venue and its data source. 


Properties
==========
This section is to describe the metadata fields for the Venues.


Local identifier
----
:Description: Unique code identifiying the Venue in the OSG (if any, otherwise "stateless identifier")
:Type: string
:Use: recommended, (0..*)
:Representation: XML element ``localIdentifier``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>

Identifiers
----
:Description: 
:Type: Wrapper element
:Use: optional, (0..*)
:Representation: XML element ``identifiers``

Identifier scheme
^^^^^^^^^^^
:Description: The scheme for the external identifier
:Type: string
:Use: mandatory (1)
:Representation: XML element ``identifierScheme``

Identifier value
^^^^^^^^^
:Description: The external identifier 
:Type: string
:Use: mandatory (1)
:Representation: XML attribute ``identifierValue``

:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Name
----
:Description: The name of the venue
:Type: string
:Use: mandatory, (1)
:Representation: XML element ``name``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Venue type
----
:Description: The type of the venue
:Type: vocabulary
.. tabularcolumns:: p{0.132\linewidth}p{0.198\linewidth}p{0.330\linewidth}
.. csv-table:: Example CSV table
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
:Use: mandatory, (1)
:Representation: XML element ``venueType``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Peer review
----
:Description: The type of peer-review taking place at the venue
:Type: controlled vocabulary
:Use: mandatory, (1)
:Representation: XML element ``peerReview``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Metadata curation
----
:Description: The type of metadata curation taking place at the venue
:Type: controlled vocabulary
:Use: mandatory, (1)
:Representation: XML element ``metadataCuration``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


ISSN
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``issn``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


eISSN
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``eissn``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Linked ISSN
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``lissn``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Issue
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``issue``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Volume
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``volume``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Edition
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``edition``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Acronym
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``acronym``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Conference place
----
:Description: 
:Type: 
:Use: 
:Representation: XML element ``place``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>


Conference dates
----
:Description: 
:Type: date period
:Use: 
:Representation: XML element ``dates``
:Example: 
.. code-block:: xml
   :linenos:

    <tag>...</tag>



Relationships
=============
TODO