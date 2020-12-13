Demographic Edit Using Python w10 ateBit
-----------------------------
The goal of this project is to create Python tools to edit demographic data.

The main aim is to provide tools which can enable users to edit demographic data
by using the variable names which are familiar to them.

For example, the following demographic data will be edited via its own variable
names:

householdID  personID  age  fname  lname  sex  drive    relref  parent
-----------  --------  ---  -----  -----  ---  -----    ------  ------
      10001         1   22   Mary   Jone    f      y    refper       3
      10001         2    3   John   Jone    m      y       son       1
      10001         3   64   Anne   Jone    f      y       mom
      10001         4   63   Paul   Jone    m      n       dad
      20001         1   25   Pete  Smith    m      n    refper
      20001         2   23    Tom  Colin    m      y  roommate

In the above data set, there are two households: 10001 and 20001.  These are two
unique households and they are added to the master key list:

  hhldIDs = ['10001', '20001']

The hhldIDs list is the main driver for iterating through the above records.
Using a Python "for-loop", the above records are iterated as follows:

  for hhldID in hhldIDs:
    for persons in getRecords(hhldIDs):
      # getRecords(hhldID) returns all persons in the household for each of
      # "hhldIDs" i.e. first, getRecords(hhldID) returns "10001" household
      # members

      # to access hhldID = 10001's personID = 1's (Mary Jone) age
      person_age1 = persons.age[1]

      # to find personID = 2's (John Jone) parent
      john_parentID = parent[2]

      # to access the name of john_parent
      john_parent_name = fname[john_parentID]


In order to accomplish the above programmable interface, the aforemationed data
set must be converted to objects of Dictionaries and Lists.  With these tools
users can edit the demographic data using the variable names.