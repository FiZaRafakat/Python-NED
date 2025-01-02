'''

Relationships in OOP : 
1) inheritance ("is-a" relationship)
2) Association ("has-a" relationship)

is-a relationship : 
   -used when one class is specialized version of another class
   - modelled using inheritance
   EG: *A Dog "is-a" Animal ---> dog class inherits from animal class.
       *A Car "is-a" Vehicle ---> car class inherits from vehicle class.

has-a relationship : 
    - represents complete + partial ownership(association) b/w classes.
    - modelled using aggregation and composition ---> association
    - possession of one object by another
    EG : *A Car "has-a" Engine ---> Engine is possessed by a car completely 
         *A library "has-a" Books ---> Books are possessed by library.

Association: connection/possession/dependency b/w two classes is association...
   EG : Person has an address, name etc ... But person is not a address etc...
Categories of Association: 
   - Aggregation
   - Compostion

'''

#Compostion (complete dependency)
# Person (NAME , ADDRESS , dob (from date and this feature can't stand alone))
# ---> another class has date (day , month , year)

# Aggregation (partial dependency)
# Student (roll no , marks , name)
# --> college (std(can stand alone), groups , classes)


