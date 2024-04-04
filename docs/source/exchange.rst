.. _Exchange:

Exchange protocols
######

Complying to SKG-IF means data can be exchanged across diverse SKGs.
This entails exposing own and consuming others' data.

As a first step, we foresee two ways to achieve this:

* Bulk .zip file
* API resolver

For the sake of simplicity, JSON has been chosen as a reference data format for the exchange as suggested by the examples described in the core model entities.

Bulk .zip file
================================================================
As a first step, adopters of the SKG-IF can expose their mapped data as a bulk ``.zip`` file (all-inclusive) where records are serialised in JSON a slip across different part files.
Each part file contains 1000 SKG-IF records in JSON lines format.
To ease the consumption of such a file, the following structure has been agreed and should be followed when exposing data in this way.


| ./dump.zip
| ├── /results
| │   ├── /00000-00999
| │   │   ├── part_00000.jsonl 
| │   │   ├── part_00001.jsonl
| │   │   ├── ...
| │   │   └── part_00999.jsonl
| │   ├── /01000-01999
| │   └── /...
| ├── /persons
| │   ├── /00000-00999
| │   ├── /01000-01999
| │   └── /...
| └── /...
| 
| 



API resolver
================================================================
Our field work suggested that providing a full-fledged API would be not feasible at this stage, as it requires extensive discussions that can be hardly met within the WG deadlines. 
In the future, we will explore its feasibility via a dedicated RDA WG.

For the time being, the easiest way we conceived is about exchanging data by engaging with a API resolver, that returns SKG-IF, if any, given a ID in input.

A SKG-IF compliant SKG should provide an implementation of endpoint managing requests of this types 

* ``https://my.skg.io/list_schemes`` which provides a comprehensive JSON list of the ids and PIDs schemes that the API is willing to resolve. The scheme ``local`` refers to ids that are valid locally in the SKG at hand, and should always be present (e.g., ``['local', 'doi', 'handle', 'cordis', 'openalex']``).

* ``https://my.skg.io/search/<schema>:<id>`` which resolves a couple ``<schema, id>`` and returns its SKG-IF representation.
   * The parameter ``schema`` is one from the list returned by the ``list_schemes`` request above.
   * The parameter ``id`` is the identifiers that we are asking a SKG-IF representation (if any).
For example, e.g., https://my.skg.io/search/orcid:0000-1111-2222-3333.





