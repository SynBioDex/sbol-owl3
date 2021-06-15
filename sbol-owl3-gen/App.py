'''
Created on 26 May 2021

@author: gokselmisirli
'''
from owlready2 import *
#import types
#import re
#from ctypes.test.test_repr import subclasses
#from dill.tests.test_nested import cadder

sbol3 = get_ontology("http://sbols.org/v3")
prov = get_ontology("https://www.w3.org/ns/prov#")
om = get_ontology("http://www.ontology-of-units-of-measure.org/resource/om-2/")

with om: 
    class Measure(Thing):
        label = "Measure"       

with sbol3: 
    #--------------SBOL Entities--------------
    class Identified(Thing):
        label = "Identified"
        
    class TopLevel(Identified):
        label = "TopLevel"
        
    class Sequence (TopLevel):
        label = "Sequence"  
         
    class Component (TopLevel):
        label = "Component"
    
    class Model (TopLevel):
        label = "Model"

    class Implementation (TopLevel):
        label = "Implementation"
        
    class Attachment (TopLevel):
        label = "Attachment"

    class Collection (TopLevel):
        label = "Collection"
    
    class Experiment(Collection):
        label = "Experiment"

    class ExperimentalData (TopLevel):
        label = "ExperimentalData"

    class CombinatorialDerivation (TopLevel):
        label = "CombinatorialDerivation"
             
    class Interaction (Identified):
        label = "Interaction"
             
    class Constraint (Identified):
        label = "Constraint"
             
    class Interface (Identified):
        label = "Interface"
         
    class Feature (Identified):
        label = "Feature"
                 
    class SubComponent (Feature):
        label = "SubComponent"

    class ComponentReference (Feature):
        label = "ComponentReference"

    class ExternallyDefined (Feature):
        label = "ExternallyDefined"

    class LocalSubComponent (Feature):
        label = "LocalSubComponent"

    class SequenceFeature (Feature):
        label = "SequenceFeature"
        
    class Location (Identified):
        label = "Location"
   
    class Range (Location):
        label = "Range"
   
    class Cut (Location):
        label = "Cut"
   
    class EntireSequence (Location):
        label = "EntireSequence"
   
    class Participation (Identified):
        label = "Participation"
    
    class VariableFeature (Identified):
        label = "VariableFeature"
    
    #--------------SBOL Vocabulary--------------
    class SBOLTerm (Thing): pass
     
    # Orientation terms
    class Orientation (SBOLTerm):pass
    
    class inline (Orientation):
        label = "inline"
    
    class reverseComplement (Orientation):
        label = "reverseComplement"
    
    Orientation.equivalent_to.append(inline | reverseComplement)
      
    #-----CombinatorialDerivationStrategy terms-----
    class CombinatorialDerivationStrategy  (SBOLTerm):
        label = "CombinatorialDerivationStrategy"
    
    class enumerate (CombinatorialDerivationStrategy):
        label = "enumerate"
    
    class sample (CombinatorialDerivationStrategy):
        label = "sample"    
    
    CombinatorialDerivationStrategy.equivalent_to.append(enumerate | sample)
  
    #-----Cardinality terms-----
    class Cardinality  (SBOLTerm):
        label = "Cardinality"
    
    class zeroOrOne (Cardinality):
        label = "zeroOrOne"

    class one (Cardinality):
        label = "one"
    
    class zeroOrMore (Cardinality):
        label = "zeroOrMore"

    class oneOrMore (Cardinality):
        label = "OneOrMore"
    
    Cardinality.equivalent_to.append(zeroOrOne | one | zeroOrMore | oneOrMore)
  
    #Orientation.equivalent_to =   [Inline, ReverseComplement]
    #Orientation.equivalent_to.append(OneOf([Inline, ReverseComplement]))
    #class ExternallyDefinedA (Thing):pass
    #ExternallyDefinedA.equivalent_to.append(orientation.only(Inline | ReverseComplement))
    
    #--------------SBOL properties-------------- 
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
        
    class hasMeasure(DataProperty):
        label = "hasMeasure"
        domain = [Identified]
        range = [om.Measure]  
        
    #-----TopLevel properties-----  
    class hasNamespace(ObjectProperty, FunctionalProperty):
        label = "hasNamespace"
        domain = [TopLevel]
        #class_property_type=["value"]
    TopLevel.is_a.append(hasNamespace.some(Thing))
    
    class hasAttachment(TopLevel >> Attachment):
        label = "hasAttachment"
    
    #-----Sequence properties-----
    class elements(DataProperty, FunctionalProperty):
        label = "elements"
        domain = [Sequence]
        range = [str] 
    Sequence.is_a.append(elements.some(str))
    
    class encoding(ObjectProperty, FunctionalProperty):
        label = "encoding"
        domain = [Sequence]
    
    #-----Component properties-----
    class type(ObjectProperty):
        label = "type"
        domain = [Or([Component, LocalSubComponent, ExternallyDefined, Interaction])]
    Component.is_a.append(type.some(Thing))
    LocalSubComponent.is_a.append(type.some(Thing))
    ExternallyDefined.is_a.append(type.some(Thing))
    Interaction.is_a.append(type.some(Thing))
    
    class role(ObjectProperty):
        label = "role"
        domain = [Or([Component, Feature, Participation])]
    Participation.is_a.append(role.some(Thing))
       
    class hasSequence(ObjectProperty):
        label = "hasSequence"
        domain = [Or([Component, Location])]
        range= [Sequence]
    Location.is_a.append(hasSequence.some(Sequence))
    Location.is_a.append(hasSequence.max(1,Sequence))
        
    class hasFeature(ObjectProperty):
        label = "hasFeature"
        domain = [Or([Component, ComponentReference])]
        range= [Feature]
    ComponentReference.is_a.append(hasFeature.some(Feature))
    ComponentReference.is_a.append(hasFeature.max(1,Feature))
         
    class hasInteraction(Component >> Interaction):
        label = "hasInteraction"

    class hasConstraint(Component >> Constraint):
        label = "hasConstraint"

    class hasModel(Component >> Model):
        label = "hasModel" 
        
    class hasInterface(Component >> Interface, FunctionalProperty):
        label = "hasInterface"  
  
    #-----Feature properties-----
    class orientation(ObjectProperty, FunctionalProperty):
        label = "orientation"
        domain = [Or([Feature, Location])]
        range = [Or([inline, reverseComplement])]
      
    #-----SubComponent properties-----
    class roleIntegration(ObjectProperty, FunctionalProperty):
        label = "roleIntegration"
        domain = [SubComponent]
    
    class instanceOf(SubComponent >> Component, FunctionalProperty):
        label = "instanceOf"
    SubComponent.is_a.append(instanceOf.some(Component))
     
    class sourceLocation(SubComponent >> Location):
        label = "sourceLocation"
    
    class hasLocation(ObjectProperty):
        label = "hasLocation"
        domain = [Or([SubComponent, LocalSubComponent, SequenceFeature])]
        range = [Location]
    SequenceFeature.is_a.append(hasLocation.some(Location))
    
    #-----ComponentReference properties-----
    class inChildOf(ComponentReference >> SubComponent, FunctionalProperty):
        label = "inChildOf"  
    ComponentReference.is_a.append(inChildOf.some(Component))
          
    #-----ExternallyDefined properties-----
    class definition(ObjectProperty, FunctionalProperty):
        label = "definition"
        domain = [ExternallyDefined]
    ExternallyDefined.is_a.append(definition.some(Thing))
    
    #-----Location properties-----
    class order(DataProperty, FunctionalProperty):
        label = "order"
        domain = [Location] 
        #range = [int]
        range= [ConstrainedDatatype(int, min_inclusive = 1)]
    
    #-----Range properties-----
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
    
    #-----Cut properties-----
    class at(DataProperty, FunctionalProperty):
        label = "start"
        domain = [Cut] 
        range= [ConstrainedDatatype(int, min_inclusive = 0)]
    Cut.is_a.append(at.some(ConstrainedDatatype(int, min_inclusive = 0)))
    
    #-----Constraint properties-----
    class restriction(ObjectProperty, FunctionalProperty):
        label = "restriction"
        domain = [Constraint] 
    Constraint.is_a.append(restriction.some(Thing))
    
    class subject(Constraint >> Feature, FunctionalProperty):
        label = "subject"
    Constraint.is_a.append(subject.some(Feature))
    
    #objectProperty = types.new_class('object', (ObjectProperty,FunctionalProperty))
    #objectProperty.python_name = 'constraintobject'
    class object(Constraint >> Feature, FunctionalProperty):
        label = "object"
    Constraint.is_a.append(object.some(Feature))
    
    #-----Interaction properties-----
    class hasParticipation(Interaction >> Participation):
        label = "hasParticipation"
     
    #-----Participation properties-----
    class participant(Participation >> Feature, FunctionalProperty):
        label = "participant"  
        
    class higherOrderParticipant(Participation >> Interaction, FunctionalProperty):
        label = "higherOrderParticipant"    
   
    #-----Interface properties-----
    class input(Interface >> Feature):
        label = "input" 
    
    class output(Interface >> Feature):
        label = "output"  
     
    class nondirectional(Interface >> Feature):
        label = "nondirectional"  
    
    #-----CombinatorialDerivation properties-----
    class strategy(FunctionalProperty):
        label = "strategy"
        domain = [CombinatorialDerivation]
        range = [Or([enumerate, sample])]
    
    class template(CombinatorialDerivation >> Component, FunctionalProperty):
        label = "template" 
    CombinatorialDerivation.is_a.append(template.some(Component))
        
    class hasVariableFeature(CombinatorialDerivation >> VariableFeature):
        label = "participant"  
    
    #-----VariableFeature properties-----
    class cardinality(FunctionalProperty):
        label = "cardinality"
        domain = [VariableFeature]
        range = [Or([zeroOrOne, one, zeroOrMore, oneOrMore])]
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
              
    #-----Implementation properties-----
    class built(Implementation>> Component, FunctionalProperty):
        label = "built"
    
    #-----Model properties-----
    class source(ObjectProperty, FunctionalProperty):
        label = "source"  
        domain = [Or([Model, Attachment])]
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
                 
    #-----Collection properties-----
    class member(Collection >> TopLevel):
        label = "member"  
    
    #-----Attachment properties-----
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
                 
    #TODO: Incorporate restrictions for sequence.encoding types.
    #TODO: Incorporate restrictions for component.type values.
    #TODO: Incorporate restrictions for component.role values.
    #TODO: Incorporate restrictions for constraint.restriction types.
    #TODO: Incorporate restrictions for interaction.type values.
    #TODO: Incorporate restrictions for participation.role values.
    #TODO: Incorporate restrictions for model.language and model.framework properties.
    
             
sbol3.save(file = "../sbolowl3.txt", format = "rdfxml")
sbol3.save(file = "../sbolowl3.rdf", format = "rdfxml")
print ("done!")