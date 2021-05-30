'''
Created on 26 May 2021

@author: gokselmisirli
'''

from owlready2 import *
import types
import re
from ctypes.test.test_repr import subclasses


sbol3 = get_ontology("http://sbols.org/v3")
prov = get_ontology("https://www.w3.org/ns/prov#")
om = get_ontology(" http://www.ontology-of-units-of-measure.org/resource/om-2/")

with om: 
    class Measure(Thing):
        label = "Measure"       



with sbol3: 
   
    class Identified(Thing):
        label = "Identified"
        
    class TopLevel(Identified):
        label = "TopLevel"
        #is_a= [hasNamespace2.some(Thing)] --> subclass
        #equivalent_to = [hasNamespace2.some(Thing)]
        
    class Sequence (TopLevel):
        label = "Sequence"  
         
    class Component (TopLevel):
        label = "Component"
            
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
        
    #TopLevel properties    
    class hasNamespace(ObjectProperty, FunctionalProperty):
        label = "hasNamespace"
        domain = [TopLevel]
        #range = [Thing] 
        #class_property_type=["value"]
    TopLevel.is_a.append(hasNamespace.some(Thing))
    
    #Sequence properties
    class elements(DataProperty, FunctionalProperty):
        label = "elements"
        domain = [Sequence]
        range = [str] 
    Sequence.is_a.append(elements.some(str))
    
    class encoding(ObjectProperty, FunctionalProperty):
        label = "encoding"
        domain = [Sequence]
        
    
        
#sbol3.TopLevel.isa = [sbol3.hasNamespace.value(str)]    
#sbol3.TopLevel.is_a.append(sbol3.hasNamespace.some(sbol3.Thing))
 
 

'''with sbol3:       
    class wasDerivedFrom(DataProperty):
        label = "wasDerivedFrom"
        domain = [sbol3.Identified]
        range = [Thing]  
'''        
        
         
  
'''
       class displayId(DataProperty, FunctionalProperty):
        label="displayId"
        domain=Identified
        range = str
'''   
        
        
sbol3.save(file = "../sbolowl3.txt", format = "rdfxml")
sbol3.save(file = "../sbolowl3.rdf", format = "rdfxml")
sbol3.save(file = "../sbolowl3.ttl", format = "turtle")



print ("done!")