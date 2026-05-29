'''
Created on 26 May 2021

@author: gokselmisirli
@author: metehanunal
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
    SBO_0000000.label = ["systems biology representation"]
    SBO_0000000.comment = ["Representation of an entity used in a systems biology knowledge reconstruction, such as a model, pathway, network."]

    SBO_0000236 = types.new_class("0000236", (SBO_0000000,))
    SBO_0000236.label = ["physical entity representation"]
    SBO_0000236.comment = ["Synonym: new synonym"]

    SBO_0000251 = types.new_class("0000251", (SBO_0000236,))
    SBO_0000251.label = ["deoxyribonucleic acid"]
    SBO_0000251.comment = ["Synonym: DNA"]

    SBO_0000250 = types.new_class("0000250", (SBO_0000236,))
    SBO_0000250.label = ["ribonucleic acid"]
    SBO_0000250.comment = ["Synonym: RNA"]

    SBO_0000252 = types.new_class("0000252", (SBO_0000236,))
    SBO_0000252.label = ["polypeptide chain"]
    SBO_0000252.comment = ["Naturally occurring macromolecule formed by the repetition of amino-acid residues linked by peptidic bonds. A polypeptide chain is synthesized by the ribosome."]

    SBO_0000247 = types.new_class("0000247", (SBO_0000236,))
    SBO_0000247.label = ["simple chemical"]
    SBO_0000247.comment = ["Simple, non-repetitive chemical entity."]

    SBO_0000253 = types.new_class("0000253", (SBO_0000236,))
    SBO_0000253.label = ["non-covalent complex"]
    SBO_0000253.comment = ["Entity composed of several independant components that are not linked by covalent bonds."]

    SBO_0000241 = types.new_class("0000241", (SBO_0000236,))
    SBO_0000241.label = ["functional entity"]
    SBO_0000241.comment = ["A real thing, defined by its properties or the actions it performs, rather than it physico-chemical structure."]

    # Occurring Entity Representation (parent for interactions)
    SBO_0000231 = types.new_class("0000231", (SBO_0000000,))
    SBO_0000231.label = ["occurring entity representation"]
    SBO_0000231.comment = ["Representation of an entity that manifests, unfolds or develops through time, such as a discrete event, or a mutual or reciprocal action or influence that happens between participating physical entities, and/or other occurring entities."]

    # Biochemical or transport reaction
    SBO_0000167 = types.new_class("0000167", (SBO_0000231,))
    SBO_0000167.label = ["biochemical or transport reaction"]
    SBO_0000167.comment = ["An event involving physical entities that results in modification of structure, location, or free energy."]

    # Biochemical reaction
    SBO_0000176 = types.new_class("0000176", (SBO_0000167,))
    SBO_0000176.label = ["biochemical reaction"]
    SBO_0000176.comment = ["An event involving one or more chemical entities that modifies the electrochemical structure of at least one of the participants."]

    # Non-covalent binding
    SBO_0000177 = types.new_class("0000177", (SBO_0000176,))
    SBO_0000177.label = ["non-covalent binding"]
    SBO_0000177.comment = ["Synonym: association"]

    # Degradation
    SBO_0000179 = types.new_class("0000179", (SBO_0000176,))
    SBO_0000179.label = ["degradation"]
    SBO_0000179.comment = ["Complete disappearance of a physical entity."]

    # Control
    SBO_0000168 = types.new_class("0000168", (SBO_0000231,))
    SBO_0000168.label = ["control"]
    SBO_0000168.comment = ["Synonym: regulation"]

    # Inhibition
    SBO_0000169 = types.new_class("0000169", (SBO_0000168,))
    SBO_0000169.label = ["inhibition"]
    SBO_0000169.comment = ["Negative modulation of the execution of a process."]

    # Stimulation
    SBO_0000170 = types.new_class("0000170", (SBO_0000168,))
    SBO_0000170.label = ["stimulation"]
    SBO_0000170.comment = ["Positive modulation of the execution of a process."]

    # Genetic production
    SBO_0000589 = types.new_class("0000589", (SBO_0000231,))
    SBO_0000589.label = ["genetic production"]
    SBO_0000589.comment = ["A composite biochemical process through which a gene sequence is fully converted into mature gene products. These gene products may include RNA species as well as proteins, and the process encompasses all intermediate steps required to generate the active form of the gene product."]

    # Participant roles
    SBO_0000003 = types.new_class("0000003", (SBO_0000000,))
    SBO_0000003.label = ["participant role"]
    SBO_0000003.comment = ["The function of a physical or conceptual entity, that is its role, in the execution of an event or process."]

    # Modifier
    SBO_0000019 = types.new_class("0000019", (SBO_0000003,))
    SBO_0000019.label = ["modifier"]
    SBO_0000019.comment = ["Substance that changes the velocity of a process without itself being consumed or transformed by the reaction."]

    # Inhibitor
    SBO_0000020 = types.new_class("0000020", (SBO_0000019,))
    SBO_0000020.label = ["inhibitor"]
    SBO_0000020.comment = ["Substance that decreases the probability of a chemical reaction without itself being consumed or transformed by the reaction."]

    # Stimulator
    SBO_0000459 = types.new_class("0000459", (SBO_0000019,))
    SBO_0000459.label = ["stimulator"]
    SBO_0000459.comment = ["Synonym: activator"]

    # Inhibited
    SBO_0000642 = types.new_class("0000642", (SBO_0000003,))
    SBO_0000642.label = ["inhibited"]
    SBO_0000642.comment = ["Conceptual or material entity that is the object of an inhibition process, and is acted upon by an inhibitor."]

    # Stimulated
    SBO_0000643 = types.new_class("0000643", (SBO_0000003,))
    SBO_0000643.label = ["stimulated"]
    SBO_0000643.comment = ["Conceptual or material entity that is the object of a stimulation process, and is acted upon by a stimulator."]

    # Modified
    SBO_0000644 = types.new_class("0000644", (SBO_0000003,))
    SBO_0000644.label = ["modified"]
    SBO_0000644.comment = ["Conceptual or material entity that is the object of a modification process, and is acted upon by a modifier."]

    # Template
    SBO_0000645 = types.new_class("0000645", (SBO_0000003,))
    SBO_0000645.label = ["template"]
    SBO_0000645.comment = ["An entity that acts as the starting material for genetic production (http://identifiers.org/biomodels.sbo/SBO:0000589)."]

    # Functional compartment
    SBO_0000289 = types.new_class("0000289", (SBO_0000003,))
    SBO_0000289.label = ["functional compartment"]
    SBO_0000289.comment = ["Logical or physical subset of the event space that contains pools, that is sets of participants considered identical when it comes to the event they are involved into. A compartment can have any number of dimensions, including 0, and be of any size including null."]

    SBO_0000011 = types.new_class("0000011", (SBO_0000003,))
    SBO_0000011.label = ["product"]
    SBO_0000011.comment = ["Substance that is produced in a reaction. In a chemical equation the Products are the elements or compounds on the right hand side of the reaction equation. A product can be produced and consumed by the same reaction, its global quantity remaining unchanged."]

    SBO_0000010 = types.new_class("0000010", (SBO_0000003,))
    SBO_0000010.label = ["reactant"]
    SBO_0000010.comment = ["Substance consumed by a chemical reaction. Reactants react with each other to form the products of a chemical reaction. In a chemical equation the Reactants are the elements or compounds on the left hand side of the reaction equation. A reactant can be consumed and produced by the same reaction, its global quantity remaining unchanged."]

    SBO_0000598 = types.new_class("0000598", (SBO_0000003,))
    SBO_0000598.label = ["promoter"]
    SBO_0000598.comment = ["A region of DNA to which various transcription factors and RNA polymerase must bind in order to initiate transcription for a gene."]

    # Modelling framework
    SBO_0000004 = types.new_class("0000004", (SBO_0000000,))
    SBO_0000004.label = ["modelling framework"]
    SBO_0000004.comment = ["Set of assumptions that underlay a mathematical description."]

    SBO_0000062 = types.new_class("0000062", (SBO_0000004,))
    SBO_0000062.label = ["continuous framework"]
    SBO_0000062.comment = ["Modelling approach where the quantities of participants are considered continuous, and represented by real values. The associated simulation methods make use of differential equations."]
  
    SBO_0000063 = types.new_class("0000063", (SBO_0000004,))
    SBO_0000063.label = ["discrete framework"]
    SBO_0000063.comment = ["Modelling approach where the quantities of participants are considered discrete, and represented by integer values. The associated simulation methods can be deterministic or stochastic."]
  
    SBO_0000693 = types.new_class("0000693", (SBO_0000004,))
    SBO_0000693.label = ["constraint-based framework"]
    SBO_0000693.comment = ["Modelling approach which captures bounds on the possible behavior of a system, which may be further reduced using an objective function."]

    SBO_0000234 = types.new_class("0000234", (SBO_0000004,))
    SBO_0000234.label = ["logical framework"]
    SBO_0000234.comment = ["Modelling approach, pioneered by Rene Thomas and Stuart Kaufman, where the evolution of a system is described by the transitions between discrete activity states of 'genes' that control each other."]

    SBO_0000681 = types.new_class("0000681", (SBO_0000004,))
    SBO_0000681.label = ["hybrid framework"]
    SBO_0000681.comment = ["Modeling approach which combines multiple canonical modeling frameworks. For example, a hybrid model could consider both continuous (represented by real values) and discrete (represented by integers) participants. Hybrid models are executed with hybrid simulation algorithms. For example, a hybrid continuous-discrete model may be simulation using a combination of stochastic simulation and ordinary differential equations."]

with so:
    SO_0000110 = types.new_class("0000110", (Thing,))
    SO_0000110.label = ["sequence_feature"]
    SO_0000110.comment = ["Any extent of continuous biological sequence."]

    SO_0000167 = types.new_class("0000167", (SO_0000110,))
    SO_0000167.label = ["promoter"]
    SO_0000167.comment = ["This term is mapped to MGED. Do not obsolete without consulting MGED ontology. The region on a DNA molecule involved in RNA polymerase binding to initiate transcription. Moved from is_a: SO:0001055 transcriptional_cis_regulatory_region as per request from GREEKC initiative in August 2020. Merged with RNA_polymerase_promoter (SO:0001203) Aug 2020. Moved up one level from is_a CRM (SO:0000727) to is_a transcriptional_cis_regulatory_region (SO:0001055) as part of the GREEKC work January 2021. Pascale Gaudet from Gene Ontology pointed out that CRM can be located upstream of the promoter and therefore cannot include the promoter. A regulatory_region composed of the TSS(s) and binding sites for TF_complexes of the core transcription machinery. A region (DNA) to which RNA polymerase binds, to begin transcription."]

    SO_0000139 = types.new_class("0000139", (SO_0000110,))
    SO_0000139.label = ["ribosome_entry_site"]
    SO_0000139.comment = ["Region in mRNA where ribosome assembles."]

    SO_0000316 = types.new_class("0000316", (SO_0000110,))
    SO_0000316.label = ["CDS"]
    SO_0000316.comment = ["A contiguous sequence which begins with, and includes, a start codon and ends with, and includes, a stop codon."]
    
    SO_0000141 = types.new_class("0000141", (SO_0000110,))
    SO_0000141.label = ["terminator"]
    SO_0000141.comment = ["Moved from transcription_regulatory_region (SO:0001679) to transcriptional_cis_regulatory_region (SO:0001055) by Dave Sant on Feb 11, 2021 when transcription_regulatory_region was merged into transcriptional_cis_regulatory_region to be consistent with GO and reduce redundancy as part of the GREEKC consortium. See GitHub Issue #527. The sequence of DNA located either at the end of the transcript that causes RNA polymerase to terminate transcription."]

    SO_0000704 = types.new_class("0000704", (SO_0000110,))
    SO_0000704.label = ["gene"]
    SO_0000704.comment = ["This term is mapped to MGED. Do not obsolete without consulting MGED ontology. A gene may be considered as a unit of inheritance. A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene may include regulatory regions, transcribed regions and/or other functional sequence regions."]

    SO_0000057 = types.new_class("0000057", (SO_0000110,))
    SO_0000057.label = ["operator"]
    SO_0000057.comment = ["Moved to transcriptional_cis_regulatory_region (SO:0001055) from gene_group_regulatory_region (SO:0000752) on 11 Feb 2021 when SO:0000752 was merged into SO:0001055. See GitHub Issue #529. A regulatory element of an operon to which activators or repressors bind thereby effecting translation of genes in that operon."]

    SO_0000804 = types.new_class("0000804", (SO_0000110,))
    SO_0000804.label = ["engineered_region"]
    SO_0000804.comment = ["A region that is engineered."]

    SO_0000234 = types.new_class("0000234", (SO_0000110,))
    SO_0000234.label = ["mRNA"]
    SO_0000234.comment = ["An mRNA does not contain introns as it is a processed_transcript. The equivalent kind of primary_transcript is protein_coding_primary_transcript (SO:0000120) which may contain introns. This term is mapped to MGED. Do not obsolete without consulting MGED ontology. Messenger RNA is the intermediate molecule between DNA and protein. It includes UTR and coding sequences. It does not contain introns."]

    SO_0000400 = types.new_class("0000400", (Thing,))
    SO_0000400.label = ["sequence_attribute"]
    SO_0000400.comment = ["An attribute describes a quality of sequence."]

    SO_0000987 = types.new_class("0000987", (SO_0000400,))
    SO_0000987.label = ["linear"]
    SO_0000987.comment = ["Attributes added to describe the different kinds of replicon. SO workshop, September 2006. A quality of a nucleotide polymer that has a 3'-terminal residue and a 5'-terminal residue."]

    SO_0000988 = types.new_class("0000988", (SO_0000400,))
    SO_0000988.label = ["circular"]
    SO_0000988.comment = ["Attributes added to describe the different kinds of replicon. SO workshop, September 2006. A quality of a nucleotide polymer that has no terminal nucleotide residues."]

    SO_0000984 = types.new_class("0000984", (SO_0000400,))
    SO_0000984.label = ["single"]
    SO_0000984.comment = ["Attributes added to describe the different kinds of replicon. SO workshop, September 2006. When a nucleotide polymer has only one strand."]


    SO_0000985 = types.new_class("0000985", (SO_0000400,))
    SO_0000985.label = ["double"]
    SO_0000985.comment = ["Attributes added to describe the different kinds of replicon. SO workshop, September 2006. When a nucleotide polymer has two strands that are reverse-complement to one another and pair together."]


    # Orientation terms
    SO_0001030 = types.new_class("0001030", (SO_0000400,))
    SO_0001030.label = ["forward"]
    SO_0001030.comment = ["Forward is an attribute of the feature, where the feature is in the 5' to 3' direction."]

    SO_0001031 = types.new_class("0001031", (SO_0000400,))
    SO_0001031.label = ["reverse"]
    SO_0001031.comment = ["Reverse is an attribute of the feature, where the feature is in the 3' to 5' direction. Again could be applied to primer."]

with chebi:
    CHEBI_50906 = types.new_class("50906", (Thing,))
    CHEBI_50906.label = ["material entity role"]
    CHEBI_50906.comment = ["A role is particular behaviour which a material entity may exhibit."]

    CHEBI_35224 = types.new_class("35224", (CHEBI_50906,))
    CHEBI_35224.label = ["effector"]
    CHEBI_35224.comment = ["A small molecule which increases (activator) or decreases (inhibitor) the activity of an (allosteric) enzyme by binding to the enzyme at the regulatory site (which is different from the substrate-binding catalytic site)."]
with go:
    GO_0003674 = types.new_class("0003674", (Thing,))
    GO_0003674.label = ["molecular_function"]
    GO_0003674.comment = ["A molecular process that can be carried out by the action of a single macromolecular machine, usually via direct physical interactions with other molecular entities. Function in this sense denotes an action, or activity, that a gene product (or a complex) performs."]

    GO_0003700 = types.new_class("0003700", (GO_0003674,))
    GO_0003700.label = ["DNA-binding transcription factor activity"]
    GO_0003700.comment = ["A transcription regulator activity that modulates transcription of gene sets via selective and non-covalent binding to a specific double-stranded genomic DNA sequence (sometimes referred to as a motif) within a cis-regulatory region. Regulatory regions include promoters (proximal and distal) and enhancers. Genes are transcriptional units, and include bacterial operons."]

with edam:
    EDAM_format_1915 = types.new_class("format_1915", (Thing,))
    EDAM_format_1915.label = ["Format"]
    EDAM_format_1915.comment = ["A defined way or layout of representing and structuring data in a computer file, blob, string, message, or elsewhere."]

    EDAM_format_1207 = types.new_class("format_1207", (EDAM_format_1915,))
    EDAM_format_1207.label = ["nucleotide"]
    EDAM_format_1207.comment = ["Alphabet for a nucleotide sequence with possible ambiguity, unknown positions and non-sequence characters."]

    EDAM_format_1208 = types.new_class("format_1208", (EDAM_format_1915,))
    EDAM_format_1208.label = ["protein"]
    EDAM_format_1208.comment = ["Alphabet for a protein sequence with possible ambiguity, unknown positions and non-sequence characters."]

    EDAM_format_1197 = types.new_class("format_1197", (EDAM_format_1915,))
    EDAM_format_1197.label = ["InChI"]
    EDAM_format_1197.comment = ["Chemical structure specified in IUPAC International Chemical Identifier (InChI) line notation."]

    EDAM_format_1196 = types.new_class("format_1196", (EDAM_format_1915,))
    EDAM_format_1196.label = ["SMILES"]
    EDAM_format_1196.comment = ["Chemical structure specified in Simplified Molecular Input Line Entry System (SMILES) line notation."]


    # Model languages
    EDAM_format_2585 = types.new_class("format_2585", (EDAM_format_1915,))
    EDAM_format_2585.label = ["SBML"]
    EDAM_format_2585.comment = ["Systems Biology Markup Language (SBML), the standard XML format for models of biological processes such as for example metabolism, cell signaling, and gene regulation."]

    EDAM_format_3240 = types.new_class("format_3240", (EDAM_format_1915,))
    EDAM_format_3240.label = ["CellML"]
    EDAM_format_3240.comment = ["CellML, the format for mathematical models of biological and other networks."]

    EDAM_format_3156 = types.new_class("format_3156", (EDAM_format_1915,))
    EDAM_format_3156.label = ["BioPAX"]
    EDAM_format_3156.comment = ["BioPAX is an exchange format for pathway data, with its data model defined in OWL."]

with sbol3 :
    class SBOLValue (Thing):
      pass
    SBOLValue.vocabulary = ["true"] # Do not create an object

    class ComponentType (SBO_0000236):
        label = "Component Type"
        comment = "Controlled vocabulary for the types of physical entities that can be represented in SBOL. The value of a Component's type property must be an instance of a class that is a subclass of ComponentType."
    ComponentType.constantList = ["true"]
    ComponentType.is_a.append(SBOLValue)
    ComponentType.equivalent_to.append(SBO_0000241 | SBO_0000247 | SBO_0000250 | SBO_0000251 | SBO_0000252 | SBO_0000253)


    class DNARNAComponentType (ComponentType):
        label = "DNA or RNA Component Type"
        comment ="Type for DNA or RNA components. The value of a Component's type property must be an instance of a class that is a subclass of DNARNAComponentType if the Component has a role that is a subclass of DNARole or RNARole."
    DNARNAComponentType.constantList = ["true"]
    ComponentType.equivalent_to.append(ComponentType | SO_0000987 | SO_0000988 | SO_0000984 | SO_0000985)

    class Encoding (SBOLValue):
        label = "Encoding"
        comment = "Controlled vocabulary for the types of encoding that can be used to represent the primary structure of a Component. The value of a Sequence's encoding property must be an instance of a class that is a subclass of Encoding."
    Encoding.constantList = ["true"]
    Encoding.equivalent_to.append(EDAM_format_1207 | EDAM_format_1208 | EDAM_format_1197 | EDAM_format_1196)

    class ComponentRole (SBOLValue):
        label = "Component Role";        
        comment = "Controlled vocabulary for the roles that a Component can play in a design. The value of a Component's role property must be an instance of a class that is a subclass of ComponentRole."
    class DNARole (ComponentRole):
        label = "DNA Role"
        comment = "Controlled vocabulary for the roles that a DNA Component can play in a design. The value of a Component's role property must be an instance of a class that is a subclass of DNARole."
    DNARole.constantList = ["true"]
    DNARole.equivalent_to.append(SO_0000110 | SO_0000167 | SO_0000139 | SO_0000316 | SO_0000141 | SO_0000704 | SO_0000057 | SO_0000804)

    class RNARole (ComponentRole):
        label = "RNA role"
        comment = "Controlled vocabulary for the roles that an RNA Component can play in a design. The value of a Component's role property must be an instance of a class that is a subclass of RNARole."
    RNARole.constantList = ["true"]
    RNARole.equivalent_to.append(SO_0000110 | SO_0000234)

    class ProteinRole (ComponentRole):
        label = "Protein Role"
        comment = "Controlled vocabulary for the roles that a Protein Component can play in a design. The value of a Component's role property must be an instance of a class that is a subclass of ProteinRole."
    ProteinRole.constantList = ["true"]
    ProteinRole.equivalent_to.append(GO_0003674 | GO_0003700)

    class SmallMoleculeRole (ComponentRole):
        label = "Small Molecule Role"
        comment = "Controlled vocabulary for the roles that a Small Molecule Component can play in a design. The value of a Component's role property must be an instance of a class that is a subclass of SmallMoleculeRole."
    SmallMoleculeRole.constantList = ["true"]
    SmallMoleculeRole.equivalent_to.append(CHEBI_50906 | CHEBI_35224)

with om:
    class Measure(Thing):
        label = "Measure"
        comment = "The purpose of the om:Measure class is to link a numerical value to a om:Unit."
with prov:
    class Activity(Thing):
        label = "Activity"
        comment = "An Activity is used to represent the execution of a process or set of processes. An Activity is linked through prov:qualifiedAssociation to one or more Associations, and is linked through prov:used to one or more Entities."
    class Association(Thing):
        label = "Association"
        comment = "An Association is used to link an Activity to one or more Agents, and to describe the role of each Agent in the execution of the Activity. An Association is linked through prov:qualifiedAssociation to an Activity, and is linked through prov:agent to one or more Agents."

    class Agent(Thing):
        label = "Agent"
        comment = "An Agent is something that bears some form of responsibility for an Activity taking place, such as a person, organization, or software agent."
    class Plan(Thing):
        label = "Plan"
        comment = "A Plan is used to describe a set of actions or steps intended to achieve a specific goal or outcome."

    class Usage(Thing):
        label = "Usage"
        comment = "A Usage is used to describe the involvement of an Entity in an Activity, specifying how the Entity was used during the execution of the Activity."

with sbol3:
    # ---------SBOL Entities--------------
    class Identified(Thing):
        label = "Identified"
        component = "All SBOL-defined classes are directly or indirectly derived from the Identified abstract class."

    class TopLevel(Identified):
        label = "TopLevel"
        component = "TopLevel is an abstract class that is extended by any Identified class that can be found at the top level of an SBOL document or file."

    class Sequence (TopLevel):
        label = "Sequence"
        comment = "The purpose of the Sequence class is to represent the primary structure of a Component object and the manner in which it is encoded."
    Sequence.domainEntity = ["true"]

    class Component (TopLevel):
        label = "Component"
        comment = "The Component class represents the structural and/or functional entities of a biological design. The primary usage of this class is to represent entities with designed sequences, such as DNA, RNA, and proteins, but it can also be used to represent any other entity that is part of a design, such as simple chemicals, molecular complexes, strains, media, light, and abstract functional groupings of other entities."
    Component.domainEntity = ["true"]

    class Model (TopLevel):
        label = "Model"
        comment = "The purpose of the Model class is to serve as a placeholder for an external computational model and provide additional meta-data to enable better reasoning about the contents of this model."
    Model.domainEntity = ["true"]

    class Implementation (TopLevel):
        label = "Implementation"
        comment = "An Implementation represents a realized instance of a Component, such a sample of DNA resulting from fabricating a genetic design or an aliquot of a specified reagent."
    Implementation.domainEntity = ["true"]

    class Attachment (TopLevel):
        label = "Attachment"
        comment = "The purpose of the Attachment class is to serve as a general container for data files, especially experimental data files. It provides a means for linking files and metadata to SBOL designs."
    Attachment.domainEntity = ["true"]

    class Collection (TopLevel):
        label = "Collection"
        comment = "The Collection class is a class that groups together a set of TopLevel objects that have something in common."
    Collection.domainEntity = ["true"]

    class Experiment(Collection):
        label = "Experiment"
        comment = "The purpose of the Experiment class is to aggregate ExperimentalData objects for subsequent analysis, usually in accordance with an experimental design."
    Experiment.domainEntity = ["true"]

    class ExperimentalData (TopLevel):
        label = "ExperimentalData"
        comment = "The purpose of the ExperimentalData class is to aggregate links to experimental data files. An ExperimentalData is typically associated with a single sample, lab instrument, or experimental condition and can be used to describe the output of the test phase of a design-build-test-learn workflow."
    ExperimentalData.domainEntity = ["true"]

    class CombinatorialDerivation (TopLevel):
        label = "CombinatorialDerivation"
        comment = "The purpose of the CombinatorialDerivation class is to specify combinatorial biological designs without having to specify every possible design variant."
    CombinatorialDerivation.domainEntity = ["true"]

    class Interaction (Identified):
        label = "Interaction"
        comment = "The Interaction class provides more detailed description of how the Feature objects of a Component are intended to work together. For example, this class can be used to represent different forms of genetic regulation (e.g., transcriptional activation or repression), processes from the central dogma of biology (e.g. transcription and translation), and other basic molecular interactions (e.g., non-covalent binding or enzymatic phosphorylation)."
    Interaction.domainEntity = ["true"]

    class Constraint (Identified):
        label = "Constraint"
        comment = "The Constraint class can be used to assert restrictions on the relationships of pairs of Feature objects contained by the same parent Component. Uses of this class include expressing containment (e.g., a plasmid transformed into a chassis strain), identity mappings (e.g., replacing a placeholder value with a complete definition), and expressing relative, sequence-based positions (e.g., the ordering of features within a template)."
    Constraint.domainEntity = ["true"]

    class Interface (Identified):
        label = "Interface"
        comment = "The Interface class is a way of explicitly specifying the interface of a Component."
    Interface.domainEntity = ["true"]

    class Feature (Identified):
        label = "Feature"
        comment = "The Feature class, is used to compose Component objects into a structural or functional hierarchy. Feature is an abstract class; only its child classes are actually instantiated."
    Feature.domainEntity = ["true"]

    class SubComponent (Feature):
        label = "SubComponent"
        comment = "The SubComponent class is a subclass of the Feature class that can be used to specify structural hierarchy."
    SubComponent.domainEntity = ["true"]

    class ComponentReference (Feature):
        label = "ComponentReference"
        comment = "The ComponentReference class is a subclass of Feature that can be used to reference Features within SubComponents."
    ComponentReference.domainEntity = ["true"]

    class ExternallyDefined (Feature):
        label = "ExternallyDefined"
        comment = "The ExternallyDefined class has been introduced so that external definitions in databases like ChEBI or UniProt can be referenced."
    ExternallyDefined.domainEntity = ["true"]

    class LocalSubComponent (Feature):
        label = "LocalSubComponent"
        comment = "The LocalSubComponent class is a subclass of Feature. This class serves as a way to create a placeholder in more complex Components, such as a variable to be filled in later or a composite that exists only within the context of the parent Component."
    LocalSubComponent.domainEntity = ["true"]

    class SequenceFeature (Feature):
        label = "SequenceFeature"
        comment = "The SequenceFeature class describes one or more regions of interest on the Sequence objects referred to by its parent Component."
    SequenceFeature.domainEntity = ["true"]

    class Location (Identified):
        label = "Location"
        comment = "The Location class is used to represent the location of Features within Sequences. This class is extended by the Range, Cut, and EntireSequence classes. Location is an abstract class; only its child classes are actually instantiated."
    Location.domainEntity = ["true"]

    class Range (Location):
        label = "Range"
        comment = "A Range object specifies a region via discrete, inclusive start and end positions that correspond to indices for characters in the elements String of a Sequence."
    Range.domainEntity = ["true"]

    class Cut (Location):
        label = "Cut"
        comment = "The Cut class has been introduced to enable the specification of a region between two discrete positions. This specification is accomplished using the at property, which specifies a discrete position that corresponds to the index of a character in the elements String of a Sequence (except in the case when at is equal to zero.)"
    Cut.domainEntity = ["true"]

    class EntireSequence (Location):
        label = "EntireSequence"
        comment = "The EntireSequence class does not have any additional properties. Use of this class indicates that the linked Sequence describes the entirety of the Component or Feature parent of this Location object."
    EntireSequence.domainEntity = ["true"]

    class Participation (Identified):
        label = "Participation"
        comment = "Each Participation represents how a particular Feature behaves in its parent Interaction."
    Participation.domainEntity = ["true"]

    class VariableFeature (Identified):
        label = "VariableFeature"
        comment = "VariableFeature class specifies a variable and set of values that will replace one of the Feature objects in the template of a CombinatorialDerivation. The variable is specified by the variable property, and the set of values is defined by the union of Component objects referred to by the variant, variantCollection, and variantDerivation properties."
    VariableFeature.domainEntity = ["true"]
    
    class Metadata (Identified):
        label = "Metadata"
        comment = "Custom data in the form of independent objects can participate in the SBOL data model if they are assigned one of the SBOL types Identified or TopLevel. An example is an RDF object that is annotated such that it represents a data sheet that describes the performance of a Component in a particular context."
    Metadata.domainEntity = ["true"]
    Metadata.is_a.append(rdfNS.type.some(Thing))#Metadata must have another RDF.type    
    Identified.is_a.append(owlNS.topObjectProperty.min(0,Metadata)) #Identified may have zero or more Metadata annotations, but Metadata must be attached to at least one Identified entity

    class GenericTopLevel (TopLevel):
        label = "GenericTopLevel"
        comment = "The GenericTopLevel class is a way to create a placeholder for a top-level entity that is not defined in the SBOL data model."
    GenericTopLevel.domainEntity = ["true"]
    GenericTopLevel.is_a.append(rdfNS.type.some(Thing))    #GenericTopLevel must have another RDF.type
    
# ---------Provenance Entities--------------
    class SBOLActivity(TopLevel):
      label = "SBOL Activity"
      comment = "A wrapper for the PROV Activity class. The purpose of this class is to allow for the inclusion of SBOL-specific properties on PROV Activities, such as the association of an Activity with a particular Component or Interaction."
    SBOLActivity.domainEntity = ["true"]
    SBOLActivity.replacementOf = [prov.Activity]
    SBOLActivity.is_a.append(prov.Activity)

    class SBOLPlan(TopLevel):
      label = "SBOL Plan"
      comment = "TODO: ASK: A wrapper for the PROV Plan class. The purpose of this class is to allow for the inclusion of SBOL-specific properties on PROV Plans, such as the association of a Plan with a particular Component or Interaction."
    SBOLPlan.domainEntity = ["true"]
    SBOLPlan.replacementOf = [prov.Plan]
    SBOLPlan.is_a.append(prov.Plan)

    class SBOLAgent(TopLevel):
      label = "SBOL Agent"
      comment = "TODO: ASK: A wrapper for the PROV Agent class. The purpose of this class is to allow for the inclusion of SBOL-specific properties on PROV Agents, such as the association of an Agent with a particular Component or Interaction."
    SBOLAgent.domainEntity = ["true"]
    SBOLAgent.replacementOf = [prov.Agent]
    SBOLAgent.is_a.append(prov.Agent)

    class SBOLUsage(Identified):
      label = "SBOL Usage"
      comment = "A wrapper for the PROV Usage class. The purpose of this class is to allow for the inclusion of SBOL-specific properties on PROV Usages, such as the association of a Usage with a particular Component or Interaction."
    SBOLUsage.domainEntity = ["true"]
    SBOLUsage.replacementOf = [prov.Usage]
    SBOLUsage.is_a.append(prov.Usage)

    class SBOLAssociation(Identified):
      label = "SBOL Association"
      comment = "A wrapper for the PROV Association class. The purpose of this class is to allow for the inclusion of SBOL-specific properties on PROV Associations, such as the association of an Association with a particular Component or Interaction."
    SBOLAssociation.domainEntity = ["true"]
    SBOLAssociation.replacementOf = [prov.Association]
    SBOLAssociation.is_a.append(prov.Association)

    class SBOLMeasure(Identified):
      label = "SBOL Measure"
      comment = "A wrapper for the PROV Measure class. The purpose of this class is to allow for the inclusion of SBOL-specific properties on PROV Measures, such as the association of a Measure with a particular Component or Interaction."
    SBOLMeasure.domainEntity = ["true"]
    SBOLMeasure.replacementOf = [om.Measure]
    SBOLMeasure.is_a.append(om.Measure)

    # ---------SBOL Vocabulary--------------
    class SBOLTerm (Thing):
      label = "SBOL Term"
      comment = "The SBOLTerm class is a way to create a placeholder for a term in an SBOL-controlled vocabulary."
    SBOLTerm.vocabulary = ["true"] # Do not create an object
    
    # Orientation terms
    class Orientation (SBOLTerm):
      label = "Orientation"
      comment = "TODO: ASK: Controlled vocabulary for the orientation of a Feature or Location. The value of a Feature or Location's orientation property must be an instance of a class that is a subclass of Orientation."
    Orientation.constantList = ["true"]

    class inline (Orientation):
        label = "inline"
        comment = "Inline is an attribute of the feature, where the feature is in the 5' to 3' direction."
    class reverseComplement (Orientation):
        label = "reverseComplement"
        comment = "Reverse complement is an attribute of the feature, where the feature is in the 3' to 5' direction."
    Orientation.equivalent_to.append(inline | reverseComplement)

    # CombinatorialDerivationStrategy terms
    class CombinatorialDerivationStrategy  (SBOLTerm):
        label = "CombinatorialDerivationStrategy"
        comment = "Controlled vocabulary for the strategies that can be used to derive new Components from a template Component. "
    CombinatorialDerivationStrategy.constantList = ["true"]

    class enumerate (CombinatorialDerivationStrategy):
        label = "enumerate"
        comment = "Enumerate is a strategy for deriving new Components from a template Component. The enumerate strategy specifies that a new Component should be derived for every possible combination of values for the variable specified by the VariableFeature objects in the template Component."
    class sample (CombinatorialDerivationStrategy):
        label = "sample"
        comment = "Sample is a strategy for deriving new Components from a template Component. The sample strategy specifies that a new Component should be derived for a random sample of the possible combinations of values for the variable specified by the VariableFeature objects in the template Component."
    CombinatorialDerivationStrategy.equivalent_to.append(enumerate | sample)

    # Cardinality terms
    class Cardinality  (SBOLTerm):
        label = "Cardinality"
        comment = "TODO: ASK: The cardinality property is REQUIRED and has type of IRI. This property specifies how many Feature objects SHOULD be derived from the template Feature during the derivation of a new Component."
    Cardinality.constantList = ["true"]

    class zeroOrOne (Cardinality):
        label = "zeroOrOne"
        comment = "No more than one Feature in the derived Component SHOULD have a prov:wasDerivedFrom property that refers to the template Feature."

    class one (Cardinality):
        label = "one"
        comment = "Exactly one Feature in the derived Component SHOULD have a prov:wasDerivedFrom property that refers to the template Feature."

    class zeroOrMore (Cardinality):
        label = "zeroOrMore"
        comment = "Any number of Feature objects in the derived Component MAY have prov:wasDerivedFrom properties that refer to the template Feature."

    class oneOrMore (Cardinality):
        label = "OneOrMore"
        comment = "At least one Feature in the derived Component SHOULD have a prov:wasDerivedFrom property that refers to the template Feature."

    Cardinality.equivalent_to.append(zeroOrOne | one | zeroOrMore | oneOrMore)

    # RoleIntegration terms
    class RoleIntegration (SBOLTerm):
        label = "RoleIntegration"
        comment = "A roleIntegration specifies the relationship between a SubComponent instance's own set of role properties and the set of role properties on the included Component."
    RoleIntegration.constantList = ["true"]

    class overrideRoles (RoleIntegration):
        label = "overrideRoles"
        comment = "In the context of this SubComponent, ignore any role given for the included Component. Instead use only the set of zero or more role properties given for this SubComponent."

    class mergeRoles (RoleIntegration):
        label = "mergeRoles"
        comment = "Use the union of the two sets: both the set of zero or more role properties given for this SubComponent as well as the set of zero or more role properties given for the included Component."

    RoleIntegration.equivalent_to.append(overrideRoles | mergeRoles)

    # NucleicAcidTopology terms
    class NucleicAcidTopology (SBOLValue):
        label = "NucleicAcidTopology"
        comment = "Specifies the topology of a nucleic acid Component, such as linear or circular. For DNA Components with a fully specified sequence, topology information is recommended and should be provided using a term from the Topology Attribute branch of the Sequence Ontology."
    NucleicAcidTopology.constantList = ["true"]
    NucleicAcidTopology.equivalent_to.append(SO_0000987 | SO_0000988 | SO_0000984 | SO_0000985)

    # ConstraintRestriction terms
    class ConstraintRestriction(SBOLTerm):
        label = "ConstraintRestriction"
        comment = "TODO: ASK: SHOULD I TAKE IT FROM THE CONSTRAINT - RESTRICTION PROPERTY: Controlled vocabulary for the types of restrictions that can be expressed in a Constraint. The value of a Constraint's restriction property must be an instance of a class that is a subclass of ConstraintRestriction."
    ConstraintRestriction.constantList = ["true"]

    # Identity relations
    class verifyIdentical(ConstraintRestriction):
        label = "verifyIdentical"
        comment = "The subject and object, after tracing through any layers of ComponentReference, MUST both refer to SubComponent objects with the same instanceOf value or both refer to ExternallyDefined objects with the same definition. Example: a promoter included via two different subsystems must be the identical."
    
    class differentFrom(ConstraintRestriction):
        label = "differentFrom"
        comment = "The subject and object, after tracing through any layers of ComponentReference, MUST NOT both refer to SubComponent objects with the same instanceOf value or both refer to ExternallyDefined objects with the same definition. Example: two fluorescent reporters must be different."

    class replaces(ConstraintRestriction):
        label = "replaces"
        comment = "In the context of the parent object of the Constraint, information about the subject should be used in place of all instances of the object. Example: the J23101 promoter replaces a generic promoter."

    # Topological relations
    class contains(ConstraintRestriction):
        label = "contains"
        comment = "The subject contains the object and they might or might not share a boundary."

    class strictlyContains(ConstraintRestriction):
        label = "strictlyContains"
        comment = "The subject entirely contains the object: they do not share a boundary."

    class equals(ConstraintRestriction):
        label = "equals"
        comment = "The subject and object occupy the same location in space."

    class covers(ConstraintRestriction):
        label = "covers"
        comment = "The subject contains the object but also shares a boundary."

    class overlaps(ConstraintRestriction):
        label = "overlaps"
        comment = "The subject and object overlap in space, but portions of each are outside of the other."

    class meets(ConstraintRestriction):
        label = "meets"
        comment = "The subject and object are connected at a shared boundary."

    class isDisjointFrom(ConstraintRestriction):
        label = "isDisjointFrom"
        comment = "The subject and object do not overlap in space."

    class precedes(ConstraintRestriction):
        label = "precedes"
        comment = "The start of the location for subject is less than the start of the location for object."

    class strictlyPrecedes(ConstraintRestriction):
        label = "strictlyPrecedes"
        comment = "The end of the location for subject is less than the start of the location for object."

    class starts(ConstraintRestriction):
        label = "starts"
        comment = "The start of the location for subject is equal to the start of the location for object and the end of the location for subject is before the end of the location for object."

    class finishes(ConstraintRestriction):
        label = "finishes"
        comment = "The start of the location for subject is after the start of the location for object and the end of the location for subject is equal to the end of the location for object."

    # Sequential restrictions
    class SequentialRestriction(ConstraintRestriction):
        label = "SequentialRestriction"
        comment = "Sequential restrictions are a subset of the ConstraintRestriction class that are used to express relative, sequence-based positions of pairs of Features within a template Component. The value of a SequentialRestriction must be one of the following: precedes, strictlyPrecedes, meets, overlaps, contains, strictlyContains, equals, starts, or finishes."
    SequentialRestriction.constantList = ["true"]
    SequentialRestriction.equivalent_to.append(precedes| strictlyPrecedes | meets | overlaps | contains | strictlyContains | equals | starts |finishes)

    # Identity restrictions    
    class IdentityRestriction(ConstraintRestriction):
        label = "IdentityRestriction"
        comment = "Identity restrictions are a subset of the ConstraintRestriction class that are used to express identity relationships between pairs of Features within a template Component. The value of an IdentityRestriction must be one of the following: verifyIdentical, differentFrom, or replaces."
    IdentityRestriction.constantList = ["true"]
    IdentityRestriction.equivalent_to.append(verifyIdentical | differentFrom | replaces)

    # Topology restrictions        
    class TopologyRestriction(ConstraintRestriction):
        label = "TopologyRestriction"
        comment = "Topology restrictions are a subset of the ConstraintRestriction class that are used to express topological relationships between pairs of Features within a template Component. The value of a TopologyRestriction must be one of the following: contains, strictlyContains, equals, covers, overlaps, meets, or isDisjointFrom."
    TopologyRestriction.constantList = ["true"]
    TopologyRestriction.equivalent_to.append(isDisjointFrom | strictlyContains | contains | equals | meets | covers | overlaps)

    # Orientation restrictions
    class OrientationRestriction(ConstraintRestriction):
        label = "OrientationRestriction"
        comment = "Orientation restrictions are a subset of the ConstraintRestriction class that are used to express orientation relationships between pairs of Features within a template Component. The value of an OrientationRestriction must be one of the following: sameOrientationAs or oppositeOrientationAs."
    OrientationRestriction.constantList = ["true"]

    class sameOrientationAs(OrientationRestriction):
        label = "sameOrientationAs"
        comment = "The subject and object Component objects MUST have the same orientation. "

    class oppositeOrientationAs(OrientationRestriction):
        label = "oppositeOrientationAs"
        comment = "The subject and object Component objects MUST have opposite orientations."
    OrientationRestriction.equivalent_to.append (sameOrientationAs | oppositeOrientationAs )

    # Interaction types
    class InteractionType(SBOLValue):
        label = "InteractionType"
    comment = "Provides a vocabulary to choose the interaction type of behavior represented by an Interaction. Interaction types are typically identified using IRIs, such as terms from the Systems Biology Ontology."
    InteractionType.constantList = ["true"]    
    InteractionType.equivalent_to.append(SBO_0000169 | SBO_0000170 | SBO_0000176 | SBO_0000177 | SBO_0000179 | SBO_0000589 | SBO_0000168)

    # Participant roles
    class ParticipationRole(SBOLValue):
        label = "ParticipationRole"
        comment = "TODO: ASK: SHOULD I TAKE IT FROM THE PARTICIPATION - ROLE PROPERTY: Provides a vocabulary to choose the role of a Participation in an Interaction. Participation roles are typically identified using IRIs, such as terms from the Systems Biology Ontology."
    ParticipationRole.constantList = ["true"]
    ParticipationRole.equivalent_to.append(SBO_0000020 | SBO_0000642 | SBO_0000459 | SBO_0000643 | SBO_0000010 | SBO_0000011 | SBO_0000598 | SBO_0000019 | SBO_0000645)

    # Model framework terms
    class ModelFramework(SBOLValue):
        label = "ModelFramework"
        comment = "Provides a vocabulary to choose the modeling framework of a Model. Model frameworks are typically identified using IRIs, such as terms from the Systems Biology Ontology."
    ModelFramework.constantList = ["true"]
    ModelFramework.equivalent_to.append(SBO_0000062 | SBO_0000063 | SBO_0000693 | SBO_0000234 | SBO_0000681)

    # Model language terms
    class ModelLanguage(SBOLValue):
        label = "ModelLanguage"
        comment = "Provides a vocabulary to choose the modeling language of a Model. Model languages are typically identified using IRIs, such as terms from the EDAM ontology."
    ModelLanguage.constantList = ["true"]
    ModelLanguage.equivalent_to.append(EDAM_format_2585 | EDAM_format_3240 | EDAM_format_3156)

    # ---------SBOL properties---------
    class comprises(ObjectProperty, TransitiveProperty):
        label = "comprises"
        comment = "TODO: ASK: The comprises property is a transitive object property that is used to link an Identified object to another Identified object that is part of it."

    class directlyComprises(comprises, ObjectProperty):
        label = "directlyComprises"
        comment = "TODO: ASK: The directlyComprises property is a non-transitive object property that is used to link an Identified object to another Identified object that is directly part of it. "

    #Identified properties
    class displayId(DataProperty, FunctionalProperty):
        label = "displayId"
        comment = "The displayId property is an OPTIONAL identifier with a data type of String. This property is intended to be an intermediate between a IRI and the name property that is machine-readable, but more human-readable than the full IRI of an object"
        domain = [Identified]
        range = [str]

    class name(DataProperty, FunctionalProperty):
        label = "name"
        comment = "The name property is OPTIONAL and has a data type of String. This property is intended to be displayed to a human when visualizing an Identified object."
        domain = [Identified]
        range = [str]

    class description(DataProperty, FunctionalProperty):
        label = "description"
        comment = "The description property is OPTIONAL and has a data type of String. This property is intended to contain a more thorough text description of an Identified object."
        domain = [Identified]
        range = [str]

    class hasMeasure(directlyComprises, Identified >> om.Measure):
        label = "hasMeasure"
        comment = "An Identified object MAY have zero or more hasMeasure properties, each of which refers to a om:Measure object that describe measured parameters for this object."
        #TODO: WHY BELOW IS COMMENTED OUT?
        #domain = [Identified]
        #range = [om.Measure]

    # TopLevel properties
    class hasNamespace(ObjectProperty, FunctionalProperty):
        label = "hasNamespace"
        comment = "A TopLevel object MUST have precisely one hasNamespace property, which contains a URL that defines the namespace portion of URLs for this object and any child objects."
        domain = [TopLevel]
    TopLevel.is_a.append(hasNamespace.some(Thing))

    class hasAttachment(TopLevel >> Attachment):
        label = "hasAttachment"
        comment = "A TopLevel object can have zero or more hasAttachment properties, each of type IRI specifying an Attachment object."

    # Sequence properties
    class elements(DataProperty, FunctionalProperty):
        label = "elements"
        comment = "The elements property is an OPTIONAL String of characters that represents the constituents of a biological or chemical molecule."
        domain = [Sequence]
        range = [str]
    # Sequence.is_a.append(elements.some(str))

    class encoding(ObjectProperty, FunctionalProperty):
        label = "encoding"
        comment = "The encoding property has a data type of IRI, and is OPTIONAL unless elements is set, in which case it is REQUIRED."
        domain = [Sequence]

    # Component properties
    #Some of these properties are used also for entities.
    class type(ObjectProperty):
        label = "type"
        comment = "A Component MUST have one or more type properties, each of type IRI specifying the category of biochemical or physical entity (for example DNA, protein, or simple chemical) that a Component object abstracts for the purpose of engineering design"
        domain = [Component | LocalSubComponent | ExternallyDefined | Interaction | SBOLActivity | SBOLMeasure]
    Component.is_a.append(type.some(Thing))
    Component.is_a.append(type.some(ComponentType))
    Component.is_a.append(type.max(1, ComponentType))
    LocalSubComponent.is_a.append(type.some(Thing))
    ExternallyDefined.is_a.append(type.some(Thing))
    Interaction.is_a.append(type.some(Thing))

    class role(ObjectProperty):
        label = "role"
        comment = "This property can be used in a Component, Feature or Participation. A Component MAY have any number of role properties, each of type IRI, that MUST identify terms from ontologies that are consistent with the type property of the Component. Each Feature can have zero or more role property IRIs describing the purpose or potential function of this Feature in the context of its parent Component. A Participation is REQUIRED to have one or more role properties, each of type IRI, that describes the behavior of a Participation (and by extension its referenced Feature) in the context of its parent Interaction."
        domain = [Component | Feature | Participation]
    Participation.is_a.append(role.some(Thing))

    class hasSequence(ObjectProperty):
        label = "hasSequence"
        comment = "This property can be used in a Component or Location. A Component MAY have any number of hasSequence properties, each of type IRI, that MUST reference a Sequence object. In a Location, the hasSequence property is REQUIRED and MUST contain the IRI of a Sequence object."
        domain = [Component | Location]
        range= [Sequence]
    Location.is_a.append(hasSequence.some(Sequence))
    Location.is_a.append(hasSequence.max(1,Sequence))
    
    class hasFeature(directlyComprises, ObjectProperty):
        label = "hasFeature"
        comment = "A Component MAY have any number of hasFeature properties, each of type IRI that MUST reference a Feature object"
        domain = [Component]
        range= [Feature]

    class refersTo(ObjectProperty, FunctionalProperty):
        label = "refersTo"
        comment = "The refersTo property is a REQUIRED IRI that refers to a Feature."
        domain = [ComponentReference]
        range= [Feature]
    ComponentReference.is_a.append(refersTo.some(Feature))
    #ComponentReference.is_a.append(refersTo.max(1,Feature)) #Alternative modelling approach. This would also work. Left it as an example for now.

    class hasInteraction(directlyComprises, Component >> Interaction):
        label = "hasInteraction"
        comment = "A Component MAY have any number of hasInteraction properties, each of type IRI, that MUST reference an Interaction object."

    class hasConstraint(directlyComprises, Component >> Constraint):
        label = "hasConstraint"
        comment = "A Component MAY have any number of hasConstraint properties, each of type IRI, that MUST reference a Constraint object."

    class hasModel(Component >> Model):
        label = "hasModel"
        comment = "A Component MAY have any number of hasModel properties, each of type IRI, that MUST reference a Model object."
    class hasInterface(directlyComprises, Component >> Interface, FunctionalProperty):
        label = "hasInterface"
        comment = "A Component MAY have zero or one hasInterface property of type IRI that MUST reference an Interface object."

    # Feature properties
    class orientation(ObjectProperty, FunctionalProperty):
        label = "orientation"
        comment = "The orientation property is OPTIONAL and has a data type of IRI."
        domain = [Feature | Location]
        range = [Orientation]

    # SubComponent properties
    class roleIntegration(ObjectProperty, FunctionalProperty):
        label = "roleIntegration"
        comment = "A roleIntegration specifies the relationship between a SubComponent instance's own set of role properties and the set of role properties on the included Component."
        domain = [SubComponent]

    class instanceOf(SubComponent >> Component, FunctionalProperty):
        label = "instanceOf"
        comment = "The instanceOf property is a REQUIRED IRI that refers to the Component providing the definition for this SubComponent."
    SubComponent.is_a.append(instanceOf.some(Component))

    class sourceLocation(directlyComprises, SubComponent >> Location):
        label = "sourceLocation"
        comment = "The sourceLocation property allows for only a portion of a Component's Sequence to be included, rather than its entirety."

    class hasLocation(directlyComprises, ObjectProperty):
        label = "hasLocation"
        comment = "A SubComponent MAY have any number of hasLocation properties, each of type IRI, that MUST refer to Location objects that indicates the location of the Sequence from the instanceOf Component in a Sequence of the parent Component. A LocalSubComponent MAY have any number of hasLocation properties, each of type IRI, that MUST refer to Location objects. In SequenceFeature, the hasLocation is REQUIRED and contains one or more IRIs, which MUST refer to Location objects."
        domain = [SubComponent | LocalSubComponent | SequenceFeature]
        range = [Location]
    SequenceFeature.is_a.append(hasLocation.some(Location))

    # ComponentReference properties
    class inChildOf(ComponentReference >> SubComponent, FunctionalProperty):
        label = "inChildOf"
        comment = "The inChildOf property is a REQUIRED IRI that refers to a SubComponent. The inChildOf property MUST refer to a SubComponent pointed directly to by the parent of the ComponentReference."
    ComponentReference.is_a.append(inChildOf.some(Component))

    # ExternallyDefined properties
    class definition(ObjectProperty, FunctionalProperty):
        label = "definition"
        comment = "The definition property is REQUIRED and is of type IRI that links to a canonical definition external to SBOL."
        domain = [ExternallyDefined]
    ExternallyDefined.is_a.append(definition.some(Thing))

    # Location properties
    class order(DataProperty, FunctionalProperty):
        label = "order"
        comment = "The order property is OPTIONAL and has a data type of Integer. If there are multiple Location objects associated with a Feature, the order property is used to specify the order (in increasing value) in which the specified Locations are to be joined to form the sequence of the Feature."
        domain = [Location]
        #range = [int]
        range= [ConstrainedDatatype(int, min_inclusive = 1)]

    # Range properties
    class start(DataProperty, FunctionalProperty):
        label = "start"
        comment = "The start property specifies the inclusive starting position of the Range. This property is REQUIRED and MUST contain an Integer value greater than zero."
        domain = [Range]
        range= [ConstrainedDatatype(int, min_inclusive = 1)]
    Range.is_a.append(start.some(ConstrainedDatatype(int, min_inclusive = 1)))

    class end(DataProperty, FunctionalProperty):
        label = "end"
        comment = "The end property specifies the inclusive ending position of the Range. This property is REQUIRED and MUST contain an Integer value greater than zero. In addition, this Integer value MUST be greater than or equal to that of the start property."
        domain = [Range]
        range= [ConstrainedDatatype(int, min_inclusive = 1)]
    Range.is_a.append(end.some(ConstrainedDatatype(int, min_inclusive = 1)))

    # Cut properties
    class at(DataProperty, FunctionalProperty):
        label = "at"
        comment = "The at property is REQUIRED and MUST contain an Integer value greater than or equal to zero. The region specified by the Cut is between the position specified by this property and the position that immediately follows it. When the at property is equal to zero, the specified region is immediately before the first discrete position or character in the elements String of a Sequence."
        domain = [Cut]
        range= [ConstrainedDatatype(int, min_inclusive = 0)]
    Cut.is_a.append(at.some(ConstrainedDatatype(int, min_inclusive = 0)))

    # Constraint properties
    class restriction(ObjectProperty, FunctionalProperty):
        label = "restriction"
        comment = "The restriction property is REQUIRED and has a data type of IRI. This property MUST indicate the type of restriction on the locations, orientations, or identities of the subject and object Feature objects in relation to each other."
        domain = [Constraint]
    Constraint.is_a.append(restriction.some(Thing))

    class subject(Constraint >> Feature, FunctionalProperty):
        label = "subject"
        comment = "The subject property is REQUIRED and MUST contain a IRI that refers to a Feature contained by the same parent Component that contains the Constraint."
    Constraint.is_a.append(subject.some(Feature))

    class object(Constraint >> Feature, FunctionalProperty):
        label = "object"
        comment = "The object property is REQUIRED and MUST contain a IRI that refers to a Feature contained by the same parent Component that contains the Constraint. This Feature MUST NOT be the same Feature that the Constraint refers to via its subject property."
    Constraint.is_a.append(object.some(Feature))

    # Interaction properties
    class hasParticipation(directlyComprises, Interaction >> Participation):
        label = "hasParticipation"
        comment = "An Interaction MAY have any number of hasParticipation properties, each of type IRI, that MUST reference a Participation object, each of which identifies the role that its referenced Feature plays in the Interaction."
    # Participation properties
    class participant(Participation >> Feature, FunctionalProperty):
        label = "participant"
        comment = "The participant property indicates a Feature object that plays the designated role in its parent Interaction object. Precisely one value MUST be specified for precisely one of participant or higherOrderParticipant."

    class higherOrderParticipant(Participation >> Interaction, FunctionalProperty):
        label = "higherOrderParticipant"
        comment = "The higherOrderParticipant property indicates an Interaction object that plays the designated role in its parent Interaction object. Precisely one value MUST be specified for precisely one of participant or higherOrderParticipant."

    # Interface properties
    class input(Interface >> Feature):
        label = "input"
        comment = "An Interface MAY have any number of input properties, each of type IRI, that MUST reference a Feature object in the same Component."

    class output(Interface >> Feature):
        label = "output"
        comment = "An Interface MAY have any number of output properties, each of type IRI, that MUST reference a Feature object in the same Component."

    class nondirectional(Interface >> Feature):
        label = "nondirectional"
        comment = "An Interface MAY have any number of nondirectional properties, each of type IRI, that MUST reference a Feature object in the same Component."
    #CombinatorialDerivation properties
    class strategy(ObjectProperty, FunctionalProperty):
        label = "strategy"
        comment = "The strategy property is OPTIONAL and has a data type of IRI."
        domain = [CombinatorialDerivation]
        range = [enumerate | sample]

    class template(CombinatorialDerivation >> Component, FunctionalProperty):
        label = "template"
        comment = "The template property is REQUIRED and MUST contain a IRI that refers to a Component. "
    CombinatorialDerivation.is_a.append(template.some(Component))

    class hasVariableFeature(directlyComprises, CombinatorialDerivation >> VariableFeature):
        label = "hasVariableFeature"
        comment = "A CombinatorialDerivation object can have zero or more hasVariableFeature properties, each of type IRI, specifying a VariableFeature. The set of hasVariableFeature properties MUST NOT contain two or more VariableFeature objects that refer to the same template."

    #VariableFeature properties
    class cardinality(ObjectProperty, FunctionalProperty):
        label = "cardinality"
        comment = "The cardinality property is REQUIRED and has type of IRI. This property specifies how many Feature objects SHOULD be derived from the template Feature during the derivation of a new Component."
        domain = [VariableFeature]
        range = [zeroOrOne | one | zeroOrMore | oneOrMore]
    VariableFeature.is_a.append(cardinality.some(Cardinality))

    class variable(VariableFeature >> Feature, FunctionalProperty):
        label = "variable"
        comment = "The variable property is REQUIRED and MUST contain a IRI that refers to a template Feature in the template Component referred to by this VariableFeature's parent CombinatorialDerivation"
    VariableFeature.is_a.append(variable.some(Feature))

    class variantMeasure(VariableFeature >> om.Measure):
        label = "variantMeasure"
        comment = "A VariableFeature object can have zero or more variantMeasure properties, each of type IRI, specifying a om:Measure object. This property specifies numerical values that are options to be applied to the variable Feature from the template when deriving a new Component."

    class variantDerivation(VariableFeature >> CombinatorialDerivation):
        label = "variantDerivation"
        comment = "A VariableFeature object can have zero or more variantDerivation properties, each of type IRI, specifying a CombinatorialDerivation object. This property enables the specification of Component objects derived in accordance with another CombinatorialDerivation to serve as options when deriving a new Feature for the variable Feature from the template."


    class variantCollection(VariableFeature >> Collection):
        label = "variantCollection"
        comment = "A VariableFeature object can have zero or more variantCollection properties, each of type IRI, specifying a Collection object. Such a Collection MUST NOT contain any objects besides Component objects or Collection objects that themselves contain only Component or Collection objects. This property enables the specification of existing groups of Component objects to serve as options."

    class variant(VariableFeature >> Component):
        label = "variant"
        comment = "A VariableFeature object can have zero or more variant properties, each of type IRI, specifying a Component object. This property specifies individual Component objects to serve as options when deriving a new Feature for the variable Feature from the template."

    #Implementation properties
    class built(Implementation>> Component, FunctionalProperty):
        label = "built"
        comment = "The built property is OPTIONAL and MAY contain a IRI that MUST refer to a Component. This Component is intended to describe the actual physical structure and/or functional behavior of the Implementation."

    # Model properties
    class source(ObjectProperty, FunctionalProperty):
        label = "source"
        comment = "The source property is REQUIRED and MUST contain a IRI reference to the source file."
        domain = [Model | Attachment]
    Model.is_a.append(source.some(Thing))
    Attachment.is_a.append(source.some(Thing))

    class language(ObjectProperty, FunctionalProperty):
        label = "language"
        comment = "The language property is REQUIRED and MUST contain a IRI that specifies the language in which the model is implemented. It is RECOMMENDED that this IRI refer to a term from the EMBRACE Data and Methods (EDAM) ontology."
        domain = [Model]
    Model.is_a.append(language.some(Thing))

    class framework(ObjectProperty, FunctionalProperty):
        label = "framework"
        comment = "The framework property is REQUIRED and MUST contain a IRI that specifies the framework in which the model is implemented. It is RECOMMENDED this IRI refer to a term from the modeling framework branch of the SBO when possible."
        domain = [Model]
    Model.is_a.append(framework.some(Thing))

    #Collection properties
    class member(Collection >> TopLevel):
        label = "member"
        comment = "A Collection object can have zero or more member properties, each of type IRI specifying a TopLevel object."
    #Attachment properties
    class format(ObjectProperty, FunctionalProperty):
        label = "format"
        comment = "The format property is OPTIONAL and MAY contain a IRI that specifies the format of the attached file. It is RECOMMENDED that this IRI refer to a term from the EMBRACE Data and Methods (EDAM) ontology"
        domain = [Attachment]

    class size(DataProperty, FunctionalProperty):
        label = "size"
        comment = "The size property is OPTIONAL and MAY contain a long indicating the file size in bytes."
        domain = [Attachment]
        range= [ConstrainedDatatype(int, min_inclusive = 0)]

    class hash(DataProperty, FunctionalProperty):
        label = "hash"
        comment = "The hash property is OPTIONAL and MAY contain a hash value for the file contents represented as a hexadecimal digest."
        domain = [Attachment]
        range= [str]

    class hashAlgorithm(DataProperty, FunctionalProperty):
        label = "hashAlgorithm"
        comment = "The hashAlgorithm property is OPTIONAL and MAY contain the name of the hash algorithm used to generate the value of the hash property. The value of this property SHOULD be a hash name string from the IANA Named Information Hash Algorithm Registry, of which sha3-256 is currently RECOMMENDED. If the hash property is set, then hashAlgorithm MUST be set as well."
        domain = [Attachment]
        range= [str]

    #Sequence related subclasses
    class SequenceWithElements (Sequence):
        label = "Sequence With Elements"
        comment = "A SequenceWithElements is a Sequence that contains elements and an encoding."
    SequenceWithElements.equivalent_to.append(Sequence & elements.some(str) & encoding.some(Encoding))

    class DNASequence (SequenceWithElements):
        label = "DNA Sequence"
        comment = "Represents a DNA sequence, with the encoding of EDAM format 1207. The elements property MUST contain only characters from the IUPAC DNA character set: A, C, G, T, U, M, R, W, S, Y, K, V, H, D, B, N and -."
    DNASequence.domainEntity = ["true"]
    DNASequence.equivalent_to.append(SequenceWithElements & encoding.some(EDAM_format_1207))

    class RNASequence (SequenceWithElements):
        label = "RNA Sequence"
        comment = "Represents an RNA sequence, with the encoding of EDAM format 1207. The elements property MUST contain only characters from the IUPAC RNA character set: A, C, G, U, M, R, W, S, Y, K, V, H, D, B, N and -."
    RNASequence.domainEntity = ["true"]
    RNASequence.equivalent_to.append(SequenceWithElements & encoding.some(EDAM_format_1207))

    class ProteinSequence (SequenceWithElements):
        label = "Protein Sequence"
        comment = "Represents a protein sequence, with the encoding of EDAM format 1208. The elements property MUST contain only characters from the IUPAC Protein character set: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y and -."
    ProteinSequence.domainEntity = ["true"]
    ProteinSequence.equivalent_to.append(SequenceWithElements & encoding.some(EDAM_format_1208))

    class InChISequence (SequenceWithElements):
        label = "InChI Sequence"
        comment = "Represents a chemical structure using the IUPAC International Chemical Identifier (InChI) format, with the encoding of EDAM format 1197. The elements property MUST contain a valid InChI string."
    InChISequence.domainEntity = ["true"]
    InChISequence.equivalent_to.append(SequenceWithElements & encoding.some(EDAM_format_1197))

    class SMILESSequence (SequenceWithElements):
        label = "SMILES Sequence"
        comment = "Represents a chemical structure using the Simplified Molecular-Input Line-Entry System (SMILES) format, with the encoding of EDAM format 1196. The elements property MUST contain a valid SMILES string."
    SMILESSequence.domainEntity = ["true"]
    SMILESSequence.equivalent_to.append(SequenceWithElements & encoding.some(EDAM_format_1196))

    #Component related subclasses
    class DNAComponent (Component):
        label = "DNA Component"
        comment = "Represents a DNA component, with the type of SBO:DNA, the role of DNARole. It restricts instances to have the sequences with the correct DNA encoding."
    DNAComponent.domainEntity = ["true"]
    DNAComponent.equivalent_to.append(Component & type.some(SBO_0000251) & role.some(DNARole) & hasSequence.only(DNASequence))

    class RNAComponent (Component):
        label = "RNA Component"
        comment = "Represents an RNA component, with the type of SBO:RNA, the role of RNARole. It restricts instances to have the sequences with the correct RNA encoding."
    RNAComponent.domainEntity = ["true"]
    RNAComponent.equivalent_to.append(Component & type.some(SBO_0000250) & role.some(RNARole) & hasSequence.only(RNASequence))

    class ProteinComponent (Component):
        label = "Protein Component"
        comment = "Represents a protein component, with the type of SBO:protein, the role of ProteinRole. It restricts instances to have the sequences with the correct protein encoding."
    ProteinComponent.domainEntity = ["true"]
    ProteinComponent.equivalent_to.append(Component & type.some(SBO_0000252) & role.some(ProteinRole) & hasSequence.only(ProteinSequence))

    class SimpleChemicalComponent (Component):
        label = "Simple Chemical Component"
        comment = "Represents a simple chemical component, with the type of SBO:simple_chemical, the role of SmallMoleculeRole. It restricts instances to have the sequences with the correct chemical encoding."
    SimpleChemicalComponent.domainEntity = ["true"]
    SimpleChemicalComponent.equivalent_to.append(Component & type.some(SBO_0000247) & role.some(SmallMoleculeRole) & hasSequence.only(InChISequence | SMILESSequence))

    class NonCovalentComplexComponent (Component):
        label = "Non-Covalent Complex Component"
        comment = "Represents a non-covalent complex component, with the type of SBO:non_covalent_complex. It restricts instances to have the sequences with the correct encoding."
    NonCovalentComplexComponent.domainEntity = ["true"]
    NonCovalentComplexComponent.equivalent_to.append(Component & type.some(SBO_0000253))

    class FunctionalEntityComponent (Component):
        label = "Functional Entity Component"
        comment = "Represents a functional entity component, with the type of SBO:functional_entity. It restricts instances to have the sequences with the correct encoding."
    FunctionalEntityComponent.domainEntity = ["true"]
    FunctionalEntityComponent.equivalent_to.append(Component & type.some(SBO_0000241))

    #DNA Component subclasses
    class GenericDNAComponent (DNAComponent):
        label = "Generic DNA Component"
        comment = "Represents a generic DNA component, with the role of SO:sequence_feature."
    GenericDNAComponent.domainEntity = ["true"]
    GenericDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000110))
    
    class PromoterDNAComponent (DNAComponent):
        label = "Promoter DNA Component"
        comment = "Represents a promoter DNA component, with the role of SO:promoter."
    PromoterDNAComponent.domainEntity = ["true"]
    PromoterDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000167))

    class RBSDNAComponent (DNAComponent):
        label = "RBS DNA Component"
        comment = "Represents a ribosome binding site DNA component, with the role of SO:RBS."
    RBSDNAComponent.domainEntity = ["true"]
    RBSDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000139))

    class CDSDNAComponent (DNAComponent):
        label = "CDS DNA Component"
        comment = "Represents a coding sequence DNA component, with the role of SO:CDS."
    CDSDNAComponent.domainEntity = ["true"]
    CDSDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000316))

    class TerminatorDNAComponent (DNAComponent):
        label = "Terminator DNA Component"
        comment = "Represents a terminator DNA component, with the role of SO:terminator."
    TerminatorDNAComponent.domainEntity = ["true"]
    TerminatorDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000141))

    class GeneDNAComponent (DNAComponent):
        label = "Gene DNA Component"
        comment = "Represents a gene DNA component, with the role of SO:gene."
    GeneDNAComponent.domainEntity = ["true"]
    GeneDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000704))

    class OperatorDNAComponent (DNAComponent):
        label = "Operator DNA Component"
        comment = "Represents an operator DNA component, with the role of SO:operator."
    OperatorDNAComponent.domainEntity = ["true"]
    OperatorDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000057))

    class EngineeredRegionDNAComponent (DNAComponent):
        label = "Engineered Region DNA Component"
        comment = "Represents an engineered region DNA component, with the role of SO:engineered_region."
    EngineeredRegionDNAComponent.domainEntity = ["true"]
    EngineeredRegionDNAComponent.equivalent_to.append(DNAComponent & role.some(SO_0000804))

    #SimpleChemicalComponent subclasses
    class EffectorSimpleChemicalComponent (SimpleChemicalComponent):
        label = "Effector Simple Chemical Component"
        comment = "Represents an effector simple chemical component, with the role of CHEBI:effector."
    EffectorSimpleChemicalComponent.domainEntity = ["true"]
    EffectorSimpleChemicalComponent.equivalent_to.append(SimpleChemicalComponent & role.some(CHEBI_35224))

    #ProteinComponent subclasses
    class TranscriptionFactorProteinComponent (ProteinComponent):
        label = "Transcription Factor Protein Component"
        comment = "Represents a transcription factor protein component, with the role of GO:DNA-binding transcription factor activity."
    TranscriptionFactorProteinComponent.domainEntity = ["true"]
    TranscriptionFactorProteinComponent.equivalent_to.append(ProteinComponent & role.some(GO_0003700))

    # Participation subclasses
    class InhibitorParticipation (Participation):
        label = "InhibitorParticipant"
        comment = "Represents a participation of a feature that inhibits an interaction, with the role of SBO:inhibitor."
    InhibitorParticipation.domainEntity = ["true"]
    InhibitorParticipation.equivalent_to.append(Participation & role.some(SBO_0000020))

    class InhibitedParticipation (Participation):
        label = "InhibitedParticipation"
        comment = "Represents a participation of a feature that is inhibited in an interaction, with the role of SBO:inhibited."
    InhibitedParticipation.domainEntity = ["true"]
    InhibitedParticipation.equivalent_to.append(Participation & role.some(SBO_0000642))

    class StimulatorParticipation (Participation):
        label = "StimulatorParticipation"
        comment = "Represents a participation of a feature that stimulates an interaction, with the role of SBO:stimulator."
    StimulatorParticipation.domainEntity = ["true"]
    StimulatorParticipation.equivalent_to.append(Participation & role.some(SBO_0000459))

    class StimulatedParticipation (Participation):
        label = "StimulatedParticipation"
        comment = "Represents a participation of a feature that is stimulated in an interaction, with the role of SBO:stimulated."
    StimulatedParticipation.domainEntity = ["true"]
    StimulatedParticipation.equivalent_to.append(Participation & role.some(SBO_0000643))

    class ReactantParticipation (Participation):
        label = "ReactantParticipation"
        comment = "Represents a participation of a feature that is a reactant in an interaction, with the role of SBO:reactant."
    ReactantParticipation.domainEntity = ["true"]
    ReactantParticipation.equivalent_to.append(Participation & role.some(SBO_0000010))

    class ProductParticipation (Participation):
        label = "ProductParticipation"
        comment = "Represents a participation of a feature that is a product in an interaction, with the role of SBO:product."
    ProductParticipation.domainEntity = ["true"]
    ProductParticipation.equivalent_to.append(Participation & role.some(SBO_0000011))

    class PromoterParticipation (Participation):
        label = "PromoterParticipation"
        comment = "Represents a participation of a feature that is a promoter in an interaction, with the role of SBO:promoter."
    PromoterParticipation.domainEntity = ["true"]
    PromoterParticipation.equivalent_to.append(Participation & role.some(SBO_0000598))

    class ModifierParticipation (Participation):
        label = "ModifierParticipation"
        comment = "Represents a participation of a feature that is a modifier in an interaction, with the role of SBO:modifier."
    ModifierParticipation.domainEntity = ["true"]
    ModifierParticipation.equivalent_to.append(Participation & role.some(SBO_0000019))

    class ModifiedParticipation (Participation):
        label = "ModifiedParticipation"
        comment = "Represents a participation of a feature that is modified in an interaction, with the role of SBO:modified."
    ModifiedParticipation.domainEntity = ["true"]
    ModifiedParticipation.equivalent_to.append(Participation & role.some(SBO_0000644))

    class TemplateParticipation (Participation):
        label = "TemplateParticipation"
        comment = "Represents a participation of a feature that is a template in an interaction, with the role of SBO:template."
    TemplateParticipation.domainEntity = ["true"]
    TemplateParticipation.equivalent_to.append(Participation & role.some(SBO_0000645))

    class InhibitionInteraction (Interaction):
        label = "InhibitionInteraction"
        comment = "Represents an inhibition interaction, with the type of SBO:inhibition, that involves at least one inhibitor participation and at least one inhibited participation."
    InhibitionInteraction.domainEntity = ["true"]
    InhibitionInteraction.equivalent_to.append(Interaction & type.some(SBO_0000169) & participant.some(InhibitorParticipation) &  participant.some(InhibitedParticipation))

    class StimulationInteraction (Interaction):
        label = "StimulationInteraction"
        comment = "Represents a stimulation interaction, with the type of SBO:stimulation, that involves at least one stimulator participation and at least one stimulated participation."
    StimulationInteraction.domainEntity = ["true"]
    StimulationInteraction.equivalent_to.append(Interaction & type.some(SBO_0000170) & participant.some(StimulatedParticipation) &  participant.some(StimulatorParticipation))

    class DegradationInteraction (Interaction):
        label = "DegradationInteraction"
        comment = "Represents a degradation interaction, with the type of SBO:degradation, that involves at least one reactant participation."
    DegradationInteraction.domainEntity = ["true"]
    DegradationInteraction.equivalent_to.append(Interaction & type.some(SBO_0000179) &  participant.some(ReactantParticipation))
    
    class BiochemicalReactionInteraction (Interaction):
        label = "BiochemicalReactionInteraction"
        comment = "Represents a biochemical reaction interaction, with the type of SBO:biochemical_reaction, that involves zero or more modifier, modified, product, and reactant participations."
    BiochemicalReactionInteraction.domainEntity = ["true"]
    BiochemicalReactionInteraction.equivalent_to.append(Interaction & type.some(SBO_0000176) & participant.min(0, ModifierParticipation) & participant.min(0, ModifiedParticipation) & participant.min(0, ProductParticipation) & participant.min(0, ReactantParticipation) )

    class NonCovalentBindingInteraction (Interaction):
        label = "NonCovalentBindingInteraction"
        comment = "Represents a non-covalent binding interaction, with the type of SBO:non_covalent_binding, that involves at least one reactant participation and at least one product participation."
    NonCovalentBindingInteraction.domainEntity = ["true"]
    NonCovalentBindingInteraction.equivalent_to.append(Interaction & type.some(SBO_0000177) & participant.some(ReactantParticipation) & participant.some(ProductParticipation))
    
    class GeneticProductionInteraction (Interaction):
        label = "GeneticProductionInteraction"
        comment = "Represents a genetic production interaction, with the type of SBO:genetic_production, that involves at least one template participation and at least one product participation."
    GeneticProductionInteraction.domainEntity = ["true"]
    GeneticProductionInteraction.equivalent_to.append(Interaction & type.some(SBO_0000589) & participant.some(TemplateParticipation) & participant.exactly(1, ProductParticipation))
    
    class ControlInteraction (Interaction):
        label = "ControlInteraction"
        comment = "Represents a control interaction, with the type of SBO:control, that involves at least one modifier participation and at least one modified participation."
    ControlInteraction.domainEntity = ["true"]
    ControlInteraction.equivalent_to.append(Interaction & type.some(SBO_0000168) & participant.some(ModifierParticipation) & participant.some(ModifiedParticipation))

with prov:
  # sbol3:Identified prov properties
  class wasDerivedFrom(ObjectProperty):
      label = "wasDerivedFrom"
      comment = "An Identified object MAY have zero or more prov:wasDerivedFrom properties, each of type IRI. This property is defined by the PROV-O ontology and is located in the https://www.w3.org/ns/prov# namespace"
      domain = [sbol3.Identified]
      range = [Thing]

   # wasInformedBy [0..*]: Activity -> TopLevel
  class wasInformedBy(ObjectProperty):
      label = "wasInformedBy"
      comment = "An prov:Activity MAY have one or more prov:wasInformedBy properties, each of type IRI that refers to another prov:Activity object."
      domain = [Activity]
      range = [Activity]

  # prov:Activity properties
  # Identified -> Activity - [0..*]
  class wasGeneratedBy(ObjectProperty):
      label = "wasGeneratedBy"
      comment = "An Identified object MAY have zero or more prov:wasGeneratedBy properties, each of type IRI."
      domain = [sbol3.Identified]
      range = [sbol3.SBOLActivity]

  # [0..1]
  class startedAtTime(DataProperty, FunctionalProperty):
      label = "startedAtTime"
      comment = "The prov:startedAtTime property is OPTIONAL and contains a DateTime value, indicating when the activity started. If this property is present, then the prov:endedAtTime property is REQUIRED."
      domain = [Activity]
      range = [datetime.datetime]

  # [0..1]
  class endedAtTime(DataProperty, FunctionalProperty):
    label = "endedAtTime"
    comment = "The prov:endedAtTime property is OPTIONAL and contains a DateTime value, indicating when the activity ended."
    domain = [Activity]
    range = [datetime.datetime]

  # Activity -> Usage - [0..*]
  class qualifiedUsage(ObjectProperty):
    label = "qualifiedUsage"
    comment = "An prov:Activity MAY have one or more prov:qualifiedUsage properties, each of type IRI that refers to an prov:Usage object."
    domain = [Activity]
    range = [Usage]

  # Activity -> Association - [0..*]
  class qualifiedAssociation(ObjectProperty):
    label = "qualifiedAssociation"
    comment = "An prov:Activity MAY have one or more prov:qualifiedAssociation properties, each of type IRI that refers to an prov:Association object."
    domain = [Activity]
    range = [Association]

  # prov:Usage properties
  # [1..1]
  class entity(ObjectProperty, FunctionalProperty):
    label = "entity"
    comment = "The prov:entity property is REQUIRED and MUST contain a IRI which MAY refer to an Identified object."
    domain = [Usage]
  SBOLUsage.is_a.append(entity.some(Thing))

  # [0..*]
  class hadRole(ObjectProperty):
    label = "hadRole"
    comment = "An prov:Usage MAY have one or more prov:hadRole properties, each of type IRI that refers to particular term(s) describing the usage of an prov:Entity referenced by the prov:entity property."
    domain = [Usage | Association]

  # prov:Association properties
  # Association -> Plan - [0..1]
  class hadPlan(ObjectProperty, FunctionalProperty):
      label = "hadPlan"
      comment = "The prov:hadPlan property is OPTIONAL and contains a IRI that refers to a prov:Plan."
      domain = [Association]
      range = [Plan]

  # Association -> Agent - [1..1]
  class agent(ObjectProperty, FunctionalProperty):
    label = "agent"
    comment = "The prov:agent property is REQUIRED and MUST contain a IRI that refers to an prov:Agent object."
    domain = [Association]
    range = [Agent]
  Association.is_a.append(agent.some(Agent))

# OM (Units of Measure) classes
with om:
  class Unit(Thing):
    label = "Unit"
    comment = "om:Unit is an abstract class that is extended by other classes to describe units of measure using a shared set of properties."
  Unit.is_a.append(rdfs.label.some(str))
  #TODO:Open again later: SBOLUnit.is_a.append(rdfs.comment.max(1, str)). This needs to be checked with the commnunity.

  class SingularUnit(Unit):
    label = "SingularUnit"
    comment = "The purpose of the om:SingularUnit class is to describe a unit of measure that is not explicitly represented as a combination of multiple units, but could be equivalent to such a representation."

  class CompoundUnit(Unit):
    label = "CompoundUnit"
    comment = "om:CompoundUnit is an abstract class that is extended by other classes to describe units of measure that can be represented as combinations of multiple other units of measure."

  class PrefixedUnit(Unit):
    label = "PrefixedUnit"
    comment = "The purpose of the om:PrefixedUnit class is to describe a unit of measure that is the multiplication of another unit of measure and a factor represented by a standard prefix such as \"milli\", \"centi\", \"kilo\", etc."

  class UnitMultiplication(Unit):
    label = "UnitMultiplication"
    comment = "The purpose of the om:UnitMultiplication class is to describe a unit of measure that is the multiplication of two other units of measure."

  class UnitDivision(Unit):
    label = "UnitDivision"
    comment = "The purpose of the om:UnitDivision class is to describe a unit of measure that is the division of one unit of measure by another."

  class UnitExponentiation(Unit):
      label = "UnitExponentiation"
      comment = "The purpose of the om:UnitExponentiation class is to describe a unit of measure that is raised to an integer power."
  class Prefix(Thing):
      label = "Prefix"
      comment = "om:Prefix is an abstract class that is extended by other classes to describe factors that are  commonly represented by standard unit prefixes."
  Prefix.is_a.append(rdfs.label.some(str))
  #TODO:Open again later: SBOLPrefix.is_a.append(rdfs.comment.max(1, str)). This should also be checked with the community.

  class SIPrefix(Prefix):
      label = "SIPrefix"
      comment = "The purpose of the om:SIPrefix class is to describe standard SI prefixes such as \"milli\", \"centi\", \"kilo\", etc."

  class BinaryPrefix(Prefix):
      label = "BinaryPrefix"
      comment = "The purpose of the om:BinaryPrefix class is to describe standard binary prefixes such as \"kibi\", \"mebi\", \"gibi\", etc."

with sbol3:
  class SBOLUnit(TopLevel):
    label = "SBOLUnit"
    comment = "A wrapper class to enable the use of OM Units in SBOL. This class allows adding custom SBOL relationships."
  SBOLUnit.domainEntity = ["true"]
  SBOLUnit.replacementOf = [om.Unit]
  SBOLUnit.is_a.append(om.Unit)
  
  class SBOLSingularUnit(SBOLUnit):
    label = "SBOLSingularUnit"
    comment = "A wrapper class to enable the use of OM SingularUnits in SBOL. This class allows adding custom SBOL relationships."
  SBOLSingularUnit.domainEntity = ["true"]
  SBOLSingularUnit.replacementOf = [om.SingularUnit]
  SBOLSingularUnit.is_a.append(om.SingularUnit)

  class SBOLCompoundUnit(SBOLUnit):
    label = "SBOLCompoundUnit"
    comment = "A wrapper class to enable the use of OM CompoundUnits in SBOL. This class allows adding custom SBOL relationships."
  SBOLCompoundUnit.domainEntity = ["true"]
  SBOLCompoundUnit.replacementOf = [om.CompoundUnit]
  SBOLCompoundUnit.is_a.append(om.CompoundUnit)

  class SBOLPrefixedUnit(SBOLUnit):
    label = "SBOLPrefixedUnit"
    comment = "A wrapper class to enable the use of OM PrefixedUnits in SBOL. This class allows adding custom SBOL relationships."
  SBOLPrefixedUnit.domainEntity = ["true"]
  SBOLPrefixedUnit.replacementOf = [om.PrefixedUnit]
  SBOLPrefixedUnit.is_a.append(om.PrefixedUnit)

  class SBOLUnitMultiplication(SBOLUnit):
    label = "SBOLUnitMultiplication"
    comment = "A wrapper class to enable the use of OM UnitMultiplications in SBOL. This class allows adding custom SBOL relationships."
  SBOLUnitMultiplication.domainEntity = ["true"]
  SBOLUnitMultiplication.replacementOf = [om.UnitMultiplication]
  SBOLUnitMultiplication.is_a.append(om.UnitMultiplication)

  class SBOLUnitDivision(SBOLUnit):
    label = "SBOLUnitDivision"
    comment = "A wrapper class to enable the use of OM UnitDivisions in SBOL. This class allows adding custom SBOL relationships."
  SBOLUnitDivision.domainEntity = ["true"]
  SBOLUnitDivision.replacementOf = [om.UnitDivision]
  SBOLUnitDivision.is_a.append(om.UnitDivision)

  class SBOLUnitExponentiation(SBOLUnit):
    label = "SBOLUnitExponentiation"
    comment = "A wrapper class to enable the use of OM UnitExponentiations in SBOL. This class allows adding custom SBOL relationships."
  SBOLUnitExponentiation.domainEntity = ["true"]
  SBOLUnitExponentiation.replacementOf = [om.UnitExponentiation]
  SBOLUnitExponentiation.is_a.append(om.UnitExponentiation)

  class SBOLPrefix(TopLevel):
    label = "SBOLPrefix"
    comment = "A wrapper class to enable the use of OM Prefixes in SBOL. This class allows adding custom SBOL relationships."
  SBOLPrefix.domainEntity = ["true"]
  SBOLPrefix.replacementOf = [om.Prefix]
  SBOLPrefix.is_a.append(om.Prefix)
  

  class SBOLSIPrefix(SBOLPrefix):
    label = "SBOLSIPrefix"
    comment = "A wrapper class to enable the use of OM SIPrefixes in SBOL. This class allows adding custom SBOL relationships."
  SBOLSIPrefix.domainEntity = ["true"]
  SBOLSIPrefix.replacementOf = [om.SIPrefix]
  SBOLSIPrefix.is_a.append(om.SIPrefix)

  class SBOLBinaryPrefix(SBOLPrefix):
    label = "SBOLBinaryPrefix"
    comment = "A wrapper class to enable the use of OM BinaryPrefixes in SBOL. This class allows adding custom SBOL relationships."
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
    label = "hasNumericalValue"
    comment = "The om:hasNumericalValue property is REQUIRED and MUST contain a single xsd:float."
    domain = [Measure]
    range  = [float]
  Measure.is_a.append(hasNumericalValue.some(float))
  
  class hasUnit(ObjectProperty, FunctionalProperty):
    label = "hasUnit"
    comment = "This property can be used in a Measure, SingularUnit or PrefixedUnit. For Measure and PrefixedUnit, the om:hasUnit property is REQUIRED and MUST contain a IRI that refers to a om:Unit. For SingularUnit, the om:hasUnit is OPTIONAL and MAY contain a IRI."
    domain = [Measure | SingularUnit |PrefixedUnit] #[1..0]
    range  = [Unit]
  Measure.is_a.append(hasUnit.some(Unit)) #[1..1]
  PrefixedUnit.is_a.append(hasUnit.some(Unit)) #[1..1]

  class symbol(DataProperty, FunctionalProperty):
    label = "symbol"
    comment = "This property can be used in a Unit or Prefix. The om:symbol property is REQUIRED and MUST contain a String. This String is commonly used to abbreviate the name of the unit of measure or prefix."
    domain = [Unit | Prefix]
    range  = [float]
  Unit.is_a.append(symbol.some(float)) # [1..]
  Prefix.is_a.append(symbol.some(float)) # [1..]

  #[1..0]
  class alternativeSymbol(DataProperty):
    label = "alternativeSymbol"
    comment = "This property can be used in a Unit or Prefix. The om:alternativeSymbols property is OPTIONAL and MAY contain a set of Strings. This property can be used to specify alternative abbreviations other than that specified using the om:symbol property"
    domain = [Unit | Prefix]
    range  = [str]

  #[1..0]
  class alternativeLabel(DataProperty):
    label = "alternativeLabel"
    comment = "This property can be used in a Unit or Prefix. The om:alternativeLabel property is OPTIONAL and MAY contain a set of Strings. This property can be used to specify alternative common names other than that specified using om:label property."
    domain = [Unit | Prefix]
    range  = [str]

  #[1..0]
  class longComment(DataProperty, FunctionalProperty):
    label = "longComment"
    comment = "This property can be used in a Unit or Prefix. The om:longcomment property is OPTIONAL and MAY contain a String. This String is a long description of the unit of measure and SHOULD be longer than any String contained by the om:comment property."
    domain = [Unit | Prefix]
    range  = [str]

  class hasFactor(DataProperty):
    label = "hasFactor"
    comment = "This property can be used in a SingularUnit or Prefix. For SingularUnit, the om:hasFactor property is OPTIONAL and MAY contain a xsd:float. If the om:hasFactor property of a om:SingularUnit is non-empty, then its om:hasUnit property SHOULD also be non-empty. For Prefix, The om:hasFactor property is REQUIRED and MUST contain an xsd:float."
    domain = [SingularUnit | Prefix] #[1..0]
    range  = [float]
  Prefix.is_a.append(hasFactor.some(float)) #[1..1]

  #[1..1]
  class hasTerm1(ObjectProperty, FunctionalProperty):
    label = "hasTerm1"
    comment = "The om:hasTerm1 property is REQUIRED and MUST contain a IRI that refers to another om:Unit. This om:Unit is the first multiplication term."
    domain = [UnitMultiplication]
    range  = [Unit]
  UnitMultiplication.is_a.append(hasTerm1.some(Unit))

  #[1..1]
  class hasTerm2(ObjectProperty, FunctionalProperty):
    label = "hasTerm2"
    comment = "The om:hasTerm2 property is REQUIRED and MUST contain a IRI that refers to another om:Unit. This om:Unit is the second multiplication term. It is okay if the om:Unit referred to by om:hasTerm1 is the same as that referred to by om:hasTerm2."
    domain = [UnitMultiplication]
    range  = [Unit]
  UnitMultiplication.is_a.append(hasTerm2.some(Unit))

  #[1..1]
  class hasNumerator(ObjectProperty,FunctionalProperty):
    label = "hasNumerator"
    comment = "The om:hasNumerator property is REQUIRED and MUST contain a IRI that refers to another om:Unit."
    domain = [UnitDivision]
    range  = [Unit]
  UnitDivision.is_a.append(hasNumerator.some(Unit))

  #[1..1]
  class hasDenominator(ObjectProperty,FunctionalProperty):
    label = "hasDenominator"
    comment = "The om:hasDenominator property is REQUIRED and MUST contain a IRI that refers to another om:Unit."
    domain = [UnitDivision]
    range  = [Unit]
  UnitDivision.is_a.append(hasDenominator.some(Unit))

  #[1..1]
  class hasBase(ObjectProperty,FunctionalProperty):
    label = "hasBase"
    comment = "The om:hasBase property is REQUIRED and MUST contain a IRI that refers to another om:Unit."
    domain = [UnitExponentiation]
    range  = [Unit]
  UnitExponentiation.is_a.append(hasBase.some(Unit))

  #[1..1]
  class hasExponent(DataProperty,FunctionalProperty):
    label = "hasExponent"
    comment = "The om:hasExponent property is REQUIRED and MUST contain an xsd:integer."
    domain = [UnitExponentiation]
    range  = [int]
  UnitExponentiation.is_a.append(hasExponent.some(int))
  
  #[1..1]
  class hasPrefix(ObjectProperty,FunctionalProperty):
    label = "hasPrefix"
    comment = "The om:hasPrefix property is REQUIRED and MUST contain a IRI that refers to a om:Prefix."
    domain = [PrefixedUnit]
    range  = [Prefix]
  PrefixedUnit.is_a.append(hasPrefix.some(Prefix))


# Save individual ontologies (with owl:imports intact for standalone validity)
sbol3.save(file = "sbol3_core.txt", format = "rdfxml")
sbol3.save(file = "sbol3_core.rdf", format = "rdfxml")
sbo.save(file = "sbo.rdf", format = "rdfxml")
so.save(file = "so.rdf", format = "rdfxml")
edam.save(file = "edam.rdf", format = "rdfxml")
chebi.save(file = "chebi.rdf", format = "rdfxml")
go.save(file = "go.rdf", format = "rdfxml")
om.save(file = "om.rdf", format = "rdfxml")
prov.save(file = "prov.rdf", format = "rdfxml")
otol.save(file = "otol.rdf", format = "rdfxml")

from rdflib import URIRef

# Merges  ontologies into a single combined rdf file
def mergeOntologies(inputFiles, outputName):
    combined = Graph()
    for f in inputFiles:
        combined.parse(f, format="xml")
    # Keep only the sbol3 owl:Ontology declaration — remove all others so the OWL API does not randomly choose one of the other ontlogies (SBO, SO, CHEBI, GO, PROV, OM)
    sbol3IRI = URIRef(sbol3.base_iri)
    for ontology in list(combined.subjects(RDF.type, OWL.Ontology)):
        if ontology != sbol3IRI:
            combined.remove((ontology, RDF.type, OWL.Ontology))
    combined.add((sbol3IRI, RDF.type, OWL.Ontology))
    combined.serialize(destination=f"{outputName}.rdf", format="xml")
    combined.serialize(destination=f"{outputName}.txt", format="xml")

mergeOntologies(["sbol3_core.rdf", "sbo.rdf", "so.rdf", "edam.rdf", "chebi.rdf", "go.rdf", "om.rdf", "prov.rdf", "otol.rdf"], "sbol3")
mergeOntologies(["sbol3_core.rdf", "om.rdf", "prov.rdf"], "sbol_om_prov")

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

robotJarFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "robot.jar")
owlPrefixes = [
    ("sbol", sbol3.base_iri),
    ("om", om.base_iri),
    ("identifiers", "https://identifiers.org/"),
    ("prov", prov.base_iri),
    ("otol", otol.base_iri)]

createOWL(robotJarFile, "sbol3.rdf", ["sbol3.owl", "sbol3.ofn", "sbol3.omn"], owlPrefixes)
createOWL(robotJarFile, "sbol_om_prov.rdf", ["sbol_om_prov.owl", "sbol_om_prov.ofn", "sbol_om_prov.omn"], owlPrefixes)

#Expects a set of tuples for: rdf input file, html output file, and the ontology title
#prefixes: list of (prefix, namespace) pairs
def createHTML(ontologies, prefixes=None):
    try:
        # Workaround for the pyLODE.pyproject.toml file issue. The following code creates a minimal pyproject.toml in the site-packages folder if it doesn't already exist. If the distribution does not include this file, then the pyLODE fails!
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
createHTML([("sbol3.rdf", "sbol3.html", "SBOL3 Ontology"), ("sbol_om_prov.rdf", "sbol_om_prov.html", "SBOL3 Core Ontology")], owlPrefixes)

print ("\ndone!")