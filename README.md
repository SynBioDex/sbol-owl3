# SBOL3 Ontology

## Ontology

The SBOL3 ontology provides a set of controlled terms that are used to describe synthetic biology designs using SBOL3. These terms support the formal representation of SBOL3 entities, their relationships, accepted values, constraints, and commonly used biological design concepts.

Terms are included for the following.

- **Descriptions of SBOL3 entities**  
  The ontology includes descriptions of SBOL3 entities such as `Component`, `Sequence`, `Feature`, `SubComponent`, `Interaction`, `Participation`, `Implementation`, `Model`, `Collection`, and other entities that are exchanged electronically in SBOL3 documents. Constraints and validation rules associated with these entities are also captured as part of the ontology.

- **Abstract SBOL3 entities**  
  Some SBOL3 entities, such as `Identified` and `TopLevel`, are not always used directly in serialized biological designs but provide an important structure for grouping and relating SBOL3 entities. The ontology exposes these entities to semantic reasoning tools through class hierarchies and parent-child relationships.

- **Controlled vocabulary terms**  
  The ontology includes terms used to restrict or standardize the values of SBOL3 properties. These include terms for component types, feature roles, interaction types, model languages, model frameworks, orientations, and other controlled values used in SBOL3 descriptions.

- **Properties linking SBOL3 entities**  
  The ontology defines properties that connect SBOL3 entities to one another or to accepted values. Examples include properties such as `hasFeature`, `hasSequence`, `hasInteraction`, `hasParticipation`, `hasRole`, `hasType`, `hasLocation`, and other relationships used to describe the structure and behavior of biological designs.

- **Metadata terms for biological design descriptions**  
  The ontology includes metadata terms for commonly used descriptions of biological design entities, such as promoters, coding sequences, terminators, ribosome binding sites, genetic circuits, molecular species, and interactions. These terms may require the combined use of multiple SBOL3 entities and properties.

## Browse

Browse the SBOL3 ontology terms via an HTML page.

## Download

The SBOL3 ontology is available in different formats.

- OWL file
- RDF file
- OMN file (Manchester Syntax)

## Cite
