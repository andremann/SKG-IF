.. _Exchange:

Exchange protocols
######

Complying to SKG-IF means data can be exchanged across diverse SKGs.
This entails exposing own and consuming others' data.

As a first step, we foresee two ways to achieve this:

* Bulk ``.zip`` file
* *Pragmatic* API

For the sake of simplicity, JSON has been chosen as a reference data format for the exchange as suggested by the examples described in the core model entities.

Bulk ``.zip`` file
================================================================
As a first step, adopters of the SKG-IF can expose their mapped data as a bulk ``.zip`` file (all-inclusive).
To ease the consumption of such a file, the following structure has been agreed and should be followed when exposing data in this way.
Part files contain 1000 records each in JSON lines format.

| ./dump.zip
| ├── /results
| │   ├── /00000-00999
| |       ├── part_00000.jsonl 
| |       ├── part_00001.jsonl
| │   ├── /01000-01999
| │   └── /...
| ├── /persons
| │   ├── /00000-00999
| │   ├── /01000-01999
| │   └── /...
| ├── /...
| 
| 




*Pragmatic* API
================================================================








