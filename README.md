# SBOL3 Ontology

The SBOL-OWL3 ontology provides a set of controlled terms that are used to describe genetic circuit designs using the SBOL3 data standard. Terms are included for the followings.

- Descriptions of SBOL entities (e.g. [Component](https://synbiodex.github.io/sbol-owl3/sbol3.html#Component), [SubComponent](https://synbiodex.github.io/sbol-owl3/sbol3.html#CSubomponent), and [Model](https://synbiodex.github.io/sbol-owl3/sbol3.html#Model)). 

- Properties that connect SBOL3 entities to one another or to accepted values. Examples include properties such as [hasFeature](https://synbiodex.github.io/sbol-owl3/sbol3.html#hasFeature), [hasSequence](https://synbiodex.github.io/sbol-owl3/sbol3.html#hasSequence), [hasInteraction](https://synbiodex.github.io/sbol-owl3/sbol3.html#hasInteraction), [hasParticipation](https://synbiodex.github.io/sbol-owl3/sbol3.html#hasParticipation), and [role](https://synbiodex.github.io/sbol-owl3/sbol3.html#role), and other relationships used to describe the structure and behavior of biological designs. 

- SBOL-specific constraints (e.g. A Component must have at least one 'type' value).

- SBOL entities (e.g. "[TopLevel](https://synbiodex.github.io/sbol-owl3/sbol3.html#TopLevel)" that are not serialised but are used to group different SBOL entities. SBOL-OWL exposes these entities to semantic reasoning tools via parent-child relationships.

- SBOL Vocabulary terms (e.g. "[inline](https://synbiodex.github.io/sbol-owl3/sbol3.html#inline)") that are used to restrict values of SBOL entities.

- Enumerations that group different SBOL terms. (e.g. "[Orientation](https://synbiodex.github.io/sbol-owl3/sbol3.html#Orientation)")

- Metadata terms (e.g. "[NonCovalentBindingInteraction](https://synbiodex.github.io/sbol-owl3/sbol3.html#NonCovalentBindingInteraction)") for commonly used descriptions of design entities. Such terms may require the use of several SBOL entities and properties.

- Wrrapper terms to add SBOL specific rules for external tems (e.g. "[SBOLActivity](https://synbiodex.github.io/sbol-owl3/sbol3.html#SBOLActivity)" which inherits from  [prov:Activity](https://synbiodex.github.io/sbol-owl3/sbol3.html#Activity) and [TopLevel](https://synbiodex.github.io/sbol-owl3/sbol3.html#TopLevel)).

### Browse
[Browse the SBOL-OWL3 terms via an HTML page.](https://synbiodex.github.io/sbol-owl3/sbol3.html)

### Download
SBOL-OWL3 is available in different formats.

- [OWL file](https://synbiodex.github.io/sbol-owl3/sbol3.owl)
- [RDF file](https://synbiodex.github.io/sbol-owl3/sbol3.rdf)
- [OMN file](https://synbiodex.github.io/sbol-owl3/sbol3.omn) (Manchester Syntax)

# Dependencies
* owlready2 0.5
* rdflib 7.6.0
* pyLODE: 3.4.3a: At the time of the development, we created a pull request for a fix to pyLODE.  This has been incorporated. So, make sure to use the latest release when it is ready!
* Robot 1.9.10: Available as a jar file within the project. Sourced from: https://github.com/ontodev/robot/releases/tag/v1.9.10
