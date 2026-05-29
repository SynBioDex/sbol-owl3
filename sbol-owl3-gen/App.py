'''
Created on 26 May 2021

@author: gokselmisirli
'''

# Dependencies: owlready2, rdflib, pylode --> pip install owlready2 rdflib pylode)
from owlready2 import *
from rdflib import Graph
from importlib.metadata import version
import rdflib
from rdflib.namespace import OWL, RDF
import sys
import re
from pathlib import Path
import types
import datetime

print('Python: ' +  sys.version)
print('owlready2: ' + version("owlready2"))
print('rdflib:' + rdflib.__version__)

sbol3 = get_ontology("http://sbols.org/v3#")
prov = get_ontology("https://www.w3.org/ns/prov#")
om = get_ontology("http://www.ontology-of-units-of-measure.org/resource/om-2/")
sbo = get_ontology("https://identifiers.org/SBO:")
sbo.base_iri = "https://identifiers.org/SBO:"
so = get_ontology("https://identifiers.org/SO:")
so.base_iri = "https://identifiers.org/SO:"
edam = get_ontology("https://identifiers.org/edam:")
edam.base_iri = "https://identifiers.org/edam:"
chebi = get_ontology("https://identifiers.org/CHEBI:")
chebi.base_iri = "https://identifiers.org/CHEBI:"
go = get_ontology("https://identifiers.org/GO:")
go.base_iri = "https://identifiers.org/GO:"
rdfNS = get_ontology("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
owlNS = get_ontology("http://www.w3.org/2002/07/owl#")

with rdfNS:
    class type(ObjectProperty):
        pass

with owlNS:
    class topObjectProperty(ObjectProperty):
        pass

#Ontology-to-library mapping ontology
otol = get_ontology("http://keele.ac.uk/scm/otol#")

with otol:

  class constantList(AnnotationProperty):
      label = "Constant list"
      comment = "If true, create an enum list."

  class vocabulary(AnnotationProperty):
      label = "Vocabulary"
      comment = "If true, an object should be created for the container class."

  class replacementOf (AnnotationProperty):
      label = "replacementOf"
      comment = "If specified, create the entity name according to the value of this property. E.g. for sbol3:SBOLActivity otol:replacementOf prov:Activity, create the entities using the Activity name only."

  class domainEntity (AnnotationProperty):
      label = "domainEntity"
      comment = "If true, indicates that the term corresponds to a domain entity. Software automation tools should create a specific entity."

with sbo:

    SBO_0000000 = types.new_class("0000000", (Thing,))
    SBO_0000000.label = ["Systems Biology Representation"]
    SBO_0000000.comment = ["Root term for Systems Biology Ontology representing all mathematical or logical terms used in systems biology."]

    SBO_0000236 = types.new_class("0000236", (SBO_0000000,))
    SBO_0000236.label = ["Physical Entity Representation"]
    SBO_0000236.comment = ["A material entity such as a molecule, complex, or cell. Representation of a discrete portion of matter that has mass and occupies space."]

    SBO_0000251 = types.new_class("0000251", (SBO_0000236,))
    SBO_0000251.label = ["DNA"]
    SBO_0000251.comment = ["DNA molecule, a polymer consisting of deoxyribonucleotide monomers."]

    SBO_0000250 = types.new_class("0000250", (SBO_0000236,))
    SBO_0000250.label = ["RNA"]
    SBO_0000250.comment = ["RNA molecule, a polymer consisting of ribonucleotide monomers."]

    SBO_0000252 = types.new_class("0000252", (SBO_0000236,))
    SBO_0000252.label = ["Protein"]
    SBO_0000252.comment = ["Protein or polypeptide. A polymer consisting of amino acid monomers linked by peptide bonds."]

    SBO_0000247 = types.new_class("0000247", (SBO_0000236,))
    SBO_0000247.label = ["Simple Chemical"]
    SBO_0000247.comment = ["A small molecule or ion. A small molecule without specific type classification."]

    SBO_0000253 = types.new_class("0000253", (SBO_0000236,))
    SBO_0000253.label = ["Non-covalent Complex"]
    SBO_0000253.comment = ["Entity composed of non-covalently bound components. Entity composed of multiple components bound together through non-covalent interactions."]

    SBO_0000241 = types.new_class("0000241", (SBO_0000236,))
    SBO_0000241.label = ["Functional Entity"]
    SBO_0000241.comment = ["An abstract entity with function but no physical form"]

    # Occurring Entity Representation (parent for interactions)
    SBO_0000231 = types.new_class("0000231", (SBO_0000000,))
    SBO_0000231.label = ["Occurring Entity Representation"]
    SBO_0000231.comment = ["Representation of an entity that develops or occurs over time, such as events, interactions, or reactions."]

    # Biochemical or transport reaction
    SBO_0000167 = types.new_class("0000167", (SBO_0000231,))
    SBO_0000167.label = ["Biochemical or Transport Reaction"]
    SBO_0000167.comment = ["An event involving physical entities that results in modification of structure, location, or free energy."]

    # Biochemical reaction
    SBO_0000176 = types.new_class("0000176", (SBO_0000167,))
    SBO_0000176.label = ["Biochemical Reaction"]
    SBO_0000176.comment = ["An event involving one or more chemical entities that alters their electrochemical structure."]

    # Non-covalent binding or dissociation
    SBO_0000177 = types.new_class("0000177", (SBO_0000176,))
    SBO_0000177.label = ["Non-covalent Binding"]
    SBO_0000177.comment = ["Association without covalent bonds. Biochemical reaction where a molecular complex breaks into smaller components."]

    # Degradation
    SBO_0000179 = types.new_class("0000179", (SBO_0000176,))
    SBO_0000179.label = ["Degradation"]
    SBO_0000179.comment = ["Breakdown of a molecule, usually into simpler components."]

    # Control
    SBO_0000168 = types.new_class("0000168", (SBO_0000231,))
    SBO_0000168.label = ["Control"]
    SBO_0000168.comment = ["Modulation of activity. Modification of the execution of an event or process. Also known as regulation."]

    # Inhibition
    SBO_0000169 = types.new_class("0000169", (SBO_0000168,))
    SBO_0000169.label = ["Inhibition"]
    SBO_0000169.comment = ["Negative modulation of activity; decreasing the rate or probability of an event."]

    # Stimulation
    SBO_0000170 = types.new_class("0000170", (SBO_0000168,))
    SBO_0000170.label = ["Stimulation"]
    SBO_0000170.comment = ["Positive modulation of activity; increasing the rate or probability of an event."]

    # Genetic production
    SBO_0000589 = types.new_class("0000589", (SBO_0000231,))
    SBO_0000589.label = ["Genetic Production"]
    SBO_0000589.comment = ["Production of a gene product. Composite biochemical process through which a gene sequence is converted into mature gene products."]

    # Participant roles
    SBO_0000003 = types.new_class("0000003", (SBO_0000000,))
    SBO_0000003.label = ["Participant Role"]
    SBO_0000003.comment = ["The function of a physical entity or process (participant) in a process or event."]

    # Modifier
    SBO_0000019 = types.new_class("0000019", (SBO_0000003,))
    SBO_0000019.label = ["Modifier"]
    SBO_0000019.comment = ["Entity that changes the velocity of a process without being consumed or transformed."]

    # Inhibitor
    SBO_0000020 = types.new_class("0000020", (SBO_0000019,))
    SBO_0000020.label = ["Inhibitor"]
    SBO_0000020.comment = ["Substance that decreases the probability of a chemical reaction without being consumed or transformed."]

    # Stimulator
    SBO_0000459 = types.new_class("0000459", (SBO_0000019,))
    SBO_0000459.label = ["Stimulator"]
    SBO_0000459.comment = ["Substance that increases the probability of a chemical reaction without being consumed or transformed."]

    # Inhibited
    SBO_0000642 = types.new_class("0000642", (SBO_0000003,))
    SBO_0000642.label = ["Inhibited"]
    SBO_0000642.comment = ["Entity that is inhibited. Conceptual or material entity that is the object of an inhibition process, acted upon by an inhibitor."]

    # Stimulated
    SBO_0000643 = types.new_class("0000643", (SBO_0000003,))
    SBO_0000643.label = ["Stimulated"]
    SBO_0000643.comment = ["Entity that is stimulated. Conceptual or material entity that is the object of a stimulation process, acted upon by a stimulator."]

    # Modified
    SBO_0000644 = types.new_class("0000644", (SBO_0000003,))
    SBO_0000644.label = ["Modified"]
    SBO_0000644.comment = ["Entity that has been modified. Conceptual or material entity that is the object of a modification process, acted upon by a modifier."]

    # Template
    SBO_0000645 = types.new_class("0000645", (SBO_0000003,))
    SBO_0000645.label = ["Template"]
    SBO_0000645.comment = ["Entity that acts as the template or starting material for genetic production."]

    # Functional compartment
    SBO_0000289 = types.new_class("0000289", (SBO_0000003,))
    SBO_0000289.label = ["Functional Compartment"]
    SBO_0000289.comment = ["An abstract entity with function but no physical form. A logical or physical subdivision of an event space containing pools of participants considered identical for the events."]

    SBO_0000011 = types.new_class("0000011", (SBO_0000003,))
    SBO_0000011.label = ["Product"]

    SBO_0000010 = types.new_class("0000010", (SBO_0000003,))
    SBO_0000010.label = ["Reactant"]

    SBO_0000598 = types.new_class("0000598", (SBO_0000003,))
    SBO_0000598.label = ["Promoter"]

    # Modelling framework
    SBO_0000004 = types.new_class("0000004", (SBO_0000000,))
    SBO_0000004.label = ["modelling framework"]
    SBO_0000004.comment = ["Set of assumptions that underlay a mathematical description."]

    SBO_0000062 = types.new_class("0000062", (SBO_0000004,))
    SBO_0000062.label = ["continuous"]
  
    SBO_0000063 = types.new_class("0000063", (SBO_0000004,))
    SBO_0000063.label = ["discrete"]
  
    SBO_0000693 = types.new_class("0000693", (SBO_0000004,))
    SBO_0000693.label = ["constraint-based"]
  
    SBO_0000234 = types.new_class("0000234", (SBO_0000004,))
    SBO_0000234.label = ["logical"]

    SBO_0000681 = types.new_class("0000681", (SBO_0000004,))
    SBO_0000681.label = ["hybrid"]
    
with so:
    SO_0000110 = types.new_class("0000110", (Thing,))
    SO_0000110.label = ["Sequence Feature"]
    SO_0000110.comment = ["A general sequence feature", "Any extent of continuous biological sequence."]

    SO_0000167 = types.new_class("0000167", (SO_0000110,))
    SO_0000167.label = ["Promoter"]
    SO_0000167.comment = ["A regulatory region that initiates transcription. A regulatory region where transcription is initiated."]

    SO_0000139 = types.new_class("0000139", (SO_0000110,))
    SO_0000139.label = ["Ribosome Binding Site"]
    SO_0000139.comment = ["Region of mRNA where the ribosome assembles to begin translation. A sequence where ribosomes bind to initiate translation."]

    SO_0000316 = types.new_class("0000316", (SO_0000110,))
    SO_0000316.label = ["Coding Sequence"]
    SO_0000316.comment = ["Coding DNA Sequence - region that can be translated into protein. Coding sequence; DNA region that codes for protein."]

    SO_0000141 = types.new_class("0000141", (SO_0000110,))
    SO_0000141.label = ["Terminator"]
    SO_0000141.comment = ["Sequence that terminates transcription. A sequence signaling the end of transcription."]

    SO_0000704 = types.new_class("0000704", (SO_0000110,))
    SO_0000704.label = ["Gene"]
    SO_0000704.comment = ["A region of genomic sequence encoding a gene product. A region of sequence that encodes functional products."]

    SO_0000057 = types.new_class("0000057", (SO_0000110,))
    SO_0000057.label = ["Operator"]
    SO_0000057.comment = ["A regulatory element controlling gene expression. A DNA regulatory element where a repressor binds to control gene expression."]

    SO_0000804 = types.new_class("0000804", (SO_0000110,))
    SO_0000804.label = ["Engineered Region"]
    SO_0000804.comment = ["A region constructed using genetic engineering. A region constructed using genetic engineering techniques."]

    SO_0000234 = types.new_class("0000234", (SO_0000110,))
    SO_0000234.label = ["mRNA"]

    SO_0000400 = types.new_class("0000400", (Thing,))
    SO_0000400.label = ["Nucleic Acid Topology"]
    SO_0000400.comment = ["An attribute describing a sequence", "An attribute describes a quality of sequence."]

    SO_0000987 = types.new_class("0000987", (SO_0000400,))
    SO_0000987.label = ["linear"]

    SO_0000988 = types.new_class("0000988", (SO_0000400,))
    SO_0000988.label = ["circular"]

    SO_0000984 = types.new_class("0000984", (SO_0000400,))
    SO_0000984.label = ["single-stranded"]

    SO_0000985 = types.new_class("0000985", (SO_0000400,))
    SO_0000985.label = ["double-stranded"]

    # Orientation terms
    SO_0001030 = types.new_class("0001030", (SO_0000400,))
    SO_0001030.label = ["inline"]
    SO_0001030.comment = ["Feature located on the forward strand. Orientation corresponding to the forward strand (5' to 3' left to right in standard representations)."]

    SO_0001031 = types.new_class("0001031", (SO_0000400,))
    SO_0001031.label = ["reverseComplement"]
    SO_0001031.comment = ["Feature located on the reverse complement strand. Orientation corresponding to the reverse strand (complementary to the forward strand)."]

with chebi:
    CHEBI_50906 = types.new_class("50906", (Thing,))
    CHEBI_50906.label = ["Material Entity"]

    CHEBI_35224 = types.new_class("35224", (CHEBI_50906,))
    CHEBI_35224.label = ["Effector"]

with go:
    GO_0003674 = types.new_class("0003674", (Thing,))
    GO_0003674.label = ["Molecular Function"]

    GO_0003700 = types.new_class("0003700", (GO_0003674,))
    GO_0003700.label = ["Transcription Factor"]

with edam:
    EDAM_format_1915 = types.new_class("format_1915", (Thing,))
    EDAM_format_1915.label = ["Format"]

    EDAM_format_1207 = types.new_class("format_1207", (EDAM_format_1915,))
    EDAM_format_1207.label = ["IUPAC DNA/RNA"]

    EDAM_format_1208 = types.new_class("format_1208", (EDAM_format_1915,))
    EDAM_format_1208.label = ["IUPAC Protein"]

    EDAM_format_1197 = types.new_class("format_1197", (EDAM_format_1915,))
    EDAM_format_1197.label = ["InChI"]

    EDAM_format_1196 = types.new_class("format_1196", (EDAM_format_1915,))
    EDAM_format_1196.label = ["SMILES"]

    # Model languages
    EDAM_format_2585 = types.new_class("format_2585", (EDAM_format_1915,))
    EDAM_format_2585.label = ["SBML"]
    EDAM_format_2585.comment = ["Systems Biology Markup Language (SBML) format."]

    EDAM_format_3240 = types.new_class("format_3240", (EDAM_format_1915,))
    EDAM_format_3240.label = ["CellML"]
    EDAM_format_3240.comment = ["CellML model language format."]

    EDAM_format_3156 = types.new_class("format_3156", (EDAM_format_1915,))
    EDAM_format_3156.label = ["BioPAX"]
    EDAM_format_3156.comment = ["Biological Pathway Exchange (BioPAX) format."]

with sbol3 :
    class SBOLValue (Thing):
      pass
    SBOLValue.vocabulary = ["true"] # Do not create an object

    class ComponentType (SBO_0000236):
        label = "Component Type"
    ComponentType.constantList = ["true"]
    ComponentType.is_a.append(SBOLValue)
    ComponentType.equivalent_to.append(SBO_0000241 | SBO_0000247 | SBO_0000250 | SBO_0000251 | SBO_0000252 | SBO_0000253)

    class DNARNAComponentType (ComponentType):
        label = "DNA or RNA Component Type"
    DNARNAComponentType.constantList = ["true"]
    ComponentType.equivalent_to.append(ComponentType | SO_0000987 | SO_0000988 | SO_0000984 | SO_0000985)

    class Encoding (SBOLValue):
        label = "Encoding"
    Encoding.constantList = ["true"]
    Encoding.equivalent_to.append(EDAM_format_1207 | EDAM_format_1208 | EDAM_format_1197 | EDAM_format_1196)

    class ComponentRole (SBOLValue):
        label = "Component Role";        
    
    class DNARole (ComponentRole):
        label = "DNA Role"
    DNARole.constantList = ["true"]
    DNARole.equivalent_to.append(SO_0000110 | SO_0000167 | SO_0000139 | SO_0000316 | SO_0000141 | SO_0000704 | SO_0000057 | SO_0000804)

    class RNARole (ComponentRole):
        label = "RNA role"
    RNARole.constantList = ["true"]
    RNARole.equivalent_to.append(SO_0000110 | SO_0000234)

    class ProteinRole (ComponentRole):
        label = "Protein Role"
    ProteinRole.constantList = ["true"]
    ProteinRole.equivalent_to.append(GO_0003674 | GO_0003700)

    class SmallMoleculeRole (ComponentRole):
        label = "Small Molecule Role"
    SmallMoleculeRole.constantList = ["true"]
    SmallMoleculeRole.equivalent_to.append(CHEBI_50906 | CHEBI_35224)

with om:
    class Measure(Thing):
        label = "Measure"

with prov:
    class Activity(Thing):
        label = "Activity"

    class Association(Thing):
        label = "Association"

    class Agent(Thing):
        label = "Agent"

    class Plan(Thing):
        label = "Plan"

    class Usage(Thing):
        label = "Usage"

with sbol3:
    # ---------SBOL Entities--------------
    class Identified(Thing):
        label = "Identified"

    class TopLevel(Identified):
        label = "TopLevel"

    class Sequence (TopLevel):
        label = "Sequence"
    Sequence.domainEntity = ["true"]

    class Component (TopLevel):
        label = "Component"
    Component.domainEntity = ["true"]

    class Model (TopLevel):
        label = "Model"
    Model.domainEntity = ["true"]

    class Implementation (TopLevel):
        label = "Implementation"
    Implementation.domainEntity = ["true"]

    class Attachment (TopLevel):
        label = "Attachment"
    Attachment.domainEntity = ["true"]

    class Collection (TopLevel):
        label = "Collection"
    Collection.domainEntity = ["true"]

    class Experiment(Collection):
        label = "Experiment"
    Experiment.domainEntity = ["true"]

    class ExperimentalData (TopLevel):
        label = "ExperimentalData"
    ExperimentalData.domainEntity = ["true"]

    class CombinatorialDerivation (TopLevel):
        label = "CombinatorialDerivation"
    CombinatorialDerivation.domainEntity = ["true"]

    class Interaction (Identified):
        label = "Interaction"
    Interaction.domainEntity = ["true"]

    class Constraint (Identified):
        label = "Constraint"
    Constraint.domainEntity = ["true"]

    class Interface (Identified):
        label = "Interface"
    Interface.domainEntity = ["true"]

    class Feature (Identified):
        label = "Feature"
    Feature.domainEntity = ["true"]

    class SubComponent (Feature):
        label = "SubComponent"
    SubComponent.domainEntity = ["true"]

    class ComponentReference (Feature):
        label = "ComponentReference"
    ComponentReference.domainEntity = ["true"]

    class ExternallyDefined (Feature):
        label = "ExternallyDefined"
    ExternallyDefined.domainEntity = ["true"]

    class LocalSubComponent (Feature):
        label = "LocalSubComponent"
    LocalSubComponent.domainEntity = ["true"]

    class SequenceFeature (Feature):
        label = "SequenceFeature"
    SequenceFeature.domainEntity = ["true"]

    class Location (Identified):
        label = "Location"
    Location.domainEntity = ["true"]

    class Range (Location):
        label = "Range"
    Range.domainEntity = ["true"]

    class Cut (Location):
        label = "Cut"
    Cut.domainEntity = ["true"]

    class EntireSequence (Location):
        label = "EntireSequence"
    EntireSequence.domainEntity = ["true"]

    class Participation (Identified):
        label = "Participation"
    Participation.domainEntity = ["true"]

    class VariableFeature (Identified):
        label = "VariableFeature"
    VariableFeature.domainEntity = ["true"]
    
    class Metadata (Identified):
        label = "Metadata"
    Metadata.domainEntity = ["true"]
    Metadata.is_a.append(rdfNS.type.some(Thing))#Metadata must have another RDF.type    
    Identified.is_a.append(owlNS.topObjectProperty.min(0,Metadata)) #Identified may have zero or more Metadata annotations, but Metadata must be attached to at least one Identified entity

    class GenericTopLevel (TopLevel):
        label = "GenericTopLevel"
    GenericTopLevel.domainEntity = ["true"]
    GenericTopLevel.is_a.append(rdfNS.type.some(Thing))    #GenericTopLevel must have another RDF.type
    
# ---------Provenance Entities--------------
    class SBOLActivity(TopLevel):
      label = "SBOL Activity"
    SBOLActivity.domainEntity = ["true"]
    SBOLActivity.replacementOf = [prov.Activity]
    SBOLActivity.is_a.append(prov.Activity)

    class SBOLPlan(TopLevel):
      label = "SBOLPlan"
    SBOLPlan.domainEntity = ["true"]
    SBOLPlan.replacementOf = [prov.Plan]
    SBOLPlan.is_a.append(prov.Plan)

    class SBOLAgent(TopLevel):
      label = "SBOL Agent"
    SBOLAgent.domainEntity = ["true"]
    SBOLAgent.replacementOf = [prov.Agent]
    SBOLAgent.is_a.append(prov.Agent)

    class SBOLUsage(Identified):
      label = "SBOL Usage"
    SBOLUsage.domainEntity = ["true"]
    SBOLUsage.replacementOf = [prov.Usage]
    SBOLUsage.is_a.append(prov.Usage)

    class SBOLAssociation(Identified):
      label = "SBOL Association"
    SBOLAssociation.domainEntity = ["true"]
    SBOLAssociation.replacementOf = [prov.Association]
    SBOLAssociation.is_a.append(prov.Association)

    class SBOLMeasure(Identified):
      label = "SBOL Measure"
    SBOLMeasure.domainEntity = ["true"]
    SBOLMeasure.replacementOf = [om.Measure]
    SBOLMeasure.is_a.append(om.Measure)

    # ---------SBOL Vocabulary--------------
    class SBOLTerm (Thing):
      label = "SBOL Term"
    SBOLTerm.vocabulary = ["true"] # Do not create an object
    
    # Orientation terms
    class Orientation (SBOLTerm):
      label = "Orientation"
    Orientation.constantList = ["true"]

    class inline (Orientation):
        label = "inline"

    class reverseComplement (Orientation):
        label = "reverseComplement"

    Orientation.equivalent_to.append(inline | reverseComplement)

    # CombinatorialDerivationStrategy terms
    class CombinatorialDerivationStrategy  (SBOLTerm):
        label = "CombinatorialDerivationStrategy"
    CombinatorialDerivationStrategy.constantList = ["true"]

    class enumerate (CombinatorialDerivationStrategy):
        label = "enumerate"

    class sample (CombinatorialDerivationStrategy):
        label = "sample"

    CombinatorialDerivationStrategy.equivalent_to.append(enumerate | sample)

    # Cardinality terms
    class Cardinality  (SBOLTerm):
        label = "Cardinality"
    Cardinality.constantList = ["true"]

    class zeroOrOne (Cardinality):
        label = "zeroOrOne"

    class one (Cardinality):
        label = "one"

    class zeroOrMore (Cardinality):
        label = "zeroOrMore"

    class oneOrMore (Cardinality):
        label = "OneOrMore"

    Cardinality.equivalent_to.append(zeroOrOne | one | zeroOrMore | oneOrMore)

    # RoleIntegration terms
    class RoleIntegration (SBOLTerm):
        label = "RoleIntegration"
    RoleIntegration.constantList = ["true"]

    class overrideRoles (RoleIntegration):
        label = "overrideRoles"

    class mergeRoles (RoleIntegration):
        label = "mergeRoles"

    RoleIntegration.equivalent_to.append(overrideRoles | mergeRoles)

    # NucleicAcidTopology terms
    class NucleicAcidTopology (SBOLValue):
        label = "NucleicAcidTopology"
    NucleicAcidTopology.constantList = ["true"]
    NucleicAcidTopology.equivalent_to.append(SO_0000987 | SO_0000988 | SO_0000984 | SO_0000985)

    # ConstraintRestriction terms
    class ConstraintRestriction(SBOLTerm):
        label = "ConstraintRestriction"
        comment = "Controlled vocabulary for the types of relationships that can be expressed in Constraints."
    ConstraintRestriction.constantList = ["true"]

    # Identity relations
    class verifyIdentical(ConstraintRestriction):
        label = "verifyIdentical"
        comment = "Subject and object must both be SubComponents with the same instanceOf or ExternallyDefined with the same definition."

    class differentFrom(ConstraintRestriction):
        label = "differentFrom"
        comment = "Subject and object must NOT refer to the same Component/definition."

    class replaces(ConstraintRestriction):
        label = "replaces"
        comment = "The definition of subject is to replace the definition of object during design resolution."

    # Topological relations
    class contains(ConstraintRestriction):
        label = "contains"
        comment = "Subject contains object; they might or might not share a boundary."

    class strictlyContains(ConstraintRestriction):
        label = "strictlyContains"
        comment = "Subject entirely contains object without sharing any boundary."

    class equals(ConstraintRestriction):
        label = "equals"
        comment = "Subject and object occupy the same location in space or sequence."

    class covers(ConstraintRestriction):
        label = "covers"
        comment = "Subject covers object."

    class overlaps(ConstraintRestriction):
        label = "overlaps"
        comment = "Subject and object overlap but portions of each are outside the other."

    class meets(ConstraintRestriction):
        label = "meets"
        comment = "Subject and object are connected at a shared boundary."

    class isDisjointFrom(ConstraintRestriction):
        label = "isDisjointFrom"
        comment = "Subject and object do not overlap in space."

    class precedes(ConstraintRestriction):
        label = "precedes"
        comment = "Start of subject location is less than start of object location."

    class strictlyPrecedes(ConstraintRestriction):
        label = "strictlyPrecedes"
        comment = "End of subject location is less than start of object location."

    class starts(ConstraintRestriction):
        label = "starts"
        comment = "Start positions are equal; subject ends before object ends."

    class finishes(ConstraintRestriction):
        label = "finishes"
        comment = "Subject starts after object starts; end positions are equal."

    # Sequential restrictions
    class SequentialRestriction(ConstraintRestriction):
        label = "SequentialRestriction"
    SequentialRestriction.constantList = ["true"]
    SequentialRestriction.equivalent_to.append(precedes| strictlyPrecedes | meets | overlaps | contains | strictlyContains | equals | starts |finishes)

    # Identity restrictions    
    class IdentityRestriction(ConstraintRestriction):
        label = "IdentityRestriction"
    IdentityRestriction.constantList = ["true"]
    IdentityRestriction.equivalent_to.append(verifyIdentical | differentFrom | replaces)

    # Topology restrictions        
    class TopologyRestriction(ConstraintRestriction):
        label = "TopologyRestriction"
    TopologyRestriction.constantList = ["true"]
    TopologyRestriction.equivalent_to.append(isDisjointFrom | strictlyContains | contains | equals | meets | covers | overlaps)

    # Orientation restrictions
    class OrientationRestriction(ConstraintRestriction):
        label = "OrientationRestriction"
    OrientationRestriction.constantList = ["true"]

    class sameOrientationAs(OrientationRestriction):
        label = "sameOrientationAs"
        comment = "Subject and object have the same strand orientation."

    class oppositeOrientationAs(OrientationRestriction):
        label = "oppositeOrientationAs"
        comment = "Subject and object have opposite strand orientations."

    OrientationRestriction.equivalent_to.append (sameOrientationAs | oppositeOrientationAs )

    # Interaction types
    class InteractionType(SBOLValue):
        label = "InteractionType"    
    InteractionType.constantList = ["true"]    
    InteractionType.equivalent_to.append(SBO_0000169 | SBO_0000170 | SBO_0000176 | SBO_0000177 | SBO_0000179 | SBO_0000589 | SBO_0000168)

    # Participant roles
    class ParticipationRole(SBOLValue):
        label = "ParticipationRole"    
    ParticipationRole.constantList = ["true"]
    ParticipationRole.equivalent_to.append(SBO_0000020 | SBO_0000642 | SBO_0000459 | SBO_0000643 | SBO_0000010 | SBO_0000011 | SBO_0000598 | SBO_0000019 | SBO_0000645)

    # Model framework terms
    class ModelFramework(SBOLValue):
        label = "ModelFramework"
    ModelFramework.constantList = ["true"]
    ModelFramework.equivalent_to.append(SBO_0000062 | SBO_0000063 | SBO_0000693 | SBO_0000234 | SBO_0000681)

    # Model language terms
    class ModelLanguage(SBOLValue):
        label = "ModelLanguage"   
    ModelLanguage.constantList = ["true"]
    ModelLanguage.equivalent_to.append(EDAM_format_2585 | EDAM_format_3240 | EDAM_format_3156)

    # ---------SBOL properties---------
    class comprises(ObjectProperty, TransitiveProperty):
        label = "comprises"

    class directlyComprises(comprises, ObjectProperty):
        label = "directlyComprises"

    #Identified properties
    class displayId(DataProperty, FunctionalProperty):
        label = "displayId"
        domain = [Identified]
        range = [str]

    class name(DataProperty, FunctionalProperty):
        label = "name"
        domain = [Identified]
        range = [str]

    class description(DataProperty, FunctionalProperty):
        label = "description"
        domain = [Identified]
        range = [str]

    class hasMeasure(directlyComprises, Identified >> om.Measure):
        label = "hasMeasure"
        #domain = [Identified]
        #range = [om.Measure]

    # TopLevel properties
    class hasNamespace(ObjectProperty, FunctionalProperty):
        label = "hasNamespace"
        domain = [TopLevel]
    TopLevel.is_a.append(hasNamespace.some(Thing))

    class hasAttachment(TopLevel >> Attachment):
        label = "hasAttachment"

    # Sequence properties
    class elements(DataProperty, FunctionalProperty):
        label = "elements"
        domain = [Sequence]
        range = [str]
    # Sequence.is_a.append(elements.some(str))

    class encoding(ObjectProperty, FunctionalProperty):
        label = "encoding"
        domain = [Sequence]

    # Component properties
    #Some of these properties are used also for entities.
    class type(ObjectProperty):
        label = "type"
        domain = [Component | LocalSubComponent | ExternallyDefined | Interaction | SBOLActivity | SBOLMeasure]
    Component.is_a.append(type.some(Thing))
    Component.is_a.append(type.some(ComponentType))
    Component.is_a.append(type.max(1, ComponentType))
    LocalSubComponent.is_a.append(type.some(Thing))
    ExternallyDefined.is_a.append(type.some(Thing))
    Interaction.is_a.append(type.some(Thing))

    class role(ObjectProperty):
        label = "role"
        domain = [Component | Feature | Participation]
    Participation.is_a.append(role.some(Thing))

    class hasSequence(ObjectProperty):
        label = "hasSequence"
        domain = [Component | Location]
        range= [Sequence]
    Location.is_a.append(hasSequence.some(Sequence))
    Location.is_a.append(hasSequence.max(1,Sequence))
    
    class hasFeature(directlyComprises, ObjectProperty):
        label = "hasFeature"
        domain = [Component]
        range= [Feature]

    class refersTo(ObjectProperty, FunctionalProperty):
        label = "refersTo"
        domain = [ComponentReference]
        range= [Feature]
    ComponentReference.is_a.append(refersTo.some(Feature))
    #ComponentReference.is_a.append(refersTo.max(1,Feature)) #Alternative modelling approach. This would also work. Left it as an example for now.

    class hasInteraction(directlyComprises, Component >> Interaction):
        label = "hasInteraction"

    class hasConstraint(directlyComprises, Component >> Constraint):
        label = "hasConstraint"

    class hasModel(Component >> Model):
        label = "hasModel"

    class hasInterface(directlyComprises, Component >> Interface, FunctionalProperty):
        label = "hasInterface"

    # Feature properties
    class orientation(ObjectProperty, FunctionalProperty):
        label = "orientation"
        domain = [Feature | Location]
        range = [Orientation]

    # SubComponent properties
    class roleIntegration(ObjectProperty, FunctionalProperty):
        label = "roleIntegration"
        domain = [SubComponent]

    class instanceOf(SubComponent >> Component, FunctionalProperty):
        label = "instanceOf"
    SubComponent.is_a.append(instanceOf.some(Component))

    class sourceLocation(directlyComprises, SubComponent >> Location):
        label = "sourceLocation"

    class hasLocation(directlyComprises, ObjectProperty):
        label = "hasLocation"
        domain = [SubComponent | LocalSubComponent | SequenceFeature]
        range = [Location]
    SequenceFeature.is_a.append(hasLocation.some(Location))

    # ComponentReference properties
    class inChildOf(ComponentReference >> SubComponent, FunctionalProperty):
        label = "inChildOf"
    ComponentReference.is_a.append(inChildOf.some(Component))

    # ExternallyDefined properties
    class definition(ObjectProperty, FunctionalProperty):
        label = "definition"
        domain = [ExternallyDefined]
    ExternallyDefined.is_a.append(definition.some(Thing))

    # Location properties
    class order(DataProperty, FunctionalProperty):
        label = "order"
        domain = [Location]
        #range = [int]
        range= [ConstrainedDatatype(int, min_inclusive = 1)]

    # Range properties
    class start(DataProperty, FunctionalProperty):
        label = "start"
        domain = [Range]
        range= [ConstrainedDatatype(int, min_inclusive = 1)]
    Range.is_a.append(start.some(ConstrainedDatatype(int, min_inclusive = 1)))

    class end(DataProperty, FunctionalProperty):
        label = "end"
        domain = [Range]
        range= [ConstrainedDatatype(int, min_inclusive = 1)]
    Range.is_a.append(end.some(ConstrainedDatatype(int, min_inclusive = 1)))

    # Cut properties
    class at(DataProperty, FunctionalProperty):
        label = "at"
        domain = [Cut]
        range= [ConstrainedDatatype(int, min_inclusive = 0)]
    Cut.is_a.append(at.some(ConstrainedDatatype(int, min_inclusive = 0)))

    # Constraint properties
    class restriction(ObjectProperty, FunctionalProperty):
        label = "restriction"
        domain = [Constraint]
    Constraint.is_a.append(restriction.some(Thing))

    class subject(Constraint >> Feature, FunctionalProperty):
        label = "subject"
    Constraint.is_a.append(subject.some(Feature))

    class object(Constraint >> Feature, FunctionalProperty):
        label = "object"
    Constraint.is_a.append(object.some(Feature))

    # Interaction properties
    class hasParticipation(directlyComprises, Interaction >> Participation):
        label = "hasParticipation"

    # Participation properties
    class participant(Participation >> Feature, FunctionalProperty):
        label = "participant"

    class higherOrderParticipant(Participation >> Interaction, FunctionalProperty):
        label = "higherOrderParticipant"

    # Interface properties
    class input(Interface >> Feature):
        label = "input"

    class output(Interface >> Feature):
        label = "output"

    class nondirectional(Interface >> Feature):
        label = "nondirectional"

    #CombinatorialDerivation properties
    class strategy(ObjectProperty, FunctionalProperty):
        label = "strategy"
        domain = [CombinatorialDerivation]
        range = [enumerate | sample]

    class template(CombinatorialDerivation >> Component, FunctionalProperty):
        label = "template"
    CombinatorialDerivation.is_a.append(template.some(Component))

    class hasVariableFeature(directlyComprises, CombinatorialDerivation >> VariableFeature):
        label = "hasVariableFeature"

    #VariableFeature properties
    class cardinality(ObjectProperty, FunctionalProperty):
        label = "cardinality"
        domain = [VariableFeature]
        range = [zeroOrOne | one | zeroOrMore | oneOrMore]
    VariableFeature.is_a.append(cardinality.some(Cardinality))

    class variable(VariableFeature >> Feature, FunctionalProperty):
        label = "variable"
    VariableFeature.is_a.append(variable.some(Feature))

    class variantMeasure(VariableFeature >> om.Measure):
        label = "variantMeasure"

    class variantDerivation(VariableFeature >> CombinatorialDerivation):
        label = "variantDerivation"

    class variantCollection(VariableFeature >> Collection):
        label = "variantCollection"

    class variant(VariableFeature >> Component):
        label = "variant"

    #Implementation properties
    class built(Implementation>> Component, FunctionalProperty):
        label = "built"

    # Model properties
    class source(ObjectProperty, FunctionalProperty):
        label = "source"
        domain = [Model | Attachment]
    Model.is_a.append(source.some(Thing))
    Attachment.is_a.append(source.some(Thing))

    class language(ObjectProperty, FunctionalProperty):
        label = "language"
        domain = [Model]
    Model.is_a.append(language.some(Thing))

    class framework(ObjectProperty, FunctionalProperty):
        label = "framework"
        domain = [Model]
    Model.is_a.append(framework.some(Thing))

    #Collection properties
    class member(Collection >> TopLevel):
        label = "member"

    #Attachment properties
    class format(ObjectProperty, FunctionalProperty):
        label = "format"
        domain = [Attachment]

    class size(DataProperty, FunctionalProperty):
        label = "size"
        domain = [Attachment]
        range= [ConstrainedDatatype(int, min_inclusive = 0)]

    class hash(DataProperty, FunctionalProperty):
        label = "hash"
        domain = [Attachment]
        range= [str]

    class hashAlgorithm(DataProperty, FunctionalProperty):
        label = "hashAlgorithm"
        domain = [Attachment]
        range= [str]

    #Sequence related subclasses
    class SequenceWithElements (Sequence):
        label = "Sequence With Elements"
    SequenceWithElements.equivalent_to.append(Sequence & elements.some(str) & encoding.some(Encoding))

    class DNASequence (SequenceWithElements):
        label = "DNA Sequence"
    DNASequence.domainEntity = ["true"]
    DNASequence.equivalent_to.append(SequenceWithElements & encoding.some(EDAM_format_1207))

    class RNASequence (SequenceWithElements):
        label = "RNA Sequence"
    RNASequence.domainEntity = ["true"]
    RNASequence.equivalent_to.append(SequenceWithElements & encoding.some(EDAM_format_1207))

    class ProteinSequence (SequenceWithElements):
        label = "Protein Sequence"
    ProteinSequence.domainEntity = ["true"]
    ProteinSequence.equivalent_to.append(SequenceWithElements & encoding.some(EDAM_format_1208))

    class InChISequence (SequenceWithElements):
        label = "InChI Sequence"
    InChISequence.domainEntity = ["true"]
    InChISequence.equivalent_to.append(SequenceWithElements & encoding.some(EDAM_format_1197))

    class SMILESSequence (SequenceWithElements):
        label = "SMILES Sequence"
    SMILESSequence.domainEntity = ["true"]
    SMILESSequence.equivalent_to.append(SequenceWithElements & encoding.some(EDAM_format_1196))

    #Component related subclasses
    class DNAComponent (Component):
        label = "DNA Component"
    DNAComponent.domainEntity = ["true"]
    DNAComponent.equivalent_to.append(Component & type.some(SBO_0000251) & role.some(DNARole) & hasSequence.only(DNASequence))

    class RNAComponent (Component):
        label = "RNA Component"
    RNAComponent.domainEntity = ["true"]
    RNAComponent.equivalent_to.append(Component & type.some(SBO_0000250) & role.some(RNARole) & hasSequence.only(RNASequence))

    class ProteinComponent (Component):
        label = "Protein Component"
    ProteinComponent.domainEntity = ["true"]
    ProteinComponent.equivalent_to.append(Component & type.some(SBO_0000252) & role.some(ProteinRole) & hasSequence.only(ProteinSequence))

    class SimpleChemicalComponent (Component):
        label = "Simple Chemical Component"
    SimpleChemicalComponent.domainEntity = ["true"]
    SimpleChemicalComponent.equivalent_to.append(Component & type.some(SBO_0000247) & role.some(SmallMoleculeRole) & hasSequence.only(InChISequence | SMILESSequence))

    class NonCovalentComplexComponent (Component):
        label = "Non-Covalent Complex Component"
    NonCovalentComplexComponent.domainEntity = ["true"]
    NonCovalentComplexComponent.equivalent_to.append(Component & type.some(SBO_0000253))

    class FunctionalEntityComponent (Component):
        label = "Functional Entity Component"
    FunctionalEntityComponent.domainEntity = ["true"]
    FunctionalEntityComponent.equivalent_to.append(Component & type.some(SBO_0000241))

    #DNA Component subclasses
    class GenericDNAComponent (DNAComponent):
        label = "Generic DNA Component"
    GenericDNAComponent.domainEntity = ["true"]
    GenericDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000110))
    
    class PromoterDNAComponent (DNAComponent):
        label = "Promoter DNA Component"
    PromoterDNAComponent.domainEntity = ["true"]
    PromoterDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000167))

    class RBSDNAComponent (DNAComponent):
        label = "RBS DNA Component"
    RBSDNAComponent.domainEntity = ["true"]
    RBSDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000139))

    class CDSDNAComponent (DNAComponent):
        label = "CDS DNA Component"
    CDSDNAComponent.domainEntity = ["true"]
    CDSDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000316))

    class TerminatorDNAComponent (DNAComponent):
        label = "Terminator DNA Component"
    TerminatorDNAComponent.domainEntity = ["true"]
    TerminatorDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000141))

    class GeneDNAComponent (DNAComponent):
        label = "Gene DNA Component"
    GeneDNAComponent.domainEntity = ["true"]
    GeneDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000704))

    class OperatorDNAComponent (DNAComponent):
        label = "Operator DNA Component"
    OperatorDNAComponent.domainEntity = ["true"]
    OperatorDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000057))

    class EngineeredRegionDNAComponent (DNAComponent):
        label = "Engineered Region DNA Component"
    EngineeredRegionDNAComponent.domainEntity = ["true"]
    EngineeredRegionDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000804))

    #SimpleChemicalComponent subclasses
    class EffectorSimpleChemicalComponent (SimpleChemicalComponent):
        label = "Effector Simple Chemical Component"
    EffectorSimpleChemicalComponent.domainEntity = ["true"]
    EffectorSimpleChemicalComponent.equivalent_to.append(SimpleChemicalComponent & role.some(CHEBI_35224))

    #ProteinComponent subclasses
    class TranscriptionFactorProteinComponent (ProteinComponent):
        label = "Transcription Factor Protein Component"
    TranscriptionFactorProteinComponent.domainEntity = ["true"]
    TranscriptionFactorProteinComponent.equivalent_to.append(ProteinComponent & role.some(GO_0003700))

    # Participation subclasses
    class InhibitorParticipation (Participation):
        label = "InhibitorParticipant"
    InhibitorParticipation.domainEntity = ["true"]
    InhibitorParticipation.equivalent_to.append(Participation & role.some(SBO_0000020))

    class InhibitedParticipation (Participation):
        label = "InhibitedParticipation"
    InhibitedParticipation.domainEntity = ["true"]
    InhibitedParticipation.equivalent_to.append(Participation & role.some(SBO_0000642))

    class StimulatorParticipation (Participation):
        label = "StimulatorParticipation"
    StimulatorParticipation.domainEntity = ["true"]
    StimulatorParticipation.equivalent_to.append(Participation & role.some(SBO_0000459))

    class StimulatedParticipation (Participation):
        label = "StimulatedParticipation"
    StimulatedParticipation.domainEntity = ["true"]
    StimulatedParticipation.equivalent_to.append(Participation & role.some(SBO_0000643))

    class ReactantParticipation (Participation):
        label = "ReactantParticipation"
    ReactantParticipation.domainEntity = ["true"]
    ReactantParticipation.equivalent_to.append(Participation & role.some(SBO_0000010))

    class ProductParticipation (Participation):
        label = "ProductParticipation"
    ProductParticipation.domainEntity = ["true"]
    ProductParticipation.equivalent_to.append(Participation & role.some(SBO_0000011))

    class PromoterParticipation (Participation):
        label = "PromoterParticipation"
    PromoterParticipation.domainEntity = ["true"]
    PromoterParticipation.equivalent_to.append(Participation & role.some(SBO_0000598))

    class ModifierParticipation (Participation):
        label = "ModifierParticipation"
    ModifierParticipation.domainEntity = ["true"]
    ModifierParticipation.equivalent_to.append(Participation & role.some(SBO_0000019))

    class ModifiedParticipation (Participation):
        label = "ModifiedParticipation"
    ModifiedParticipation.domainEntity = ["true"]
    ModifiedParticipation.equivalent_to.append(Participation & role.some(SBO_0000644))

    class TemplateParticipation (Participation):
        label = "TemplateParticipation"
    TemplateParticipation.domainEntity = ["true"]
    TemplateParticipation.equivalent_to.append(Participation & role.some(SBO_0000645))

    class InhibitionInteraction (Interaction):
        label = "InhibitionInteraction"
    InhibitionInteraction.domainEntity = ["true"]
    InhibitionInteraction.equivalent_to.append(Interaction & type.some(SBO_0000169) & participant.some(InhibitorParticipation) &  participant.some(InhibitedParticipation))

    class StimulationInteraction (Interaction):
        label = "StimulationInteraction"
    StimulationInteraction.domainEntity = ["true"]
    StimulationInteraction.equivalent_to.append(Interaction & type.some(SBO_0000170) & participant.some(StimulatedParticipation) &  participant.some(StimulatorParticipation))

    class DegradationInteraction (Interaction):
        label = "DegradationInteraction"
    DegradationInteraction.domainEntity = ["true"]
    DegradationInteraction.equivalent_to.append(Interaction & type.some(SBO_0000179) &  participant.some(ReactantParticipation))
    
    class BiochemicalReactionInteraction (Interaction):
        label = "BiochemicalReactionInteraction"
    BiochemicalReactionInteraction.domainEntity = ["true"]
    BiochemicalReactionInteraction.equivalent_to.append(Interaction & type.some(SBO_0000176) & participant.min(0, ModifierParticipation) & participant.min(0, ModifiedParticipation) & participant.min(0, ProductParticipation) & participant.min(0, ReactantParticipation) )

    class NonCovalentBindingInteraction (Interaction):
        label = "NonCovalentBindingInteraction"
    NonCovalentBindingInteraction.domainEntity = ["true"]
    NonCovalentBindingInteraction.equivalent_to.append(Interaction & type.some(SBO_0000177) & participant.some(ReactantParticipation) & participant.some(ProductParticipation))
    
    class GeneticProductionInteraction (Interaction):
        label = "GeneticProductionInteraction"
    GeneticProductionInteraction.domainEntity = ["true"]
    GeneticProductionInteraction.equivalent_to.append(Interaction & type.some(SBO_0000589) & participant.some(TemplateParticipation) & participant.exactly(1, ProductParticipation))
    
    class ControlInteraction (Interaction):
        label = "ControlInteraction"
    ControlInteraction.domainEntity = ["true"]
    ControlInteraction.equivalent_to.append(Interaction & type.some(SBO_0000168) & participant.some(ModifierParticipation) & participant.some(ModifiedParticipation))

with prov:
  # sbol3:Identified prov properties
  class wasDerivedFrom(ObjectProperty):
      label = "wasDerivedFrom"
      domain = [sbol3.Identified]
      range = [Thing]

   # wasInformedBy [0..*]: Activity -> TopLevel
  class wasInformedBy(ObjectProperty):
      label = "wasInformedBy"
      domain = [Activity]
      range = [Activity]

  # prov:Activity properties
  # Identified -> Activity - [0..*]
  class wasGeneratedBy(ObjectProperty):
      label = "wasGeneratedBy"
      domain = [sbol3.Identified]
      range = [sbol3.SBOLActivity]

  # [0..1]
  class startedAtTime(DataProperty, FunctionalProperty):
      label = "startedAtTime"
      domain = [Activity]
      range = [datetime.datetime]

  # [0..1]
  class endedAtTime(DataProperty, FunctionalProperty):
    label = "endedAtTime"
    domain = [Activity]
    range = [datetime.datetime]

  # Activity -> Usage - [0..*]
  class qualifiedUsage(ObjectProperty):
    label = "qualifiedUsage"
    domain = [Activity]
    range = [Usage]

  # Activity -> Association - [0..*]
  class qualifiedAssociation(ObjectProperty):
    label = "qualifiedAssociation"
    domain = [Activity]
    range = [Association]

  # prov:Usage properties
  # [1..1]
  class entity(ObjectProperty, FunctionalProperty):
    label = "entity"
    domain = [Usage]
  SBOLUsage.is_a.append(entity.some(Thing))

  # [0..*]
  class hadRole(ObjectProperty):
    label = "hadRole"
    domain = [Usage | Association]

  # prov:Association properties
  # Association -> Plan - [0..1]
  class hadPlan(ObjectProperty, FunctionalProperty):
      label = "hadPlan"
      domain = [Association]
      range = [Plan]

  # Association -> Agent - [1..1]
  class agent(ObjectProperty, FunctionalProperty):
    label = "agent"
    domain = [Association]
    range = [Agent]
  Association.is_a.append(agent.some(Agent))

# OM (Units of Measure) classes
with om:
  class Unit(Thing):
    label = "Unit"
  Unit.is_a.append(rdfs.label.some(str))
  #TODO:Open again later: SBOLUnit.is_a.append(rdfs.comment.max(1, str)). This needs to be checked with the commnunity.

  class SingularUnit(Unit):
    label = "SingularUnit"

  class CompoundUnit(Unit):
    label = "CompoundUnit"

  class PrefixedUnit(Unit):
    label = "PrefixedUnit"

  class UnitMultiplication(Unit):
    label = "UnitMultiplication"

  class UnitDivision(Unit):
    label = "UnitDivision"

  class UnitExponentiation(Unit):
      label = "UnitExponentiation"

  class Prefix(Thing):
      label = "Prefix"
  Prefix.is_a.append(rdfs.label.some(str))
  #TODO:Open again later: SBOLPrefix.is_a.append(rdfs.comment.max(1, str)). This should also be checked with the community.

  class SIPrefix(Prefix):
      label = "SIPrefix"

  class BinaryPrefix(Prefix):
      label = "BinaryPrefix"

with sbol3:
  class SBOLUnit(TopLevel):
    label = "Unit"
  SBOLUnit.domainEntity = ["true"]
  SBOLUnit.replacementOf = [om.Unit]
  SBOLUnit.is_a.append(om.Unit)
  
  class SBOLSingularUnit(SBOLUnit):
    label = "SingularUnit"
  SBOLSingularUnit.domainEntity = ["true"]
  SBOLSingularUnit.replacementOf = [om.SingularUnit]
  SBOLSingularUnit.is_a.append(om.SingularUnit)

  class SBOLCompoundUnit(SBOLUnit):
    label = "CompoundUnit"
  SBOLCompoundUnit.domainEntity = ["true"]
  SBOLCompoundUnit.replacementOf = [om.CompoundUnit]
  SBOLCompoundUnit.is_a.append(om.CompoundUnit)

  class SBOLPrefixedUnit(SBOLUnit):
    label = "PrefixedUnit"
  SBOLPrefixedUnit.domainEntity = ["true"]
  SBOLPrefixedUnit.replacementOf = [om.PrefixedUnit]
  SBOLPrefixedUnit.is_a.append(om.PrefixedUnit)

  class SBOLUnitMultiplication(SBOLUnit):
    label = "UnitMultiplication"
  SBOLUnitMultiplication.domainEntity = ["true"]
  SBOLUnitMultiplication.replacementOf = [om.UnitMultiplication]
  SBOLUnitMultiplication.is_a.append(om.UnitMultiplication)

  class SBOLUnitDivision(SBOLUnit):
    label = "UnitDivision"
  SBOLUnitDivision.domainEntity = ["true"]
  SBOLUnitDivision.replacementOf = [om.UnitDivision]
  SBOLUnitDivision.is_a.append(om.UnitDivision)

  class SBOLUnitExponentiation(SBOLUnit):
    label = "UnitExponentiation"
  SBOLUnitExponentiation.domainEntity = ["true"]
  SBOLUnitExponentiation.replacementOf = [om.UnitExponentiation]
  SBOLUnitExponentiation.is_a.append(om.UnitExponentiation)

  class SBOLPrefix(TopLevel):
    label = "Prefix"
  SBOLPrefix.domainEntity = ["true"]
  SBOLPrefix.replacementOf = [om.Prefix]
  SBOLPrefix.is_a.append(om.Prefix)
  

  class SBOLSIPrefix(SBOLPrefix):
    label = "SIPrefix"
  SBOLSIPrefix.domainEntity = ["true"]
  SBOLSIPrefix.replacementOf = [om.SIPrefix]
  SBOLSIPrefix.is_a.append(om.SIPrefix)

  class SBOLBinaryPrefix(SBOLPrefix):
    label = "BinaryPrefix"
  SBOLBinaryPrefix.domainEntity = ["true"]
  SBOLBinaryPrefix.replacementOf = [om.BinaryPrefix]
  SBOLBinaryPrefix.is_a.append(om.BinaryPrefix)

  #Disjoint classes
  AllDisjoint([SubComponent, ComponentReference, LocalSubComponent, ExternallyDefined, SequenceFeature])
  AllDisjoint([Range,Cut, EntireSequence])
  AllDisjoint([Component, Sequence, Model, Implementation, Attachment, Collection, ExperimentalData, CombinatorialDerivation, SBOLActivity, SBOLPlan, SBOLAgent, SBOLMeasure, SBOLBinaryPrefix, SBOLSIPrefix, SBOLUnitMultiplication, SBOLUnitDivision, SBOLUnitExponentiation, SBOLPrefixedUnit, SBOLCompoundUnit, SBOLSingularUnit])


# OM Object Properties
with om:
  #[1-1]
  class hasNumericalValue(DataProperty, FunctionalProperty):
    label = ["hasNumericalValue"]
    domain = [Measure]
    range  = [float]
  Measure.is_a.append(hasNumericalValue.some(float))
  
  class hasUnit(ObjectProperty, FunctionalProperty):
    label = ["hasUnit"]
    domain = [Measure | SingularUnit |PrefixedUnit] #[1..0]
    range  = [Unit]
  Measure.is_a.append(hasUnit.some(Unit)) #[1..1]
  PrefixedUnit.is_a.append(hasUnit.some(Unit)) #[1..1]

  class symbol(DataProperty, FunctionalProperty):
    label = ["symbol"]
    domain = [Unit | Prefix]
    range  = [float]
  Unit.is_a.append(symbol.some(float)) # [1..]
  Prefix.is_a.append(symbol.some(float)) # [1..]

  #[1..0]
  class alternativeSymbol(DataProperty):
    label = ["alternativeSymbol"]
    domain = [Unit | Prefix]
    range  = [str]

  #[1..0]
  class alternativeLabel(DataProperty):
    label = ["alternativeSymbol"]
    domain = [Unit | Prefix]
    range  = [str]

  #[1..0]
  class longComment(DataProperty, FunctionalProperty):
    label = ["longcomment"]
    domain = [Unit | Prefix]
    range  = [str]

  class hasFactor(DataProperty):
    label = ["hasFactor"]
    domain = [SingularUnit | Prefix] #[1..0]
    range  = [float]
  Prefix.is_a.append(hasFactor.some(float)) #[1..1]

  #[1..1]
  class hasTerm1(ObjectProperty, FunctionalProperty):
    domain = [UnitMultiplication]
    range  = [Unit]
  UnitMultiplication.is_a.append(hasTerm1.some(Unit))

  #[1..1]
  class hasTerm2(ObjectProperty, FunctionalProperty):
    domain = [UnitMultiplication]
    range  = [Unit]
  UnitMultiplication.is_a.append(hasTerm2.some(Unit))

  #[1..1]
  class hasNumerator(ObjectProperty,FunctionalProperty):
    domain = [UnitDivision]
    range  = [Unit]
  UnitDivision.is_a.append(hasNumerator.some(Unit))

  #[1..1]
  class hasDenominator(ObjectProperty,FunctionalProperty):
    domain = [UnitDivision]
    range  = [Unit]
  UnitDivision.is_a.append(hasDenominator.some(Unit))

  #[1..1]
  class hasBase(ObjectProperty,FunctionalProperty):
    domain = [UnitExponentiation]
    range  = [Unit]
  UnitExponentiation.is_a.append(hasBase.some(Unit))

  #[1..1]
  class hasExponent(DataProperty,FunctionalProperty):
    domain = [UnitExponentiation]
    range  = [int]
  UnitExponentiation.is_a.append(hasExponent.some(int))
  
  #[1..1]
  class hasPrefix(ObjectProperty,FunctionalProperty):
    domain = [PrefixedUnit]
    range  = [Prefix]
  PrefixedUnit.is_a.append(hasPrefix.some(Prefix))


# Temporary outputs will be in ../supplementary, main ontology files (sbol3.rdf, sbol3.owl, sbol3.ofn, sbol3.omn) will be in the parent folder. 
SUPP = Path(__file__).parent.parent / "supplementary"
MAIN = Path(__file__).parent.parent
os.makedirs(SUPP, exist_ok=True)

# Save individual ontologies: sbol3core.rdf, sbo.rdf, so.rdf, edam.rdf, chebi.rdf, go.rdf, om.rdf, prov.rdf, otol.rdf
sbol3.save(file = str(SUPP / "sbol3core.rdf"), format = "rdfxml")
sbo.save(file = str(SUPP / "sbo.rdf"), format = "rdfxml")
so.save(file = str(SUPP / "so.rdf"), format = "rdfxml")
edam.save(file = str(SUPP / "edam.rdf"), format = "rdfxml")
chebi.save(file = str(SUPP / "chebi.rdf"), format = "rdfxml")
go.save(file = str(SUPP / "go.rdf"), format = "rdfxml")
om.save(file = str(SUPP / "om.rdf"), format = "rdfxml")
prov.save(file = str(SUPP / "prov.rdf"), format = "rdfxml")
otol.save(file = str(SUPP / "otol.rdf"), format = "rdfxml")

from rdflib import URIRef

# Merges  ontologies into a single combined rdf file
def mergeOntologies(inputFiles, rdfOutputFile):
    combined = Graph()
    for f in inputFiles:
        combined.parse(f, format="xml")
    # Keep only the sbol3 owl:Ontology declaration — remove all others so the OWL API does not randomly choose one of the other ontlogies (SBO, SO, CHEBI, GO, PROV, OM)
    sbol3IRI = URIRef(sbol3.base_iri)
    for ontology in list(combined.subjects(RDF.type, OWL.Ontology)):
        if ontology != sbol3IRI:
            combined.remove((ontology, RDF.type, OWL.Ontology))
    combined.add((sbol3IRI, RDF.type, OWL.Ontology))
    combined.serialize(destination=rdfOutputFile, format="xml")

#Create sbol3.rdf by merging the individual ontologies. From sbol3core.rdf, sbo.rdf, so.rdf, edam.rdf, chebi.rdf, go.rdf, om.rdf, prov.rdf, otol.rdf. 
mergeOntologies(
    [SUPP / "sbol3core.rdf", SUPP / "sbo.rdf", SUPP / "so.rdf", SUPP / "edam.rdf", SUPP / "chebi.rdf", SUPP / "go.rdf", SUPP / "om.rdf", SUPP / "prov.rdf", SUPP / "otol.rdf"],
    MAIN / "sbol3.rdf"
)

# Also create a merged file for the SBOL-OM-PROV subset, since SBOL imports  a subset of prov-o and om2.
mergeOntologies(
    [SUPP / "sbol3core.rdf", SUPP / "om.rdf", SUPP / "prov.rdf"],
    SUPP / "sbol3core_om_prov.rdf"
)

# Convert to OWL, OWL Functional, and Manchester Syntax
import subprocess, os
def createOWL(robotJar, inputFile, outputFiles, prefixes):
    if not os.path.isfile(robotJar):
        print("robot.jar could not be found on the current folder. Could not create the ontology files!")
        return
    for outputFile in outputFiles:
        cliCmd = ["java", "-jar", robotJar, "convert"]
        for prefix, namespace in prefixes:
            cliCmd += ["--add-prefix", f"{prefix}: {namespace}"]
        cliCmd += ["-i", inputFile, "-o", outputFile]
        cliResult = subprocess.run(cliCmd, capture_output=True, text=True)
        if cliResult.returncode != 0:
            print(f"{outputFile} conversion failed:", cliResult.stderr.strip())
        else:
            print(f"{outputFile} created!")
    
    # Replace identifiers.org URIs with identifiers:localname. This is due to the OWL-API behaviour. It does not shorten local names with colons or starting with digits.
    identifiersPattern = re.compile(r'<https://identifiers\.org/([^>]+)>')
    for fileName in outputFiles:
        file = Path(fileName)
        if not file.is_file() or file.suffix not in (".omn", ".ofn"):
            continue
        file.write_text(identifiersPattern.sub(r'identifiers:\1', file.read_text(encoding="utf-8")), encoding="utf-8")
        print(f"{fileName} - identifiers prefix applied!")

robotJarFile = Path(__file__).parent / "robot.jar"
owlPrefixes = [
    ("sbol", sbol3.base_iri),
    ("om", om.base_iri),
    ("identifiers", "https://identifiers.org/"),
    ("prov", prov.base_iri),
    ("otol", otol.base_iri)]

createOWL(robotJarFile, MAIN / "sbol3.rdf",
    [MAIN / "sbol3.owl", MAIN / "sbol3.ofn", MAIN / "sbol3.omn"],
    owlPrefixes)
createOWL(robotJarFile, SUPP / "sbol3core_om_prov.rdf",
    [SUPP / "sbol3core_om_prov.owl", SUPP / "sbol3core_om_prov.ofn", SUPP / "sbol3core_om_prov.omn"],
    owlPrefixes)

#Expects a set of tuples for: rdf input file, html output file, and the ontology title
#prefixes: list of (prefix, namespace) pairs
def createHTML(ontologies, prefixes=None):
    try:
        # Workaround for the pyLODE.pyproject.toml file issue. The following code creates a minimal pyproject.toml in the site-packages folder if it doesn't already exist. If the distribution does not include this file, then pyLODE fails!
        import site
        tomlFile = Path(site.getsitepackages()[0]) / "pyproject.toml"
        if not tomlFile.exists():
            tomlFile.write_text(f'[project]\nversion = "{version("pylode")}"\n', encoding="utf-8")

        import logging
        import pylode
        from pylode import OntPub
        from rdflib import Literal, Graph, URIRef
        from rdflib.namespace import DCTERMS
        # Set the logger level to avoid pylode debug and info messages
        logging.getLogger("root").setLevel(logging.WARNING)
        logging.getLogger("asyncio").setLevel(logging.WARNING)
        print(f"Python version\t: {sys.version}")
        print(f"pyLODE version\t: {pylode.__version__}")
        print(f"pyLODE file\t: {pylode.__file__}")
        for ontFile, htmlFile, title in ontologies:
            graph = Graph()
            graph.parse(ontFile, format="xml")
            sbolIRI = URIRef(sbol3.base_iri)
            if prefixes:
                for prefix, namespace in prefixes:
                    graph.bind(prefix, namespace, override=True, replace=True)
            graph.add((sbolIRI, DCTERMS.title, Literal(title)))
            OntPub(ontology=graph).make_html(destination=htmlFile)
            print(f"{htmlFile} created!")
    except Exception as e:
        print(f"{htmlFile} could not be created: {e}")

print("\nCreating the HTML files:")      
createHTML([
    (MAIN / "sbol3.rdf", MAIN / "sbol3.html", "SBOL3 Ontology"),
    (SUPP / "sbol3core_om_prov.rdf", SUPP / "sbol3core_om_prov.html", "SBOL3 Core Ontology")
], owlPrefixes)

print ("\ndone!")